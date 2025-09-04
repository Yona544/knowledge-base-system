AdsStmtClearTablePasswords




Advantage Database Server 12  

AdsStmtClearTablePasswords

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtClearTablePasswords  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtClearTablePasswords Advantage Client Engine ace\_Adsstmtcleartablepasswords Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtClearTablePasswords  Advantage Client Engine |  |  |  |  |

Clears all table encryption passwords associated with the statement handle.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtClearTablePasswords( ADSHANDLE hStatement ); |

Parameters

|  |  |
| --- | --- |
| hStatement(I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |

Remarks

This function removes all table encryption passwords set using [AdsStmtSetTablePassword](ace_adsstmtsettablepassword.htm).

Example

[Click Here](ace_more_examples.htm#adsstmtcleartablepasswords_example)

See Also

[AdsStmtEnableEncryption](ace_adsstmtenableencryption.htm)

[AdsStmtDisableEncryption](ace_adsstmtdisableencryption.htm)

[AdsStmtSetTablePassword](ace_adsstmtsettablepassword.htm)