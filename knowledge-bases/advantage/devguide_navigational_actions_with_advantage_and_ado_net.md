Navigational Actions with Advantage and ADO.NET




Advantage Database Server 12  

     Navigational Actions with Advantage and ADO.NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Navigational Actions with Advantage and ADO.NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Navigational Actions with Advantage and ADO.NET Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Navigational\_Actions\_with\_Advantage\_and\_ADO\_NET Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 18 - The .NET Data Provider > Navigational Actions with Advantage and ADO.NET / Dear Support Staff, |  |
| Navigational Actions with Advantage and ADO.NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Most of the navigational features that you can access with other data access mechanisms, such as ADO and TDataSet, are implemented in the ADO.NET DataSet, DataTable, or DataView classes. For example, indexing, sorting, filtering, and seeking are all operations that are performed on a DataTable's cached records using a DataView. In other words, these operations do not involve Advantage, other than using Advantage as the original source of the data that is manipulated in memory.

There is, in fact, only one ADO.NET navigational operation that involves Advantage-scanning. Specifically, using an AdsDataReader (or an AdsExtendedReader, which as you learned earlier, also supports filters, ranges, and seeks), you can perform a record-by-record navigation of data. This operation is demonstrated in the following section.