AdsFindNextTable




Advantage Database Server 12  

AdsFindNextTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFindNextTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFindNextTable Advantage Client Engine ace\_Adsfindnexttable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFindNextTable  Advantage Client Engine |  |  |  |  |

Finds the next table matching the file mask provided in a previous call to [AdsFindFirstTable](ace_adsfindfirsttable.htm).

Syntax

UNSIGNED32 ENTRYPOINT AdsFindNextTable( ADSHANDLE hConnect,

SIGNED32 lHandle,

UNSIGNED8 \*pucFileName,

UNSIGNED16 \*pusFileLen );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of connection. |
| lHandle (I) | Find handle from a call to AdsFindFirstTable. |
| pucFileName (O) | Next matching tablename is returned in this buffer. |
| pusFileLen (I/O) | Length of pucFileName on input, length of returned data on output. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_FILE\_FOUND | No tables were found. |

Remarks

Use AdsFindNextTable to continue a search started with the [AdsFindFirstTable](ace_adsfindfirsttable.htm) API.

Call [AdsFindClose](ace_adsfindclose.htm) when your work with the find handle (lHandle) is complete.

Example

usLen = ADS\_MAX\_TABLE\_NAME;

strcpy( (char\*)aucTableMask, "x:\\data\\\*.adt" );

ulRetVal = AdsFindFirstTable( hConn, aucTableMask, aucTable,

&usLen, &hFindHandle );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

 

while ( ulRetVal != AE\_NO\_FILE\_FOUND )

{

 

// Do your work with the tablename, which is now in the aucTable buffer.

 

// now get the next table

usLen = ADS\_MAX\_TABLE\_NAME;

ulRetVal = AdsFindNextTable( hConn, hFindHandle,

aucTable, &usLen );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

}

 

AdsFindClose( hConn, hFindHandle );

See Also

[AdsFindFirstTable](ace_adsfindfirsttable.htm)

[AdsFindClose](ace_adsfindclose.htm)

[AdsFindFirstTable62](ace_adsfindfirsttable62.htm)

[AdsFindNextTable62](ace_adsfindnexttable62.htm)