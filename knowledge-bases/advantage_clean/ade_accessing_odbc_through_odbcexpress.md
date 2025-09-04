---
title: Ade Accessing Odbc Through Odbcexpress
slug: ade_accessing_odbc_through_odbcexpress
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_accessing_odbc_through_odbcexpress.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4419b0248f646f1fbdc53c98af5ac5dd88b5d819
---

# Ade Accessing Odbc Through Odbcexpress

Accessing ODBC Through ODBCExpress

Accessing ODBC through ODBCExpress

Advantage TDataSet Descendant

| Accessing ODBC through ODBCExpress  Advantage TDataSet Descendant |  |  |  |  |

ODBCExpress allows a Delphi application to access ODBC data without the BDE. For more information about ODBCExpress, see their web site at www.odbcexpress.com.

THdbc

The THdbc component provides properties and methods specific to the connection. The following properties define the connection to the ODBC Data Source.

| Property | Description |
| CursorLib | Specifies the Cursor Library to be used for the connection. This should be set to "Use ODBC". |
| DataSource | Defines the ODBC Data Source to be used for the connection. |
| KeepConnection | Indicates if the connection to the Data Source will be maintained when all associated TTable and TQuery components are inactive. This should generally be set to True to avoid connecting to and disconnecting from the DSN with the execution of each SQL statement. |
| InfoPrompt | Indicates if a login prompt will be displayed when the connection is opened. |

TOEQuery

| Property | Description |
| DataSource | If the THdbc component is used this should be set to the name of that component. Otherwise, it should be set to the name of the DSN you have established to access the data. |
| SQL | This is a TStrings property that contains the actual SQL statement to be executed. If it is a SELECT statement, the result-set can be used to populate data controls. |
| RequestLive | This controls whether or not ODBCExpress attempts to return a live (updateable) result set to the user. If False, a read-only result-set will be returned. If True, ODBCExpress will return an updateable result set if possible. Note that if you plan to set this to True in order to get updateable result sets, you should have a unique index built on the table you are querying. This will allow ODBCExpress to construct efficient UPDATE statements. |
| UpdateMode | Indicates how the WHERE clause of the UPDATE statement is constructed when ODBCExpress must create an UPDATE statement in response to an edit of a field in a live result set. In general, it is best to use upWhereKeyOnly, which causes ODBCExpress to use only key fields in the WHERE clause. In order for ODBCExpress to use this option, though, the table being edited must have an existing unique index. Otherwise, ODBCExpress will construct a WHERE clause that uses every column in the table. |

There are several other components available to control ODBC data access with ODBCExpress. A description of these components, as well as a more detailed description of the components described here can be found in the ODBCExpress Help file.
