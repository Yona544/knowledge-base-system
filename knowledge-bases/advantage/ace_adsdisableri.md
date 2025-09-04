AdsDisableRI




Advantage Database Server 12  

AdsDisableRI

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDisableRI  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDisableRI Advantage Client Engine ace\_Adsdisableri Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDisableRI  Advantage Client Engine |  |  |  |  |

Disables referential integrity (RI) enforcement for record insertions and updates.

Syntax

UNSIGNED32 AdsDisableRI( ADSHANDLE hConnection );

Parameters

|  |  |
| --- | --- |
| hConnection (I) | Connection handle. |

Remarks

AdsDisableRI can be used to temporarily disable referential integrity constraints on the database.

Note Disabling referential integrity constraints can lead to logical data corruption. This API should be used with extreme caution.

See Also

[AdsEnableRI](ace_adsenableri.htm)

[AdsDisableUniqueEnforcement](ace_adsdisableuniqueenforcement.htm)

[AdsEnableUniqueEnforcement](ace_adsenableuniqueenforcement.htm)

[AdsDisableAutoIncEnforcement](ace_adsdisableautoincenforcement.htm)

[AdsEnableAutoIncEnforcement](ace_adsenableautoincenforcement.htm)