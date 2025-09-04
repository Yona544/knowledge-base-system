AdsMgGetInstallInfo




Advantage Database Server 12  

AdsMgGetInstallInfo

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetInstallInfo  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetInstallInfo Advantage TDataSet Descendant ade\_Adsmggetinstallinfo Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetInstallInfo  Advantage TDataSet Descendant |  |  |  |  |

Returns Advantage Database Server installation information

Syntax

function AdsMgGetInstallInfo( hMgmtHandle : ADSHANDLE;

pstInstallInfo : pADS\_MGMT\_INSTALL\_INFO;

pusStructSize : pWord ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server to get installation information. |
| pstInstallInfo (O) | Returned installation information structure. |
| pusStructSize (I/O) | Size (in bytes) of pstInstallInfo structure on input. On output, size (in bytes) of data returned. |

Remarks

AdsMgGetInstallInfo returns a structure containing Advantage Database Server installation information such as the Advantage Database Server version and the installation date.

It is possible that the size of the ADS\_MGMT\_INSTALL\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional installation data that may exist if using a newer version of the Advantage Database Server will not be returned in pstInstallInfo. The pstInstallInfo structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_INSTALL\_INFO structure in the current version of the Advantage Database Server. If the size of the pstInstallInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible installation information.

Since it is possible that the size of the ADS\_MGMT\_INSTALL\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_INSTALL\_INFO ) rather than being initialized with a literal value.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

stInstallInfo : ADS\_MGMT\_INSTALL\_INFO;

usSize : UNSIGNED16;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

usSize := sizeof( ADS\_MGMT\_INSTALL\_INFO );

ulRetVal := ACE.AdsMgGetInstallInfo( hMgmtHandle, @stInstallInfo, @usSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not get Installation Information.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The registered owner is: '

+ stInstallInfo.aucRegisteredOwner ),

'Registered Owner',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[ADS\_MGMT\_INSTALL\_INFO](ade_ads_mgmt_install_info.htm)