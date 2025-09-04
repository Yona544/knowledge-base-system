---
title: Ade Gettablesandlinks Tadsdictionary Method
slug: ade_gettablesandlinks_tadsdictionary_method
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_gettablesandlinks_tadsdictionary_method.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2c954dd199c09be9d0e5274efde22f34f632342b
---

# Ade Gettablesandlinks Tadsdictionary Method

GetTablesAndLinks

TAdsDictionary.GetTablesAndLinks

Advantage TDataSet Descendant

| TAdsDictionary.GetTablesAndLinks  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure TAdsDictionary.GetTablesAndLinks( poLinkNames : TStringList;

poTableNames : TStringList );

Parameters

| poLinkNames (O) | String list that linked dictionary names are returned in |
| poTableNames (O) | String list that table names are returned in |

Remarks

GetTablesAndLinks is similar to the [GetTableNames](ade_gettablenames_ddictionary.md) method, except GetTablesAndLinks will also return the names of all tables that are visible in the dictionary through a link to an outside dictionary.

The link names and table names are returned in two separate lists, primarily to allow users to combine the two names however necessary. This method was implemented with report writers in mind, so a common use might be to combine the link name and the table name with a "dot" in between for use in an SQL statement (select \* from "mylink"."mytable").

Each entry placed in poTableNames will have a corresponding entry in poLinkNames, even if the table in question lives in the current dictionary (not a linked table). If a table lives in the current dictionary, its associated link name will contain an empty string.

Note The string lists passed in must be able to accept duplicate entries. See the Delphi TStringList.Duplicates documentation for more details.

 

Note Only tables and links that the current user has access to will be returned. See Advantage Data Dictionary User Permissions for more information.

Example

procedure TForm1.Button1Click(Sender: TObject);

var

Links : TStringList;

Tables : TStringList;

i : integer;

begin

Links := TStringList.Create;

Tables := TStringList.Create;

 

try

with AdsDictionary1 do

begin

Connect;

GetTablesAndLinks( Links, Tables );

 

for i := 0 to ( Links.Count - 1 ) do

if ( Links.Strings[i] = '' ) then

Memo1.Lines.Add( Tables.Strings[i] )

else

Memo1.Lines.Add( Links.Strings[i] + '.' + Tables.Strings[i] );

end;

 

finally

Links.Free;

Tables.Free;

end;

end;

See Also

[GetTableNames](ade_gettablenames_ddictionary.md)

[CreateDDLink](ade_createddlink_tadsdictionary.md)

[DropDDLink](ade_dropddlink_tadsdictionary.md)

[GetDDLinkNames](ade_getddlinknames_tadsdictionary.md)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.md)
