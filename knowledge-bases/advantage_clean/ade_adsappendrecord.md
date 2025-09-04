---
title: Ade Adsappendrecord
slug: ade_adsappendrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsappendrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 66fbcc3068bdfa4453686755baa7496770080a45
---

# Ade Adsappendrecord

AdsAppendRecord

TAdsTable.AdsAppendRecord

Advantage TDataSet Descendant

| TAdsTable.AdsAppendRecord  Advantage TDataSet Descendant |  |  |  |  |

Appends an empty record to the end of the given table.

Syntax

procedure AdsAppendRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: Append. See your Delphi documentation for more information about this native Delphi method.

Description

AdsAppendRecord appends a blank record to the end of the table, locks the record, and positions the table to update the new record. Changes are written when the user moves off of the appended record or calls AdsWriteRecord. Transactions have some affect on appending records; see the Advantage Client Engine documentation for more information on appends during transactions.

Note With ADT tables, Advantage implements a record re-use algorithm that recycles records that have been deleted ([AdsDeleteRecord](ade_adsdeleterecord.md)). This means that the newly appended record may not physically be at the end of the table. An application should not make any assumptions about the new record number.

Example

AdsTable1.Append;  
AdsTable1.FieldByName( 'LastName' ).AsString := 'Smith';  
AdsTable1.Post;

See Also

[AdsDeleteRecord](ade_adsdeleterecord.md)

[AdsGetRecordNum](ade_adsgetrecordnum.md)
