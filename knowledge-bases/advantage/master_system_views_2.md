system.ansi\_views




Advantage Database Server 12  

system.ansi\_views

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.ansi\_views  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.ansi\_views Advantage SQL Engine master\_System\_views\_2 Advantage SQL > System Views > Views > system.ansi\_views / Dear Support Staff, |  |
| system.ansi\_views  Advantage SQL Engine |  |  |  |  |

Contains one row for each view in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | View name. |
| View\_Stmt\_Len | ShortInt | 2 | The length of the SQL statement used to generate the view. |
| View\_Stmt | Memo | variable | The SQL statement used to generate the view. |
| Comment | Memo | variable | The description of the view. |