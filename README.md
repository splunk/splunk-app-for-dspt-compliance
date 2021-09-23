# Splunk App for DSPT Compliance
This app has been created to assist in yearly compliance to the Data Security and Protection Toolkit (DSPT). 
The DSPT Audit applies, for example, to the UK National Health Service (NHS). 

## Features
* Recurrent retrieval of cyber alerts from NHS feeds to enrich data analysis
* Dashboards to ease compliance with the DSPT for audit purposes:
    
    | **Dashboard Name**     | **Description**                                     |
    |------------------------|-----------------------------------------------------|
    | Overview               | General overview of monitored data                  |
    | Cyber Alerts           | Cyber Alerts details                                |
    | Evidence Questionnaire | Enables users to fill in the evidence questionnaire |
    |          ...           |                                                     |
    |         TODO           |     Keep filling this table                         |

## Getting Started
### Requirements
* [Splunk Common Information Model App](https://splunkbase.splunk.com/app/1621/)
* [Lookup File Editor](https://splunkbase.splunk.com/app/1724/)
* Accelerated Data Models

Data required to fully utilise this app:

* Active Directory
* Edge Firewalls
* Windows Event Logs
* Windows Update Logs
* Anti Virus Logs

### Installation
Please refer to the [Splunk Documentation](https://docs.splunk.com/Documentation/AddOns/released/Overview/Installingadd-ons) for guidance on installing the Add-On in your environment. The app needs to be installed on the SH tier.

#### Configure Cyber Alerts Indexing
By default the app comes with a pre-configured and enabled input named `main`, that will daily fetch cyber alerts via NHS REST API and store them in the default index.

For customizations or additional feeds, from your Splunk instance Web Interface:
* Browse to *Settings / Data Inputs*
* Select *Splunk App for DSPT Compliance* and provide the following info:
    * **Name** of the input
    * **REST API** endpoint to fetch cyber alerts
    * **Enable Checkpoint** - to align with your events duplication policy
    * (Optional) **More settings** - to specify host, interval, index and sourcetype

> Dear **admins**, if you decide to store cyber alerts in another index, please make sure you update the macro `default_index` with *Definition* such as `index=<YOUR_INDEX>`

### Usage
Once installed, from your Splunk instance Web Interface, select the app *DSPT Compliance* and navigate through the dashboards to verify content.

TODO
> *Eventually add screenshots / more info about Questionnaire / anything else users might need to know when using the app*

#### Troubleshooting
Useful SPL searches to:
* Verify NHS Cyber Alerts indexing `index=_internal nhs_cyberalerts.py`
* Verify the index has been populated with NHS Cyber Alerts `index=main`
    > Please replace `main` with the index  specified in the configuration and make sure the time range is set on `All time`

## Contributing
If you would like to contribute to this app, see [CONTRIBUTING](CONTRIBUTING.md).

## References
* [NHS Cyber Alerts API](https://digital.nhs.uk/services/data-security-centre/cyber-alerts-api/get-cyber-alerts)

## Credits
App has been developed by Kevin Pyart, Senior Splunk SE (UK Public Sector)

For Support please contact kpyart@splunk.com

## License
TODO
> *If planning to open source this app, recommendation is **Apache 2.0***
