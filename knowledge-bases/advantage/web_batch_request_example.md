Batch Request Example




Advantage Database Server 12  

Batch Request Example

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Batch Request Example  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Batch Request Example Advantage Web Platform web\_batch\_request\_example Advantage Web Development > Advantage Web Platform > Batch Operations > Batch Request Example / Dear Support Staff, |  |
| Batch Request Example  Advantage Web Platform |  |  |  |  |

The following is an example of a BATCH request that defines within it a POST, a MERGE, and a DELETE operation. Note the BATCH Content-Type header. It must be multipart/mixed with a boundary definition of the form batch\_IDENT where IDENT is typically a GUID, although the Advantage Web Platform does not require that to be the case. It can be any character sequence (without spaces). The boundary value (batch\_IDENT) is used to mark the beginning of each change set with --batch\_IDENT and it terminates the entire batch body with --batch\_IDENT--.  Note that protocol specification for the BATCH operation at <http://www.odata.org/documentation/batch> incorrectly specifies that the boundary is of the form batch(IDENT).

Within the batch boundary, one or more change sets can be specified (the beginning of each is marked with --batch\_IDENT. The --batch\_IDENT boundary is expected to be followed by a Content-Type header that defines the change set boundary of the form changset\_IDENT. Each item in the change set begins with --changeset\_IDENT and the entire change set is terminated by --changeset\_IDENT--. Each change set entry must have a Content-Type header with a value of application/http and a Content-Transfer-Encoding header with a value of binary.  Each actual entry (e.g., a POST or a DELETE) follows the same format as its non-batch counterpart. The following example contains one change set.

The [Batch Response Example](web_batch_response_example.htm) shows the response to this request.

POST https://localhost:6282/adsweb/pupdir/v1/$batch HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Accept: application/atom+xml,application/xml

Accept-Charset: UTF-8

Content-Type: multipart/mixed; boundary=batch\_a84a6577-2c9f-4a58-a34f-602f83541620

Content-Length: 2639

 

--batch\_a84a6577-2c9f-4a58-a34f-602f83541620

Content-Type: multipart/mixed; boundary=changeset\_abfb4d62-6597-480c-8406-369fa972cb8c

 

--changeset\_abfb4d62-6597-480c-8406-369fa972cb8c

Content-Type: application/http

Content-Transfer-Encoding: binary

 

POST https://localhost:6282/adsweb/pupdir/v1/TestData HTTP/1.1

Content-ID: 1

Content-Type: application/atom+xml;type=entry

Content-Length: 755

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

 <category scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" term="testdd.Model.Entities.TestData" />

 <title />

 <author>

   <name />

 </author>

 <updated>2011-05-02T21:54:15.1701523Z</updated>

 <id />

 <content type="application/xml">

   <m:properties>

     <d:AutoInc m:type="Edm.Int32">0</d:AutoInc>

     <d:PK>IDnew</d:PK>

     <d:RowVersion m:type="Edm.Decimal">0</d:RowVersion>

     <d:i m:type="Edm.Int32">1005</d:i>

   </m:properties>

 </content>

</entry>

--changeset\_abfb4d62-6597-480c-8406-369fa972cb8c

Content-Type: application/http

Content-Transfer-Encoding: binary

 

MERGE https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz') HTTP/1.1

Content-ID: 3

Content-Type: application/atom+xml;type=entry

Content-Length: 823

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">

 <category scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" term="Model.TestData" />

 <title />

 <author>

   <name />

 </author>

 <updated>2011-05-02T21:54:15.1701523Z</updated>

 <id>https://localhost:6282/adsweb/pupdir/v1/TestData('IDxyz')</id>

 <content type="application/xml">

   <m:properties>

     <d:AutoInc m:type="Edm.Int32">1</d:AutoInc>

     <d:PK>IDxyz</d:PK>

     <d:RowVersion m:type="Edm.Decimal">3</d:RowVersion>

     <d:i m:type="Edm.Int32">100</d:i>

   </m:properties>

 </content>

</entry>

--changeset\_abfb4d62-6597-480c-8406-369fa972cb8c

Content-Type: application/http

Content-Transfer-Encoding: binary

 

DELETE https://localhost:6282/adsweb/pupdir/v1/TestData('IDold') HTTP/1.1

Content-ID: 5

 

--changeset\_abfb4d62-6597-480c-8406-369fa972cb8c--

--batch\_a84a6577-2c9f-4a58-a34f-602f83541620--