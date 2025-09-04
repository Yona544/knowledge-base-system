---
title: Ace Adsgetftsindexinfo
slug: ace_adsgetftsindexinfo
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetftsindexinfo.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a7e1daf30fcefd24f54c20115f507fd7af8d6e04
---

# Ace Adsgetftsindexinfo

AdsGetFTSIndexInfo

AdsGetFTSIndexInfo / AdsGetFTSIndexInfoW

Advantage Client Engine

| AdsGetFTSIndexInfo / AdsGetFTSIndexInfoW  Advantage Client Engine |  |  |  |  |

Return information about the given full text search index. The string information may be returned in ANSI, UTF8 or UTF16 encoding.

Syntax

UNSIGNED32 AdsGetFTSIndexInfo

(

ADSHANDLE hIndex,

UNSIGNED8 \*pucOutput,

UNSIGNED32 \*pulBufLen,

UNSIGNED8 \*\*ppucField,

UNSIGNED32 \*pulMinWordLen,

UNSIGNED32 \*pulMaxWordLen,

UNSIGNED8 \*\*ppucDelimiters,

UNSIGNED8 \*\*ppucNoiseWords,

UNSIGNED8 \*\*ppucDropChars,

UNSIGNED8 \*\*ppucConditionalChars,

UNSIGNED8 \*\*ppucReserved1,

UNSIGNED8 \*\*ppucReserved2,

UNSIGNED32 \*pulOptions

);

 

UNSIGNED32 AdsGetFTSIndexInfoW

(

ADSHANDLE hIndex,

WCHAR \*pwcOutput,

UNSIGNED32 \*pulBufLen,

WCHAR \*\*ppwcField,

UNSIGNED32 \*pulMinWordLen,

UNSIGNED32 \*pulMaxWordLen,

WCHAR \*\*ppwcDelimiters,

WCHAR \*\*ppwcNoiseWords,

WCHAR \*\*ppwcDropChars,

WCHAR \*\*ppwcConditionalChars,

WCHAR \*\*ppwcReserved1,

WCHAR \*\*ppwcReserved2,

UNSIGNED32 \*pulOptions

);

Parameters

| hIndex (I) | Full text search index handle. |
| pucOutput (O)  pwcOutput (O) | Pointer to memory that all the string information will be returned in. It must be long enough to hold the field name, delimiters, noise words, drop characters, and conditional characters. See the Remarks section for more information. |
| pulBufLen (I/O) | Length of pucOutput on input. On output, it contains the length (or required length) of the actual data. For AdsGetFTSIndexInfo, the unit for this parameter is number of bytes. For AdsGetFTSIndexInfoW, the unit for this parameter is number of UTF16 characters. |
| ppucField (O)  ppwcField (O) | The null terminated field name on which the index is created. This parameter can be NULL. |
| pulMinWordLen (O) | Minimum word size. This parameter can be NULL. |
| pulMaxWordLen (O) | Maximum word size. This parameter can be NULL. |
| ppucDelimiters (O)  ppwcDelimiters (O) | Null terminated string of delimiter characters. This parameter can be NULL. |
| ppucNoiseWords (O)  ppwcNoiseWords (O) | Null terminated string of space delimited noise words. This parameter can be NULL. |
| ppucDropChars (O)  ppwcDropChars (O) | Null terminated string of drop characters. This parameter can be NULL. |
| ppucConditionalChars (O)  ppwcConditionalChars(O) | Null terminated string of conditional drop characters. This parameter can be NULL. |
| ppucReserved1  ppwcReserved1 | Reserved for future use. |
| ppucReserved2  ppwcReserved2 | Reserved for future use. |
| pulOptions (O) | Bit mask of options used to create the full text search index. The possible values include ADS\_FTS\_INDEX, ADS\_FTS\_FIXED, ADS\_FTS\_CASE\_SENSITIVE, ADS\_FTS\_KEEP\_SCORE, and ADS\_FTS\_PROTECT\_NUMBERS. |

Remarks

This API returns information about a given full text search (FTS) index. Its use of input and output buffers is somewhat different than other Advantage Client Engine APIs. This API makes use of a single output buffer and sets the other character pointers to point into this one buffer. A single buffer (pucOutput or pwcOutput) is provided by the caller. The parameters ppucField/ppwcField, ppucDelimiters/ppwcDelimiters, ppucNoiseWords/ppwcNoiseWords, ppucDropChars/ppwcDropChars, and ppucConditionalChars/ppwcConditionalChars are set by the API to point into this buffer on output (if they are not passed in as NULL to the API). The values they point to will be null terminated strings.

The AdsGetFTSIndexInfo may return the strings in ANSI encoding or UTF8 encoding, depending on the type of field being indexed. If the field is one of the Unicode field types, NChar, NVarChar or NMemo, the strings returned will be encoded in UTF8 with Byte Order Mark (BOM) of 0xEF, 0xBB and 0xBF as the leading characters. The BOM is not part of the option. It is used only to signify that the field is a Unicode field and the option is encoded in UTF8. If the field is not a Unicode field type, the returned string options will be encoded in ANSI and no BOM will be present in the string.

