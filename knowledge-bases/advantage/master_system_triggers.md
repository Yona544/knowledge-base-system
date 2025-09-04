system.triggers




Advantage Database Server 12  

system.triggers

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.triggers  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.triggers Advantage SQL Engine master\_System\_triggers Advantage SQL > System Views > Views > system.triggers / Dear Support Staff, |  |
| system.triggers  Advantage SQL Engine |  |  |  |  |

Contains one row for each trigger in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Trigger name. |
| Trig\_TableName | Character | 200 | The table the trigger is assigned to. For [database triggers](master_database_triggers.htm), this is null. |
| Trig\_Event\_Type | Integer | 4 | The type of event that causes a trigger to fire. |
| Trig\_Trigger\_Type | Integer | 4 | The kind of event the trigger should fire on. |
| Trig\_Container\_Type | Integer | 4 | The type of container holding the trigger. |
| Trig\_Container | Memo | variable | The name of the trigger container. This value varies depending on the container type. |
| Trig\_Function\_Name | Character | 260 | The name of the function called when the trigger is executed. |
| Trig\_Priority | Integer | 4 | Determines when the trigger is fired in relation to other triggers. |
| Trig\_Options | Integer | 4 | Options for the trigger in numeric format. |
| Comment | Memo | variable | The description of the trigger. |