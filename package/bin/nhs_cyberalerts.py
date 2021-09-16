import import_declare_test
import sys
import json
import os.path as op
import traceback
from splunklib import modularinput as smi
from solnlib import conf_manager
from solnlib import log
from solnlib.modular_input import checkpointer


APP_NAME = __file__.split(op.sep)[-3]
CONF_NAME = "splunk_app_for_dspt_compliance"

from apiclient import (
    JsonResponseHandler,
)
from apiclient.exceptions import APIClientError
from nhs_client import NHSClient as nhs_client

def get_log_level(session_key, logger):
    """
    This function returns the log level for the addon from configuration file.
    :param session_key: session key for particular modular input.
    :return : log level configured in addon.
    """
    try:
        
        settings_cfm = conf_manager.ConfManager(
            session_key,
            APP_NAME,
            realm="__REST_CREDENTIAL__#{}#configs/conf-{}_settings".format(APP_NAME, CONF_NAME))

        logging_details = settings_cfm.get_conf(
            CONF_NAME+"_settings").get("logging")

        log_level = logging_details.get('loglevel') if (
            logging_details.get('loglevel')) else 'INFO'
        return log_level

    except Exception:
        logger.error(
            "Failed to fetch the log details from the configuration taking INFO as default level.")
        return 'INFO'


def get_account_details(session_key, account_name, logger):
    """
    This function retrieves account details from addon configuration file.
    :param session_key: session key for particular modular input.
    :param account_name: account name configured in the addon.
    :param logger: provides logger of current input.
    :return : account details in form of a dictionary.   
    """
    try:
        cfm = conf_manager.ConfManager(
            session_key, APP_NAME, realm='__REST_CREDENTIAL__#{}#configs/conf-{}_account'.format(APP_NAME, CONF_NAME))
        account_conf_file = cfm.get_conf(CONF_NAME + '_account')
        logger.info(f"Fetched configured account {account_name} details.")
        return {
            "username": account_conf_file.get(account_name).get('username'),
            "password": account_conf_file.get(account_name).get('password'),
        }
    except Exception as e:
        logger.error("Failed to fetch account details from configuration. {}".format(
            traceback.format_exc()))
        sys.exit(1)


class NHS(smi.Script):

    def __init__(self):
        super(NHS, self).__init__()
        self.input_type = "splunk_app_for_dspt_compliance"

    def get_scheme(self):
        scheme = smi.Scheme(self.input_type)
        scheme.description = 'Go to the add-on\'s configuration UI and configure modular inputs under the Inputs menu.'
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True
        scheme.use_single_instance = False

        scheme.add_argument(
            smi.Argument(
                'name',
                title='Name',
                description='Input Name',
                required_on_create=True
            )
        )

        #
        # Adding custom fields
        #
        scheme.add_argument(
            smi.Argument(
                "rest_api",
                title="REST API",
                description="Endpoint to fetch NHS cyber alerts",
                data_type=smi.Argument.data_type_string,
                required_on_create=True,
                required_on_edit=True
            )
        )

        scheme.add_argument(
            smi.Argument(
                "enable_checkpoint",
                title="Enable Checkpoint",
                description="Keep enabled to prevent indexing duplicates",
                data_type=smi.Argument.data_type_boolean,
                required_on_create=True,
                required_on_edit=False
            )
        )
        return scheme

    def validate_input(self, definition):
        pass

    def stream_events(self, inputs, ew):

        meta_configs = self._input_definition.metadata
        session_key = meta_configs['session_key']

        input_items = {}
        input_name = list(inputs.inputs.keys())[0]
        input_items = inputs.inputs[input_name]

        # Generate logger with input name
        _, input_name = (input_name.split('//', 2))
        logger = log.Logs().get_logger('{}_input'.format(APP_NAME))

        # Log level configuration
        log_level = get_log_level(session_key, logger)
        logger.setLevel(log_level)
        logger.debug("Modular input invoked.")

        #
        # Input logic begins here
        #
        self.stanza_name = input_name

        checkpoint = checkpointer.FileCheckpointer(meta_configs['checkpoint_dir'])
        
        url = input_items.get("rest_api")
        use_checkpoint = bool(int(input_items.get("enable_checkpoint")))

        # Initializing NHS client
        client = nhs_client(
            response_handler=JsonResponseHandler
        )

        # Initializing EventWriter to ingest data in Splunk
        ew = smi.EventWriter()

        #
        # Fetch Cyber Alerts
        #
        try:
            logger.info("Retrieving info from {} - Please be patient".format(url))

            response = client.get_all_cyberalerts("{}".format(url.rstrip('/')))
            logger.debug("Analysing response of {} pages".format(len(response)))
            
            lst_skipped_alerts = []

            for page in response:
                for alert in page["items"]:
                    alert_id = alert["threatId"]

                    if use_checkpoint:
                        # Verify if already ingested
                        if checkpoint.get(alert_id):
                            lst_skipped_alerts.append(alert_id)
                            continue

                    logger.debug("Ingesting alert ({}) to stanza {}".format(alert_id, self.stanza_name))
                    
                    # Converting milliseconds epoch to seconds
                    ev_time = float(alert["publishedDate"]/1000)
                    
                    event = smi.Event(data=json.dumps(alert),
                                time=ev_time,
                                source=self.input_type,
                                sourcetype=input_items.get("sourcetype"), 
                                index=input_items.get("index"))
                    
                    ew.write_event(event)

                    if use_checkpoint:
                        checkpoint.update(alert_id, "ingested")

        except APIClientError as ex:
            raise Exception("An error occurred when fetching cyber alerts - {}".format(ex))
    
        logger.info("Done fetching cyber alerts. Skipped {}. Till next execution.".format(len(lst_skipped_alerts)))

if __name__ == '__main__':
    exit_code = NHS().run(sys.argv)
    sys.exit(exit_code)