To determine how much buffer space is required, this API can be called the pulBufLen value set to 0 The value pointed to by pulBufLen will be updated on return to indicate the required length. For AdsGetFTSIndexInfo, the returned length is the number of bytes required. For AdsGetFTSIndexInfoW, the returned length is the number of UTF16 characters required.

If certain values are not desired, they can be NULL values. For example, if the calling function does not need the delimiter characters, it can pass NULL for the ppucDelimiter or ppwcDelimiters parameter.

Example in C/C++

 

// Variable declarations for the information parameters

ADSHANDLE hTable, hIndex;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulBufLen;

UNSIGNED32 ulMinWordLen, ulMaxWordLen;

UNSIGNED32 ulOptions;

UNSIGNED8 \*pucBuf;

UNSIGNED8 \*pucField;

UNSIGNED8 \*pucDelimiters;

UNSIGNED8 \*pucNoiseWords;

UNSIGNED8 \*pucDropChars;

UNSIGNED8 \*pucConditionalChars;

 

// open the table

 

// Retrieve the desired index handle

ulRetVal = AdsGetIndexHandle( hTable, "files", &hIndex );

 

// Determine how large a buffer is required for output information

// This call will return AE\_INSUFFICIENT\_BUFFER if the index handle is a valid

// FTS index.

ulBufLen = 0;

pucBuf = NULL;

ulRetVal = AdsGetFTSIndexInfo( hIndex, pucBuf, &ulBufLen, &pucField, &ulMinWordLen,

&ulMaxWordLen, &pucDelimiters, &pucNoiseWords,

&pucDropChars, &pucConditionalChars,

NULL, NULL, // reserved parameters

&ulOptions );

 

if ( ulRetVal != AE\_INSUFFICIENT\_BUFFER )

AdsShowError( NULL );

 

// allocate memory for the call

pucBuf = (UNSIGNED8\*)malloc( ulBufLen );

 

// now call and get the information

ulRetVal = AdsGetFTSIndexInfo( hIndex, pucBuf, &ulBufLen, &pucField, &ulMinWordLen,

&ulMaxWordLen, &pucDelimiters, &pucNoiseWords,

&pucDropChars, &pucConditionalChars,

NULL, NULL, // reserved parameters

&ulOptions );

Example in Delphi

 

procedure GetFTSIndexInfo

(

poDataSet : TAdsDataSet; // (I) for error handling

strIndexName : string; // (I) FTS index handle

var strField : string; // (O) field it is indexed on

var strDelimiters: string; // (O) delimiter characters

var strNoise : string; // (O) noise words

var strDropChars : string; // (O) drop (ignore) characters

var strConditionalChars: string;// (O) conditional drop characters

var ulMinWord: Longword; // (O) minimum word length

var ulMaxWord: Longword; // (O) maximum word length (key length)

var ulOptions: Longword // (O) FTS index options (ORed together)

);

var

pucBuffer: PChar;

ulRetCode : UNSIGNED32;

ulBufLen : UNSIGNED32;

pucField : PChar;

pucDelimiters : PChar;

pucNoiseWords : PChar;

pucDropChars : PChar;

pucConditionalChars : PChar;

hFTS : AdsHandle;

 

begin

 

// Get the index handle from the index name.

ACECheck( poDataSet, ACE.AdsGetIndexHandle( poDataSet.Handle,

PChar( strIndexName ),

@hFTS ) );

 

 

// Initialize pucBuffer (the only one that gets set to allocated

// memory). The others simply get set to point into the one buffer

// so they do not need to be initialized.

pucBuffer := nil;

 

try

// Make a call to see how long a buffer we need

ulBufLen := 0;

ulRetCode := ACE.AdsGetFTSIndexInfo( hFTS, nil, @ulBufLen,

@pucField, nil, nil,

@pucDelimiters,

@pucNoiseWords,

@pucDropChars,

@pucConditionalChars,

nil, nil, nil );

 

// Should have gotten an insufficient buffer error

if ( ulRetCode <> AE\_INSUFFICIENT\_BUFFER ) then

AceCheck( poDataSet, ulRetCode );

 

 

pucBuffer := StrAlloc( ulBufLen );

 

// Get the data

AceCheck( poDataSet, ACE.AdsGetFTSIndexInfo( hFTS, pucBuffer,

@ulBufLen,

@pucField,

@ulMinWord,

@ulMaxWord,

@pucDelimiters,

@pucNoiseWords,

@pucDropChars,

@pucConditionalChars,

nil, nil,

@ulOptions ));

 

strField := pucField;

strDelimiters := pucDelimiters;

strNoise := pucNoiseWords;

strDropChars := pucDropChars;

strConditionalChars := pucConditionalChars;

 

finally

if pucBuffer <> nil then

StrDispose( pucBuffer );

end;

 

end; {\* GetFTSIndexInfo \*}

 

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)
