AdsMgGetActivityInfo




Advantage Database Server 12  

AdsMgGetActivityInfo

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetActivityInfo  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetActivityInfo Advantage TDataSet Descendant ade\_Adsmggetactivityinfo Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetActivityInfo  Advantage TDataSet Descendant |  |  |  |  |

Returns information about current activity on the Advantage Database Server

Syntax

function AdsMgGetActivityInfo( hMgmtHandle : ADSHANDLE;

pstActivityInfo : pADS\_MGMT\_ACTIVITY\_INFO;

pusStructSize : pWord ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server to get activity information. |
| pstActivityInfo (O) | Returned activity information structure. |
| pusStructSize (I/O) | Size (in bytes) of pstActivityInfo structure on input. On output, size of ADS\_MGMT\_ACTIVITY\_INFO structure on the Advantage Database Server. |

Remarks

AdsMgGetActivityInfo returns a structure containing information about current activity on the Advantage Database Server. Included is such information as the number of operations that have been performed by the Advantage Database Server since it has been running, the length of time the Advantage Database Server has running, and the "in use", "max used", and "rejected" number of such values as connections, tables, and index files.

It is possible that the size of the ADS\_MGMT\_ACTIVITY\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional activity data that may exist if using a newer version of the Advantage Database Server will not be returned in pstActivityInfo. The pstActivityInfo structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_ACTIVITY\_INFO structure in the current version of the Advantage Database Server. If the size of the pstActivityInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible activity information.

Since it is possible that the size of the ADS\_MGMT\_ACTIVITY\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with size of( ADS\_MGMT\_ACTIVITY\_INFO ) rather than being initialized with a literal value.

Example

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

stActivityInfo : ADS\_MGMT\_ACTIVITY\_INFO;

usSize : UNSIGNED16;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

usSize := sizeof( ADS\_MGMT\_ACTIVITY\_INFO );

ulRetVal := ACE.AdsMgGetActivityInfo( hMgmtHandle, @stActivityInfo, @usSize ) ;

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'An error has been encountered.', 'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The number of days the server has been running is: '

+ IntToStr( stActivityInfo.stUpTime.usDays )),

'Up Time',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[ADS\_MGMT\_ACTIVITY\_INFO](ade_ads_mgmt_activity_info.htm)