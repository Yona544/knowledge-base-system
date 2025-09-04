---
title: Ade Getddlinknames Tadsdictionary
slug: ade_getddlinknames_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getddlinknames_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a23aa8cc97ddd0ddca7211bd5d0578b0967466b9
---

# Ade Getddlinknames Tadsdictionary

GetDDLinkNames

TAdsDictionary.GetDDLinkNames

Advantage TDataSet Descendant

| TAdsDictionary.GetDDLinkNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves a list of the names of the links in the data dictionary.

Syntax

procedure TAdsDictionary.GetDDLinkNames( poLinkNames: TStringList );

Parameters

| poLinkNames (I/O) | A TStringList to hold the returned link names. |

Remarks

TAdsDictionary.GetDDLinkNames will retrieve all the data dictionary link objects names associated with the data dictionary.

Example

The following example opens a data dictionary and gets all of the associated link names.

procedure GetLinkNames;

var

oDictionary : TAdsDictionary;

oLinkNames : TStringList;

begin

 

try

{\* Create the components \*}

oDictionary := TAdsDictionary.Create( nil );

oLinkNames := TStringList.Create;

 

oDictionary.ConnectPath := 'n:\MyData\Master.add';

oDictionary.AdsServerTypes := [stADS\_REMOTE];

oDictionary.UserName := 'AdsSys';

oDictionary.Password := 'SuperSecret';

oDictionary.LoginPrompt := False;

 

oDictionary.IsConnected := True;

 

{\* Get the names \*}

oDictionary.GetDDLinkNames( oLinkNames );

 

finally

 

if ( Assigned( oLinkNames ) ) then

begin

FreeAndNil( oLinkNames );

end;

 

if ( Assigned( oDictionary ) ) then

begin

FreeAndNil( oDictionary );

end

end;

end;

See Also

[GetIndexNames](ade_getindexnames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)

[GetViewNames](ade_getviewnames.md)
