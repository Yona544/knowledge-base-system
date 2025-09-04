---
title: Devguide Finding A Record Based On Data
slug: devguide_finding_a_record_based_on_data
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_finding_a_record_based_on_data.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: e31e825c7e98b79b2d80d158dda137c76f2dc75c
---

# Devguide Finding A Record Based On Data

Finding a Record Based on Data

     Finding a Record Based on Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Finding a Record Based on Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

TDataSets support a number of methods for locating records based on their contents. These include FindKey, FindNearest, and Locate, in addition to the brute-force method of scanning through every record in the table. Of these techniques, FindKey and FindNearest are the fastest and easiest to use for locating a record using the currently selected index.

Both of these methods take a single parameter consisting of a constant array. You represent a constant array by enclosing one or more values within brackets, separating the values using commas when there is more than one value. Both of these methods search for the first element of the array in the first field of the current index, then search for the second value, if present, in the second field of the current index, and so on.

FindKey is a Boolean function that returns True if a matching record is found. If FindKey returns True, the located record is made the current record. FindNearest is a procedure. It always repositions the current record to the closest match to the search criteria (which might actually be the current record).

The use of FindNearest is demonstrated in the following event handler. This event handler is associated with the OnChange event of the Edit named SearchText. After clicking the Show Invoice Table and the Set Invoice No Index buttons, this code permits an incremental search through the INVOICE table:

procedure TForm1.SearchTextChange(Sender: TObject);  
begin  
  if (not AdsTable1.Active) or  
    (AdsTable1.TableName <> 'INVOICE') or  
    (AdsTable1.IndexName <> 'Invoice No') then  
    begin  
      ShowMessage('Click Show Invoice Table and Select ' +  
        'Invoice No Index before performing an ' +  
        'incremental search');  
      Exit;  
    end;  
  AdsTable1.FindNearest([SearchText.Text]);  
end;

   
NOTE: Unlike the BDE, ADS employs indexes with the Locate and Lookup methods whenever appropriate indexes are available, and creates AOFs (Advantage Optimized Filters) when they are not available. As a result, these methods are much faster than their BDE counterparts. However, Locate and Lookup are more complicated to use than FindKey and FindNearest. For information on using Locate and Lookup, refer to the Advantage help.
