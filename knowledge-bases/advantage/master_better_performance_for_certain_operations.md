Better Performance for Certain Operations




Advantage Database Server 12  

Better Performance for Certain Operations

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Better Performance for Certain Operations  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Better Performance for Certain Operations Advantage Concepts master\_Better\_performance\_for\_certain\_operations Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > Better Performance for Certain Operations / Dear Support Staff, |  |
| Better Performance for Certain Operations  Advantage Concepts |  |  |  |  |

The Advantage proprietary file format is optimized for use by Advantage and thus provides better performance for certain operations versus performing those operations on Xbase files.

Advantage proprietary ADI index files support per index order write locking and updating. Thus, if an ADI index file contains multiple index orders, then different Advantage applications can obtain a write lock and make updates to different index orders in the same index file at the same time. This "per index order write locking and updating" functionality does not exist in Xbase file formats. If you have compound index files with many index orders, and concurrent updates to the database are occurring, the updates of the index files will be faster with Advantage proprietary index files than with Xbase index files.

When reading memo field data with Xbase file formats, it requires two operations be sent to the Advantage Database Server. One to get the length of the memo data from the memo file, and the other to read that length of memo data from the memo file. With the Advantage proprietary file format, the length of the memo data is stored in the memo field in an ADT record. Therefore it requires just a single operation be sent to the Advantage Database Server to read memo data. Retrieval of ADM memo data should be nearly twice as fast as retrieval of Xbase memo data.

Advantage proprietary ADI index key data is always stored in binary collating order. Internal comparisons of ADI keys can always be done with a simple left to right comparison, regardless of data type. Xbase index file key data is not always stored in binary collating order. Conversion of Xbase key data is sometimes necessary before comparison operations can be performed. When using non-USA collation with character data index keys, Xbase key data comparison is always adversely affected. Index lookups and updates will almost always be faster with the Advantage proprietary file format than with Xbase file formats.

Xbase file formats do not remove deleted records from DBF tables, nor are index keys that reference those deleted records removed from index orders. If an application is configured to "hide" deleted Xbase records, those deleted records must be filtered out by the Advantage Database Server even when traversing the data in indexed order. The Advantage proprietary file format never has index [keys](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) referencing records that have been deleted. Deleted record filtering is never necessary when traversing data in an indexed order. Thus, record traversal in indexed order will be faster with the Advantage proprietary file format than with Xbase file formats.

When appending or inserting records into an Xbase table, a new record is always added to the end of the table. When appending or inserting records into an Advantage proprietary file format table, a record that has been previously deleted will be reused rather than adding a new record to the end of a table. Since increasing the size of a file takes time, appends and insertions of records into a table will be faster on average with Advantage proprietary tables than with Xbase tables.

The Advantage Transaction Processing System (TPS) uses internal lists in memory to keep track of what data is pre-transaction data, which is only visible to the applications not involved with the transaction, and what data has been updated within the transaction, which is only visible to the application in the midst of the transaction. This TPS visibility functionality is slightly faster with Advantage proprietary file format than Xbase file formats due to extra data stored in the record that indicates to the Advantage Database Server which user has updated the record during a transaction.

Several field types take less storage space with Advantage proprietary ADT tables than with Xbase DBF tables. This leads to smaller record sizes with ADTs than with DBFs. Smaller record sizes mean less data on the network, and thus faster transfer of records across the network when using Advantage proprietary tables rather than Xbase tables.