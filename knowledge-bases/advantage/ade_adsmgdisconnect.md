AdsMgDisconnect




Advantage Database Server 12  

AdsMgDisconnect

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgDisconnect  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgDisconnect Advantage TDataSet Descendant ade\_Adsmgdisconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgDisconnect  Advantage TDataSet Descendant |  |  |  |  |

Disconnects the management API connection from the given server

Syntax

function AdsMgDisconnect( hConnect: ADSHANDLE ): UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of management API connection. |

Remarks

AdsMgDisconnect currently is stubbed to call AdsDisconnect. It is recommended you use AdsMgDisconnect to disconnect the management API connection. A future release of the Advantage Client Engine may not support using a standard connection handle in place of a management API connection handle.

In a future release, AdsMgDisconnect may be used to disconnect the management API from the specified server.

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

 

ulRetVal := ACE.AdsMgDisConnect( hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not disconnect from server.', 'Connection Error', ID\_OK );

exit;

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[AdsMgDisconnect](ade_adsmgdisconnect.htm)