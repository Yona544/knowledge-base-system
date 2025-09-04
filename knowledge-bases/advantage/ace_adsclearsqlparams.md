AdsClearSQLParams




Advantage Database Server 12  

AdsClearSQLParams

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearSQLParams  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearSQLParams Advantage Client Engine ace\_Adsclearsqlparams Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearSQLParams  Advantage Client Engine |  |  |  |  |

Clears out parameters on this statement previously set using the AdsSet\* APIs

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearSQLParams( ADSHANDLE hStatement ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |

Remarks

Use AdsClearSQLParams to clear all values assigned to parameters and free their associated memory. If this function is not called, then parameter values will remain until the statement handle is closed. If the SQL statement text is changed via the [AdsPrepareSQL](ace_adspreparesql.htm) function, then the old parameter values are assigned to the new statements parameters from left to right.

This method should be used to prevent the accidental use of old parameters with new statements and to free allocated resources. See [AdsPrepareSQL](ace_adspreparesql.htm) for more details.

Example

[Click Here](ace_more_examples.htm#adsclearsqlparamsexample)

See Also

[AdsPrepareSQL](ace_adspreparesql.htm)