---
title: Ade Adscustomizeaof
slug: ade_adscustomizeaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscustomizeaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b40390e948d0e6fc5254d2b9f52e298ee332f6a4
---

# Ade Adscustomizeaof

AdsCustomizeAOF

TAdsTable.AdsCustomizeAOF

Advantage TDataSet Descendant

| TAdsTable.AdsCustomizeAOF  Advantage TDataSet Descendant |  |  |  |  |

Adds records to or remove records from an existing Advantage Optimized Filter (AOF).

Syntax

| type | TAdsAOFCustomizeOptions = ( coADD, coREMOVE, coTOGGLE ); |
| procedure | AdsCustomizeAOF( ulNumRecs: Longint;  pulRecords: pUNSIGNED32;  eOption: TAdsAOFCustomizeOptions ); |

Parameters

| ulNumRecs | Number of records to customize. The maximum number of records that can be customized in a single call is 16,383. |
| pulRecords | Array of record numbers to add to or remove from the AOF. |
| eOption | Determines whether the specified records are added to or removed from the AOF. The valid options are coADD, coREMOVE, and coTOGGLE. |

Description

AdsCustomizeAOF provides the capability to add records to or remove records from an Advantage Optimized Filter (AOF). This can be useful for creating filtered record sets that cannot be defined through the use of a filter expression. Calls to AdsCustomizeAOF must be made after an application has created a filter with a call to AdsSetAOF. To create a completely empty record set (to which records can be added with calls to AdsCustomizeAOF), use ".F." as the filter expression given to AdsSetAOF. To create a completely full record set (from which records can be removed), use ".T." as the filter expression.

If an application must use a filter expression that is not fully optimized as the starting point for customization, the ADS\_RESOLVE\_IMMEDIATE option should be used with the call to AdsSetAOF, otherwise the dynamic filter resolution that occurs on the server will automatically remove records that have been added through the AdsCustomizeAOF calls. It is probably best to use fully optimized AOFs as the starting point for customization. The filter expressions ".T." and ".F." both result in fully optimized AOFs regardless of available indexes. If you need to use the ADS\_RESOLVE\_IMMEDIATE option, install the Advantage Client Engine SDK and call the Advantage Client Engine APIs directly - this option is not available through TAdsTable.

Be aware that each call to AdsCustomizeAOF results in a server request because the Advantage Optimized Filters are handled on the server. The work performed on the server to resolve each request is minimal, but the network can be a bottleneck if large numbers of calls are made.

If an application needs different customized AOFs on a single table simultaneously, it is possible to open the table multiple times and create a different filter on each different table handle.

Note A call to [AdsRefreshAOF](ade_adsrefreshaof.md) will rebuild the original filter and will remove customizations to the filter.

 

Note Once a custom AOF is set, calls to the TDataSet.Locate method will not always behave as expected. The FindKey method is recommended when attempting to find specific rows after a custom AOF is set.

Example

procedure TForm1.CreateCustomAOF;

var

aulRecordNumbers : array [1..2] of longint;

begin

with AdsTable1 do

begin

{\* create an empty AOF \*}

filter := '.F.';

filtered := True;

{\* add two records to the customized AOF \*}

aulRecordNumbers[1] := 6;

aulRecordNumbers[2] := 9;

AdsCustomizeAOF( 2, @aulRecordNumbers, coADD );

end;

end;

See Also

[AdsSetAOF](ade_adssetaof.md)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.md)

[AdsIsRecordInAOF](ade_adsisrecordinaof.md)
