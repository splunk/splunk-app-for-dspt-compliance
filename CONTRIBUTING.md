# Contributing Guidelines
Splunk welcomes contribution from the community, and your feedback and enhancements are appreciated as well. There is always code that can be clarified, functionality that can be extended, new data filters to develop, documentation to refine. If you see something you think should be fixed or added, go for it!

* Open a [pull-request](https://github.com/splunk/splunk-app-for-dspt-compliance/pulls)
* File a [feature request / bug report](https://github.com/splunk/splunk-app-for-dspt-compliance/issues)

## How to contribute
This app is built using `Splunk UCC framework`. To contribute please:
* Clone this repository
* Locally install and use the UCC framework by following [instructions](https://github.com/splunk/addonfactory-ucc-generator#how-to-use)
* Apply your changes to `package/*` only

## Automatic Release
A [GitHub Action](https://github.com/splunk/splunk-app-for-dspt-compliance/actions/workflows/manual-release.yml) is provided to:
* Bump the app version
* Create a release
* *Under development* - Eventually upload the release to Splunkbase to keep them aligned

This action can be **manually triggered** by clicking on _Actions / Manual Release / Run Workflow_ and by providing:
* **Bump part** - Either major, minor or patch
* (Optional) **Changelog notes** - By default all commit messages beginning from the last release are included
