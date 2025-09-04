GetTablesAndLinks




Advantage Database Server 12  

TAdsDictionary.GetTablesAndLinks

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetTablesAndLinks  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetTablesAndLinks Advantage TDataSet Descendant ade\_Gettablesandlinks\_tadsdictionary\_method Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetTablesAndLinks  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

procedure TAdsDictionary.GetTablesAndLinks( poLinkNames : TStringList;

poTableNames : TStringList );

Parameters

|  |  |
| --- | --- |
| poLinkNames (O) | String list that linked dictionary names are returned in |
| poTableNames (O) | String list that table names are returned in |

Remarks

GetTablesAndLinks is similar to the [GetTableNames](ade_gettablenames_ddictionary.htm) method, except GetTablesAndLinks will also return the names of all tables that are visible in the dictionary through a link to an outside dictionary.

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

[GetTableNames](ade_gettablenames_ddictionary.htm)

[CreateDDLink](ade_createddlink_tadsdictionary.htm)

[DropDDLink](ade_dropddlink_tadsdictionary.htm)

[GetDDLinkNames](ade_getddlinknames_tadsdictionary.htm)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.htm)