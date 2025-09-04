---
title: Ade Getindexfileproperty
slug: ade_getindexfileproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getindexfileproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 243dca608793cd33cde7c8ac988e96b7333b326e
---

# Ade Getindexfileproperty

GetIndexFileProperty

TAdsDictionary.GetIndexFileProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetIndexFileProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves an index file property into the supplied buffer from the data dictionary.

Syntax

TAdsDictionary.GetIndexFileProperty( strTableName : string;

strIndexFileName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 );

Parameters

| strTableName | Name of the table in the database with the specified index. |
| strIndexFileName | Name of the index file. |
| usPropertyID | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of the property stored in the buffer. |

Remarks

TAdsDictionary.GetIndexFileProperty retrieves a property of the specified index file associated with the specified table from the data dictionary. The following are the valid values of usPropertyID and the expected return values in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_INDEX\_FILE\_PATH | Returns in pvProperty the absolute path of the index file. The pvProperty parameter should point to an array of characters (PChar type) and usPropertyLen must be passed in as the size of the array. The size of the array must be sufficient to store the full file path of the index file including the NULL terminator. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_FILE\_PAGESIZE | Returns in pvProperty the index page size of the index file. The pvProperty parameter should be a pointer to a 4-byte integer variable and usPropertyLen must be 4 - the size of the integer variable. See AdsCreateIndex61 in the Advantage Client Engine Help (ACE.HLP) for additional information on the index page size. (Note that each of the Advantage products and their corresponding Help files are installed separately.) Since configurable index page size is a new functionality introduced in the 6.1 release. An AE\_PROPERTY\_NOT\_SET error may be returned when trying to retrieve this property on a data dictionary created prior to the 6.1 release. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |

Example

This example opens a data dictionary that does not require an administrative password and retrieving the path for the index Test1.adi.

procedure GetIndexFilePropertyExample;

var

oAdsDictionary : TAdsDictionary;

oIndexFileNames : TStringList;

usLength : UNSIGNED16;

aucIndexPath : array [ 0..ADS\_MAX\_PATH ] of char;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE,

'This is a demo database.' );

{\* The CreateDictionary call leaves a connection open.\*}

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

{\* now we are going to make the call to getviewnames \*}

oIndexNames := TStringList.Create;

oAdsDictionary.GetIndexFileNames( 'offices', oIndexFileNames );

oAdsDictionary.GetIndexFileNames( 'salesreps', oIndexFileNames );

if ( oIndexFileNames.Count > 0 ) then

begin

usLength = sizeof( aucIndexPath );

oAdsDictionary.GetIndexFileProperty( 'offices',

oIndexFileNames.Strings[ 0 ],

ADS\_DD\_INDEX\_FILE\_PATH,

@aucIndexPath,

usLength );

end;

oAdsDictionary.IsConnected := FALSE;

oAdsDictionary.Free;

oIndexFileNames.Free;

end;

See Also

[SetTableProperty](ade_settableproperty.md)

[SetFieldProperty](ade_setfieldproperty.md)

[GetFieldProperty](ade_getfieldproperty.md)
