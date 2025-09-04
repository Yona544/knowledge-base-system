Batch Response using JSON




Advantage Database Server 12  

Batch Response using JSON

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Batch Response using JSON  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Batch Response using JSON Advantage Web Platform web\_batch\_response\_json Advantage Web Development > Advantage Web Platform > Batch Operations > Batch Response using JSON / Dear Support Staff, |  |
| Batch Response using JSON  Advantage Web Platform |  |  |  |  |

The following is an example JSON response corresponding to the [example JSON request](web_batch_request_json.htm).

HTTP/1.1 202 Accepted

Date: Mon, 21 May 2012 20:13:41 GMT

Server: Apache/2.2.22 (Win32) mod\_ssl/2.2.22 OpenSSL/0.9.8p-fips

Access-Control-Allow-Origin:

DataServiceVersion: 2.0

Cache-Control: no-cache

Content-Length: 2262

Content-Type: multipart/mixed; boundary=batchresponse\_c7a44f7b-7b1a-9c4d-b572-d61e040f8924

 

 

--batchresponse\_c7a44f7b-7b1a-9c4d-b572-d61e040f8924

Content-Type: multipart/mixed; boundary=changesetresponse\_1e4b49d4-62e0-704a-a9b4-6329eab0605a

 

--changesetresponse\_1e4b49d4-62e0-704a-a9b4-6329eab0605a

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 201 Created

Content-ID: 1

Content-Type: application/json; charset=utf-8

Location: http://localhost:6272/adsweb/pupdir/v1/test1z(11)

 

{

 "d": {

   "results": [

     {

       "\_\_metadata": {

         "uri": "http://localhost:6272/adsweb/pupdir/v1/test1z(11)",

         "key\_fields": "AUTOINC",

         "rows\_affected": 1,

         "last\_autoinc": 0

       },

       "AUTOINC": 11,

       "CHARACTER": "inserted guy 1",

       "LOGICAL": false,

       "DATE": "1979-07-18T00:00:00",

       "TIME": "02:30:54",

       "TIMESTAMP": "1988-08-08T12:34:00",

       "INTEGER": -32766,

       "dbl": -2.14748e+009,

       "CURRENCY": 32.78,

       "SHORTINT": 32,

       "RAW": null,

       "BINARY": null,

       "IMAGE": null,

       "MEMO": "MEMO!!!",

       "rowversion": 11

     }

   ]

 }

}

 

--changesetresponse\_1e4b49d4-62e0-704a-a9b4-6329eab0605a

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 201 Created

Content-ID: 2

Content-Type: application/json; charset=utf-8

Location: http://localhost:6272/adsweb/pupdir/v1/test1z(12)

 

{

 "d": {

   "results": [

     {

       "\_\_metadata": {

         "uri": "http://localhost:6272/adsweb/pupdir/v1/test1z(12)",

         "key\_fields": "AUTOINC",

         "rows\_affected": 1,

         "last\_autoinc": 0

       },

       "AUTOINC": 12,

       "CHARACTER": "inserted guy 2",

       "LOGICAL": true,

       "DATE": "1999-06-30T00:00:00",

       "TIME": "02:00:00",

       "TIMESTAMP": "1999-03-03T04:00:00",

       "INTEGER": 89,

       "dbl": 100000,

       "CURRENCY": 1.00035e+006,

       "SHORTINT": 456,

       "RAW": null,

       "BINARY": null,

       "IMAGE": null,

       "MEMO": "memo data",

       "rowversion": 12

     }

   ]

 }

}

 

 

--changesetresponse\_1e4b49d4-62e0-704a-a9b4-6329eab0605a--

--batchresponse\_c7a44f7b-7b1a-9c4d-b572-d61e040f8924--