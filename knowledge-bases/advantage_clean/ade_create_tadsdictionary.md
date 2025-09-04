---
title: Ade Create Tadsdictionary
slug: ade_create_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_create_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0328b5def81f75c031a8a8003505aa7442c07f3b
---

# Ade Create Tadsdictionary

Create

TAdsDictionary.Create

Advantage TDataSet Descendant

| TAdsDictionary.Create  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.Create( AOwner : TComponent );

Parameters

| AOwner (I) | The owner of the TAdsDictionary component. |

Remarks

This is the constructor for the TAdsDictionary object. It will automatically get called at design time. If the component needs to be created during runtime this constructor needs to be called before creating a data dictionary.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure CreateExample;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;
