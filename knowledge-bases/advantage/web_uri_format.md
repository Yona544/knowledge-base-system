URI Format




Advantage Database Server 12  

URI Format

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| URI Format  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - URI Format Advantage Web Platform web\_URI\_Format Advantage Web Development > Advantage Web Platform > URI Format / Dear Support Staff, |  |
| URI Format  Advantage Web Platform |  |  |  |  |

OData URI Formats are described in detail here: <http://www.odata.org/documentation/uri-conventions>

The following describes the basics of the Advantage-specific URL format. More details are in the following sections describing the various aspects of the supported functionality.

https://hostname:6282/adsweb/<LOCATION>/<API\_VERSION>/<COLLECTION>

The server name and /adsweb prefix will be in all requests. For example:

https://servername.com:6282/adsweb/

The LOCATION segment will be the name of the Location element in the adsweb.conf file. In the default adsweb.conf file this Location is called "example\_db" via this line:

   <Location /adsweb/example\_db>

If you changed that line to <Location /adsweb/MyDB> then your URL would start with:

https://servername.com:6282/adsweb/MyDB

Note that the name is an alias, it is independent of the data dictionary you specify in [DbConnectionString](web_installing_the_awp.htm). In addition, when you change the adsweb.conf file you need to re-start the service via the net stop AdvantageWebPlatform and net start AdvantageWebPlatform commands.

The next segment after the Location is the API\_VERSION and the COLLECTION name (generally the name of a table or a view in the database). The API\_VERSION is currently "v1". The URI to retrieve the contents of a specific record based on primary key from a table named Customers might be:

https://servername.com:6282/adsweb/MyDB/Customers(1525)

More examples are given in the description of Collections.