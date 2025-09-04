AXSQLNTX and Index Optimization




Advantage Database Server 12  

AXSQLNTX and Index Optimization

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AXSQLNTX and Index Optimization  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - AXSQLNTX and Index Optimization Advantage AXSQL RDDs vo\_Axsqlntx\_and\_index\_optimization Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > AXSQLNTX and Index Optimization / Dear Support Staff, |  |
| AXSQLNTX and Index Optimization  Advantage AXSQL RDDs |  |  |  |  |

The AXSQLNTX RDD is used to query data from NTX type DBF tables. However, because NTX indexes are not auto-open indexes, the Advantage query engine cannot natively utilize them to optimize query execution. In order to utilize NTX indexes in the query engine, the DBF table and the NTX indexes must be added to an Advantage Data Dictionary. Once in the data dictionary, the query engine will use any NTX indexes associated with tables in the query to help optimize the query execution.