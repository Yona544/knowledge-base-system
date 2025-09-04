AdsShowDeleted




Advantage Database Server 12  

AdsShowDeleted

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsShowDeleted  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsShowDeleted Advantage Client Engine ace\_Adsshowdeleted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsShowDeleted  Advantage Client Engine |  |  |  |  |

Defines whether deleted records are visible in DBF tables

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsShowDeleted (UNSIGNED16 usShowDeleted); |

Parameters

|  |  |
| --- | --- |
| usShowDeleted (I) | If non-zero, deleted records will be visible in DBF tables. The default value is True. |

Remarks

In DBF tables, deleted records still physically exist inside tables so they can be returned to client applications.

AdsShowDeleted controls whether the Advantage Database Server filters out records that are marked for deletion in DBF tables. If usShowDeleted is False, then the server will filter the deleted records, and the client will never "see" those records. This call also affects all currently connected servers and all server connections that are made after the call. [AdsGotoRecord](ace_adsgotorecord.htm) does not respect the setting from this call.

Note AdsShowDeleted has no effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved by a client application.

AdsShowDeleted is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adsshowdeletedexample)

See Also

[AdsGetDeleted](ace_adsgetdeleted.htm)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.htm)

[AdsDeleteRecord](ace_adsdeleterecord.htm)

[AdsRecallRecord](ace_adsrecallrecord.htm)