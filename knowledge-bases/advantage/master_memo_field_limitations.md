Memo Field Limitations




Advantage Database Server 12  

Memo Field Limitations

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Memo Field Limitations  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Memo Field Limitations Advantage SQL Engine master\_Memo\_field\_limitations Advantage SQL > SQL Functionality > Memo Field Limitations / Dear Support Staff, |  |
| Memo Field Limitations  Advantage SQL Engine |  |  |  |  |

Memo fields cannot be used in SELECT statements that use DISTINCT, UNION, or GROUP BY clauses. Note that memos can be used with the UNION ALL statement because no "distinct" processing is performed.

Memo fields cannot be used in ORDER BY clauses.