AdsFindClose




Advantage Database Server 12  

AdsFindClose

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFindClose  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFindClose Advantage Client Engine ace\_Adsfindclose Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFindClose  Advantage Client Engine |  |  |  |  |

Close a find handle and free all resources associated with it

Syntax

UNSIGNED32 ENTRYPOINT AdsFindClose( ADSHANDLE hConnect, SIGNED32 lHandle );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of connection. |
| lHandle (I) | Find handle to close. |

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

[AdsFindNextTable](ace_adsfindnexttable.htm)

[AdsFindFirstTable62](ace_adsfindfirsttable62.htm)

[AdsFindNextTable62](ace_adsfindnexttable62.htm)