AdsGetHandleLong




Advantage Database Server 12  

AdsGetHandleLong

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetHandleLong  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetHandleLong Advantage Client Engine ace\_Adsgethandlelong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetHandleLong  Advantage Client Engine |  |  |  |  |

Returns the long value for this handle set with a call to [AdsSetHandleLong](ace_adssethandlelong.htm).

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetHandleLong (ADSHANDLE hObj,  UNSIGNED32 \*pulValue); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of a connection, table, cursor, or an index order. |
| pulValue (O) | Returns the value that has been set for this handle. |

Remarks

Returns the value set for this handle in a previous call to AdsSetHandleLong. This function allows one value to be stored for this handle. The value stored is at the users discretion. The Advantage Client Engine does not use the value for any operation, but simply stores it. The value is readable as long as the handle is valid.

If a value for this handle has not been set, the function returns AE\_INVALID\_HANDLE.

Example

[Click Here](ace_examples.htm#adsgethandlelongexample)

See Also

[AdsSetHandleLong](ace_adssethandlelong.htm)