Prefer Traditional Xbase Unique Index Behavior




Advantage Database Server 12  

Prefer Traditional Xbase Unique Index Behavior

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Prefer Traditional Xbase Unique Index Behavior  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Prefer Traditional Xbase Unique Index Behavior Advantage Concepts master\_Prefer\_traditional\_xbase\_unique\_index\_behavior Advantage Concepts > Advantage File Formats > Xbase File Format > Prefer Traditional Xbase Unique Index Behavior / Dear Support Staff, |  |
| Prefer Traditional Xbase Unique Index Behavior  Advantage Concepts |  |  |  |  |

An Xbase index order created with the "unique" property will only include records that are referenced by unique values. If two records result in the identical [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. If the record (of the two with identical key values) referenced by the unique index is modified such that the key value changes, that index key will be removed from the index, but the other record with the identical key value will NOT be added to the unique index. Therefore, no key will be referencing the unique record in the index. Unique Xbase index orders do not guarantee uniqueness of the field(s) in the index orders key expression.

Unique indexes in the Advantage proprietary file format guarantee uniqueness of the field(s) in the index orders key expression. If the value(s) in the field(s) in an Advantage Proprietary unique index order change such that they are no longer unique, the update will fail.

If you do not want to guarantee uniqueness of field(s) in a table, and if the traditional Xbase behavior of the "unique" property in Xbase indexes is desirable to you, then you may want to use the Xbase file format.