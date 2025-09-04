---
title: Master Sp Enabletriggers
slug: master_sp_enabletriggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_enabletriggers.htm
source: Advantage CHM
tags:
  - master
checksum: 6d07f430603d7d97e9b0d1af7af0825d6430d289
---

# Master Sp Enabletriggers

sp\_EnableTriggers

sp\_EnableTriggers

Advantage SQL Engine

| sp\_EnableTriggers  Advantage SQL Engine |  |  |  |  |

Enable a database trigger or triggers.

Syntax

sp\_EnableTriggers(

 ObjectName, CHARACTER,200,

 Parent, CHARACTER,200,

 AllUsers, LOGICAL,

 Options, INTEGER )

Parameters

| ObjectName (I) | Name of DD object. Can be a table, view, or a trigger. |
| Parent (I) | Name of table or view when ObjectName is the name of a table trigger. For [database triggers](master_database_triggers.md), this should be null. |
| AllUsers (I) | TRUE if the setting should affect all users. FALSE for only the current user. |
| Options (I) | Must be zero. Reserved for future use. |

Output

None.

Special Return Codes

AE\_UNABLE\_TO\_ENABLE\_TRIGGERS

Remarks

The sp\_EnableTriggers system procedure is used to enable triggers in a database. Triggers can be enabled for the current user or for all users. To enable triggers for the current user, specify empty or NULL strings for ObjectName and Parent and specify FALSE for AllUsers. To enable triggers for all users and all triggers of a database, specify empty or NULL strings for ObjectName and Parent, but specify TRUE for AllUsers. To enable all triggers for a specific table, specify the database table name for ObjectName and NULL or an empty string for Parent. To enable a single trigger, specify the database trigger name for ObjectName and the table name that contains the trigger for Parent. When enabling a single trigger or all triggers for a specific table, the AllUsers flag is ignored. The setting will then affect all database users.

The disabled state of a trigger is determined using the following hierarchy: user, database, table, trigger. This means that the user level disabled state has precedence over the database level. Likewise, the table level disabled state has precedence over the trigger level. Furthermore, the disabled state of a level cannot be altered when a higher level is already disabled. For example, a table's disabled state cannot be altered if triggers are already disabled on the database level. However, this does not apply to the user level in that a user may enable triggers on the database or lower levels despite their current user disabled trigger state.

Changes in the disabled trigger state will take effect immediately. If a user has already begun firing a trigger, the trigger will run as it would normally. However, if a user is in the middle of a recursive trigger or a referential integrity cascade for example, a trigger's disabled state could change in the middle of the overall operation.

Appropriate ALTER permissions are required to enable triggers on the database, table, and trigger levels. For example, ALTER TABLE permissions are required on a table to enable triggers on it. In contrast, no permissions are required for users to enable triggers on themselves.

Note Enabling triggers for the current user only affects the connection on which the enable request was processed. Different connections using the same user name will not be affected.

Examples

// Enable all triggers for a single user

EXECUTE PROCEDURE sp\_EnableTriggers( NULL, NULL, FALSE, 0 )

 

// Enable all triggers for all users

EXECUTE PROCEDURE sp\_EnableTriggers( NULL, NULL, TRUE, 0 )

 

// Enable all triggers on a specific table (all users is assumed)

EXECUTE PROCEDURE sp\_EnableTriggers( 'customers', NULL, FALSE, 0 )

 

// Enable a specific trigger on a specific table (all users is assumed)

EXECUTE PROCEDURE sp\_EnableTriggers( 'auditTrigger', 'customers', FALSE, 0 )

See Also

[sp\_DisableTriggers](master_sp_disabletriggers.md)
