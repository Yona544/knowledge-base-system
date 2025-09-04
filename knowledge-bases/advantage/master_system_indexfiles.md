system.indexfiles




Advantage Database Server 12  

system.indexfiles

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.indexfiles  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.indexfiles Advantage SQL Engine master\_System\_indexfiles Advantage SQL > System Views > Views > system.indexfiles / Dear Support Staff, |  |
| system.indexfiles  Advantage SQL Engine |  |  |  |  |

Contains one row for each index file in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Index file name. |
| Parent | Character | 200 | The name of the table associated with the index file. |
| Index\_File\_Path | Character | 260 | The absolute path to the index file. |
| Index\_File\_PageSize | Integer | 4 | The index page size for the index file. |