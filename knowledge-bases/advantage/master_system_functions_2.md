system.ansi\_functions




Advantage Database Server 12  

system.ansi\_functions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.ansi\_functions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.ansi\_functions Advantage SQL Engine master\_System\_functions\_2 Advantage SQL > System Views > Views > system.ansi\_functions / Dear Support Staff, |  |
| system.ansi\_functions  Advantage SQL Engine |  |  |  |  |

Contains one row for each function in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | CICharacter | 200 | Function name. |
| Package | CICharacter | 200 | Name of the package that the function is part of. May be NULL or empty string. |
| Return Type | CICharacter | 20 | Data type of the function. |
| Input Parameters | Memo | Variable | Input parameters in comma separated list. |
| Implementation | Memo | Variable | The SQL script that implements the function. |
| Comment | Memo | Variable | Function description. |
| User\_Defined\_Prop | Blob | Variable | Inaccessible at the moment. |