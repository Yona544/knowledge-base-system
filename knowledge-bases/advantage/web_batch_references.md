Batch References




Advantage Database Server 12  

Batch References

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Batch References  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Batch References Advantage Web Platform web\_batch\_references Advantage Web Development > Advantage Web Platform > Batch Operations > Batch References / Dear Support Staff, |  |
| Batch References  Advantage Web Platform |  |  |  |  |

BATCH request entries can contain references to previous entries by using an aliasing mechanism via Content-ID header values. This is particularly useful in situations where a POST operation creates a new record where the primary key value is created at the server (e.g., an auto-increment or a key created by a trigger). For example, if your database contains a referential integrity (RI) rule between two tables, then the relationship can be updated within a batch request using a reference to the new entries.  The following example shows the creation of two records, one in a table named Parent and one in a table named Child.  The last operation in the batch is a POST with a $links operation, which causes the Child record to be associated with the Parent record (it sets the foreign key field of the child to the parents primary key). The new Parent record has a Content-ID header of 1 and the new Child record has a Content-ID header of 2.  The $links operation references the parent as $1 and the child as $2 (in the body of the $links operation).

POST https://localhost:6282/adsweb/pupdir/v1/$batch HTTP/1.1

User-Agent: Microsoft ADO.NET Data Services

DataServiceVersion: 1.0;NetFx

MaxDataServiceVersion: 2.0;NetFx

Authorization: Basic YWRzc3lzOg==

Accept: application/atom+xml,application/xml

Accept-Charset: UTF-8

Content-Type: multipart/mixed; boundary=batch\_74775423-5b00-44fd-87bd-2fa77b6ee480

Host: localhost:6282

Content-Length: 2515

Expect: 100-continue

 

--batch\_74775423-5b00-44fd-87bd-2fa77b6ee480

Content-Type: multipart/mixed; boundary=changeset\_45c07d1c-8dce-4247-b2d5-34c9fe727054

 

--changeset\_45c07d1c-8dce-4247-b2d5-34c9fe727054

Content-Type: application/http

Content-Transfer-Encoding: binary

 

POST https://localhost:6282/adsweb/pupdir/v1/Parent HTTP/1.1

Content-ID: 1

Content-Type: application/atom+xml;type=entry

Content-Length: 649

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

 <category scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" term="testdd.Model.Entities.Parent" />

 <title />

 <author>

   <name />

 </author>

 <updated>2011-05-02T22:47:08.0908283Z</updated>

 <id />

 <content type="application/xml">

   <m:properties>

     <d:pk m:type="Edm.Int32">0</d:pk>

     <d:value>pvalue</d:value>

   </m:properties>

 </content>

</entry>

--changeset\_45c07d1c-8dce-4247-b2d5-34c9fe727054

Content-Type: application/http

Content-Transfer-Encoding: binary

 

POST https://localhost:6282/adsweb/pupdir/v1/Child HTTP/1.1

Content-ID: 2

Content-Type: application/atom+xml;type=entry

Content-Length: 701

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

 <category scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" term="testdd.Model.Entities.Child" />

 <title />

 <author>

   <name />

 </author>

 <updated>2011-05-02T22:47:08.0918284Z</updated>

 <id />

 <content type="application/xml">

   <m:properties>

     <d:cpk m:type="Edm.Int32">0</d:cpk>

     <d:fk m:type="Edm.Int32" m:null="true" />

     <d:lookup>cvalue</d:lookup>

   </m:properties>

 </content>

</entry>

--changeset\_45c07d1c-8dce-4247-b2d5-34c9fe727054

Content-Type: application/http

Content-Transfer-Encoding: binary

 

POST $1/$links/Child HTTP/1.1

Content-ID: 3

Content-Type: application/xml

Content-Length: 143

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<uri xmlns="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">$2</uri>

--changeset\_45c07d1c-8dce-4247-b2d5-34c9fe727054--

--batch\_74775423-5b00-44fd-87bd-2fa77b6ee480--