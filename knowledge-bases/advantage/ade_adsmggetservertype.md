AdsMgGetServerType




Advantage Database Server 12  

AdsMgGetServerType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetServerType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetServerType Advantage TDataSet Descendant ade\_Adsmggetservertype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetServerType  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage server type of the current management API connection

Syntax

function AdsMgGetServerType( hMgmtHandle : ADSHANDLE;

pusServerType : pWord ): UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle. |
| pusServerType (O) | Advantage server type of the current management API connection. |

Remarks

AdsMgGetServerType returns the Advantage server type of the current management connection.

If connected to the Advantage Database Server for Windows, ADS\_MGMT\_NT\_SERVER or ADS\_MGMT\_NT\_SERVER\_64\_BIT is returned.

If connected to the Advantage Local Server, ADS\_MGMT\_LOCAL\_SERVER is returned.

If connected to the Advantage Database Server for Linux, ADS\_MGMT\_LINUX\_SERVER or ADS\_MGMT\_LINUX\_SERVER\_64\_BIT is returned.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

usServerType : WORD;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

ulRetVal := AdsMgGetServerType( hMgmtHandle, @usServerType);

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not determine server type.',

'Error', ID\_OK );

exit;

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)