---
title: Ade Removetable
slug: ade_removetable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removetable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d54a184ea6dfe37d2bb0c057e21933ed8cf3f784
---

# Ade Removetable

RemoveTable

TAdsDictionary.RemoveTable

Advantage TDataSet Descendant

| TAdsDictionary.RemoveTable  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Disassociates a table with the data dictionary.

Syntax

TAdsDictionary.RemoveTable( strTableName : string;

bDelete : boolean );

Parameters

| strTableName | Name of the table identifying the table object in the data dictionary. |
| bDelete | If this parameter is TRUE, the physical files will be removed from storage permanently. |

Remarks

TAdsDictionary.RemoveTable disassociates a table, its memo file and its index files with the data dictionary. It can also optionally remove the table, memo and index files permanently. After an ADT table is disassociated with the data dictionary, it can be opened through regular non-data dictionary bound connection.

DROP permissions on the table are required to remove a table from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note TAdsDictionary.RemoveTable requires exclusive open of the table. An error will be returned if the table cannot be opened exclusively. If the table is the parent of any referential integrity in the data dictionary, the function will return an error.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveTableExample;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

{\* now we are going to add a couple tables from our sample tables \*}

oAdsDictionary.AddTable( 'offices',

'd:\demo\offices.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddTable( 'salesreps',

'd:\demo\salesreps.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.RemoveTable( 'salesreps', TRUE );

oAdsDictionary.RemoveTable( 'offices', FALSE );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

end;

See Also

[AddTable](ade_addtable.md)
