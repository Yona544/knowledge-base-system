Database Directory




Advantage Database Server 12  

Database Directory

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Database Directory  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - Database Directory Advantage ODBC Driver odbc\_Database\_directory Advantage ODBC Driver > Using the Advantage ODBC Driver with SQL > Database Directory / Dear Support Staff, |  |
| Database Directory  Advantage ODBC Driver |  |  |  |  |

For [free connections](javascript:hhpopuplink.TextPopup(popid_709342792X,FontFace,-1,-1,-1,-1)), a directory must be selected as the Database or Data Dictionary Path for the Advantage ODBC Driver to reference (e.g., x:\data). All [free tables](javascript:hhpopuplink.TextPopup(popid_1881894412X,FontFace,-1,-1,-1,-1)) in the directory will be available to the driver.

By specifying a directory as the Database or Data Dictionary Path for [free connections](javascript:hhpopuplink.TextPopup(popid_709342792X,FontFace,-1,-1,-1,-1)), this implies that the directory is a database. When referencing information about databases using the Advantage ODBC Driver for free connections, you may substitute directory for the references to database.

Tables can be in different directories than the Database or Data Dictionary Path directory for [free connections](javascript:hhpopuplink.TextPopup(popid_709342792X,FontFace,-1,-1,-1,-1)) by giving a fully-qualified path (either UNC or path with a drive letter) for a table name. The USE statement can be used to change the default database directory for free connections.

For [database connections](javascript:hhpopuplink.TextPopup(popid_727119539X,FontFace,-1,-1,-1,-1)), it should be a valid path name including the Advantage Data Dictionary file name (e.g., x:\database\mydictionary.add).