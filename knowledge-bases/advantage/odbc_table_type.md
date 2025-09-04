Table Type




Advantage Database Server 12  

Table Type

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Table Type |  |  | Feedback on: Advantage Database Server 12 - Table Type odbc\_Table\_type Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Table Type |  |  |  |  |

The Table Type specifies the index type and memo file type to be used with the database files associated by the "Database or Data Dictionary Path" directory. These options are available:

|  |  |
| --- | --- |
| · | Advantage - Support for Advantage proprietary ADT tables with ADI index and ADM memo file formats. |

|  |  |
| --- | --- |
| · | FoxPro - Support for FoxPro-compatible DBF tables with CDX index and FPT memo file formats. |

|  |  |
| --- | --- |
| · | Visual FoxPro  Support for Visual FoxPro-compatible DBF tables with CDX index and FPT memo file formats. The Visual FoxPro table type is a superset of of the original FoxPro support. It provides support for additional features such as NULL field values, new field types, candidate indexes, long field names, etc. |

|  |  |
| --- | --- |
| · | Clipper - Support for CA-Clipper-compatible DBF tables with NTX index and DBT memo file formats. |

The Table Type is used to determine what table type to open and for creating index files of the specified type.

Note When opening tables on database connections, this setting is ignored. When creating new tables on database connections, this setting is respected and affects the type of the table as well as index and memo file types. In order for newly created tables and indexes to be added to the data dictionary, remember that you must be logged in to the data dictionary as administrator (user ADSSYS).

 

Note When using free connections, the Advantage ODBC Driver only supports auto-open indexes. To use NTX indexes and other non-auto-open indexes, you must use a database connection. Create a database (defined in an Advantage Data Dictionary) and add the tables and the associated NTX index files to that database. Then use those tables on that database connection. The NTX index files will then get automatically opened when the corresponding DBF table is opened. You can use the Advantage Data Architect to create a database and data dictionary.