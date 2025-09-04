---
title: Devguide Finding A Record Based On Data 1
slug: devguide_finding_a_record_based_on_data_1
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_finding_a_record_based_on_data_1.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 5fa3925365149a0b7c9449431ebea8ba934faca8
---

# Devguide Finding A Record Based On Data 1

Finding a Record Based on Data

     Finding a Record Based on Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Finding a Record Based on Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADO supports two methods for searching for data in a Recordset. One of these, Find, performs a record-by-record search for data. When used with server-side cursors, these sequential reads are performed by ADS, but nonetheless the sequential nature of this operation means that it is often relatively slowespecially when the result set is large.

The second method, Seek, is only supported in server-side cursors by OLE DB providers that also support indexes and fortunately, the Advantage OLE DB Provider is one of them. Unlike Find, Seek uses Advantage indexes on server-side cursors to quickly locate records. Compared to Find, Seek is typically much faster at finding records with server-side cursors.

Before you can call Seek on a Recordset, you must set an index that you will use to find the record you are looking for. Once the index is set, you call Seek, passing either a single value or an array of values. If you pass a single value, ADS will search the current index for that value in the first field of the index.

You pass an array of values to Seek when you want to search on more than one expression of a multisegment index order. (A multisegment index order is based on two or more fields or expressions.) In this case, Seek searches for the first array element in the first field or expression of the current index, then searches the second array element, if present, in the second field or expression of the current index, and so on.

The second, optional parameter, SeekOption, defines how the Seek is performed. Valid values for this second parameter include adSeekAfter, adSeekAfterEQ, adSeekBefore, adSeekBeforeEQ, adSeekFirstEQ, and adSeekLastEQ. The default value is adSeekFirstEQ.

If a matching record is found, based on the SeekOption, the record associated with the value or values is made the current record. If the value or values are not found, the Recordset will point to the end-of-file marker.

The use of Seek is demonstrated in the following code segment. This code is associated with the change event of the TextBox named SearchText. After clicking the Show Invoice Table and Set Invoice No Index buttons, this code permits an incremental search through the INVOICE table:

If AdsRecordset.State <> adStateOpen Then  
  MsgBox "Please open Invoice table before searching  
    for an invoice"  
  Exit Sub  
End If  
If AdsRecordset.Index <> "Invoice No" Then  
  MsgBox "You must set the Invoice No index " + \_"  
    "before searching"  
  Exit Sub  
End If  
AdsRecordset.Seek SearchText.Text, adSeekAfterEQ  
If AdsRecordset.EOF Then  
  MsgBox "End of file"  
End If
