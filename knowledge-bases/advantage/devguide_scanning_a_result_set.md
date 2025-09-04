Scanning a Result Set




Advantage Database Server 12  

     Scanning a Result Set

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Scanning a Result Set Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Scanning\_a\_Result\_Set Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Scanning a Result Set / Dear Support Staff, |  |
| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Scanning is the process of sequentially reading every record in a result set or table, or every record in the range and/or filtered view of the result set or table if either a filter or a range, or both, are active. In most cases, scanning involves an initial navigation to the first record of the result set or table, followed by repeated calls to advance one record until all of the records have been visited.

Although scanning is a common task, it is important to note that it necessarily requires the client application to retrieve all of the records in the result set. This is not a problem when few records are involved, but if a large number of records are being scanned, network resources may be taxed.

   
TIP: If you are using ADS, and you must scan a large number of records, implement the operation using a stored procedure as described in Chapter 7. Scanning from a stored procedure executed from ADS requires no network resources when the server and the data are located on the same machine.  
 

The following code demonstrates the scanning of an AdsTable. This code, associated with the OnClick event handler of the List Products button (shown in Figure 15-2), navigates the entire PRODUCTS table, assigning data from each record to the ProductList list box:

procedure TForm1.ListProductsBtnClick(Sender: TObject);  
begin  
  DataSource1.DataSet := nil;  
  if AdsTable1.Active then AdsTable1.Close;  
  AdsTable1.TableName := 'PRODUCTS';  
  AdsTable1.Open;  
  AdsTable1.First;  
  while not AdsTable1.EOF do  
  begin  
    ProductList.Items.Add(AdsTable1.Fields[0].AsString +  
      '      ' + AdsTable1.Fields[1].AsString);  
    AdsTable1.Next;  
  end;  
  AdsTable1.Close;  
end;