---
title: Devguide Connecting To Data 1
slug: devguide_connecting_to_data_1
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_connecting_to_data_1.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 47df7dcbe1e79c62e576d18a95455fab1261d396
---

# Devguide Connecting To Data 1

Connecting to Data

     Connecting to Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Connecting to Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You connect to a data dictionary or to a directory in which free tables are located by calling the getConnection method of the DriverManager. The getConnection method takes a connection string, which must be prefaced by the driver manager class that you want to get the connection for. For a connection to ADS, this prefix is jdbc:extendedsystems:advantage:.

Prior to calling getConnection, you must have instantiated the Advantage JDBC Driver. This is done by calling the forClass method of the Class class, passing the name of the Advantage JDBC Driver as an argument.

Because numerous event handlers associated with the MainFrame class use this connection, a variable of type Connection (a JDBC class) is declared in the MainFrame's class declaration, which places this variable in scope of all event handlers that need it. This variable declaration and several additional JDBC class variables that are used in two or more event handlers in this project are shown here:

public class MainFrame extends JFrame {  
  Connection conn;  
  Statement stmt;  
  PreparedStatement prepStmt;  
  //additional declarations

The Connection variable (conn) in the preceding segment is assigned a connection from a private method that is called from the MainFrame class constructor. This method, databaseInit, is shown in the following code segment:

private void databaseInit() throws Exception{  
   
Class.forName  
  ("com.extendedsystems.jdbc.advantage.ADSDriver");  
  conn =   
    DriverManager.getConnection("jdbc:extendedsystems:" +  
    "advantage://server:6262/share/adsbook/"+  
    "demodictionary.add;user=adsuser;password=password");  
  stmt = conn.createStatement();  
  prepStmt = conn.prepareStatement("SELECT \* FROM INVOICE "+  
    "WHERE [customer id] = ?" );  
}

As you can see from the preceding method, forName is passed the name of the class of the Advantage JDBC Driver, which instantiates the driver. When the getConnection method of the DriverManager is called, it locates the instantiated driver by means of the prefix in the connection string.

In addition to containing the prefix for the Advantage JDBC Driver, this connection includes a URL (uniform resource locator) that points to the TCP/IP port on the machine named server where the data is located. This URL also includes an optional data location, identified by a share on that server (named share in this instance), and a qualified path to the data dictionary. Two additional parameters, the user name and password, are passed in this connection string as well.

   
NOTE: If an exception is raised when you attempt to connect, verify that your URL is correct and try again. You should also ensure that all clients on the same machine use a remote connection (since the Java driver only uses remote).  
 

Because this connection string refers to the DemoDictionary data dictionary, and this dictionary requires logins, this particular connection string contains all of the essential parameters needed to connect to this database. Additional parameters could have been passed in this connection string as name/value pairs, where an equal sign separates the name and value. As you can see in the preceding connection string, when the connection string contains two or more name/value pairs, semicolons separate them. The full list of the optional connection string parameters is shown in Table 16-1.

 

| Parameter | Description |
| Catalog | If the data directory or data dictionary path is not provided in the connection URL, set it to the qualified name of the data dictionary or the file location on the specified server where the free tables are located. |
| CharType | Identifies the character set used by the server. Can be set to ansi or oem. The default is ansi. |
| LockType | Identifies the type of locking to be used by ADS. Can be set to compatibility or proprietary. The default is proprietary. |
| Password | If the data dictionary requires login, use this parameter to submit the user's password. |
| ShowDeleted | Set to true to include deleted records in DBF files. Set to false to suppress deleted records. The default is false. |
| TableType | Used to identify the type of table when connecting to free tables. This parameter can be set to adt, cdx, or ntx. The default is adt. This property is not used when you connect to a data dictionary. |
| User | If the data dictionary requires login, use this parameter to submit the user's user name. |

Table 16-1: The Advantage Java JDBC Driver Connection String Parameters
