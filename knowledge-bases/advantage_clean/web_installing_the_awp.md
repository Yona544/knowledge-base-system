---
title: Web Installing The Awp
slug: web_installing_the_awp
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_installing_the_awp.htm
source: Advantage CHM
tags:
  - web
checksum: 6d9817f5c73ff4c7c0b8074aa799d5d00be01d8e
---

# Web Installing The Awp

Installing and Configuring the Advantage Web Platform

Installing and Configuring the Advantage Web Platform

Advantage Web Platform

| Installing and Configuring the Advantage Web Platform  Advantage Web Platform |  |  |  |  |

Installation Notes

The Advantage Web Platform is built as an Apache web server module, thus the installation program includes a copy of the Apache HTTP Server. After a successful installation, Apache will run as a Windows service with the name "Advantage Web Platform".

The installation script will prompt you to decide if you want to expose the example database. If you chose that option, you can perform a quick test to see if the system is working. The example\_db location created by the installation includes a small data dictionary placed in a folder under the target installation location. If you have Advantage Database Server on the same machine on which you installed the Advantage Web Platform, enter the following command in a web browser to retrieve an XML result set.

https://YourServer.And.Domain:6282/adsweb/example\_db/v1/Tasks

The result can be obtained as JSON:

https://YourServer.And.Domain:6282/adsweb/example\_db/v1/Tasks?$format=json

If Advantage Database Server is not running on the same system, it will be necessary to edit adsweb.conf to point example\_db to the correct location and copy the sample database.

Browser Note: If you want to test some service URL's, the best browser to use is Google Chrome. Chrome understands the application/json content type that the service returns and will display the content directly in your browser.  Some browsers require modifications in order to display application/json content (otherwise they will just try to save the response to a file).

Errors

If you encounter general errors that do not include an error description in the response, check the Apache error log file, which by default is located in c:\Program Files\Advantage NN.n\adsweb\apache\logs\error.log

Configuration

After the installation is finished, you will need to expose a database to test. Alternately, if you chose to expose the example database, you will not have to manually configure your own, but it is still a good idea to open the adsweb.conf file to get an idea of how Locations are exposed.

Apache Location Directives (<http://httpd.apache.org/docs/2.0/mod/core.html#location>) are used to map a URL to a specific database and its set of configuration options.

To modify Locations and add new Locations, edit the c:\Program Files\Advantage NN.n\adsweb\apache\conf\adsweb.conf file. If you make any changes, you will need to restart the service. There are two ways to refresh the configuration for a running service:

1) The service can be gracefully restarted using the following command, which will stop the Apache child service:

apache\bin\httpd -n AdvantageWebPlatform -k restart

2) Or you can start and stop the Windows service via the following two commands:

net stop AdvantageWebPlatform

net start AdvantageWebPlatform

 

DbConnectionString

DbConnectionString specifies the connection string that will be used to connect to the database. The [AdsConnect101](ace_adsconnect101.md) documentation contains the available connection string options. An example of this property is:

DbConnectionString "Data Source=c:\data\example\_db\tasks.add;ServerType=remote;Pooling=True;user id=adssys;SQLTimeout=30;"

The Data Source value should typically be a data dictionary. The Advantage Web Platform currently provides only minimal support for free connections.  It is possible to retrieve the contents of a table, but many other operations will not work because of the lack of metadata available, which makes it difficult for many clients to retrieve information necessary for useful queries. Many OData operations also rely on primary key fields (not available on free tables) to identify records for update and delete operations. In addition, free table connections are not as secure as data dictionary connections, and therefore not recommended for exposure via the web. To completely disable free table access (and only allow the use of data dictionary tables), add "CheckFreeTableAccess=TRUE;" to the DbConnectionString.

- Do not use mapped or subst drives in your database connection string. The service can not resolve those paths. Use a physical drive letter or UNC.

- For performance reasons, you should normally include "Pooling=True;" in the connection string to enable [connection pooling](web_connection_pooling.md).

