---
title: Ade Setviewproperty
slug: ade_setviewproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_setviewproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9c9276af22a79b42862d66a263d850c769953ecc
---

# Ade Setviewproperty

SetViewProperty

TAdsDictionary.SetViewProperty

Advantage TDataSet Descendant

| TAdsDictionary.SetViewProperty  Advantage TDataSet Descendant |  |  |  |  |

Sets one property associated with a view in the data dictionary.

Syntax

procedure TAdsDictionary.SetViewProperty( strViewName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16 ); UNSIGNED32

Parameters

| strViewName (I) | Name of the view object to set the associated property. |
| usPropertyID (I) | Index of a view property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the strViewName does not specify a valid view in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid view property ID, or the specified property cannot be set. |

Remarks

SetViewProperty sets one property associated with the specified view. The new property overwrites the existing property in the data dictionary. The primary benefit to using this API over deleting and re-creating the view is that it maintains existing permissions on the view object. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the view. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the view description is removed. |
| ADS\_DD\_VIEW\_STMT | Changes the SQL SELECT statement associated with the view. |

Example

Create a view then modify the comment associated with it.

procedure CreateAndModifyView;

var

poDictionary : TAdsDictionary;

begin

 

poDictionary := TAdsDictionary.Create( nil );

 

try

 

poDictionary.ConnectPath := 'n:\MyData\Master.add';

poDictionary.AdsServerTypes := [stADS\_REMOTE];

poDictionary.UserName := 'AdsSys';

poDictionary.Password := 'SuperSecret';

poDictionary.LoginPrompt := False;

 

poDictionary.IsConnected := True;

 

poDictionary.AddView( 'View1',

'',

'select \* from offices' );

 

poDictionary.SetViewProperty( 'View1',

ADS\_DD\_COMMENT,

PChar( 'Simple view on the offices table' ),

length( 'Simple view on the offices table' ) + 1 );

 

finally

poDictionary.IsConnected := False;

 

FreeAndNil( poDictionary );

end;

 

end;

See Also

[AddView](ade_addview.md)

[RemoveView](ade_removeview.md)

[GetViewProperty](ade_getviewproperty.md)
