---
title: Web Batch Put Json
slug: web_batch_put_json
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_batch_put_json.htm
source: Advantage CHM
tags:
  - web
checksum: aed19c85550d5730093740eec720e7bc5547ec9d
---

# Web Batch Put Json

Batch PUT and DELETE with JSON

Batch PUT and DELETE with JSON

Advantage Web Platform

| Batch PUT and DELETE with JSON  Advantage Web Platform |  |  |  |  |

A PUT (update) operation with JSON in the payload is also very similar to an [ATOM/XML request](web_batch_request_example.md).  This example of a request and response uses JSON.  Note that with the DELETE, there is no difference since it does not contain any JSON in the request body or in the response.

POST http://localhost:6272/adsweb/pupdir/v1/$batch HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Accept: application/json

Content-Type: multipart/mixed; boundary=batch\_21f38718-29c3-4482-807c-c3f155be0fff

Content-Length: 860

Expect: 100-continue

 

--batch\_21f38718-29c3-4482-807c-c3f155be0fff

Content-Type: multipart/mixed; boundary=changeset\_875d84f1-ddf3-483d-b28d-5ae14782a00f

 

--changeset\_875d84f1-ddf3-483d-b28d-5ae14782a00f

Content-Type: application/http

Content-Transfer-Encoding: binary

 

PUT http://localhost:6272/adsweb/pupdir/v1/test2z(5) HTTP/1.1

Content-ID: 88

Content-Type: application/json;type=entry

Content-Length: 119

 

{

 "\_\_metadata": {

         "uri": "https://localhost:6282/adsweb/pupdir/v1/test2z(5)"

 },

 "CHARACTER": "my update"

}

 

--changeset\_875d84f1-ddf3-483d-b28d-5ae14782a00f

Content-Type: application/http

Content-Transfer-Encoding: binary

 

DELETE http://localhost:6272/adsweb/pupdir/v1/test2z(7) HTTP/1.1

Content-ID: 89

 

--changeset\_875d84f1-ddf3-483d-b28d-5ae14782a00f--

--batch\_21f38718-29c3-4482-807c-c3f155be0fff--

 

The response to the above request might be:

HTTP/1.1 202 Accepted

Date: Mon, 21 May 2012 20:14:36 GMT

Server: Apache/2.2.22 (Win32) mod\_ssl/2.2.22 OpenSSL/0.9.8p-fips

Access-Control-Allow-Origin:

DataServiceVersion: 2.0

Cache-Control: no-cache

Content-Length: 610

Content-Type: multipart/mixed; boundary=batchresponse\_21ccd30d-0db0-3144-b774-3d656cd3602c

 

 

--batchresponse\_21ccd30d-0db0-3144-b774-3d656cd3602c

Content-Type: multipart/mixed; boundary=changesetresponse\_369796c2-979f-f945-999f-729fcf65c08d

 

--changesetresponse\_369796c2-979f-f945-999f-729fcf65c08d

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 204 No Content

Content-ID: 88

 

--changesetresponse\_369796c2-979f-f945-999f-729fcf65c08d

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 204 No Content

Content-ID: 89

 

 

--changesetresponse\_369796c2-979f-f945-999f-729fcf65c08d--

--batchresponse\_21ccd30d-0db0-3144-b774-3d656cd3602c--
