---
title: Web Result Set Format
slug: web_result_set_format
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_result_set_format.htm
source: Advantage CHM
tags:
  - web
checksum: 6e61c10cd80185584f56a5c9fe96156f9c4cb5c4
---

# Web Result Set Format

Advantage Web Platform Result Set Format

Result Set Format

Advantage Web Platform

| Result Set Format  Advantage Web Platform |  |  |  |  |

This brief examples of the format of the result sets returned by the Advantage Web Platform. When in doubt about what will be returned, the easiest way to see the result set format is to open your URL in a browser (Google Chrome is recommended, it handles JSON result sets the best). More details for JSON results can be found at: <http://www.odata.org/documentation/json-format>.  For information about XML results, see <http://www.odata.org/documentation/atom-format>.

Example Results

This is an example of a JSON result:

{

 "d": {

   "results": [

     {

       "\_\_metadata": {

         "uri": "https://myserver.com:6282/adsweb/example\_db/v1/Tasks(1)",

         "key\_fields": "id",

         "rows\_affected": 0,

         "last\_autoinc": 0

       },

       "id": 1,

       "rowversion": 50,

       "name": "Task 1",

       "started": "2011-10-05T00:00:00",

       "finished": "2011-11-07T00:00:00"

     },

     {

       "\_\_metadata": {

         "uri": "https://myserver.com:6282/adsweb/example\_db/v1/Tasks(2)",

         "key\_fields": "id",

         "rows\_affected": 0,

         "last\_autoinc": 0

       },

       "id": 2,

       "rowversion": 53,

       "name": "Another task",

       "started": "2012-12-16T00:00:00",

       "finished": null

     }

   ],

   "\_\_next": "https://myserver.com:6282/adsweb/example\_db/v1/Tasks?$filter=id le 4&$skiptoken=2"

 }

}

 

The same result set returned as XML looks like this:

<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom" xml:base="https://myserver.com:6282/adsweb">

   <title type="text">Tasks</title>

   <id>

https://myserver.com:6282/adsweb/example\_db/v1/Tasks

   </id>

   <updated/>

   <link rel="self" title="Tasks" href="Tasks"/>

   <entry>

       <id>

https://myserver.com:6282/adsweb/example\_db/v1/Tasks(1)

       </id>

       <title type="text"/>

       <updated/>

       <author>

           <name/>

       </author>

       <link rel="edit" title="Tasks" href="adsweb/example\_db/v1/Tasks(1)"/>

       <category term="Model.Tasks" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>

       <content type="application/xml">

           <m:properties>

               <d:id m:type="Edm.Int32">1</d:id>

               <d:rowversion m:type="Edm.Int64">50</d:rowversion>

               <d:name m:type="Edm.String">Task 1</d:name>

               <d:started m:type="Edm.DateTime">2011-10-05T00:00:00</d:started>

               <d:finished m:type="Edm.DateTime">2011-11-07T00:00:00</d:finished>

           </m:properties>

       </content>

   </entry>

   <entry>

       <id>

https://myserver.com:6282/adsweb/example\_db/v1/Tasks(2)

       </id>

       <title type="text"/>

       <updated/>

       <author>

           <name/>

       </author>

       <link rel="edit" title="Tasks" href="adsweb/example\_db/v1/Tasks(2)"/>

       <category term="Model.Tasks" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>

       <content type="application/xml">

           <m:properties>

               <d:id m:type="Edm.Int32">2</d:id>

               <d:rowversion m:type="Edm.Int64">53</d:rowversion>

               <d:name m:type="Edm.String">Another task</d:name>

               <d:started m:type="Edm.DateTime">2012-12-16T00:00:00</d:started>

               <d:finished m:type="Edm.DateTime" m:null="true"/>

           </m:properties>

       </content>

   </entry>

   <link rel="next" href="https://myserver.com:6282/adsweb/example\_db/v1/Tasks?$filter=id le 3&$skiptoken=2"/>

</feed>

Errors

Errors are returned as JSON objects when possible:

{

 "error": {

   "code": "7200",

   "message": {

     "lang": "en-US",

     "value": "Error 7200:  AQE Error:  State = HY000;   NativeError = 5004;  [iAnywhere Solutions][Advantage SQL][ASA] Error 5004:  Either ACE could not find the specified file, or you do not have sufficient rights to access the file. Table name: test1"

   }

 }

}

 

A note on interpreting results: It is best to always check the content-type header in your request before deciding what to do with the results. If the content-type is application/json, it is safe to parse the results as JSON. If some other http error occurred, you may get html text back. Parsing that as JSON will end up with your parser encountering errors.

Field Names with Spaces

When retrieving data from entities (tables) that contain field/column names with spaces, note that the spaces in the names will be replaced with underscores in result sets and associated metadata. The various clients that build proxy classes from the metadata and that create objects from the results use the field names as identifiers. Typically in those situations, spaces cannot be used in the identifiers. So, for example, if a column name is of the form Last Name, the client code will likely need to refer to it as Last\_Name.

Paging

If a request from a client results in more rows than the page limit of the service (see [DbPageSize](web_installing_the_awp.md) option), the result set will have a \_\_next member which includes the URL to load in order to continue paging. The default page limit is 100 rows.
