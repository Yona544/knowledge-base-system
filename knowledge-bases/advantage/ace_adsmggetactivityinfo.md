AdsMgGetActivityInfo




Advantage Database Server 12  

AdsMgGetActivityInfo

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetActivityInfo  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetActivityInfo Advantage Client Engine ace\_Adsmggetactivityinfo Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetActivityInfo  Advantage Client Engine |  |  |  |  |

Returns information about current activity on the Advantage Database Server

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgGetActivityInfo (ADSHANDLE hMgmtConnect,  ADS\_MGMT\_ACTIVITY\_INFO \*pstActivityInfo,  UNSIGNED16 \*pusStructSize); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Management API connection handle of server to get activity information. |
| pstActivityInfo (O) | Returned activity information structure. |
| pusStructSize (I/O) | Size (in bytes) of pstActivityInfo structure on input. On output, size of ADS\_MGMT\_ACTIVITY\_INFO structure on the Advantage Database Server. |

Remarks

AdsMgGetActivityInfo returns a structure containing information about current activity on the Advantage Database Server. Included is such information as the number of operations that have been performed by the Advantage Database Server since it has been running, the length of time the Advantage Database Server has running, and the "in use", "max used", and "rejected" number of such values as connections, tables, and index files.

It is possible that the size of the ADS\_MGMT\_ACTIVITY\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional activity data that may exist if using a newer version of the Advantage Database Server will not be returned in pstActivityInfo. The pstActivityInfo structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_ACTIVITY\_INFO structure in the current version of the Advantage Database Server. If the size of the pstActivityInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible activity information.

Since it is possible that the size of the ADS\_MGMT\_ACTIVITY\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_ACTIVITY\_INFO ) rather than being initialized with a literal value.

Note With the Advantage Local Server, AdsMgGetActivityInfo will only return information for the instance of Advantage Local Server currently loaded into memory.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmggetactivityinfo_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[ADS\_MGMT\_ACTIVITY\_INFO](ace_ads_mgmt_activity_info.htm)