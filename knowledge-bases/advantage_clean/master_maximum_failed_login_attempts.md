---
title: Master Maximum Failed Login Attempts
slug: master_maximum_failed_login_attempts
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_maximum_failed_login_attempts.htm
source: Advantage CHM
tags:
  - master
checksum: 2b3e3221719a8845fc39eb3a9a5d3c34eccab404
---

# Master Maximum Failed Login Attempts

Maximum Failed Login Attempts

Maximum Failed Login Attempts

Advantage Database Server

| Maximum Failed Login Attempts  Advantage Database Server |  |  |  |  |

If a user name is used by an unauthorized person or is stolen, a common technique to gain access is called "brute force attack". This is a method of systematically trying different passwords until the correct password is found.

The Advantage Database Server keeps track of how many times a user has entered a wrong password. By default, the maximum allowed failed password attempts is 5. This seems to be a reasonable number given the fact that the brute force method would fail hundreds of times before having a chance at being successful, but an authorized user would most likely never reach 5 failed attempts. If a user does reach the maximum failed attempts, their Internet access will be disabled until the administrator re-enables the access.

See [Enabling Internet Access in the Data Dictionary](master_enabling_internet_access_in_the_data_dictionary.md) for more information.

By default Advantage Database Server will only enforce the maximum failed login attempts for Internet Connections.  If you wish to enforce the limit for all remote server connections, you can enable the "Enforce Max Failed Logins" property on the data dictionary.  This will cause Advantage Database Server to count all failed login attempts (from internet or remote server connections) and disable the login of any user that exceeds the maximum.  See [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) or [sp\_ModifyDatabase](master_sp_modifydatabase.md) on how to enable or disable this enforcement property.  Once a user has their login disabled, a database administrator may re-enable them by setting their "Logins Disabled" property to FALSE by using the [AdsDDSetUserPropery](ace_adsddsetuserproperty.md) API or the [sp\_ModifyUserProperty](master_sp_modifyuserproperty.md) system procedure.
