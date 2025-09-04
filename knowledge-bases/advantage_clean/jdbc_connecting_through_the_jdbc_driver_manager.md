---
title: Jdbc Connecting Through The Jdbc Driver Manager
slug: jdbc_connecting_through_the_jdbc_driver_manager
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_connecting_through_the_jdbc_driver_manager.htm
source: Advantage CHM
tags:
  - jdbc
checksum: d0f4ae20aa1b2fd9c07556be5a6fc62dea55941e
---

# Jdbc Connecting Through The Jdbc Driver Manager

Connecting Through the JDBC Driver Manager

Connecting Through the JDBC Driver Manager

Advantage JDBC Driver

| Connecting Through the JDBC Driver Manager  Advantage JDBC Driver |  |  |  |  |

One way of connecting to a database is through the JDBC driver manager using the method DriverManager.getConnection. This method uses a string containing a URL. The following is an example of using the JDBC driver manager to connect to Advantage Database Server while passing the user name and password:

Class.forName("com.sap.jdbc.advantage.ADSDriver");

Connection conn = DriverManager.getConnection ("jdbc:sap:advantage://server1:6262/test/data;user=user1;password=up1");

URL Examples

The complete connection URL format used with the driver manager is:

jdbc:sap:advantage://hostname:port[;property=value...]

where:

| hostname | is the TCP/IP address or TCP/IP host name of the Advantage Database Server to which you are connecting. |
| port | is the number of the TCP/IP port that the Advantage Database Server is listening. |
| property=value | specifies connection properties. See [Connection String Properties](jdbc_connection_string_properties.md) for a list of connection properties and their values. |

The location of the database can be specified after the <hostname:port> portion of the connection URL or it can be specified using the catalog property. The following two URLs connect to the same database in the 'userdata' share on 'server1'.

conn = DriverManager.getConnection ( "jdbc:sap:advantage://server1:6262/userdata/db1/db.add" );

conn = DriverManager.getConnection ( "jdbc:sap:advantage://server1:6262;catalog = //server1/userdata/db1/db.add" );

Although UNC path is the preferred method for specifying the location of the database, it is possible to use the drive letter notation on the server to make the connection. For example, if the 'userdata' share on the 'server1' is actually "c:\userdata" on a Microsoft Windows 2003 server, the following URL can be use to obtain the connection.

conn = DriverManager.getConnection ( "jdbc:sap:advantage://server1:6262;catalog = c:\\userdata\\db1\\db.add" );

To connect to the Advantage Database Server to use free tables, specify the directory path as the catalog or specify the directory path after the <hostname:port>. The following three statements will make the equivalent connection.

conn = DriverManager.getConnection ( "jdbc:sap:advantage://server1:6262/userdata/db2" );

conn = DriverManager.getConnection ( "jdbc:sap:advantage://server1:6262;catalog = //server1/userdata/db2" );

conn = DriverManager.getConnection ( "jdbc:sap:advantage://server1:6262;catalog = c:\\userdata\\db2" );

Note that when connecting to the Internet port of the Advantage Database Server, free table connection is not allowed. An Advantage Data Dictionary must be used to authenticate the user.
