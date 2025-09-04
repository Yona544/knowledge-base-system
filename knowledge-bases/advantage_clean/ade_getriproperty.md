---
title: Ade Getriproperty
slug: ade_getriproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getriproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 726a03bbc4d91b2aa5333e256c5da4635b8bd7ba
---

# Ade Getriproperty

GetRIProperty

TAdsDictionary.GetRIProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetRIProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Gets the selected property for the Referential Integrity object.

Syntax

TAdsDictonary.GetRIProperty( strRIName : string;

usPropertyID : UNSIGNED16;

pvProperty : pointer;

var usLength : UNSIGNED16 );

Parameters

| strRIName | The name of the RI Object. |
| usProperty | The property to retrieve. ( See below for possible values ) |
| pvProperty | A buffer to hold the property. |
| usLength | The size of the buffer on input and the size of the property on output. |

Remarks

TAdsDictionary.GetRIProperty will retrieve the selected RI property.

The following are the valid values of usPropertyID:

| usPropertyID | Description |
| ADS\_DD\_RI\_PRIMARY\_TABLE | The parent table of the RI Object. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_PRIMARY\_INDEX | The primary key index of the RI Object. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_FOREIGN\_TABLE | The name of the child table of the RI constraint that contains the foreign key index. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_FOREIGN\_INDEX | The name of the foreign key index of the RI constraint. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_NO\_PKEY\_ERROR | The custom error message used for primary key violation errors. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_CASCADE\_ERROR | The custom error message used for cascade errors. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_UPDATERULE | The update rule for the RI Object. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_RI\_DELETERULE | The delete rule for the RI Object. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |

Example

This example creates an RI object, then gets the parent table name.

procedure GetRIPropertyExample;

var

oAdsDictionary : TAdsDictionary;

aucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

usLength : UNSIGNED16;

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

 

{\* now we need to set the primary indexes for offices \*}

 

usLength := 7;

oAdsDictionary.SetTableProperty( 'offices',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

pChar( 'office' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

{\* now we create the RI \*}

 

oAdsDictionary.CreateRI( 'NewRI',

'',

'offices',

'office',

'salesreps',

'rep\_office',

ADS\_DD\_RI\_CASCADE,

ADS\_DD\_RI\_CASCADE );

 

 

{\* now we are going to get the parent table property \*}

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetRIProperty( 'NewRI',

ADS\_DD\_RI\_PRIMARY\_TABLE,

@aucProperty,

usLength );

 

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

end;

See Also

[CreateRI](ade_createri.md)

[RemoveRI](ade_removeri.md)

[GetRINames](ade_getrinames.md)
