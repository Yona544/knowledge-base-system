---
title: Master Check Rights
slug: master_check_rights
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_check_rights.htm
source: Advantage CHM
tags:
  - master
checksum: 6fd212982ee618f1ba3b5fbec1e9047b383c23e6
---

# Master Check Rights

Check Rights

Check Rights

Advantage Concepts

| Check Rights  Advantage Concepts |  |  |  |  |

When a non-Advantage application, whether it is a database application or other application, needs to open or create a file on the file server, the network operating system will verify that the user has sufficient network access rights to that directory and/or file before allowing that user to open or create the file. If the user has no network access rights to the directory and/or file, the network operating system will not allow the application to open or create the file. If the user has limited network access rights to the directory and/or file, such as read-only access, the network operating system will only allow the application to open a file for read-only use.

The Advantage Database Server "Check Rights" security method for free connections obeys this same concept of verifying user network access rights. The client-side code checks for the existence of the table prior to attempting to open it. If the client workstation does not have access to the table, then the client will not send the open request to the server. This security model allows a developer to base their applications table access rights on the network access rights. Note that this only applies to direct free table opens. It has no affect with SQL queries and data dictionary-bound tables.

Beginning with version 10.0, the default behavior has been changed. The Advantage clients no longer perform the existence checks for performance reasons, even if the application's Advantage driver specifies "Check Rights". If your application relies on the older behavior, you can re-enable it with [AdsSetRightsChecking](ace_adssetrightschecking.md).

Linux users, see [Linux Rights Checking](master_linux_rights_checking.md).

See Also

[Database Security](master_database_security.md)
