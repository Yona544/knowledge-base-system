\_\_GetURIs Service Operation




Advantage Database Server 12  

\_\_GetURIs Service Operation

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| \_\_GetURIs Service Operation  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - \_\_GetURIs Service Operation Advantage Web Platform web\_GetURIs\_Service Advantage Web Development > Advantage Web Platform > GetURIs Service / Dear Support Staff, |  |
| \_\_GetURIs Service Operation  Advantage Web Platform |  |  |  |  |

The Advantage Web Platform provides the capability to enumerate and retrieve a list of exposed Locations in the adsweb.conf file through the \_\_GetURIs service operation. This operation can only be run against the [root dictionary](master_root_dictionary.htm).  It will return all Locations that are flagged with the [DbEnableGetURIs](web_installing_the_awp.htm) directive.

For example, this request:

https://localhost:6282/adsweb/rootdd/v1/\_\_GetURIs?$format=json

Will return a result set like this:

{

 "d": {

   "results": [

     {

       "Location": "/adsweb/example\_db"

     },

     {

       "Location": "/adsweb/myDB"

     }

   ]

 }

}

This service operation is used by the Advantage Web Administrator utility to more easily display a list of available databases for configuration purposes. While any valid Location can be enumerated, the general purpose is to enumerate any root dictionaries available in an environment that contains multiple instances of Advantage Database Server.