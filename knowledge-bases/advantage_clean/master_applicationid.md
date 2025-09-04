---
title: Master Applicationid
slug: master_applicationid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_applicationid.htm
source: Advantage CHM
tags:
  - master
checksum: 700f72e2699914a1f8ec5289cb327f9f67874ea5
---

# Master Applicationid

APPLICATIONID()

APPLICATIONID()

Advantage Concepts

| APPLICATIONID()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to retrieve the Application ID of the connection.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

APPLICATIONID( ) à cAppID

Parameters

| None |  |

Return Value

The application ID for the current connection.

Remarks

The Application ID is initialized by default to the file name of the application (executable) that connected to the Advantage Database Server (only for ACE based clients). The Application ID can be set and retrieved using the sp\_SetApplicationID and sp\_GetApplicationID system procedures.

See Also

[sp\_SetApplicationID](master_sp_setapplicationid.md)

[sp\_GetApplicationID](master_sp_getapplicationid.md)

[DATABASE()](master_database.md)

[USER()](master_user.md)
