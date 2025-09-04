sp\_DisableTriggers




Advantage Database Server 12  

sp\_DisableTriggers

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DisableTriggers  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DisableTriggers Advantage SQL Engine master\_Sp\_disabletriggers Advantage SQL > System Procedures > Procedures > sp\_DisableTriggers / Dear Support Staff, |  |
| sp\_DisableTriggers  Advantage SQL Engine |  |  |  |  |

Disable a database trigger or triggers.

Syntax

sp\_DisableTriggers(

 ObjectName, CHARACTER,200,

 Parent, CHARACTER,200,

 AllUsers, LOGICAL,

 Options, INTEGER )

Parameters

|  |  |
| --- | --- |
| ObjectName (I) | Name of DD object. Can be a table, view, or a trigger. |
| Parent (I) | Name of table or view when ObjectName is the name of a trigger. For [database triggers](master_database_triggers.htm), this should be null. |
| AllUsers (I) | TRUE if the setting should affect all users. FALSE for only the current user. |
| Options (I) | Must be zero. Reserved for future use. |

Output

None

Special Return Codes

AE\_UNABLE\_TO\_DISABLE\_TRIGGERS

Remarks

The sp\_DisableTriggers system procedure is used to disable triggers in a database. Triggers can be disabled for the current user or for all users. To disable triggers for the current user, specify empty or NULL strings for ObjectName and Parent and specify FALSE for AllUsers. To disable triggers for all users and all triggers of a database, specify empty or NULL strings for ObjectName and Parent, but specify TRUE for AllUsers. To disable all triggers for a specific table, specify the database table name for ObjectName and NULL or an empty string for Parent. To disable a single trigger, specify the database trigger name for ObjectName and the table name that contains the trigger for Parent. When disabling a single trigger or all triggers for a specific table, the AllUsers flag is ignored. The setting will then affect all database users.

The disabled state of a trigger is determined using the following hierarchy: user, database, table, trigger. This means that the user level disabled state has precedence over the database level. Likewise, the table level disabled state has precedence over the trigger level. Furthermore, the disabled state of a level cannot be altered when a higher level is already disabled. For example, a table's disabled state cannot be altered if triggers are already disabled on the database level. However, this does not apply to the user level in that a user may disable triggers on the database or lower levels despite their current user disabled trigger state.

Changes in the disabled trigger state will take effect immediately. If a user has already begun firing a trigger, the trigger will run as it would normally. However, if a user is in the middle of a recursive trigger or a referential integrity cascade for example, a trigger's disabled state could change in the middle of the overall operation.

Appropriate ALTER permissions are required to disable triggers on the database, table, and trigger levels. For example, ALTER TABLE permissions are required on a table to disable triggers on it. In order to disable triggers on the current connection, membership in the [DB:Admin](master_database_base_roles.htm) group is required.

Note Disabling triggers for the current user only affects the connection on which the disable request was processed. Different connections using the same user name will not be affected.

Examples

// Disable all triggers for a single user (DB:Admin membership is required)

EXECUTE PROCEDURE sp\_DisableTriggers( NULL, NULL, FALSE, 0 )

 

// Disable all triggers for all users

EXECUTE PROCEDURE sp\_DisableTriggers( NULL, NULL, TRUE, 0 )

 

// Disable all triggers on a specific table (all users is assumed)

EXECUTE PROCEDURE sp\_DisableTriggers( 'customers', NULL, FALSE, 0 )

 

// Disable a specific trigger on a specific table (all users is assumed)

EXECUTE PROCEDURE sp\_DisableTriggers( 'auditTrigger', 'customers', FALSE, 0 )

See Also

[sp\_EnableTriggers](master_sp_enabletriggers.htm)