system.relations




Advantage Database Server 12  

system.relations

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.relations  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.relations Advantage SQL Engine master\_System\_relations Advantage SQL > System Views > Views > system.relations / Dear Support Staff, |  |
| system.relations  Advantage SQL Engine |  |  |  |  |

Contains one row for each referential integrity constraint in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Referential integrity constraint name. |
| RI\_Primary\_Table | Character | 200 | The name of the primary table. |
| RI\_Primary\_Index | Character | 200 | The name of the primary key used in the referential integrity constraint. |
| RI\_Foreign\_Table | Character | 200 | The name of the foreign table. |
| RI\_Foreign\_Index | Character | 200 | The name of the foreign key used in the referential integrity constraint. |
| RI\_UpdateRule | ShortInt | 2 | The numeric representation of the update rule used by the referential integrity constraint. |
| RI\_DeleteRule | ShortInt | 2 | The numeric representation of the deletion rule used by the referential integrity constraint. |
| RI\_No\_Pkey\_Error | Memo | variable | The custom error message returned when a new foreign key value does not exist in the primary key. |
| RI\_Cascade\_Error | Memo | variable | The custom error message returned when a cascading update or delete fails. |