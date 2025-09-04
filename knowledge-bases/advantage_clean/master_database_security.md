---
title: Master Database Security
slug: master_database_security
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_database_security.htm
source: Advantage CHM
tags:
  - master
checksum: 3cc4e02bcbf957aa036a0a455da2d677eae79c42
---

# Master Database Security

Database Security

Database Security

Advantage Concepts

| Database Security  Advantage Concepts |  |  |  |  |

Database security is essential for controlling access to the files in your database. If database security is not present, there is little or no control over whom can update data, delete files, and/or possibly corrupt data in the database. The Advantage Database Server provides two methods of database security for free connections:

- [Check Rights](master_check_rights.md): Checking the user's network access rights before opening files for that user.

- [Ignore Rights](master_ignore_rights.md): Ignore Rights: Allowing access to the database via an Advantage application only. Beginning with version 10.0, the client no longer performs rights checking by default. The default behavior is to use Ignore Rights regardless of the setting provided by the application. The pre version 10.0 behavior can be restored with a call to [AdsSetRightsChecking](ace_adssetrightschecking.md).

The Advantage Database Server provides User Account database security for database connections. See the Flexible User Access Control section in [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

Database security for Free Connections) is specified via:

- The TAdsTable/TAdsQuery.TAdsTableOptions.AdsRightsCheck value with the Advantage TDataSet Descendant.

- The AdsOpenTable API with the Advantage Client Engine API

- The RightsChecking value in the ODBC registry entry section for the Advantage ODBC Driver.

- The ADSPROP\_INIT\_SECURITY\_MODE property in Initialization Properties or the "SecurityMode" provider-specific Connection parameter with the Advantage OLE DB Provider.

- The AX\_RightsCheck function with the Advantage CA-Visual Objects RDD.

Linux users, see [Linux Rights Checking](master_linux_rights_checking.md).
