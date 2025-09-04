---
title: Ade Adsgeterrorstring
slug: ade_adsgeterrorstring
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgeterrorstring.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7dfb89a272878fc0f78bb4839914fcbdce0de56a
---

# Ade Adsgeterrorstring

AdsGetErrorString

TAdsTable.AdsGetErrorString

Advantage TDataSet Descendant

| TAdsTable.AdsGetErrorString  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the error string for the given error code.

Syntax

function AdsGetErrorString( ulErrorCode : Longint ) : String;

Parameter

| ulErrorCode | An Advantage error code. |

Description

AdsGetErrorString is used to retrieve the error string for a specific error code. Errors that occur in the Advantage Client Engine are 5000 class errors. There are also relevant error messages built into the Advantage Client Engine for server and communications layer errors. By calling AdsGetErrorString, AdsShowError, or AdsGetLastError an application can display immediate information on failures that have occurred.

AdsGetLastError can also be used to return information about any valid Advantage error code. When used immediately after an Advantage Client Engine error occurs, additional error information will be returned.

Example

{ This method appears in ADSFUNC.PAS }

function TAdsTable.AdsGetErrorString( ulErrorCode: Longint ): string;

var

acErrorStr : array[0..ERROR\_STRING\_LEN] of char;

usLen : UNSIGNED16;

begin

usLen := ERROR\_STRING\_LEN;

ACECheck2( ACE.AdsGetErrorString( ulErrorCode, @acErrorStr, @usLen ) );

Result := StrPas( @acErrorStr );

end;

See Also

[AdsGetLastError](ade_adsgetlasterror.md)

[AdsShowError](ade_adsshowerror.md)
