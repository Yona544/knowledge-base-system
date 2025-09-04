AdsGetTableRights




Advantage Database Server 12  

AdsGetTableRights

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableRights  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableRights Advantage Client Engine ace\_Adsgettablerights Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableRights  Advantage Client Engine |  |  |  |  |

Retrieves the type of rights checking used with a table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableRights (ADSHANDLE hTable,  UNSIGNED16 \*pusRights); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusRights (O) | Type of rights checking used to open the table (ADS\_CHECKRIGHTS, ADS\_IGNORERIGHTS). |

Remarks

AdsGetTableRights will retrieve the type of rights checking specified during the table open.

Example

[Click Here](ace_examples.htm#adsgettablerightsexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)