# Splunk App for DSPT Compliance
This app has been created to assist in yearly compliance to the Data Security and Protection Toolkit (DSPT). 
The DSPT Audit applies, for example, to the UK National Health Service (NHS). 

## Features
* Recurrent retrieval of cyber alerts from NHS feeds to enrich data analysis
* Dashboards to ease compliance with the DSPT for audit purposes:
    * TODO complete table below opportunely
    
    | **Dashboard Name**     | **Description**                                     |
    |------------------------|-----------------------------------------------------|
    | Overview               | General overview of monitored data                  |
    | Cyber Alerts           | Cyber Alerts details                                |
    | Evidence Questionnaire | Enables users to fill in the evidence questionnaire |
    |                        |                                                     |
    |                        |                                                     |

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
* Select *splunk_app_for_dspt_compliance* and provide the following info:
    * **Name** of the input
    * **REST API** endpoint to fetch cyber alerts
    * **Enable Checkpoint** - to align with your alerts duplication policy
    * (Optional) **More settings** - to specify host, interval, index and sourcetype

> Dear **admins**, if you decide to store cyber alerts in another index, please make sure you update the macro `default_index` with *Definition* such as `index=<YOUR_INDEX>`

### Usage
* Data Inputs TODO
* 

#### Troubleshooting
Useful SPL searches to:
* Verify NHS Cyber Alerts indexing `index=_internal nhs_cyberalerts.py`
* Verify the index has been populated with NHS Cyber Alerts `index=main`
    > Please replace `main` with the index  specified in the configuration and make sure the time range is set on `All time`

## Contributing
This app is built using `Splunk UCC framework`. To contribute please:
* Clone this repository
* Locally install and use the UCC framework by following [instructions](https://github.com/splunk/addonfactory-ucc-generator#how-to-use)
* Apply your changes to `package/*` only

Splunk welcomes contribution from the community, and your feedback and enhancements are appreciated as well. There is always code that can be clarified, functionality that can be extended, new data filters to develop, documentation to refine. If you see something you think should be fixed or added, go for it!
* Open a [pull-request](https://github.com/splunk/splunk-app-for-dspt-compliance/pulls)
* File a [feature request / bug report](https://github.com/splunk/splunk-app-for-dspt-compliance/issues)

## References
* [NHS Cyber Alerts API](https://digital.nhs.uk/services/data-security-centre/cyber-alerts-api/get-cyber-alerts)

## Credits
App has been developed by Kevin Pyart, Senior Splunk SE (UK Public Sector)

For Support please contact kpyart@splunk.com

## License
TODO
