AdsFindNextTable62




Advantage Database Server 12  

AdsFindNextTable62

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFindNextTable62  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFindNextTable62 Advantage Client Engine ace\_Adsfindnexttable62 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFindNextTable62  Advantage Client Engine |  |  |  |  |

Finds the next table matching the file mask provided in a previous call to [AdsFindFirstTable62](ace_adsfindfirsttable62.htm).

Syntax

UNSIGNED32 ENTRYPOINT AdsFindNextTable62 ( ADSHANDLE hConnect,

SIGNED32 lHandle,

UNSIGNED8 \*pucDDName,

UNSIGNED16 \*pusDDLen,

UNSIGNED8 \*pucFileName,

UNSIGNED16 \*pusFileLen );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of connection. |
| lHandle (I) | Find handle from a call to AdsFindFirstTable. |
| pucDDName (O) | If the table found is in a linked dictionary, the name of the link is returned in this buffer. |
| pusDDLen (I/O) | Length of pucDDName on input, length of returned data on output. |
| pucFileName (O) | Next matching tablename is returned in this buffer. |
| pusFileLen (I/O) | Length of pucFileName on input, length of returned data on output. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_FILE\_FOUND | No tables were found. |

Remarks

Use AdsFindNextTable62 to continue a search started with the [AdsFindFirstTable62](ace_adsfindfirsttable62.htm) API.

Call [AdsFindClose](ace_adsfindclose.htm) when your work with the find handle (lHandle) is complete.

Example

usLen = ADS\_MAX\_TABLE\_NAME;

usAliasLen = ADS\_MAX\_OBJECT\_NAME;

ulRetVal = AdsFindFirstTable62( hConn, aucTableMask,

aucDictionaryAlias, &usAliasLen,

aucTable, &usLen, &hFindHandle );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

 

while ( ulRetVal != AE\_NO\_FILE\_FOUND )

{

 

// Do your work with aucDictionaryAlias and aucTable here...

 

// now get the next table

usLen = ADS\_MAX\_TABLE\_NAME;

usAliasLen = ADS\_MAX\_OBJECT\_NAME;

ulRetVal = AdsFindNextTable62( hConn, hFindHandle,

aucDictionaryAlias, &usAliasLen, aucTable, &usLen );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

}

 

AdsFindClose( hConn, hFindHandle );

See Also

[AdsFindFirstTable](ace_adsfindfirsttable.htm)

[AdsFindNextTable](ace_adsfindnexttable.htm)

[AdsFindClose](ace_adsfindclose.htm)

[AdsFindFirstTable62](ace_adsfindfirsttable62.htm)