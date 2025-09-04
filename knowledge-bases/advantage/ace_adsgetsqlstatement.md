AdsGetSQLStatement




Advantage Database Server 12  

AdsGetSQLStatement

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetSQLStatement  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetSQLStatement Advantage Client Engine ace\_Adsgetsqlstatement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetSQLStatement  Advantage Client Engine |  |  |  |  |

Returns the SQL statement text associated with the statement handle passed in.

Syntax

UNSIGNED32 AdsGetSQLStatement( ADSHANDLE hStmt,

UNSIGNED8 \*pucSQL,

UNSIGNED16 \*pusLen );

Parameters

|  |  |
| --- | --- |
| hStmt (I) | Statement handle to retrieve the SQL statement text from. |
| pucSQL (O) | Buffer to return the statement in. |
| pusLen (I/O) | Length of pucSQL buffer on input, number of bytes returned on output. |

Remarks

Use AdsGetSQLStatement to retrive the SQL statement text last executed on hStmt