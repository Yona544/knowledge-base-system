---
title: Master Root Dictionary
slug: master_root_dictionary
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_root_dictionary.htm
source: Advantage CHM
tags:
  - master
checksum: a310df0aada4592654587d488bbfe1c6e7f261ff
---

# Master Root Dictionary

Root Dictionary

Root Dictionary

Advantage Database Server

| Root Dictionary  Advantage Database Server |  |  |  |  |

The concept of a root dictionary was introduced in v11 of Advantage. The root dictionary was primarily added in this release to help support the Advantage Web Administrator utility and some functionality in the Advantage Web Platform. But it may also provide functionality that you may find useful in other situations. Initially, the root dictionary functionality is limited to providing some additional security enhancements.

- Two new [database roles](master_database_base_roles.md) SERVER:Admin and SERVER:Monitor have been added.  These apply to users with membership in these roles only when the user is connected to the root dictionary.

- Some new system procedures such as [sp\_mgGetCrashDumpInfo](master_sp_mggetcrashdumpinfo.md), [sp\_mgGetErrorLog](master_sp_mggeterrorlog.md), [sp\_GetLinks](master_sp_getlinks.md), and [sp\_mgSetConfigValue](master_sp_mgsetconfigvalue.md) can only be called when connected to the root dictionary.

- [sp\_mgKillUser](master_sp_mgkilluser.md) now requires DB:Admin or SERVER:Admin membership. If a user is a member of SERVER:Admin and is connected to the root dictionary, then the user can use sp\_mgKillUser to disconnect any user on the server. Otherwise, sp\_mgKillUser now only allows users to be disconnected by members of DB:Admin and only if the user is in the same dictionary as the DB:Admin user.

- [sp\_mgKillUser](master_sp_mgkilluser.md) allows wild card (an asterisk) to be given as the user name when run by SERVER:Admin members on the root dictionary.

- With the Web Administrator Utility, it is possible to run queries against other dictionaries when connected to the root dictionary. Note that this requires the [\_\_Query service](web_query_service_operation.md) to be enabled on the root dictionary and [pass-through queries](web_pass_through_queries.md) to be enabled on the target dictionary (see [sp\_ModifyDatabase](master_sp_modifydatabase.md) and [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm "ace_a") and the ADS\_DD\_QUERY\_VIA\_ROOT property). This pass-through query capability means it is possible to expose a single dictionary through the Advantage Web Platform but be able to perform some administration on other databases on the same server. To enable pass-through queries, you can use Advantage Data Architect to modify the settings under the Advanced tab of the data dictionary properties dialog. Or you can modify them directly with the system procedure.  For example, "EXECUTE PROCEDURE sp\_ModifyDatabase( 'Query\_Via\_Root', '3' )" will enable pass-through queries and pass-through procedure requests.

- For security reasons, system procedures can only be executed against the root dictionary through the Advantage Web Platform. To execute system procedures through the web platform against non-root dictionaries, it would be necessary to enable the \_\_Query service and use an SQL statement.

A single installation of Advantage Database Server can have only one root dictionary. It is specified by the [ROOT\_DICTIONARY](master_root_dictionary_config.md) configuration parameter. This configuration parameter can be set on the Windows platform by using the Advantage configuration utility (ads\_cfg.exe) under the file locations tab. Note that the path supplied in the configuration value must match exactly the path of the dictionary when it is opened.  You can use the system variable [::Conn.IsRoot](master_system_variables.md) to determine if a dictionary is the root dictionary. For example, after setting the ROOT\_DICTIONARY configuration parameter and restarting Advantage Database Server for it to be recognized, you can run the query:

SELECT ::Conn.IsRoot FROM system.iota;

when connected to the root dictionary to verify that it is indeed recognized as the root dictionary.

You can specify an existing dictionary as the root.  However, you can also create a new empty dictionary as the root dictionary for use with the Advantage Web Administrator Utility for management purposes. This might be desirable if you do not want to expose an existing dictionary through the Advantage Web Platform.

\_\_rootdd System Alias

A system alias named \_\_rootdd is available that resolves to the path of the configured root dictionary.  Applications can then connect to the root dictionary using a path like \\server\\_\_rootdd.
