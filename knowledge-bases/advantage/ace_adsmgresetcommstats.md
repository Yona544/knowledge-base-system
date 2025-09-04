AdsMgResetCommStats




Advantage Database Server 12  

AdsMgResetCommStats

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgResetCommStats  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgResetCommStats Advantage Client Engine ace\_Adsmgresetcommstats Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgResetCommStats  Advantage Client Engine |  |  |  |  |

Resets all Advantage Database Server communication statistics to zero

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgResetCommStats ( ADSHANDLE hMgmtConnect ); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Management API connection handle of server to reset communication statistics. |

Remarks

AdsMgResetCommStats resets all Advantage Database Server communication statistics to zero. This function is useful when used in conjunction with AdsMgGetCommStats to determine how often corrupted packets are being discovered.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmgresetcommstats_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[AdsMgGetCommStats](ace_adsmggetcommstats.htm)

[ADS\_MGMT\_COMM\_STATS](ace_ads_mgmt_comm_stats.htm)