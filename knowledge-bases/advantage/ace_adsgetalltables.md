AdsGetAllTables




Advantage Database Server 12  

AdsGetAllTables

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetAllTables  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetAllTables Advantage Client Engine ace\_Adsgetalltables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetAllTables  Advantage Client Engine |  |  |  |  |

Returns an array of handles of all open tables and cursors

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetAllTables (ADSHANDLE ahTable[],  UNSIGNED16 \*pusArrayLen); |

Parameters

|  |  |
| --- | --- |
| ahTable[] (O) | Returns table and cursor handles in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

AdsGetAllTables will return the handles for all open tables and cursors. The handle array must be supplied with each element having room for a handle (not byte). If there are more handles than the array can hold, the array will be filled with the handles that fit, an error will be returned, and the number of open tables and cursors will be returned in the pusArrayLen parameter.

Example

[Click Here](ace_examples.htm#adsgetalltablesexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetNumOpenTables](ace_adsgetnumopentables.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)