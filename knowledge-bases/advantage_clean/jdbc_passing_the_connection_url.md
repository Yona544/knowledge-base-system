---
title: Jdbc Passing The Connection Url
slug: jdbc_passing_the_connection_url
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_passing_the_connection_url.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 1af5fef73db1bb86b5c3036b6cf5c2feb71a38cc
---

# Jdbc Passing The Connection Url

Passing the Connection URL

Passing the Connection URL

Advantage JDBC Driver

| Passing the Connection URL  Advantage JDBC Driver |  |  |  |  |

After registering the driver, you must pass your database connection information in the form of a connection URL. The following is a template URL for the Advantage JDBC Driver. Substitute the values specific to your database.

jdbc:sap:advantage://server\_name:6262

For example, to specify a connection URL that includes the user ID "user1" and the password "secret":

Connection conn = DriverManager.getConnection

("jdbc:sap:advantage://server1:6262","user1","secret");

Note The server\_name is an IP address or a host name, assuming that your network resolves host names to IP addresses. You can test this by using the ping command to access the host name and verifying that you receive a reply with the correct IP address.

 

The numeric value after the server name is the port number on which the Advantage Database Server is listening. The values listed here are sample defaults. You should determine the port number that your database is using and substitute that value.

 

For the complete list of Connection URL parameters see [Connection String Properties](jdbc_connection_string_properties.md).
