---
title: Web Batch Request Json
slug: web_batch_request_json
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_batch_request_json.htm
source: Advantage CHM
tags:
  - web
checksum: c1787e185ff6f334767ad024041298a1161c9806
---

# Web Batch Request Json

Batch Request using JSON

Batch Request using JSON

Advantage Web Platform

| Batch Request using JSON  Advantage Web Platform |  |  |  |  |

The following is an example of a BATCH request that uses JSON in the payload. The request is essentially the same as one using [ATOM/XML](web_batch_request_example.md) except that the data for each operation (e.g., for a POST) is given in JSON format.  Note that the Content-Type header still must be given as "multipart/mixed", and it uses the same boundary formats.  The [example JSON response is here](web_batch_request_json.md).

POST http://localhost:6272/adsweb/pupdir/v1/$batch HTTP/1.1

Authorization: Basic bWx3Og==

Accept: application/json

Content-Type: multipart/mixed; boundary=batch\_09dd2b28-d806-4c37-b5dc-b25357ceedab

Content-Length: 1671

Expect: 100-continue

 

--batch\_09dd2b28-d806-4c37-b5dc-b25357ceedab

Content-Type: multipart/mixed; boundary=changeset\_7aa6f303-c7bf-4491-8ff0-af61ff878e4a

 

--changeset\_7aa6f303-c7bf-4491-8ff0-af61ff878e4a

Content-Type: application/http

Content-Transfer-Encoding: binary

 

POST http://localhost:6272/adsweb/pupdir/v1/test1z HTTP/1.1

Content-ID: 1

Content-Type: application/json;type=entry

Content-Length: 435

 

{

 "\_\_metadata": {

         "uri": "http://localhost:6272/adsweb/pupdir/v1/\_\_query",

         "key\_fields": "",

         "rows\_affected": -1,

         "last\_autoinc": 0,

         "error": null

 },

 "autoinc": 1,

 "character": "inserted guy 1",

 "logical": false,

 "date": "1979-07-18T00:00:00.0000000",

 "time": "2012-05-21T02:30:54.0000000",

 "timestamp": "1988-08-08T12:34:00.0000000-06:00",

 "integer": -32766,

 "dbl": -2147480000,

 "currency": 32.78,

 "shortint": 32,

 "memo": "MEMO!!!",

 "rowversion": 1

}

 

--changeset\_7aa6f303-c7bf-4491-8ff0-af61ff878e4a

Content-Type: application/http

Content-Transfer-Encoding: binary

 

POST http://localhost:6272/adsweb/pupdir/v1/test1z HTTP/1.1

Content-ID: 2

Content-Type: application/json;type=entry

Content-Length: 440

 

{

 "\_\_metadata": {

         "uri": "http://localhost:6272/adsweb/pupdir/v1/\_\_query",

         "key\_fields": "",

         "rows\_affected": -1,

         "last\_autoinc": 0,

         "error": null

 },

 "autoinc": 2,

 "character": "inserted guy 2",

 "logical": true,

 "date": "1999-06-30T00:00:00.0000000",

 "time": "2012-05-21T02:00:00.0000000",

 "timestamp": "1999-03-03T04:00:00.0000000-07:00",

 "integer": 89,

 "dbl": 100000,

 "currency": 1000350,

 "shortint": 456,

 "memo": "memo data",

 "rowversion": 2

}

 

 

--changeset\_7aa6f303-c7bf-4491-8ff0-af61ff878e4a--

--batch\_09dd2b28-d806-4c37-b5dc-b25357ceedab--
