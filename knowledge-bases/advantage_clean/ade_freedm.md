---
title: Ade Freedm
slug: ade_freedm
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_freedm.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ad10a695aa8dd8599fe9ee19a55c02088766ae42
---

# Ade Freedm

FreeDM

TAdsAEPSessionMgr.FreeDM

Advantage TDataSet Descendant

| TAdsAEPSessionMgr.FreeDM  Advantage TDataSet Descendant |  |  |  |  |

[TAdsAEPSessionMgr](ade_tadsaepsessionmgr.md)

Destroys a data module stored in the session manager.

Syntax

procedure FreeDM( id : integer )

Parameters

The id parameter is the unique value used to identify this data module in a previous call to the AddDM method.

Description

Call FreeDM to free the memory associated with a data module stored with a previous call to If you would like to close tables or perform other clean-up actions do so in the data modules OnDestroy event.

Example

function Shutdown( ulConnectionID: UNSIGNED32;

pucUserName: PChar;

pucPassword: PChar

): UNSIGNED32; stdcall; // Do not change the prototype.

begin

 

Result := AE\_SUCCESS;

 

if assigned( AEPSessionMgr ) then

AEPSessionMgr.FreeDM( ulConnectionID );

 

end;

See Also

[AddDM](ade_adddm.md)

[GetDM](ade_getdm.md)
