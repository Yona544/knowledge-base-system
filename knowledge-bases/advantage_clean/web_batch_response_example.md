---
title: Web Batch Response Example
slug: web_batch_response_example
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_batch_response_example.htm
source: Advantage CHM
tags:
  - web
checksum: c873c0138743a76e8fffcccfb6463cbf068dc6f0
---

# Web Batch Response Example

Batch Response Example

Batch Response Example

Advantage Web Platform

| Batch Response Example  Advantage Web Platform |  |  |  |  |

The response to a BATCH request contains boundaries similar to the request. The response body contains change set boundaries with specific responses for each entry in the request.  The following is an example response to the [example request](web_batch_request_example.md):

HTTP/1.1 202 Accepted

Date: Mon, 02 May 2011 21:54:15 GMT

Server: Apache/2.2.16 (Win32) mod\_ssl/2.2.16 OpenSSL/0.9.8p-fips PHP/5.3.5

Content-Length: 2050

Content-Type: multipart/mixed; boundary=batchresponse\_f0b5c813-7c86-174f-b637-eb695e6a474f

 

 

--batchresponse\_f0b5c813-7c86-174f-b637-eb695e6a474f

Content-Type: multipart/mixed; boundary=changesetresponse\_7d444564-695d-7243-ba5d-b034dbd56da9

 

--changesetresponse\_7d444564-695d-7243-ba5d-b034dbd56da9

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 201 Created

Content-ID: 1

Content-Type: application/atom+xml; charset=utf-8

Location: https://localhost:6282/adsweb/pupdir/v1/TestData('IDnew')

 

<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>

<feed xml:base="https://localhost:6282/adsweb" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

   <title type="text">TestData</title>

   <id>https://localhost:6282/adsweb/pupdir/v1/TestData</id>

   <updated></updated>

   <link rel="self" title="TestData" href="TestData" />

   <entry>

       <id>https://localhost:6282/adsweb/pupdir/v1/TestData('IDnew')</id>

       <title type="text"></title>

       <updated></updated>

       <author>

           <name />

       </author>

       <link rel="edit" title="TestData" href="https://localhost:6282/adsweb/pupdir/v1/TestData('IDnew')" />

       <category term="Model.TestData" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />

       <content type="application/xml">

           <m:properties>

               <d:PK m:type="Edm.String">IDnew</d:PK>

               <d:AutoInc m:type="Edm.Int32">3</d:AutoInc>

               <d:RowVersion m:type="Edm.Int64">4</d:RowVersion>

               <d:i m:type="Edm.Int32">1005</d:i>

           </m:properties>

       </content>

   </entry>

</feed>

--changesetresponse\_7d444564-695d-7243-ba5d-b034dbd56da9

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 204 No Content

Content-ID: 3

 

--changesetresponse\_7d444564-695d-7243-ba5d-b034dbd56da9

Content-Type: application/http

Content-Transfer-Encoding: binary

 

HTTP/1.1 204 No Content

Content-ID: 5

 

 

--changesetresponse\_7d444564-695d-7243-ba5d-b034dbd56da9--

--batchresponse\_f0b5c813-7c86-174f-b637-eb695e6a474f--
