Setting an Index




Advantage Database Server 12  

     Setting an Index

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Setting an Index  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Setting an Index Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Setting\_an\_Index\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 17 - MDAC, OLE DB, ADO > Setting an Index / Dear Support Staff, |  |
| Setting an Index  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

From within an ADO application, you select an available index for one of two reasons. Either you want to sort the records in your Recordset based on the index expression, or you want to use the index to enable high-speed searches using a Recordset.

Fortunately, selecting an index that you have defined in a table's index file is straightforward. You assign the name of an index order to the Index property of a Recordset that returns either a dynamic (live) cursor or a table that is opened directly using the adCmdTableDirect command type. If you are connected to a data dictionary, the index order name can be in any of your table's auto-open indexes.

You return to the natural index order by setting the Index property of the Recordset to an empty string. Setting an index is demonstrated in the following code segment, which is associated with the Select Invoice No Index button shown in Figure 17-1:

If AdsRecordset.State <> adStateOpen Then  
    MsgBox "Please open Invoice table before setting index"  
    Exit Sub  
  End If  
AdsRecordset.Index = "Invoice No"

Note that you cannot set an index if the Recordset is already actively employing a filter. However, you can apply a filter on a Recordset that is using an index.