GetTableAndLinkNames




Advantage Database Server 12  

TAdsConnection.GetTableAndLinkNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetTableAndLinkNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetTableAndLinkNames Advantage TDataSet Descendant ade\_Gettableandlinknames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetTableAndLinkNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Syntax

procedure TAdsConnection.GetTableAndLinkNames( poLinkNames : TStrings; poTableNames : TStrings;

strFileMask : String );

Parameters

|  |  |
| --- | --- |
| poLinkNames (O) | String list that linked dictionary names are returned in. |
| poTableNames (O) | String list that table names are returned in. |
| strFileMask (I) | Mask to use for the search (when not on a dictionary connection). |

Remarks

GetTableAndLinkNames is similar to the [GetTableNames](ade_gettablenames.htm) method, except GetTableAndLinkNames will also return the names of all tables that are visible in dictionaries through a dictionary link. If called on a free connection GetTableAndLinkNames will behave just as [GetTableNames](ade_gettablenames.htm) does.

The link names and table names are returned in two separate lists, primarily to allow users to combine the two names however necessary. This method was implemented with report writers in mind, so a common use might be to combine the link name and the table name with a "dot" in between for use in an SQL statement (select \* from "mylink"."mytable").

Each entry placed in poTableNames will have a corresponding entry in poLinkNames, even if the table in question is not a linked table. If a table is not a linked table, its associated link name will contain an empty string.

The TAdsConnection.[IsConnected](ade_isconnected_tadsconnection.htm) property must be set to True before calling GetTableAndLinkNames. If GetTableAndLinkNames is called on a connection that uses the TAdsConnection.ConnectPath property, all files matching the strFileMask parameter will be returned. If GetTableAndLinkNames is called on a connection that uses the TAdsConnection.AliasName property, tables matching the alias tabletype will be returned, and the strMask parameter will be ignored. If GetTableAndLinkNames is called using an alias that points to an Advantage Data Dictionary, or a connection path that points to an Advantage Data Dictionary, the strFileMask parameter will be ignored, and all tables registered in the data dictionary will be returned.

Note The string lists passed in must be able to accept duplicate entries. See the Delphi TStringList.Duplicates documentation for more details.

Example

procedure TForm1.Button5Click(Sender: TObject);

var

Links : TStringList;

Tables : TStringList;

i : integer;

begin

Links := TStringList.Create;

Tables := TStringList.Create;

 

try

with AdsConnection1 do

begin

Connect;

GetTableAndLinkNames( Links, Tables, '' );

 

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

[GetTableNames](ade_gettablenames.htm)