---
title: Devguide Using A Parameterized Query
slug: devguide_using_a_parameterized_query
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_a_parameterized_query.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: bdfbc00de69da92cba8833d1e15555f35baf709d
---

# Devguide Using A Parameterized Query

Using a Parameterized Query

     Using a Parameterized Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using a Parameterized Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The AdsQuery component supports both named and positional parameters. You must bind data to every parameter of a parameterized query prior to executing it. You can do this either using the Params property, which is a collection property indexed by parameter position, or the ParamByName method, which takes a parameter name as an argument. Both of these approaches return a TParam, which you use to assign a value to the parameter.

The AdsQuery2 component on this project's main form has the following SQL statement assigned to its SQL property:

SELECT \* FROM INVOICE WHERE [Customer ID] = :cust

The parameter, named cust, is bound and the query executed from the event handler shown in the following code segment. This event handler is associated with the Show Invoices button (shown in Figure 15-2):

procedure TForm1.ShowInvoicesBtnClick(Sender: TObject);  
begin  
  if AdsQuery2.Active then AdsQuery2.Close;  
  if ParamText.Text = '' then  
  begin  
    ShowMessage('Please enter a customer number');  
    Exit;  
  end;  
  AdsQuery2.Params[0].AsInteger := StrToInt(ParamText.Text);  
  AdsQuery2.Open;  
  DataSource1.DataSet := AdsQuery2;  
end;