- In the above example, SQLTimeout is included to put an upper limit on query processing at the server. This would be particularly useful if you enable the [\_\_query service](web_query_service_operation.md).

DbAuthentication

DbAuthentication is used to specify how incoming connections will be authenticated. Three options are supported:

| 1. | None: No authentication required. If Apache is not prompting for authentication, you will very likely want to only expose this data as a read-only feed. To accomplish this, set up a database user with read-only privileges, and specify that username and password in your DbConnection string. You should test this setup by trying to perform an update to make sure it fails. |

| 2. | Database (default): User credentials will be prompted for, and routed to Advantage for verification via existing user accounts in the database. |

| 3. | Apache: Used if you would rather use an Apache module for authentication. If specified, you must then provide Apache directives for your specific module. For example, you could use the AuthBasicProvider and AuthUserFile directives to implement authentication via an Apache passwd file. Note that if you use Apache authentication you must then provide a database username and password in your DbConnection string. |

DbAuthentication "Database"

SetHandler

This option is required and should not be modified. If this option doesnt exist then URL routes matching this location will not be forwarded to the Advantage module and will not be handled.

SetHandler adsweb

SSLRequireSSL

This directive indicates that HTTPS is required; it forbids access through plain HTTP. For most installations, you will probably want to enable this. Otherwise, all traffic will be in the clear and even user names and passwords could be extracted from the packets by anyone sniffing the network. The password is base-64 encoded, but that would not stop a real attacker. For development and testing, though, it is sometimes much simpler to use HTTP because it is simpler to debug problems. If this directive is not given for a Location, then you can use requests over HTTP to port 6272 (or whatever port you specified for the Listen directive. For example:

http://localhost:6272/adsweb/mydd/v1/mytable

To specify the directive:

SSLRequireSSL

DbFormatJSON

By default, the Advantage Web Platform will return JSON data in a condensed format for the most efficient use of the network. For debugging purposes, however, it is often nice to see results as nicely formatted JSON. The DbFormatJSON option can be used on a per-Location basis to specify if you want JSON formatted. No arguments are required, just the existence of the directive is sufficient.

DbFormatJSON

ServerName

This directive is typically specified in the httpd.conf file. When the Apache server starts up, it attempts to determine the servers fully qualified domain name (FQDN).  (This is then used when constructing some URIs that are returned to the client in the data payload, such as the \_\_next link when paging is used.)  In certain configurations, Apache can determine the FQDN incorrectly.  Because of this, Apache has introduced the ServerName configuration parameter, which, if specified, will always be used instead of the value Apache automatically determines.  If the \_\_next links or ID fields of the data payload contain the domain localdomain (or if the hostname does not match that of your server), specify a ServerName entry in the httpd.conf or the extra\httpd-ssl.conf file.  (If SSL communications are used, the entry would be placed in extra\httpd-ssl.conf, otherwise, place the entry in the main httpd.conf.)  The setup script attempts to configure this value in both configuration files, but they should be checked for accuracy.

If the host has no configured domain name, then the IP address should be used instead of the host name.  See Apache documentation here for more information.

ServerName hostname.domainname.com:6272

DbEnableQueryService

Enables the [\_\_query service operation](web_query_service_operation.md), which is disabled by default.  The \_\_query service allows for ad hoc queries to be executed against the server.

DbEnableQueryService

DbPageSize

Limits the maximum number of rows to return to client per request. The page size limits the amount of resource that the service consumes to fill each client request. Full filling larger pages demands more resource on the server. If there are more rows available than the page size, the \_\_next link reference will be included in the result. The client can use the \_\_next reference to request for additional rows. See this WCF example for more information on server side page limit and the usage of the \_\_next reference.

If This option is not specified in the configuration file, the default page size is 100 rows.

DbPageSize 20

DbEnableGetURIs

This directive indicates that the Location containing the directive can be enumerated and returned with the [\_\_GetURIs service operation](web_geturis_service.md).

DbEnableGetURIs
