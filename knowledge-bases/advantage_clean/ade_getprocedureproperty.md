---
title: Ade Getprocedureproperty
slug: ade_getprocedureproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getprocedureproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 468dd10561edbb0a3bcc67d70fb0cc41bda66e6b
---

# Ade Getprocedureproperty

GetProcedureProperty

TAdsDictionary.GetProcedureProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetProcedureProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure GetProcedureProperty( strProcName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 ); virtual;

Parameters

| strProcName (I) | The name of the stored procedure in the data dictionary. |
| usPropertyID (I) | The property to retrieve. (see below for possible values.) |
| pvProperty (O) | A buffer to hold the property value. |
| usPropertyLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

GetProcedureProperty will retrieve the specified property of the stored procedure from the data dictionary.

The following are the valid values for usPropertyID:

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The comment string that is stored in the data dictionary. |
| ADS\_DD\_PROC\_INPUT | The stored procedure input parameters in same format used by AdsCreateTable when describing field definitions. |
| ADS\_DD\_PROC\_OUTPUT | The stored procedure output parameters in same format used by AdsCreateTable when describing field definitions. |
| ADS\_DD\_PROC\_DLL\_NAME | The name of the Advantage Extended Procedures file that contains the stored procedure. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_PROC\_DLL\_FUNCTION\_NAME | The name of the function within the Advantage Extended Procedure file that is called when the procedure is executed. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_PROC\_INVOKE\_OPTION | This value determines the format of the stored procedure. At this time, the value is always equal to ADS\_STORED\_PROC. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |

Example

procedure GetProcedurePropertyExample

var

oAdsDictionary : TAdsDictionary;

usPropertyLen : UNSIGNED16;

pucProperty : array[0..ADS\_DD\_MAX\_PROPERTY\_LEN] of char;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

oAdsDictionary.AddProcedure( 'NewProcedure',

'.\sp.aep',

'Echo',

ADS\_STORED\_PROC,

'InParam,Char,10',

'OutParam,Char,10',

'This is a stored procedure' );

 

usPropertyLen := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetProcedureProperty( 'NewProcedure',

ADS\_DD\_PROC\_DLL\_NAME,

@pucProperty,

usPropertyLen );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

end;

See Also

[AddProcedure](ade_addprocedure.md)

[RemoveProcedure](ade_removeprocedure.md)
