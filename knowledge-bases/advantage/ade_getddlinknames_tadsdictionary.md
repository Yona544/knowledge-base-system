GetDDLinkNames




Advantage Database Server 12  

TAdsDictionary.GetDDLinkNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetDDLinkNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetDDLinkNames Advantage TDataSet Descendant ade\_Getddlinknames\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetDDLinkNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves a list of the names of the links in the data dictionary.

Syntax

procedure TAdsDictionary.GetDDLinkNames( poLinkNames: TStringList );

Parameters

|  |  |
| --- | --- |
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

[GetIndexNames](ade_getindexnames.htm)

[GetTableNames](ade_gettablenames_ddictionary.htm)

[GetIndexFileNames](ade_getindexfilenames.htm)

[GetViewNames](ade_getviewnames.htm)