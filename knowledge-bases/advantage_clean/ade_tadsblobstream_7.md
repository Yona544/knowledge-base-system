---
title: Ade Tadsblobstream 7
slug: ade_tadsblobstream_7
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsblobstream_7.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3c9900ca6851ca3c8f953b37c38893dbd828883d
---

# Ade Tadsblobstream 7

TAdsBlobStream

TAdsBlobStream

Advantage TDataSet Descendant

| TAdsBlobStream  Advantage TDataSet Descendant |  |  |  |  |

[Methods](ade_tadsblobstream_methods.md)

TAdsBlobStream is a descendant from TStream providing methods of manipulation to allow applications to read from or write to field objects that represent Binary Large OBject (BLOB) fields. This is very similar to a TBlobStream implementation.

Unit

AdsData

Description

Use TAdsBlobStream to access or modify the value of a BLOB field object. There are three predefined field types that will work with BLOB streams (TBlobField, TGraphicField, and TMemoField). In order to use TAdsBlobStream, you need to create an instance of the object. There are methods associated with the object that will allow you to read and write the data without needing to know the internal structure.

Note Do not forget to free the TAdsBlobStream instance, and only use one TAdsBlobStream instance per record. If you need to access multiple BLOBs, create new TAdsBlobStream instances.

\*\*\*

[TAdsBlobStream](ade_tadsblobstream_7.md) is equivalent to Delphis TBlobStream. Because of implementation details, the new component with a different name had to be created.

Use TAdsBlobStream to access or modify the value of a Blob field object. Blob field objects are TBlobField objects and descendants of TBlobField such as TGraphicField and TMemoField. Blob fields use Blob streams to implement many of their data access properties and methods.

TAdsBlobStream allows objects that have no specialized knowledge of how data is stored in a Blob field to read or write such data by employing the uniform stream interface.

To use a Blob stream, create an instance of TAdsBlobStream, use the methods of the stream to read or write the data, and then free the Blob stream. Do not use the same instance of TAdsBlobStream to access data from more than one record. Instead, create a new TAdsBlobStream object every time you need to read or write Blob data on a new record.
