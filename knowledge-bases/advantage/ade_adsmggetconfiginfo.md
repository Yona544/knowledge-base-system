AdsMgGetConfigInfo




Advantage Database Server 12  

AdsMgGetConfigInfo

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetConfigInfo  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetConfigInfo Advantage TDataSet Descendant ade\_Adsmggetconfiginfo Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetConfigInfo  Advantage TDataSet Descendant |  |  |  |  |

Returns Advantage Database Server configuration information

Syntax

function AdsMgGetConfigInfo( hMgmtHandle : ADSHANDLE;

pstConfigValues : pADS\_MGMT\_CONFIG\_PARAMS;

pusConfigValuesStructSize : pWord;

pstConfigMemory : pADS\_MGMT\_CONFIG\_MEMORY;

pusConfigMemoryStructSize : pWord ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server to get configuration information. |
| pstConfigValues (O) | Returned configuration parameter value structure. |
| pusConfigValueStructSize (I/O) | Size (in bytes) of pstConfigValues structure on input. On output, size (in bytes) of data returned. |
| pstConfigMemory (O) | Returned configuration parameter memory structure. |
| pusConfigMemoryStructSize (I/O) | Size (in bytes) of pstConfigMemory structure on input. On output, size (in bytes) of data returned. |

Remarks

When the Advantage Database Server is started/loaded, several values are available to be configured to fine tune the use of the Advantage Database Server. Many of these configurable parameters affect how much server memory is used when the Advantage Database Server is started/loaded. The remaining configurable parameters affect other non-memory Advantage features. AdsMgGetConfigInfo returns two structures. The first, pstConfigValues, contains the current settings of all Advantage Database Server configuration parameters. The second, pstConfigMemory, contains the memory taken up by the applicable configuration parameters. Each pstConfigMemory structure data member contains the total memory (in bytes) taken up for each setting. To determine how much memory is required per setting, divide the memory size by the number configured.

Since it is possible that the size of the ADS\_MGMT\_CONFIG\_PARAMS and/or ADS\_MGMT\_CONFIG\_MEMORY structures will increase in future releases of Advantage, it is highly recommended that on input the pusConfigValueStructSize and pusConfigMemoryStructSize parameters are literally initialized with sizeof( ADS\_MGMT\_CONFIG\_PARAMS ) and sizeof( ADS\_MGMT\_CONFIG\_MEMORY ), respectively, rather than being initialized with literal values.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

stConfigValues : ADS\_MGMT\_CONFIG\_PARAMS;

stConfigMemory : ADS\_MGMT\_CONFIG\_MEMORY;

usSize : UNSIGNED16;

usSize2 : UNSIGNED16;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

usSize := sizeof( ADS\_MGMT\_CONFIG\_PARAMS );

usSize2 := sizeof( ADS\_MGMT\_CONFIG\_MEMORY );

ulRetVal := ACE.AdsMgGetConfigInfo( hMgmtHandle, @stConfigValues, @usSize,

@stConfigMemory, @usSize2 );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not get Configuration Information.',

'Communication Error', ID\_OK );

exit;

end

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[ADS\_MGMT\_CONFIG\_PARAMS](ade_ads_mgmt_config_params.htm)

[ADS\_MGMT\_CONFIG\_MEMORY](ade_ads_mgmt_config_memory.htm)