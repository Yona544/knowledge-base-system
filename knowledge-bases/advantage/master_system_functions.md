system.functions




Advantage Database Server 12  

system.functions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.functions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.functions Advantage SQL Engine master\_System\_functions Advantage SQL > System Views > Views > system.functions / Dear Support Staff, |  |
| system.functions  Advantage SQL Engine |  |  |  |  |

Contains one row for each function in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | CICharacter | 200 | Function name. |
| Package | CICharacter | 200 | Name of the package that the function is part of. May be NULL or empty string. |
| Return Type | CICharacter | 20 | Data type of the function. |
| Input Parameters | Memo | Variable | Input parameters in comma separated list. |
| Implementation | NMemo | Variable | The SQL script that implements the function. |
| Comment | Memo | Variable | Function description. |
| User\_Defined\_Prop | Blob | Variable | Inaccessible at the moment. |