AdsDisableUniqueEnforcement




Advantage Database Server 12  

AdsDisableUniqueEnforcement

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDisableUniqueEnforcement  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDisableUniqueEnforcement Advantage Client Engine ace\_Adsdisableuniqueenforcement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDisableUniqueEnforcement  Advantage Client Engine |  |  |  |  |

Disables unique key enforcement for record insertions and updates.

Syntax

UNSIGNED32 AdsDisableUniqueEnforcement(ADSHANDLE hConnection);

Parameters

|  |  |
| --- | --- |
| hConnection (I) | Connection handle. |

Remarks

AdsDisableUniqueEnforcement can be used to temporarily disable the maintenance of unique key indexes on all tables associated with the connection.

Note Disabling unique key maintenance can lead to logical data corruption. This API should be used with extreme caution.

See Also

[AdsEnableUniqueEnforcement](ace_adsenableuniqueenforcement.htm)

[AdsDisableRI](ace_adsdisableri.htm)

[AdsEnableRI](ace_adsenableri.htm)

[AdsDisableAutoIncEnforcement](ace_adsdisableautoincenforcement.htm)

[AdsEnableAutoIncEnforcement](ace_adsenableautoincenforcement.htm)