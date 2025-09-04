---
title: Dotnet Adsextendedreader Seek
slug: dotnet_adsextendedreader_seek
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_seek.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d7a8b18103d60f59c66c2f4ea1aa9f43eb6f5b87
---

# Dotnet Adsextendedreader Seek

AdsExtendedReader.Seek

AdsExtendedReader.Seek

Advantage .NET Data Provider

| AdsExtendedReader.Seek  Advantage .NET Data Provider |  |  |  |  |

Performs an indexed search. Scopes and filters are respected.

public bool Seek ( object[] seekValue, SeekType seekType );

Remarks

Seek provides the fastest way for the Advantage Database Server to locate a record. The seekValue object array parameter is used by the Advantage Client Engine to build a seekable index key for the server to seek through the indicated index for a matching key. The Advantage Client Engine converts seekValue objects according to the objects type. The seekValue array elements correspond to the index key segments. For example, a single segment index (e.g., on lastname), would need only a single element array containing the value to seek for. An index with, for example, two segment (e.g., "lastname;firstname") can have a one or two element seekValue array. If, in this example, the seekValue array had only a single element, then it must correspond to the lastname field.

The SeekType parameter determines the type of seek performed. By sending SeekType.SoftSeek for the seekType parameter, the Advantage Client Engine will perform a "soft" seek, which means that if the desired key is not found in the index, the table will be positioned at the first key logically greater than the seek key. On SeekType.HardSeek, if the desired key is not found, the table is positioned at EOF. When SeekType.SeekGT is indicated, a "soft" seek will be performed on the key that is the next possible index key after the key sent in the seekValue parameter. If SeekGT is used and any key is found, Seek returns true. When SeekType.SeekLast is indicated, the Advantage Client Engine will perform a seek for the last key in the indicated index order that matches the seekValue. If the key is not in the index, Seek will position the table at EOF and return false. An empty seekValue is defined to match all index keys and will position the table to the last record.

Seek returns true if successful. If the specified key is not found on a "soft" seek, Seek returns false. The length of the seekValue objects define the length of the key matching performed during the seek operation. For example, a seekValue of "A" will find the first record whose index key starts with "A", and Seek will return true if it finds such a record regardless of whether it is a "soft" seek or not. An empty seekValue is defined to match all index keys and will position the table at the first record, except in the case of SeekLast, which will position to the last record.

Example

Because the Advantage Client Engine builds the key, the application needs to provide the values to seek for (not the key). If, for example, an index is built on a combination of a string, an integer field, and a date field, then the following call can be used to seek for the corresponding values. This will work for an ADI index where the fields are concatenated together (e.g., name;id;date). It would also work for a DBF-style index formatted as a string such as name+str(id,5)+dtos(date).

rdr.ActiveIndex = "indexname";

bool bSeek = rdr.Seek( new object[] { "Frasier", 33,

new DateTime(1977,1,6) },

AdsExtendedReader.SeekType.HardSeek );

if ( bSeek )

Console.WriteLine( rdr.RecordNumber.ToString() );

See Also

[PartialMatch](dotnet_adsextendedreader_partialmatch.md)

[SeekType](dotnet_adsextendedreader_seektype.md)

[SetRange](dotnet_adsextendedreader_setrange.md)
