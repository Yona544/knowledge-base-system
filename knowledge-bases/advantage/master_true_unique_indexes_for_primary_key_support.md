True Unique Indexes for Primary Key Support




Advantage Database Server 12  

True Unique Indexes for Primary Key Support

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| True Unique Indexes for Primary Key Support  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - True Unique Indexes for Primary Key Support Advantage Concepts master\_True\_unique\_indexes\_for\_primary\_key\_support Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > True Unique Indexes for Primary Key Support / Dear Support Staff, |  |
| True Unique Indexes for Primary Key Support  Advantage Concepts |  |  |  |  |

An ADI index order created with the "unique" property enforces all records in the table to be referenced via a unique [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)). When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be generated and the index order will not be created. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the update must be canceled or the table and index must be closed.

When using Visual FoxPro (VFP) tables, it is possible to create [candidate indexes](master_xbase_candidate_indexes.htm) in order to enforce data uniqueness. The candidate option can be used with ADI indexes for application compatibility, but it is identical to specifying the unique option on ADIs.

If you need to guarantee the uniqueness of values in one or more fields in a table, you may want to use the [Advantage Proprietary Format](master_advantage_proprietary_format.htm) and [Advantage Proprietary Unique Indexes](master_adi_unique_indexes.htm). If you need this functionality with the DBF table format, then you can use Visual FoxPro tables.