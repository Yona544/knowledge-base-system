---
title: Master User
slug: master_user
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_user.htm
source: Advantage CHM
tags:
  - master
checksum: 58ad5a633476a1d8f30dbcd7cae037fac1c0b612
---

# Master User

USER()

USER()

Advantage Concepts

| USER()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the user name of the current connection.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

USER() à cUser

Parameters

| None |  |

Return Value

The database user name of the connected user

Remarks

For database connections, this function returns the name of the logged in user on the current connection. For free connections, the name returned is the client computer name.

See Also

[APPLICATIONID()](master_applicationid.md)

[DATABASE()](master_database.md)
