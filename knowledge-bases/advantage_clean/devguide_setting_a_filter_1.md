---
title: Devguide Setting A Filter 1
slug: devguide_setting_a_filter_1
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_setting_a_filter_1.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 87f8049345968243b2a851a2ba479b75c276e04b
---

# Devguide Setting A Filter 1

Setting a Filter

     Setting a Filter

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Setting a Filter  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You use a filter to limit a Recordset to a subset of records. When executed on a server-side Recordset, Advantage produces an AOF (Advantage Optimized Filter), after which it repopulates the Recordset based on the filtered view.

You set a filter by assigning a filter expression to a Recordset's Filter property. You drop a filter by setting the Filter property to an empty string.

Although the filter expressions that you can assign to the Filter property of a Recordset are similar to those that you can set to Advantage using other mechanisms (such as using the Advantage Data Architect or the Advantage TDataSet Descendant), there is one important difference. If you include a field name that contains embedded spaces, you must enclose the field name in square brace delimiters.

Setting and dropping a filter is demonstrated in the following code, which is located in the click subprocedure for the Set Filter button shown in Figure 17-1:

If AdsRecordset.State <> adStateOpen Then  
  MsgBox "Please open Invoice table before setting a filter"  
  Exit Sub  
End If  
If FilterBtn.Caption = "Drop Filter" Then  
  AdsRecordset.Filter = ""  
  FilterBtn.Caption = "Set Filter"  
Else  
  AdsRecordset.Filter = FilterText.Text  
  FilterBtn.Caption = "Drop Filter"  
End If  
Set DataGrid1.DataSource = AdsRecordset

If you run this project, click the Show Invoice Table button and then enter the following filter expression:

[Customer ID] = 12037 and [Employee ID] = 89

Once you click the Set Filter button, the DataGrid at the bottom of the form will display only two records, as shown in Figure 17-5.

   
NOTE: Although a filter does not rely on the current index, the speed with which a filter can be applied is directly related to the available indexes on the table. Specifically, filters can be applied quickly when the expressions in the filter expression map to available indexes on the underlying table.  
 

Figure 17-5: A filter has been applied to a Recordset
