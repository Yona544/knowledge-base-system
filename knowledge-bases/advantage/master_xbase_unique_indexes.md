Xbase Unique Indexes




Advantage Database Server 12  

Xbase Unique Indexes

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Xbase Unique Indexes  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Xbase Unique Indexes Advantage Concepts master\_Xbase\_unique\_indexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Xbase Unique Indexes  Advantage Concepts |  |  |  |  |

An Xbase index order created with the "unique" property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added to the index, and no error is reported. If the record (of the two with identical key values) referenced by the unique index is modified such that the key value changes, that index key will be removed from the index, but the other record with the identical key value will NOT be added to the unique index. Therefore, no key will be referencing the unique record in the index. Unique Xbase index orders do not guarantee uniqueness of the field(s) in the index order's key expression. This is the traditional Xbase behavior of the "unique" property in Xbase indexes.

Note The Visual FoxPro (VFP) table type supports candidate indexes, which do enforce uniqueness of the field(s) in the index orders key expression. See [Xbase Candidate Indexes](master_xbase_candidate_indexes.htm).