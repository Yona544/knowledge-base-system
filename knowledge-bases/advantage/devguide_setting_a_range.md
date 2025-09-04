Setting a Range




Advantage Database Server 12  

     Setting a Range

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Setting a Range  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Setting a Range Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Setting\_a\_Range Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Setting a Range / Dear Support Staff, |  |
| Setting a Range  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Delphi uses the term range instead of scope, but it means the same thing. A range defines a subset of records to view in a table, based on an index.

You set a range in Delphi by calling SetRange. This method takes two parameters, both of which are constant arrays. The first constant array contains the beginning values of the range, where the first value defines the beginning of the range based on the first field of the current index, the second value, if present, defines the beginning of the range on the second field of the index, and so on. The second constant array contains the ending values of the range, again on a field-by-field basis, based on the current index.

The following code, which is associated with the OnClick event handler of the Set Range button, demonstrates how to apply a range:

procedure TForm1.SetRangeBtnClick(Sender: TObject);  
begin  
  if SetRangeBtn.Caption = 'Set Range' then  
  begin  
    if (not AdsTable1.Active) or  
      (AdsTable1.TableName <> 'INVOICE') or  
      (AdsTable1.IndexName <> 'Invoice No') then  
      begin  
        ShowMessage('Click Show Invoice Table ' +  
          'and Select Invoice '+  
          'No Index before setting a range');  
        Exit;  
      end;  
    AdsTable1.SetRange([StartRange.Text], [EndRange.Text]);  
    SetRangeBtn.Caption := 'Clear Range';  
  end  
  else  
  begin  
    AdsTable1.CancelRange;  
    SetRangeBtn.Caption := 'Set Range';  
  end;  
end;

An example of a range set on the INVOICE table is shown in Figure   
15-5. Notice that there are only three records, out of more than 2,000 records, in this range.

Figure 15-5: A range limits the records available in a table

   
NOTE: If you are testing this code and you set a range, clear the range before continuing to the next section. Clear the range by clicking the Clear Range button (the button whose caption alternates between Set Range and Clear Range).