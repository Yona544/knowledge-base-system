Using the Advantage ODBC Driver with Delphi




Advantage Database Server 12  

Using the Advantage ODBC Driver with Delphi

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using the Advantage ODBC Driver with Delphi  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Using the Advantage ODBC Driver with Delphi Advantage TDataSet Descendant ade\_Using\_the\_advantage\_odbc\_driver\_with\_delphi Advantage TDataSet Descendant > Using the Advantage ODBC Driver with Delphi > Using the Advantage ODBC Driver with Delphi / Dear Support Staff, |  |
| Using the Advantage ODBC Driver with Delphi  Advantage TDataSet Descendant |  |  |  |  |

In addition to TAdsQuery, the Advantage ODBC Driver is another mechanism for accessing your data with SQL statements. ODBC Data Sources can be accessed from Delphi applications using either the TTable component or the TQuery component. The interface provided by Delphi to access ODBC data is the BDE. There are also third-party BDE replacements available to allow access to the Advantage ODBC Driver without requiring the installation of the BDE. See the ODBCExpress sample application that is available from the Downloads section of the Advantage Developer Zone Web site at http://DevZone.AdvantageDatabase.com.

When properly optimized, the Advantage ODBC Driver provides high-performance SQL access to Advantage data. Indexes and Advantage Optimized Filters are used to resolve the WHERE clause of the SQL statement at the server and return the smallest possible result-set to the client workstation. The Advantage ODBC Help file contains more information about optimizing data to enhance performance.

Choosing an Advantage Data Access Interface

The TAdsTable control provides the developer with a record-based data access method. Record-based data access is often the choice for developers when a high level of control over the data is required. A record pointer is maintained for each instance of the table and updates can be made directly to the current record. Indexes and filters can be explicitly accessed. Although there is generally more code required, transactional systems that access and then update specific records will generally see higher performance with the record-based data access methods provided by the Advantage TAdsTable components.

In contrast, SQL was developed to process data using relational algebra and uses a result-set as the basic unit of data rather than the record. This data access method provides a small, flexible language that is optimal for writing reports or summarizing data. Systems that require large amounts of data to be processed, reported, or summarized may benefit from using SQL. The simplicity and flexibility of the language lends itself to report writers and user-defined queries. The drawback, though, is that the increased flexibility can come at a performance cost if used indiscriminately. For example, it is simple to construct a query that locates a specific record through the use of a WHERE clause, but it might not be optimized if no indexes are available for the search. When using a record-based method such as TAdsTable, it is more obvious that an index is needed for something like a Seek operation. With SQL, though, the WHERE clause is the same regardless of whether or not indexes are available for optimization and, thus, it is easier for a developer to assume that an index is not needed.

If you are going to use SQL in your application, you can accomplish this by using either TAdsQuery or the Advantage ODBC Driver. You may find that it is simpler to use TAdsQuery rather than ODBC. Because it is a TDataSet descendant, it does not need the BDE or third-party components as does the ODBC driver. In addition, TAdsQuery requires fewer layers of indirection and, thus, may provide better performance than the ODBC driver.

Accessing the Advantage ODBC Driver in Delphi

All ODBC drivers require a mechanism within Delphi to provide access to the ODBC Data Source. Delphi ships with the BDE, which is the Delphi interface for ODBC data. There are also third-party products available to replace the BDE as an ODBC interface. To see an example demonstrating the Advantage ODBC Driver with the BDE and with ODBCExpress, refer to the Downloads section of the Advantage Developer Zone Web site at http://DevZone.AdvantageDatabase.com.

[Accessing ODBC Through the BDE](ade_accessing_odbc_through_the_bde.htm)

[Accessing ODBC Through ODBCExpress](ade_accessing_odbc_through_odbcexpress.htm)