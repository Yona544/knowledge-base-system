Full Text Search Index Updates




Advantage Database Server 12  

Full Text Search Index Updates

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Index Updates  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Index Updates Advantage Concepts master\_Full\_text\_search\_index\_updates Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Index Updates  Advantage Concepts |  |  |  |  |

Unless an index was created with the "fixed" option (ADS\_FTS\_FIXED API option or NOTMAINTAINED SQL option), Advantage will attempt to maintain the index. If, however, your application updates BLOBs in chunks, Advantage cannot maintain the index. The AdsSetBinary API allows portions of binary and image fields to be updated in a piece-wise fashion. Most applications, though, update the entire value with a single call.

Advantage does not update FTS indexes during transactions. FTS index modifications are not visible until the transaction is committed. This means that FTS queries on fields updated in transactions will return results based on the state of the FTS index prior to the transaction. The following statements illustrate this:

INSERT into apdd ( word, definition ) values ( testcase, test some different data );

BEGIN transaction;

UPDATE apdd set definition = other data where word = testcase;

SELECT \* from apdd where contains( definition, test data );

The select statement will return the newly inserted row (if there is an FTS index on the field) because it will evaluate the rowset based on the index, which will not be updated until the COMMIT is issued. Note that if there is no FTS index, then the CONTAINS will be evaluated by examining the physical data, so the statement will not return the newly inserted record.

Normally, with FTS index updates, only the modified data is changed in the index. In other words, if the data changes from "first test case" to "second test case", then the only changes to the FTS index will to be to remove the "first" key and add the "second" key. If, however, the FTS index is on a VarChar field, all old keys will be removed and all new keys will be added with each update.