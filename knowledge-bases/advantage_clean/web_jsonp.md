---
title: Web Jsonp
slug: web_jsonp
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_jsonp.htm
source: Advantage CHM
tags:
  - web
checksum: 4a8be7567b64c697b0e8b4f3d03a3553ed42031a
---

# Web Jsonp

JSONP

JSONP

Advantage Web Platform

| JSONP  Advantage Web Platform |  |  |  |  |

JSONP, also referred to as "JSON with padding" is a simple addition to the JSON format to allow the client to request data from a server in a different domain. To obtain a JSONP result, just specify the $callback operator in the request with a callback name.  For example,

https://localhost:6282/adsweb/example\_db/v1/Tasks?$format=json&$callback=mycallback

The result will be wrapped in the specified callback:

mycallback( {

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

     }

   ]

 }

}

)

The use of JSONP may be automated by the client you are using. For example, with datajs, you can set the enableJsonpCallback property to true for a request.

Security Note:  Some people consider using JSONP in a web application to be insecure because it allows the application to avoid browsers' same origin policy. You should exercise caution if you make JSONP requests. If you are developing an application that requires the use of multiple origin URLs, you may want to consider using an alternative such as a server side proxy.
