---
title: Devguide Setting A Filter
slug: devguide_setting_a_filter
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_setting_a_filter.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 7438bb7e3874070a929ee39ebfe349b71348553a
---

# Devguide Setting A Filter

Setting a Filter

     Setting a Filter

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Setting a Filter  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A filter is similar to a range in that it can limit a table to a subset of records. Unlike a range, however, a filter does not rely on the current index.

You set a filter by assigning a filter expression to an AdsTable's Filter property, and then setting the Filtered property to True. You drop a filter by setting the Filter property to an empty string or by setting Filtered to False (or both). Setting and dropping a filter is demonstrated in the following code, which is located in the OnClick event handler for the Set Filter button (shown in Figure 15-2):

procedure TForm1.FilterBtnClick(Sender: TObject);  
begin  
if FilterBtn.Caption = 'Drop Filter' then  
  begin  
    AdsTable1.Filtered := False;  
    FilterBtn.Caption := 'Set Filter';  
  end  
  else  
  begin  
    if (not AdsTable1.Active) or  
      ( not (DataSource1.DataSet is TAdsTable)) then  
      begin  
        ShowMessage('Please open a table before '+  
          'setting a filter');  
        Exit;  
      end;  
    AdsTable1.Filter := FilterText.Text;  
    AdsTable1.Filtered := True;  
    FilterBtn.Caption := 'Drop Filter';  
  end;  
end;

If you run this project and click the Show the Invoice Table button, and then enter the following filter expression, the DBGrid at the bottom of the form will display only two records if you click the Set Filter button:

Customer ID = 12037 and Employee ID = 89

   
NOTE: Although a filter does not rely on the current index, the speed with which a filter can be applied is directly related to the available indexes on the table. Specifically, filters use AOFs. (AOFs are described in Chapter 3.) As a result, filters can be applied quickly when the expressions in the filter expression map to available indexes on the underlying table. By comparison, filters applied when you use the BDE do not use indexes, making filters under Advantage significantly faster than the corresponding filters under the BDE.  
 

 

   
NOTE: If you are testing this code, and you set a filter, drop the filter before continuing to the next section. Drop the filter by clicking the Drop Filter button (the button whose caption alternates between Set Filter and Drop Filter).
