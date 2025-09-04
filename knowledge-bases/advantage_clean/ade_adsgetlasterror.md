---
title: Ade Adsgetlasterror
slug: ade_adsgetlasterror
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetlasterror.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a6b39a9be12c9a13b04728554b714420d0db82de
---

# Ade Adsgetlasterror

AdsGetLastError

TAdsTable.AdsGetLastError

Advantage TDataSet Descendant

| TAdsTable.AdsGetLastError  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the result of the last Advantage Client Engine function call.

Syntax

function AdsGetLastError( var strError : String ) : Longint;

Parameter

| strError | Returns the error string corresponding to return value. It will be similar to the string return by AdsGetErrorString but may have information specific to the error instance such as table names. |

Description

The error code returned by this function will be the same as the one returned by the last Advantage Client Engine function call. The first action of each Advantage Client Engine function is to clear the previous error if there is one. Thus, a call to AdsGetLastError is valid only for the most recent function call as opposed to the most recently occurring error. If no error occurred on the last Advantage Client Engine function call, a 0 (zero) is returned.

Example

procedure TForm1.ShowLastAdvantageError( oTable : TAdsTable );

var

strError : string;

lErrorCode : longint;

begin

lErrorCode := oTable.AdsGetLastError( strError );

if ( lErrorCode <> 0 ) then

Application.MessageBox( pchar(strError), 'Advantage Error', 0 );

end;

See Also

[AdsGetErrorString](ade_adsgeterrorstring.md)

[AdsShowError](ade_adsshowerror.md)
