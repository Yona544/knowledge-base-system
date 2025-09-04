---
title: Ade Getindexproperty
slug: ade_getindexproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getindexproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: df18c997cb462b93fecc27ed03b215035f9947c7
---

# Ade Getindexproperty

GetIndexProperty

TAdsDictionary.GetIndexProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetIndexProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves an index property into the supplied buffer from the data dictionary.

Syntax

TAdsDictionary.GetIndexProperty( strTableName : string;

strIndexName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 );

Parameters

| strTableName | Name of the table in the database with the specified index. |
| strIndexName | Name of the index. |
| usPropertyID | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of the property stored in the buffer. |

Remarks

TAdsDictionary.GetIndexProperty retrieves a property of the specified index associated with the specified table from the data dictionary. The following are the valid values of usPropertyID and the expected return values in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_INDEX\_FILE\_NAME | Returns in pvProperty the name of the index file where the index is located. The pvProperty parameter should point to an array of characters (PChar type) and usPropertyLen must be passed in as the size of the array. The size of the array must be sufficient to store the name of the index file including the NULL terminator. |
| ADS\_DD\_INDEX\_EXPRESSION | Returns in pvProperty the index expression of the index. The pvProperty parameter should point to an array of characters (PChar type) and usPropertyLen must be passed in as the size of the pvProperty buffer. The size of the array must be sufficient to store the index expression including the NULL terminator. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_CONDITION | Returns in pvProperty the index condition of the index. The pvProperty parameter should point to an array of characters (PChar type) and usPropertyLen must be passed in as the size of the pvProperty buffer. The size of the array must be sufficient to store the index condition including the NULL terminator. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_OPTIONS | Returns in pvProperty the index options of the index. The pvProperty parameter should be a pointer to a 4-byte integer variable and usPropertyLen must be 4 - the size of the integer variable. The index options are ORed together into the bit field. The possible options in the bit field are ADS\_COMPOUND, ADS\_DESCENDING, ADS\_UNIQUE, and ADS\_CANDIDATE. See [AdsCreateIndex](ade_adscreateindex.md) for additional information on the index options. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_KEY\_LENGTH | Returns the length of the keys in the index. The pvProperty parameter should be a pointer to a 2-byte unsigned integer variable (WORD) and usPropertyLen must be 2 - the size of the integer variable. |
| ADS\_DD\_INDEX\_KEY\_TYPE | Returns the type of the keys in the index. The pvProperty parameter should be a pointer to a 2-byte unsigned integer variable (WORD) and usPropertyLen must be 2 - the size of the integer variable. Possible key types are ADS\_STRING, ADS\_NUMERIC, ADS\_DATE, ADS\_LOGICAL, and ADS\_RAW. See [AdsGetKeyType](ade_adsgetkeytype.md) for additional information. |

Example

procedure GetIndexPropertyExample;

 

var

 

oAdsDictionary : TAdsDictionary;

 

oIndexNames : TStringList;

 

usLength : UNSIGNED16;

 

aucIndexExpression : array [ 0..ADS\_MAX\_INDEX\_EXPR\_LEN] of char;

 

begin

 

{\* call the constructor \*}

 

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

 

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE,

'This is a demo database.' );

 

{\* The CreateDictionary call leaves an administrative

connection open.\*}

 

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

 

oAdsDictionary.GetIndexNames( 'offices', oIndexNames );

 

oAdsDictionary.GetIndexNames( 'salesreps', oIndexNames );

 

usLength := sizeof( aucIndexExpression );

 

oAdsDictionary.GetIndexProperty( 'offices',

 

oIndexNames.Strings[ 0 ],

 

ADS\_DD\_INDEX\_EXPRESSION,

 

@aucIndexExpression ,

 

usLength );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

oIndexNames.Free;

 

end;

See Also

[SetTableProperty](ade_settableproperty.md)

[SetFieldProperty](ade_setfieldproperty.md)

[GetFieldProperty](ade_getfieldproperty.md)
