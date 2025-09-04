---
title: Web Stored Procedures
slug: web_stored_procedures
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_stored_procedures.htm
source: Advantage CHM
tags:
  - web
checksum: 29ebaeb3309c1f809431d67f67f779e973f83c49
---

# Web Stored Procedures

Stored Procedures

[System procedures](master_using_sql_to_modify_data_dictionaries.md) and user-defined [stored procedures](master_stored_procedures.md) can be invoked as service operations in the Advantage Web Platform.  If the [\_\_Query](web_query_service_operation.md) service operation is enabled, they can be run with the EXECUTE PROCEDURE SQL statement. However, it is possible to invoke procedures with a GET and POST requests using the procedure's URI. For example, this GET:

http://localhost:6272/adsweb/rootdd/v1/sp\_mgGetActivityInfo?$format=json

will return a result set such as:

{

 "d": {

   "results": [

     {

       "\_\_metadata": {

         "uri": "http://myserver.com:6272/adsweb/rootdd/v1/sp\_mgGetActivityInfo",

         "key\_fields": "",

         "rows\_affected": 0,

         "last\_autoinc": 0

       },

       "Operations": 1161,

       "LoggedErrors": 1,

       "UpTime": "0 Days 4 Hours 44 Minutes 57 Seconds",

       "EQThreshold": 0,

       "EQActiveThreads": 0,

       "EQOperations": 0

     }

   ]

 }

}

Note, though, that for security reasons, system procedures can only be invoked against the [root dictionary](master_root_dictionary.md). The above example was run against a root dictionary since it uses [sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.md), which is one of the built-in system procedures. In addition, only system procedures associated with [SERVER:Admin and SERVER:Monitor](master_database_base_roles.md) roles can be invoked. However, user-defined procedures that are available in the exposed Location's dictionary can be called depending on user permissions associated with the request.

To invoke procedures with parameters, pass the parameter values in the URI with the name of the parameter followed by an equals sign and the parameter value. For example, the following invokes sp\_mgGetErrorLog and asks for 5 entries from the ADT error log and 2 entries from the DBF error log. Note that the parameter names must match the actual procedure definition. The order of parameters in the URI does not matter. Extra parameters (that are not named by the procedure) are ignored.

http://localhost:6272/adsweb/alsroot/v1/sp\_mgGetErrorLog?MaxAdtEntries=5&MaxDbfEntries=2&$format=json

It is also possible to use [$filter and $orderby](web_collections.md) in the request as well as $top and $skiptoken. The following orders the results in descending order on the DateTime field:

http://localhost:6272/adsweb/alsroot/v1/sp\_mgGetErrorLog?MaxAdtEntries=5&MaxDbfEntries=2&$orderby=DateTime%20desc&$format=json

Because the Advantage Web Platform must be able to distinguish stored procedures from tables efficiently from the name (since the URI format is not necessarily distinct), it retrieves system and user-defined procedure names and parameter definitions once for each dictionary and caches them for subsequent requests. If you define new procedures in a dictionary or change the parameter definitions, you can flush the old definitions from the web platform service with the \_\_ClearObjectInfoCache service operation (with a POST). For example,

POST http://localhost.com:6272/adsweb/pupdir/v1/\_\_ClearObjectInfoCache HTTP/1.1
