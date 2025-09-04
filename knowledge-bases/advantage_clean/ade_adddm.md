---
title: Ade Adddm
slug: ade_adddm
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adddm.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 120726aad8266ecf3a39aecb662c12e757b1fae3
---

# Ade Adddm

AddDM

TAdsAEPSessionMgr.AddDM

Advantage TDataSet Descendant

| TAdsAEPSessionMgr.AddDM  Advantage TDataSet Descendant |  |  |  |  |

[TAdsAEPSessionMgr](ade_tadsaepsessionmgr.md)

Adds an Identifier/DataModule pair to the session manager.

Syntax

procedure AddDM( id : integer; dm : TDataModule )

Parameters

The id parameter is the unique value used to locate this data module with other TAdsAEPSessionMgr methods. It is recommended you pass the connection identifier (ulConnectionID) that is passed to all AEP functions in this parameter.

The dm parameter is a pointer to a TDataModule object.

Description

Call AddDM to add a data module to the list of modules maintained by a TAdsAEPSessionMgr object.

Example

function Startup( ulConnectionID: UNSIGNED32; pucUserName: PChar; pucPassword: PChar ): UNSIGNED32; stdcall; // Do not change the prototype.   
var  
  dm1 : TDM1;   
begin  
  Result := AE\_SUCCESS;   
  DM1 := TDM1.Create( nil );   
   
  try   
    {\* Open the data module and configure DataConn to point to your data   
    \* dictionary. \*}   
    DM1.DataConn.UserName := StrPas( pucUserName );  
    DM1.DataConn.Password := StrPas( pucPassword );   
    DM1.DataConn.Connect;  
   
    {\* Place tables on the data module, assign DataConn as their Databasname   
     \* property, and then open them here. \*}   
  except on E : EAdsDatabaseError do   
    Result := E.ACEErrorCode;   
  end;   
   
  {\* Add this data module to the session manager, so we can retrieve it for   
   \* the user identified by ulConnectionID the next time they need it. \*}   
  AEPSessionMgr.AddDM( ulConnectionID, DM1 );   
   
end;

See Also

[GetDM](ade_getdm.md)

[FreeDM](ade_freedm.md)
