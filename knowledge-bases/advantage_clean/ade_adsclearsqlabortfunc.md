---
title: Ade Adsclearsqlabortfunc
slug: ade_adsclearsqlabortfunc
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclearsqlabortfunc.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a326302b3d508ad8bbc3b6412fbeacad6b08216e
---

# Ade Adsclearsqlabortfunc

AdsClearSQLAbortFunc

TAdsQuery.AdsClearSQLAbortFunc

Advantage TDataSet Descendant

| TAdsQuery.AdsClearSQLAbortFunc  Advantage TDataSet Descendant |  |  |  |  |

Clears the SQL abort callback function registered using AdsRegisterSQLAbortFunc.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md) and [AdsClearCallbackFunction](ade_adsclearcallbackfunction.md) instead, as they work better with threads and have more complete functionality.

Syntax

procedure AdsClearSQLAbortFunc;

Description

AdsClearSQLAbortFunc will make the Advantage Client Engine stop calling the registered callback function. AdsRegisterSQLAbortFunc is used to abort an SQL query.

Example

function MySQLAbortFunc : Longint ; stdcall;

begin

if ( gbCancelRequested ) then

Result := 1

else

Result := 0;

end;

 

procedure TForm1.RegisterButtonClick(Sender: TObject);

begin

AdsQuery1.AdsRegisterSQLAbortFunc( @MySQLAbortFunc );

end;

 

procedure TForm1.ClearButtonClick(Sender: TObject);

begin

AdsQuery1.AdsClearSQLAbortFunc;

end;

See Also

[AdsRegisterSQLAbortFunc](ade_adsregistersqlabortfunc.md)
