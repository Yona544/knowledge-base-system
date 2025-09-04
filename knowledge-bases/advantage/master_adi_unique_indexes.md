ADI Unique Indexes




Advantage Database Server 12  

ADI Unique Indexes

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADI Unique Indexes  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ADI Unique Indexes Advantage Concepts master\_Adi\_unique\_indexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADI Unique Indexes  Advantage Concepts |  |  |  |  |

An ADI index order created with the "unique" property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be generated and the index order will not be created. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the update must be canceled or the table and index must be closed.