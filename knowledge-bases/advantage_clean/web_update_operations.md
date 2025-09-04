---
title: Web Update Operations
slug: web_update_operations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_update_operations.htm
source: Advantage CHM
tags:
  - web
checksum: 6abef6d6926837d8f5afc93c46cc126536156cff
---

# Web Update Operations

Advantage Web Platform Update Operations

Update Operations

Advantage Web Platform

| Update Operations  Advantage Web Platform |  |  |  |  |

Table data can be modified using POST, PUT, MERGE, and DELETE requests.  POST operations are used to insert new records, PUT and MERGE operations update existing records, and DELETE operations delete records. According to the OData specification, a PUT operation completely replaces the specified entry, which means that any field that is not specified would be set to its default value. However, the Advantage Web Platform treats PUT operations the same as MERGE operations, which only modify the specified field data.

POST Operations

A POST operation can be used to insert a new record into a table.  For example, the following HTTP request adds a record using a POST with an XML representation of the new record in the body:

POST https://localhost:6282/adsweb/pupdir/v1/TestData HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Accept: application/atom+xml,application/xml

Accept-Charset: UTF-8

Content-Type: application/atom+xml

Content-Length: 750

 

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

 <category scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" term="testdd.Model.Entities.TestData" />

 <title />

 <author>

   <name />

 </author>

 <updated>2011-05-02T20:45:25.922728Z</updated>

 <id />

 <content type="application/xml">

   <m:properties>

     <d:AutoInc m:type="Edm.Int32">0</d:AutoInc>

     <d:PK>IDxyz</d:PK>

     <d:RowVersion m:type="Edm.Decimal">0</d:RowVersion>

     <d:i m:type="Edm.Int32">42</d:i>

   </m:properties>

 </content>

</entry>

The response to POST operations contains a full representation of the newly created record.  This is useful particularly if the table has auto-updating fields; the newly created values can be retrieved from the response. The above request could produce the following response:

HTTP/1.1 200 OK

Date: Mon, 02 May 2011 20:45:26 GMT

Server: Apache/2.2.16 (Win32) mod\_ssl/2.2.16 OpenSSL/0.9.8p-fips PHP/5.3.5

Location: https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz')

Content-Length: 1157

Content-Type: application/atom+xml; charset=utf-8

 

<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>

<feed xml:base="https://localhost:6282/adsweb" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

   <title type="text">TestData</title>

   <id>https://localhost:6282/adsweb/pupdir/v1/TestData</id>

   <updated></updated>

   <link rel="self" title="TestData" href="TestData" />

   <entry>

       <id>https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz')</id>

       <title type="text"></title>

       <updated></updated>

       <author>

           <name />

       </author>

       <link rel="edit" title="TestData" href="https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz')" />

       <category term="Model.TestData" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />

       <content type="application/xml">

           <m:properties>

               <d:PK m:type="Edm.String">IDxyz</d:PK>

               <d:AutoInc m:type="Edm.Int32">15</d:AutoInc>

               <d:RowVersion m:type="Edm.Int64">83</d:RowVersion>

               <d:i m:type="Edm.Int32">42</d:i>

           </m:properties>

       </content>

   </entry>

</feed>

PUT/MERGE Operations

The Advantage Web Platform treats PUT and MERGE operations the same. A true PUT operation replaces the specified record and sets each unspecified field to its default value (e.g., NULL). A MERGE operation updates only the specified fields in the record. The Advantage Web Platform treats PUT operations as if they were MERGE operations.

The following is an example MERGE that updates a field in a specified record.

MERGE https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz') HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Accept: application/atom+xml,application/xml

Accept-Charset: UTF-8

Content-Type: application/atom+xml

Content-Length: 670

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

 <category scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" term="Model.TestData" />

 <title />

 <author>

   <name />

 </author>

 <updated>2011-05-02T20:59:58.0272952Z</updated>

 <id>https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz')</id>

 <content type="application/xml">

   <m:properties>

     <d:i m:type="Edm.Int32">144</d:i>

   </m:properties>

 </content>

</entry>

The response for the above request would be:

HTTP/1.1 204 No Content

Date: Mon, 02 May 2011 20:59:58 GMT

Server: Apache/2.2.16 (Win32) mod\_ssl/2.2.16 OpenSSL/0.9.8p-fips PHP/5.3.5

Content-Length: 0

Content-Type: text/plain

DELETE Operations

The DELETE operation deletes the record specified by the URI. The following is an example of a DELETE.

DELETE https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz') HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Accept: application/atom+xml,application/xml

Accept-Charset: UTF-8

Content-Type: application/atom+xml

Content-Length: 0

The response:

HTTP/1.1 204 No Content

Date: Mon, 02 May 2011 21:10:54 GMT

Server: Apache/2.2.16 (Win32) mod\_ssl/2.2.16 OpenSSL/0.9.8p-fips PHP/5.3.5

Content-Length: 0

Content-Type: text/plain
