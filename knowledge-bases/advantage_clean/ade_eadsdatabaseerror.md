---
title: Ade Eadsdatabaseerror
slug: ade_eadsdatabaseerror
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d6a60b78e6b0471ba4ede7248371a1c96c3e5c62
---

# Ade Eadsdatabaseerror

EADSDatabaseError

EADSDatabaseError

Advantage TDataSet Descendant

| EADSDatabaseError  Advantage TDataSet Descendant |  |  |  |  |

| [Properties](ade_eadsdatabaseerror_properties.md) | [Methods](ade_eadsdatabaseerror_methods.md) |

EADSDatabaseError is the exception class for Advantage specific database errors.

Unit

adsdata

Description

EADSDatabaseError is raised when the Advantage TDataSet Descendant component detects a database error. Use EADSDatabaseError in an exception handling block or to manually create a database exception.

EADSDatabaseError is a child of the EDatabaseError object and contains information properties beyond those provided in EDatabaseError. EADSDatabaseError contains all properties and methods that exist in EDatabaseError and the following additional properties:

property ACEErrorCode : UNSIGNED32;

property SQLErrorCode : UNSIGNED32;

property DataSetInstanceName : STRING;

property DataSetInstanceOwner : STRING;

property DatabaseName : STRING;

property DatabasePath : STRING;

property TableName : STRING;

property ColumnName : STRING;

The additional properties provided in EADSDatabaseError do not have to be utilized. If your application currently has exception blocks that trap EDatabaseError instances they will still catch EADSDatabaseError instances as well.

It is possible for an EDatabaseError to be raised by the Advantage TDataSet Descendants parent, TDataSet. In this situation the error object will be of the EDatabaseError type, not EADSDatabaseError. For this reason it is recommended that when trapping database errors you always include a block for EDatabaseError. EADSDatabaseError is a child of EDatabaseError, and because of this hierarchy instances of either of these errors will always be caught in an EDatabaseError block. Examples of two methods of trapping database errors are included below. Example1 uses runtime type checking to determine the error object type, whereas Example2 includes an exception block for each error type.

Example1

try

{\* code for try/except block \*}

 

except

on E: EDatabaseError do

begin

if ( E is EADSDatabaseError ) then

begin

{\* do what youd like with the extended properties \*}

ErrorString := (E as EAdsDatabaseError).DataSetInstanceOwner + ':' +

(E as EADSDatabaseError).Databasename + ':' +

E.message;

application.messagebox( pchar(ErrorString), 'ADS Database Error', 0 )

end

else

application.messagebox( pchar(E.message), 'Native Database Error', 0 );

end;

end;

Example2

try

{\* code for try/except block \*}

 

except

on E: EADSDatabaseError do

begin

{\* do what youd like with the extended properties \*}

ErrorString := E.DataSetInstanceOwner + ':' +

E.Databasename + ':' +

E.Message;

application.messagebox( pchar(ErrorString), 'ADS Database Error', 0 );

end;

on E: EDatabaseError do

application.messagebox( pchar(E.message), 'Native Database Error', 0 );

end;
