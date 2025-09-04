AdsGetDeleted




Advantage Database Server 12  

AdsGetDeleted

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetDeleted  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetDeleted Advantage Client Engine ace\_Adsgetdeleted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetDeleted  Advantage Client Engine |  |  |  |  |

Retrieves the current show deleted setting

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetDeleted (UNSIGNED16 \*pbShowDeleted); |

Parameters

|  |  |
| --- | --- |
| pbShowDeleted (O) | Contains the retrieved deleted setting. |

Remarks

AdsGetDeleted will return the current value of the ShowDeleted setting, which can be set by [AdsShowDeleted](ace_adsshowdeleted.htm). True means that deleted records in a DBF table will be visible to the user.

AdsGetDeleted is a global setting that affects the behavior of the entire application.

Note AdsShowDeleted has no effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved by a client application.

Example

[Click Here](ace_examples.htm#adsgetdeleteexample)

See Also

[AdsDeleteRecord](ace_adsdeleterecord.htm)

[AdsRecallRecord](ace_adsrecallrecord.htm)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.htm)

[AdsShowDeleted](ace_adsshowdeleted.htm)