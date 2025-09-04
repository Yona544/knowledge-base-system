AX\_PercentIndexed()




Advantage Database Server 12  

AX\_PercentIndexed()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_PercentIndexed()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_PercentIndexed() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_percentindexed Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_PercentIndexed() / Dear Support Staff, |  |
| AX\_PercentIndexed()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Indicates the percent completion of an index build

Syntax

AX\_PercentIndexed() -> numeric

Returns

Returns an integer between 0 and 100 that indicates what percentage of an index build has been completed.

Description

When creating an index, you may specify an expression (usually a UDF) that is evaluated for each record being indexed. This allows the program to display some type of completion/process meter without having the UDF embedded in the index expression. The INDEX...EVAL clause for procedural style code and the cbEval argument for DBServer:SetOrderCondition() for object-oriented style code allows you to specify the UDF. The UDF is stored on the client while the index building occurs on the server.

Advantage ignores the EVERY/nInterval arguments that are used in conjunction with EVAL/cbEval to specify the number of records to process before the EVAL/cbEval expression is evaluated. Instead, Advantage evaluates the clause every 2 seconds on the client.

The AX\_PercentIndexed() function returns an integer that reflects the current percent of completion of the index build.

Note When using EVAL/cbEval, Visual Objects indicates the percentage based on how many records have been extracted from the database table to sort. Visual Objects extracts a block of records, sorts it, and repeats this process until all records in the table have been extracted. Once the blocks are sorted, the index is built. Thus, the extraction/sorting of records is more significant than the build time. Advantage, on the other hand, has shorter record extraction times relative to the build.

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.htm) for code sample for the AxDBServer class.

|  |
| --- |
| GLOBAL oDB as AxDBServer |
|  |
| cbEval := {|| MyFunct() }  // Indexing code block |
| oDB := AxDBServer{ "TEST", .F., .F., "DBFNTXAX" } |
| oDB:SetOrderCondition(cFor, cbForCondition, lAll,cbWhileCondition, cbEval, ; |
| nStep, nStart, nNext, nRecord, lRest, lDescend) |
| oDB:CreateIndex( "Test1", "LastName + FirstName" ) |
|  |
|  |
| proc MyFunct() |
| ? oDB:AX\_PercentIndexed() |

Procedural Example

|  |
| --- |
| Field LastName, FirstName |
|  |
| USE test VIA "DBFNTXAX" |
| INDEX ON LastName + FirstName to Test1 Eval { || MyFunct() } |
|  |
| Procedure MyFunct() |
| ? AX\_PercentIndexed() |