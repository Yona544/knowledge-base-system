system.publications




Advantage Database Server 12  

system.publications

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.publications  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.publications Advantage SQL Engine master\_System\_publications Advantage SQL > System Views > Views > system.publications / Dear Support Staff, |  |
| system.publications  Advantage SQL Engine |  |  |  |  |

Contains one row for each publication in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Publication name. |
| Comment | Memo | Variable | The description of the publication. |
| Options | Integer | 4 | The options used when creating the publication. See [sp\_CreatePublication](master_sp_createpublication.htm). |
| User\_Defined\_Prop | Binary | Variable | The user defined property. |