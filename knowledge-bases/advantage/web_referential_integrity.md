Advantage Web Platform Referential Integrity Relationships




Advantage Database Server 12  

Referential Integrity Relationships

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Referential Integrity Relationships  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Referential Integrity Relationships Advantage Web Platform web\_referential\_integrity Advantage Web Development > Advantage Web Platform > Referential Integrity Relationships / Dear Support Staff, |  |
| Referential Integrity Relationships  Advantage Web Platform |  |  |  |  |

It is possible to maintain referential integrity (RI) relationships by using the $links operation in a POST request. The $links operator creates a new relationship between two records. For this to work with the Advantage Web Platform, the two tables involved must have an existing referential integrity (RI) rule defined between them. Currently, only the POST request type for $links is supported.

A $links operation has the following format:

POST https://path/ParentTable(key)/$links/ChildTable HTTP/1.1

The body of the request must contain the URI that uniquely defines the record in the ChildTable that is to reference the ParentTable.

The following is an example that links a record in a table named Parent with a key value of 5 to a record in a table named Child with a key value of 10.  The result is that the field defined as the foreign key in the Child table will be set to value 5:

POST https://localhost:6282/adsweb/pupdir/v1/Parent(5)/$links/Child HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Accept: application/atom+xml,application/xml

Accept-Charset: UTF-8

Content-Type: application/xml

Content-Length: 213

 

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<uri xmlns="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">

https://localhost:6282/adsweb/pupdir/v1/Child(10)</uri>

The response to the above request is HTTP/1.1 204 No Content.