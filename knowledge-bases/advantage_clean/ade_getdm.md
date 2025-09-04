---
title: Ade Getdm
slug: ade_getdm
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getdm.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: de15ae898f4da8c7198c1502de344c0ee03084c0
---

# Ade Getdm

GetDM

TAdsAEPSessionMgr.GetDM

Advantage TDataSet Descendant

| TAdsAEPSessionMgr.GetDM  Advantage TDataSet Descendant |  |  |  |  |

[TAdsAEPSessionMgr](ade_tadsaepsessionmgr.md)

Retrieves the data module associated with the identifier passed in the id parameter.

Syntax

function GetDM( id : integer ) : TDataModule

Description

Call GetDM to retrieve a pointer to a data module stored with a previous call to [AddDM](ade_adddm.md).

Parameters

The id parameter is the unique value used to identify this data module in a previous call to the AddDM method.

Example

function MyProcedure( ulConnectionID: UNSIGNED32;

pusUserName: PChar;

pucPassword: PChar;

pucProcName: PChar;

ulRecNum: UNSIGNED32;

pucTable1: PChar;

pucTable2: PChar ): UNSIGNED32; stdcall; // Do not change prototype

var

DM1 : TDM1;

begin

 

Result := AE\_SUCCESS;

 

{\* Get this connection's data module from the session manager. \*}

DM1 := TDM1( AEPSessionMgr.GetDM( ulConnectionID ) );

 

{\* Use the ParamsConn connection to retrieve any input parameters passed

\* to this procedure. \*}

DM1.ParamsConn.Disconnect;

DM1.ParamsConn.ConnectPath := ExtractFileDir( StrPas( pucTable1 ) );

 

with DM1 do

begin

tblInput.tablename := ExtractFileName( StrPas( pucTable1 ) );

tblOutput.tablename := ExtractFileName( StrPas( pucTable2 ) );

 

{\* The code commented out below shows how input parameters may be

\* read. \*}

// tblInput.open;

// strManufacturer := tblInput.FieldByName( 'mfr' ).Value;

// strProduct := tblInput.FieldByName( 'product' ).Value;

// tblInput.close;

 

 

{\* Place to business logic of your procedure here. \*}

 

 

{\* Finally return any output parameters. \*}

// tblOutput.open;

// tblOutput.append;

// tblOutput.FieldByName( 'total\_price' ).Value := 68.99;

// tblOutput.post;

// tblOutput.close;

 

end; {\* with DM1 \*}

 

end;

See Also

[AddDM](ade_adddm.md)

[FreeDM](ade_freedm.md)
