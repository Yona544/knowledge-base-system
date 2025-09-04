Full Text Search Indexes




Advantage Database Server 12  

 

     Full Text Search Indexes

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Full Text Search Indexes Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Full\_Text\_Search\_Indexes Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > Full Text Search Indexes / Dear Support Staff, |  |
| Full Text Search Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Full text search (FTS) was one of the more powerful and exciting new features to be introduced in ADS 7.0. With FTS you can find records based on the words in your text fields, including the presence or absence of specific words, the number of instances of specific words, and the proximity of specific words to each other. For example, you can select all records in which the word "punctual" appears in a comment field. Alternatively, you can select all records in which the word "performance" appears near the word "database."

Like an AOF, an FTS may be fully or partially optimized, or not optimized at all. When an FTS is not optimized, it means that Advantage must read data from every record in the table, searching for the selection criteria. As you can imagine, unless your table is relatively small, an FTS that is not optimized can be slow.

In order to have a fully or partially optimized FTS, you must create one or more FTS index orders. An FTS index order contains one key for each search word in each record. A fully optimized FTS can determine which records contain the search words from the FTS index alone. A partially optimized FTS refers to the records that might satisfy the search criteria, but Advantage must read the individual records identified by the index to complete the operation.

For example, imagine that you want to search for all records that contain the word "database" in the Comments field. If you have created an FTS index order on the Comments field, the selection of which records contain this word can be performed exclusively through the index. However, in order to find those records in which the word "performance" appears in proximity to the word "database," an FTS is used initially to identify those records that contain both words in the Comments field, but a record-by-record examination of those identified records is necessary to make a final determination. Such a search is partially optimized.

You can create FTS index orders for both ADT tables and for FoxPro DBF tables that use CDX indexes. You cannot create FTS index orders for Clipper DBF tables that use NTX indexes. You can still perform FTS selections on Clipper tables, but they will not be optimized by definition.