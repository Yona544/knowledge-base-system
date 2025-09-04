AdsStmtDisableEncryption




Advantage Database Server 12  

AdsStmtDisableEncryption

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtDisableEncryption  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtDisableEncryption Advantage Client Engine ace\_Adsstmtdisableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtDisableEncryption  Advantage Client Engine |  |  |  |  |

Does not encrypt the cursor generated after executing the SQL statement.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtDisableEncryption( ADSHANDLE hStatement ); |

Parameter

|  |  |
| --- | --- |
| hStatement(I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |

Remarks

This function reverses the effect of [AdsStmtEnableEncryption](ace_adsstmtenableencryption.htm).

Example

[Click Here](ace_more_examples.htm#adsstmtdisableencryption_example)

See Also

[AdsStmtEnableEncryption](ace_adsstmtenableencryption.htm)