7053 VarChar fields are not supported with this operation




Advantage Database Server 12  

7053 VarChar fields are not supported with this operation

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7053 VarChar fields are not supported with this operation  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7053 VarChar fields are not supported with this operation Advantage Error Guide error\_7053\_varchar\_fields\_are\_not\_supported\_with\_this\_operation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7053 VarChar fields are not supported with this operation  Advantage Error Guide |  |  |  |  |

Problem: A Copy To, Append From, Copy Table, Copy Table Contents, or Memo Pack operation was attempted but the table contained at least one VarChar field (a.k.a. weakly-typed VariField). The Copy To, Append From, Copy Table, Copy Table Contents, and Memo Pack operations cannot handle VarChar fields.

Solution: Specify tables that do not contain VarChar fields before attempting the Copy To, Append From, Copy Table, Copy Table Contents, or Memo Pack operations. This error will result if a pack operation is performed on an encrypted table. To perform the pack operation, first decrypt the table. Once finished, the table may be encrypted again.