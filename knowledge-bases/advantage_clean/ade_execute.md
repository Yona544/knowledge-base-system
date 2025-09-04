---
title: Ade Execute
slug: ade_execute
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_execute.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9e834ef4d65485556817beb427b86261ad44392d
---

# Ade Execute

Execute

TAdsConnection.Execute

Advantage TDataSet Descendant

| TAdsConnection.Execute  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Executes an SQL Statement

Syntax

function Execute( const SQL: string; Params: TParams = nil; Cache: Boolean = False;

Cursor: PADSHANDLE = nil): Integer; overload; virtual;

 

function Execute(oAdsDatasetOptions : TAdsDatasetOptions; const SQL: string;

Params: TParams = nil; Cache: Boolean = False;

Cursor: PADSHANDLE = nil): Integer; overload; virtual;

 

TAdsDatasetOptions = record

musAdsLockType : UNSIGNED16; { Specific table lock type }

musAdsCharType : UNSIGNED16; { Specific char type }

musAdsRightsCheck : UNSIGNED16; { rights checking is enabled }

musAdsTableType : UNSIGNED16; { Table type }

end;

Description

Use Execute to execute an SQL statement without the overhead of using a TAdsQuery object. Execute supports SQL statements that DO NOT return a result set.

SQL is a string value containing the statement to be executed.

Params is a TParams object containing the parameter values to use in the statement.

Cache is a boolean value used to specify whether a cached statement handle should be re-used when executing this statement. If executing the same statement multiple times setting this parameter to TRUE can significantly enhance performance. If this parameter is TRUE and you are executing multiple statements that are different (different SQL string) you may quickly consume server resources.

The Cursor parameter is used internally and should never be passed to this function by an application developer.

oAdsDatasetOptions is a record that can be used to pass statement options to the Execute method. This record is only necessary if you require options other than the defaults. The option values are defined in ace.pas

musAdsLockType options: ADS\_PROPRIETARY\_LOCKING, ADS\_COMPATIBLE\_LOCKING

default: ADS\_PROPRIETARY\_LOCKING

 

musAdsCharType options: ADS\_ANSI, ADS\_OEM

default: ADS\_ANSI

 

musAdsRightsCheck options: ADS\_CHECKRIGHTS, ADS\_IGNORERIGHTS

default: ADS\_CHECKRIGHTS

 

musAdsTableType options: ADS\_ADT, ADS\_CDX, ADS\_VFP

default: ADS\_ADT

Note This method is not supported for Delphi3 or C++Builder3.

The return value is an integer representation of the number of rows affected by the statement.

Example 1

procedure Tform1.Test ( cache : boolean );

var

i : integer;

params : tparams;

begin

adsconnection1.connect;

 

params := tparams.create();

params.CreateParam( ftInteger, 'empid', ptInput );

 

for i := 0 to 40000 do

begin

params[0].Value := i;

adsconnection1.Execute( 'insert into demo10 (empid) values (:empid)', params, cache );

 

if ( i mod 50 ) = 0 then

begin

label1.caption := inttostr( i );

application.processmessages;

end;

end;

 

adsconnection1.Disconnect;

end;

Example 2

procedure Tform1.Test ( cache : boolean );

var

i : integer;

params : tparams;

stDataSetOptions : TAdsDatasetOptions;

begin

adsconnection1.connect;

 

params := tparams.create();

params.CreateParam( ftInteger, 'empid', ptInput );

 

stDataSetOptions.musAdsLockType := ADS\_COMPATIBLE\_LOCKING;

stDataSetOptions.musAdsCharType := ADS\_OEM;

stDataSetOptions.musAdsRightsCheck := ADS\_IGNORERIGHTS;

stDataSetOptions.musAdsTableType := ADS\_CDX;

 

for i := 0 to 40000 do

begin

params[0].Value := i;

adsconnection1.Execute( stDataSetOptions, 'insert into demo10 (empid) values (:empid)', params, cache );

 

if ( i mod 50 ) = 0 then

begin

label1.caption := inttostr( i );

application.processmessages;

 

end;

end;

 

adsconnection1.Disconnect;

end;
