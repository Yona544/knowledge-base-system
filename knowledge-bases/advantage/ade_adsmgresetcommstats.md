AdsMgResetCommStats




Advantage Database Server 12  

AdsMgResetCommStats

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgResetCommStats  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgResetCommStats Advantage TDataSet Descendant ade\_Adsmgresetcommstats Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgResetCommStats  Advantage TDataSet Descendant |  |  |  |  |

Resets all Advantage Database Server communication statistics to zero

Syntax

function AdsMgResetCommStats( hMgmtHandle : ADSHANDLE ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server to reset communication statistics. |

Remarks

AdsMgResetCommStats resets all Advantage Database Server communication statistics to zero. This function is useful when used in conjunction with AdsMgGetCommStats to determine how often corrupted packets are being discovered.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

ulRetVal := ACE.AdsMgResetCommStats( hMgmtHandle );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not reset communication statistics.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('Communication statistics reset.'),

'Informtaion',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[AdsMgGetCommStats](ade_adsmggetcommstats.htm)

[ADS\_MGMT\_COMM\_STATS](ade_ads_mgmt_comm_stats.htm)