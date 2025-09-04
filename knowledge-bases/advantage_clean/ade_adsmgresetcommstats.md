---
title: Ade Adsmgresetcommstats
slug: ade_adsmgresetcommstats
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsmgresetcommstats.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 42ca342fbed341317616c384fac25375a8e98934
---

# Ade Adsmgresetcommstats

AdsMgResetCommStats

AdsMgResetCommStats

Advantage TDataSet Descendant

| AdsMgResetCommStats  Advantage TDataSet Descendant |  |  |  |  |

Resets all Advantage Database Server communication statistics to zero

Syntax

function AdsMgResetCommStats( hMgmtHandle : ADSHANDLE ):UNSIGNED32;

Parameters

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

[AdsMgConnect](ade_adsmgconnect.md)

[AdsMgGetCommStats](ade_adsmggetcommstats.md)

[ADS\_MGMT\_COMM\_STATS](ade_ads_mgmt_comm_stats.md)
