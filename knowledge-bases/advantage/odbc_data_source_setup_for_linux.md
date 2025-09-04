Data Source Setup for Linux




Advantage Database Server 12  

Data Source Setup for Linux

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Source Setup for Linux  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - Data Source Setup for Linux Advantage ODBC Driver odbc\_Data\_source\_setup\_for\_linux Advantage ODBC Driver > Installation and Distribution > Data Source Setup for Linux / Dear Support Staff, |  |
| Data Source Setup for Linux  Advantage ODBC Driver |  |  |  |  |

Once the Advantage ODBC Driver is installed, a data source may need to be configured to use the Advantage ODBC Driver. The data source is an entry in the odbc.ini text file. When adata source is defined for the Advantage Driver, all information specific to the Advantage Driver and database files is stored under the Data Source entry.

The database files and indexes must be stored on your file server, and the Advantage Database Server must be loaded in order to access the files.

The Data Source settings may be modified at any time. Multiple Advantage Data Sources may need to be defined for your environment. If different settings are needed for ODBC connections in one application, separate data sources may be required.