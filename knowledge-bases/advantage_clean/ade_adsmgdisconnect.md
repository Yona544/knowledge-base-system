---
title: Ade Adsmgdisconnect
slug: ade_adsmgdisconnect
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsmgdisconnect.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 78b001187e6d4e939995da5583a7cb1ce5688444
---

# Ade Adsmgdisconnect

AdsMgDisconnect

AdsMgDisconnect

Advantage TDataSet Descendant

| AdsMgDisconnect  Advantage TDataSet Descendant |  |  |  |  |

Disconnects the management API connection from the given server

Syntax

function AdsMgDisconnect( hConnect: ADSHANDLE ): UNSIGNED32;

Parameters

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

[AdsMgConnect](ade_adsmgconnect.md)

[AdsMgDisconnect](ade_adsmgdisconnect.md)
