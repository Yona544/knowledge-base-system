Accessing an ADS Table




Advantage Database Server 12  

     Accessing an ADS Table

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Accessing an ADS Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Accessing an ADS Table Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Accessing\_an\_ADS\_Table Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Accessing an ADS Table / Dear Support Staff, |  |
| Accessing an ADS Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The easiest way to access data is with an AdsTable component. At a minimum, you must set the AdsTable's AdsConnection property to an AdsConnection (this is often done at design time), its TableName property to the name of a table or view you want to access, and the Active property to True. Calling the AdsTable's Open method sets the AdsTable's Active property to True.

This is demonstrated in the following event handler, which is associated with the Show Invoice Table button (shown in Figure 15-2):

procedure TForm1.ShowInvoiceBtnClick(Sender: TObject);  
begin  
  if AdsTable1.Active then AdsTable1.Close;  
  AdsTable1.TableName := 'INVOICE';  
  AdsTable1.Open;  
  DataSource1.DataSet := AdsTable1;  
end;