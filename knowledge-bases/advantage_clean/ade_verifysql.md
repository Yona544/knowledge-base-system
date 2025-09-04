---
title: Ade Verifysql
slug: ade_verifysql
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_verifysql.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ff950e9ae939e6b716daf5ecc4d8fe60288efd55
---

# Ade Verifysql

VerifySQL

TAdsQuery.VerifySQL

Advantage TDataSet Descendant

| TAdsQuery.VerifySQL  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Verifies the validity of an SQL statement without executing it.

Syntax

procedure VerifySQL;

Description

VerifySQL sends the SQL statement residing in TAdsQuery.SQL to the Advantage Database Server to determine if it is a valid SQL statement. This is useful to call prior to executing a time consuming SQL statement. In the event of an invalid statement, an exception will be raised with the corresponding error message in the exception object.

Example

try

AdsConnection1 := TAdsConnection.Create( nil );

AdsQuery1 := TAdsQuery.Create( nil );

 

AdsConnection1.AdsServerTypes := [stADS\_LOCAL];

AdsConnection1.ConnectPath := 'c:\testdata';

AdsConnection1.Name := 'Conn';

 

AdsQuery1.SourceTableType := ttAdsADT;

AdsQuery1.DatabaseName := 'Conn';

AdsQuery1.SQL.Add('SELECT \* from demo10');

AdsQuery1.VerifySQL;

AdsQuery1.ExecSQL;

 

except

on E: Exception do

Application.MessageBox(PChar(E.Message), 'Error', MB\_OK);

end;
