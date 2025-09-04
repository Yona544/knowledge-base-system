CreateDictionary




Advantage Database Server 12  

TAdsDictionary.CreateDictionary

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.CreateDictionary  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.CreateDictionary Advantage TDataSet Descendant ade\_Createdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.CreateDictionary  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Creates a data dictionary.

Syntax

TAdsCreateDictionary.CreateDictionary( strPath : string;

bEncrypt : boolean;

strDescription : string );

Parameters

|  |  |
| --- | --- |
| strPath | Full file path of the dictionary to create. |
| bEncrypt | True will cause the data dictionary file to be encrypted. |
| strDescription | An optional description of the database in the data dictionary. If empty-string then no description is stored in the data dictionary. The database description can be added or changed later with [TAdsDictionary.SetDatabaseProperty](ade_setdatabaseproperty.htm). |

Special Error Codes

|  |  |
| --- | --- |
| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |
| AE\_DICTIONARY\_ALREADY\_EXISTS | An Advantage data dictionary already exists at the indicated path. |

Description

TAdsDictionary.CreateDictionary connects to the Advantage Database Server and creates the data dictionary files (\*.ADD, \*.AI \*.AM). It will open an ADSSYS user connection after the database has been created. This connection can be used to call other TAdsDictionary administrative methods.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

This example creates a data dictionary without encrypting the files.

procedure CreatingDDExample;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a database.');

 

{\*

\* The CreateDictionary call leaves an ADSSYS connection open. We

\* can close this connection by setting IsConneted to FALSE.

\*}

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[Create](ade_create_tadsdictionary.htm)

[Destroy](ade_destroy_tadsdictionary.htm)