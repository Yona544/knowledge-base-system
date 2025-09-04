AdsEnableAutoIncEnforcement




Advantage Database Server 12  

AdsEnableAutoIncEnforcement

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsEnableAutoIncEnforcement  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsEnableAutoIncEnforcement Advantage Client Engine ace\_Adsenableautoincenforcement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsEnableAutoIncEnforcement  Advantage Client Engine |  |  |  |  |

Enables the enforcement of the read/only status of auto-increment values.

Syntax

UNSIGNED32 AdsEnableAutoIncEnforcement( ADSHANDLE hConnect );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Valid connection handle. |

Remarks

AdsEnableAutoIncEnforcement restores the default behavior of auto-increment fields on the given connection. By default, auto-increment values are generated and maintained by Advantage. This API is used to re-enable the enforcement of auto-increment values after a call to AdsDisableAutoIncEnforcement.

See Also

[AdsDisableAutoIncEnforcement](ace_adsdisableautoincenforcement.htm)

[AdsDisableUniqueEnforcement](ace_adsdisableuniqueenforcement.htm)

[AdsEnableUniqueEnforcement](ace_adsenableuniqueenforcement.htm)

[AdsDisableRI](ace_adsdisableri.htm)

[AdsEnableRI](ace_adsenableri.htm)