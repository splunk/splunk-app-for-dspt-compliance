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

#### Configure Cyber Alerts Indexing
From your Splunk instance Web Interface:
* Browse to *Settings / Data Inputs*
* Select *splunk_app_for_dspt_compliance* and provide the following info:
    * **Name** of the input
    * **Interval** in seconds - how often the app will fetch cyber alerts
    * **REST API** endpoint to fetch cyber alerts from
    * **Enable Checkpoint** - to align with your duplication policy
    * (Optional) **More settings** - to specify host, index and sourcetype if different from default 

### Usage

## Contributing
App has been developed by Kevin Pyart, Senior Splunk SE (UK Public Sector)

For Support please contact kpyart@splunk.com

TODO : Are PRs / Issues welcome ?

## License
TODO
