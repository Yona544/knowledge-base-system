Data Source Setup for Windows




Advantage Database Server 12  

Data Source Setup for Windows

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Source Setup for Windows  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - Data Source Setup for Windows Advantage ODBC Driver odbc\_Data\_source\_setup\_for\_windows Advantage ODBC Driver > Installation and Distribution > Data Source Setup for Windows / Dear Support Staff, |  |
| Data Source Setup for Windows  Advantage ODBC Driver |  |  |  |  |

Once the Advantage ODBC Driver is installed, a data source needs to be configured to use the Advantage ODBC Driver. The data source is an entry in the Windows Registry. When a data source is defined for the Advantage Driver, all information specific to the Advantage Driver and database files is stored under the Data Source entry in the Windows Registry.

The database files and indexes must be stored on your file server, and the Advantage Database Server must be loaded in order to access the files.

The Data Source settings may be modified at any time. Using the ODBC Administrator, you may modify the Data Source and Option settings.

For specific information about the screen fields see the [Data Source Setup Screen](odbc_data_source_setup_screen.htm).

To Setup the Data Source:

|  |  |
| --- | --- |
| 1. | From the ODBC Administrator, click Add. |

|  |  |
| --- | --- |
| 2. | Highlight the Advantage SQL ODBC line, then click OK. |

|  |  |
| --- | --- |
| 3. | Type a unique data source name. For example, type AdvData. This name is used by applications to reference the data source. |

|  |  |
| --- | --- |
| 4. | Specify the database or data dictionary path. Type a valid path name to a mapped drive on the server where the Advantage Database Server is installed or the path and file name of your Advantage Data Dictionary. Click Browse to select a database path or check the Data Dictionary check box and then browse to select a data dictionary file. |

Note Multiple Advantage data sources may need to be defined for your environment. If different settings are needed for ODBC connections in one application, separate data sources may be required.

|  |  |
| --- | --- |
| 5. | Review the options and change them to your desired setup. |

|  |  |
| --- | --- |
| 6. | Once the Options are reviewed and/or altered, click OK to exit and save the settings. The new data source is displayed. |

|  |  |
| --- | --- |
| 7. | Click Close to exit the ODBC Administrator. |