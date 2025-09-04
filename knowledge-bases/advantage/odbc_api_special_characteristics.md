API Special Characteristics




Advantage Database Server 12  

API Special Characteristics

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| API Special Characteristics  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - API Special Characteristics Advantage ODBC Driver odbc\_Api\_special\_characteristics Advantage ODBC Driver > Using the Advantage ODBC Driver with SQL > API Special Characteristics / Dear Support Staff, |  |
| API Special Characteristics  Advantage ODBC Driver |  |  |  |  |

SQL Statement Limitations

The Advantage ODBC Driver applies the following restrictions to SQL statements:

|  |  |
| --- | --- |
| · | Maximum of 255 characters in a table and index names. |

|  |  |
| --- | --- |
| · | Maximum of 128 characters in column names |

|  |  |
| --- | --- |
| · | Maximum of 128 characters in index names |

|  |  |
| --- | --- |
| · | Maximum of 20 Columns in ORDER BY |

|  |  |
| --- | --- |
| · | Maximum of 15 Columns in index |

|  |  |
| --- | --- |
| · | Maximum of 255 Database name length |

Database API Parameters

There are several API parameters that may be sent with SQLGetInfo() to return information specific to the Advantage Database Server. The constants and return values are described below:

|  |  |
| --- | --- |
| InfoType | Return Value |
| SQL\_DATABASE\_NAME | Long pointer to the current table qualifier. This may be in the form of drive:directory (e.g., as in the ODBC Administrator, like "C:\XISAM\DATA" ) or any other table qualifier (e.g., ""[c:]"\data]"). For more information on table qualifiers, see [Advantage SQL Engine](master_advantage_sql_engine.htm). |
| SQL\_DBMS\_NAME | "Advantage" |
| SQL\_DBMS\_VER | Current version |
| SQL\_DRIVER\_NAME | "ADSODBC.DLL" |
| SQL\_QUALIFIER\_NAME\_SEPARATOR | "\" |
| SQL\_QUALIFIER\_TERM | "DIRECTORY" |
| SQL\_SEARCH\_PATTERN\_ESCAPE | "\" |
| SQL\_SERVER\_NAME | "Advantage" or "ADSODBC.DLL" |