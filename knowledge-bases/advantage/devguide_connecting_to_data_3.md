Connecting to Data




Advantage Database Server 12  

     Connecting to Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connecting to Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Connecting to Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Connecting\_to\_Data\_3 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 18 - The .NET Data Provider > Connecting to Data / Dear Support Staff, |  |
| Connecting to Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You connect to a data dictionary or a directory in which free tables are located using an AdsConnection object found in the Advantage.Data.Provider namespace. At a minimum, you must provide the AdsConnection object with sufficient information to locate your data and configure how the data should be accessed. This is done using the ConnectionString property. This property accepts name/value pairs using the parameters listed in Table 18-1. If you use more than one name/value pair, separate them with semicolons.

 

|  |  |
| --- | --- |
| Parameter | Description |
| CharType | Set to the character set type for DBF files. Valid values are ANSI and OEM. The default value is ANSI. |
| CommType | The communication protocol to use to connect to ADS. Under Windows and Linux, the default is UDP\_IP. To use TCP/IP, set CommType to TCP\_IP. To use IPX, set CommType to IPX. |
| Compression | Set to ALWAYS, INTERNET, NEVER, or empty. If left empty (the default), the ADS.INI file will control the compression setting. This parameter is not used by ALS. |
| Connection Lifetime | The number of seconds after which a connection will be destroyed after being returned to the connection pool. The default is 0. |
| Data Source | The path to your free tables or data dictionary. If you are using a data dictionary, you must include the data dictionary filename in this path. It is recommended that this path be a UNC path. Data Source is a required parameter. |
| DbfsUseNulls | Set to TRUE to return empty fields from DBF files as NULL values. If set to FALSE, empty fields are returned as empty data values. The default is FALSE. |
| EncryptionPassword | Set to an optional password to use for accessing encrypted free tables. This parameter is ignored for data dictionary connections. |
| Enlist | Set to TRUE to enlist the connection in the threads current transaction context (created by TransactionScope) when the connection is opened. The default is TRUE. This property is only applicable if you are using the .NET Framework version 2.0 or later. |
| IncrementUserCount | Set to TRUE to increment the user count when the connection is made. Set to FALSE to make a connection without incrementing the user count. The default is FALSE. |
| Initial Catalog | Optional name of a data dictionary if the data dictionary is not specified in the Data Source parameter. |
| LockMode | Set to PROPRIETARY or COMPATIBLE to define the locking mechanism used for DBF tables. Use COMPATIBLE when your connection must share data with non-ADS applications. The default is PROPRIETARY. |
| Max Pool Size | The maximum number of connections to maintain in the connection pool. The default is 100. |
| Min Pool Size | The minimum number of connections to maintain in the connection pool. The default is 0. |
| Password | When connecting to a data dictionary that requires logins, set to the user's password. |
| Pooling | Set to TRUE to enable connection pooling. Set to FALSE to disable it. The default is TRUE. |
| ReadOnly | Set to TRUE to open tables readonly. Set to FALSE to open tables as editable (read-write). This setting applies to all CommandType values. The default is FALSE. |
| SecurityMode | Set to CHECKRIGHTS to observe the user's network access rights before opening files. Set to IGNORERIGHTS to access files regardless of the user's network rights. The default is CHECKRIGHTS. This property applies only to free table connections. |
| ServerType | Set to the type of ADS server you want to connect to. Use LOCAL, REMOTE, or AIS (Internet). To attempt to connect to two or more types, separate the server types using a vertical bar (|). This is demonstrated in the ConnectionString shown later in this chapter. |
| Shared | Set to TRUE to open tables shared. Set to FALSE to open tables exclusively. This setting only applies to CommandType.TableDirect. The default is TRUE. |
| ShowDeleted | Set to TRUE to include deleted records in DBF files. Set to FALSE to suppress deleted records. The default is FALSE. |
| StoredProcedure Connection | Set to TRUE if connecting from within a stored procedure. When set to TRUE, the connection does not increment the user count. The default is FALSE. |
| TableType | Set to ADT, CDX, or NTX to define the default table type. The default is ADT. This parameter is ignored for data dictionary connections. |
| TrimTrailingSpaces | Set to TRUE to trim trailing spaces from character fields. Set to FALSE to preserve trailing spaces. The default is FALSE. |
| User ID | If connecting to a data dictionary that requires logins, set to the user's user name. |

Table 18-1: The Advantage Data Provider Connection String Parameters

   
NOTE: The parameter values for CharType, LockMode, SecurityMode, ServerType, and TableType parameters also have longer name versions. For example the value ADS\_ANSI can be used instead of ANSI. The longer names are recognized for compatibility with OLE DB (ADO) connection strings. You can find the longer versions of these values in Table 17-1 of Chapter 17 or in the Advantage help.  
 

 

With the Advantage .NET Data Provider, the connection string property values can be enclosed in either single quotes or double quotes, if necessary. For example, if the password contains a semicolon (the connection string parameter delimiter), it would be necessary to enclose it in single quotes or double quotes.

For any of the optional connection string parameters that you fail to provide, the Advantage .NET Data Provider will automatically employ the default parameters.

Because the AdsConnection object that is used by this project must be used by a number of methods, the AdsConnection variable and several other variables that must be repeatedly referenced are declared public members of the Form class. The following is this declaration:

public AdsConnection connection;  
public AdsCommand command;  
public AdsCommand paramCommand;  
public AdsDataReader dataReader;

The data source location of the data dictionary is also declared as a constant member of this class. This constant refers to a share named "share," on a server named "server," as shown in the following declaration:

private const String DataPath = "\\\\server\\share\\" +  
   "adsbook\\DemoDictionary.add;";

This connection, named AdsConnection, is created, configured, and opened from the InitializeDataComponents method of the form, along with several other objects. InitializeDataComponents is called from the Form's constructor. The relevant portion of this custom private method is shown in the following code:

private void InitalizeDataComponents() {  
  connection = new AdsConnection();  
  connection.ConnectionString = "Data Source=" + DataPath +   
    ";user ID=adsuser;password=password;" +   
    "ServerType= LOCAL | REMOTE;TrimTrailingSpaces=True";  
  connection.Open();  
  command = new AdsCommand();  
  command = connection.CreateCommand();  
  //additional statements follow

   
NOTE: If you have difficulty connecting, it might be because you have other client applications, such as the Advantage Data Architect, connected using a local connection. Ensure that all clients on the same machine use the same type of connection.