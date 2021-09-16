# Splunk App for DSPT Compliance
This app has been created to assist in yearly compliance to the Data Security and Protection Toolkit (DSPT). 
The DSPT Audit applies, for example, to the UK National Health Service (NHS). 

## Features
Data required to fully utilise this app:

1.Active Directory
2.Edge Firewalls
3.Windows Event Logs
4.Windows Update Logs
5.Anti Virus Logs

Pre requisits:
Splunk Common Information Model App
Accelerated Data Models required -

## Getting Started
### Installation
TODO

#### Configure Cyber Alerts Indexing
From your Splunk instance Web Interface:
* Browse to *Settings / Data Inputs*
* Select *splunk_app_for_dspt_compliance* and provide the following info:
    * **Name** of the input
    * **REST API** endpoint to fetch cyber alerts
    * **Enable Checkpoint** - to align with your alerts duplication policy
    * (Optional) **More settings** - to specify host, interval, index and sourcetype

### Usage
TODO

#### Troubleshooting
Useful SPL searches to:
* Verify NHS Cyber Alerts indexing `index=_internal nhs_cyberalerts.py`

* Verify the index has been populated with NHS Cyber Alerts `index=main`
    > Please replace `main` with the index  specified in the configuration and make sure the time range is set on `All time`

## Contributing
App has been developed by Kevin Pyart, Senior Splunk SE (UK Public Sector)

For Support please contact kpyart@splunk.com

TODO : Are PRs / Issues welcome ?

## License
TODO
