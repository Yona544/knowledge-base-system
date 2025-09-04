---
title: Dotnet Adsextendedreader Gotobof
slug: dotnet_adsextendedreader_gotobof
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_gotobof.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2c62475abcad70c5d9ae85e6a198e23e9f743acc
---

# Dotnet Adsextendedreader Gotobof

AdsExtendedReader.GotoBOF

AdsExtendedReader.GotoBOF

Advantage .NET Data Provider

| AdsExtendedReader.GotoBOF  Advantage .NET Data Provider |  |  |  |  |

Sets the table position to BOF (beginning of file), which is prior to the first record.

public void GotoBOF();

Remarks

This positions the reader prior to the first record in the record set. A call to AdsDataReader.Read after a call to GotoBOF will position the reader on the first record. This simulates the situation of a newly opened reader. It allows code such as the following to work as expected:

reader.GotoBOF();

while ( reader.Read() )

{

// do stuff

}

See Also

[AdsDataReader.Read](dotnet_adsdatareader_read.md)

[GotoTop](dotnet_adsextendedreader_gototop.md)

[BOF](dotnet_adsextendedreader_bof.md)
