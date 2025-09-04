Connecting to Advantage Using the Advantage ODBC Driver




Advantage Database Server 12  

     Connecting to Advantage Using the Advantage ODBC Driver

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connecting to Advantage Using the Advantage ODBC Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Connecting to Advantage Using the Advantage ODBC Driver Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Connecting\_to\_Advantage\_Using\_the\_Advantage\_ODBC\_Driver Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 19 - ODBC, PHP, DBI/Perl > Connecting to Advantage Using the Advantage ODBC Driver / Dear Support Staff, |  |
| Connecting to Advantage Using the Advantage ODBC Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Before you can execute SQL statements against Advantage, you must obtain a connection to Advantage through the ODBC driver. Advantage supports two ODBC API functions for obtaining a connection. These are SQLConnect and SQLDriverConnect.

You use SQLConnect when there is a DSN (data source name) for the directory or data dictionary that you want to connect to. SQLDriverConnect, by comparison, does not require a DSN. Instead, the connection request is passed to SQLDriverConnect in its connection string. How you connect using these functions is described in the following sections.

Connecting Through ODBC Using a Data Source Name

A DSN is a definition that is stored on the workstation, and can be used to connect to data using an ODBC driver. Under the Windows operating system, DSN definitions are stored in the Windows Registry, while in Linux these definitions appear in a configuration file named odbc.ini.

Windows users typically do not add the Windows Registry entries for a DSN manually. Instead, they use an applet found in either the Control Panel (for older Windows installations), or the Administrative Tools page of the Control Panel. The name of this applet depends on which operating system you are using, but it always includes the letters ODBC. In Windows 2000 and Windows XP, for example, it is called Data Sources (ODBC).

To define a DSN manually, run this utility after you have installed the Advantage ODBC Driver on the workstation. If your client application is going to run under an end user account, you can add a user DSN. If your application is going to run under some other account, such as IUSER\_MACHINE (used by Microsoft's Internet Information Server), add a system DSN.

Once you have decided to add either a user or system DSN (by selecting either the User or System tabs of this applet), click the Add button. Windows responds by displaying the Create New Data Source dialog box shown in Figure 19-1. Select Advantage StreamlineSQL ODBC from this list, and then click Finish.

Figure 19-1: The Create New Data Source dialog box in Windows

You will then see the Advantage StreamlineSQL ODBC Driver Setup dialog box, shown in Figure 19-2. You use this dialog box to configure the DSN.

Set Data Source Name to the name you will use to refer to this DSN, and provide an optional description for the Description field.

If you will use this DSN to connect to a data dictionary, check the Data Dictionary checkbox and enter the full path to the data dictionary in the provided field. If you will use this DSN to connect to free tables, enter the data directory path here. In most cases, you will want to use a UNC (universal naming convention) path in this field.

Figure 19-2: The Advantage StreamlineSQL ODBC Driver Setup dialog box

Use the Table Type, Locking Type, Advantage Locking, Character Set, and Packet Compression dropdown lists to define what data you are connecting to and how. To configure the size of memo blocks created by ODBC, or to adjust the number of tables to cache, set the corresponding fields. Also, you can configure the ODBC driver to show deleted rows for DBF tables, as well as trim trailing spaces from character fields.

When you are done configuring your DSN, click the OK button to save the DSN definition in the Windows Registry.

It is also possible to create a DSN by writing to the Windows Registry programmatically. This approach is useful if you want to create an automated setup for your client applications, rather than having to enter the DSN information manually on every machine. Note, however, that you should extensively test any code that writes to the Windows Registry, after making a backup of the Registry, as inappropriate changes to the Windows Registry can render a computer unstable or even unusable.

   
TIP: For guidance on creating Registry entries programmatically, start by adding a DSN using the Data Sources (ODBC) applet. Then, inspect the entries that this applet added to the Registry for the keys, values, and data that you need to insert. You will find these entries in HKEY\_CURRENT\_USER\ SOFTWARE\ODBC\ODBC.INI for user DSNs, and HKEY\_LOCAL\_MACHINE\SOFTWARE\ODBC\ ODBC.INI for system DSNs. You can also find information on creating DSNs at http://msdn.Microsoft.com.  
 

In Linux, you create a DSN by adding entries to the odbc.ini file. Refer to the Advantage help for information on working with the odbc.ini file.

Once you have created the DSN that you are going to use, you will be able to call the SQLConnect function of the ODBC API. This function takes seven parameters. The first parameter is a connection handle that you previously allocated by calling SQLAllocHandle. The remaining parameters are string and integer pairs, where you pass the DSN name, user name, and password in the second, fourth, and sixth parameters, respectively; and the lengths of these strings in the third, fifth, and seventh parameters.

Connecting Through ODBC Using a Connection String

The primary drawback to using a DSN is that you must define the DSN on each workstation, which increases the complexity of your client installations. Fortunately, ODBC provides an alternative to using a DSN. This second mechanism employs a connection string.

The ODBC API includes two functions that accept a connection string: SQLDriverConnect and SQLBrowseConnect. Advantage only supports SQLDriverConnect.

SQLDriverConnect takes eight parameters. The first parameter is a connection handle, which you obtain by calling SQLAllocHandle, and the second is the Windows handle of your client application. The third and fifth parameters are used for the input connection string and the completed connection string, respectively. (The completed connection string is the version of the connection string used by ODBC to connect to the database. It includes any parameters that have been expanded by ODBC, as well as any default values not included in the input connection string.) The fourth parameter is the size of the input connection string, and the sixth parameter is the size of the buffer that you have allocated for the completed connection string.

The seventh parameter is the size of the completed connection string that was written to the buffer referenced in the fifth parameter, and the eighth parameter permits you to configure whether or not the ODBC driver manager should prompt the user for additional connection information, if needed. For example, if you pass empty strings in place of the user name and password parameters, and a user name and password are required to connect, you can instruct SQLDriverConnect to prompt the user for this information at runtime.

The connection string itself consists of zero or more parameters that you use to connect to Advantage in the form of name/value pairs. The name and value parts are separated by an equal sign (=), and individual name/value pairs are separated by semicolons. Table 19-1 shows a complete list of the connection string parameters and the values that you can assign to them.

 

|  |  |
| --- | --- |
| Parameter | Description |
| AdvantageLocking | Set to ON to use Advantage proprietary locking, or OFF to use compatibility locking. The default value is ON. |
| CharSet | Set to either ANSI or OEM. The default is ANSI. |
| Compression | Set to ALWAYS, INTERNET, NEVER, or empty. If left empty (the default), the ADS.INI file will control the compression setting. This parameter is not used by ALS. |
| CommType | The communication protocol to use to connect to ADS. Under Windows and Linux, the default is UDP\_IP. To use TCP/IP, set CommType to TCP\_IP. To use IPX, set CommType to IPX. |
| DefaultType | Set to FoxPro, Advantage, or Clipper. This parameter is ignored for data dictionary connections, but is required for free tables. The default is Advantage. |
| Description | This parameter is not used. |

Table 19-1: The Advantage ODBC Driver Connection String Parameters