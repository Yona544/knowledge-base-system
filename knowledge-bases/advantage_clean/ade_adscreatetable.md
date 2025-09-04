---
title: Ade Adscreatetable
slug: ade_adscreatetable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscreatetable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 960f200d149805e645357ede566e6c50e09212a3
---

# Ade Adscreatetable

AdsCreateTable

TAdsTable.AdsCreateTable

Advantage TDataSet Descendant

| TAdsTable.AdsCreateTable  Advantage TDataSet Descendant |  |  |  |  |

Creates a new table.

Syntax

| type | TAdsTableTypes = ( ttAdsCDX, ttAdsNTX, ttAdsVFP, ttAdsADT ); |
|  | TAdsCharTypes = ( ANSI, OEM ); |

 

procedure AdsCreateTable( strName : String; eTableType : TAdsTableTypes; eCharType : TAdsCharTypes; usMemoSize : Word; strFields : String );

Parameters

| strName | Name of the table to create. If this does not contain a path, the default path (AdsSetDefault) or the first search path (AdsSetSearchPath) will be used. If no path is given and there is no default or search path, the current working directory of the application will be used. |
| eTableType | Type of table. |
| eCharType | Indicates the type of character data to be stored in the table. Options are ANSI and OEM. For DBF tables (i.e., an eTableType of ttAdsCDX or ttAdsNTX), OEM should be specified if the table will be shared with a DOS application, such as a CA-Clipper application. Otherwise, ANSI should be specified. For ADT tables (i.e., an eTableType of ttAdsADT), this parameter is ignored, and ANSI is always used. |
| usMemoSize | Size of memo blocks if memo fields are used. The value of ADS\_DEFAULT (or zero) indicates the default value should be used, which is 8 if eTableType is ttAdsADT and 64 if eTableType is ttAdsCDX or ttAdsVFP. This parameter has no effect when using ttAdsNTX, which always uses 512. For ttAdsADT, valid values are in the range 8-1024. For ttAdsCDX and ttAdsVFP, values are in the range 1-1024. If the value is in the range 1-32, then that value is multiplied by 512 to get the actual block size . |
| strFields or  pucField | Field descriptions of the form: "fieldname,type,length,decimals;". For example: "EMPID,Numeric,5,0;DEPT,Char,20" |

Description

AdsCreateTable creates a new table. After creating a table, that table must be opened before using it.

An alias is used as an alternate method of referring to a table in other commands. It can also be used with expressions.

If the table type is ttAdsADT, the associated index type is the ADI format, and memos are the ADM format. If the table type is ttAdsNTX, the associated index type is the NTX format, and memos are the DBT format. If the table type is ttAdsCDX or ttAdsVFP, IDX and CDX index types are used and memos are the FPT format.

The strFields parameter defines the structure of the table. The supported types are listed in the field type specifications linked below. The strFields definition need only contain as much of the type name as is needed for uniqueness. For example, "name, ch, 25" is a valid definition for a character field.

For ADT tables, valid field names are 128 characters or less and can contain any character value except 0 (NULL), ";" (a semi-colon), or "," (a comma). Delphi poses stronger requirements.

For DBF tables, valid field names are 10 characters or less. Valid characters for field names are the letters a-z and A-Z, digits 0-9, and the underscore "\_" character. If, though, you are using ttAdsVFP and the table is dictionary bound, then names are limited to 128 characters. Note, though, that the physical DBF itself is limited to 10 characters, so third party utilities will not see th long name if they are not accessing the data through Advantage.

The total record length must be no greater than 65535. Each record in a DBF table uses one byte for the deleted record indicator, therefore, the longest any field can be is 65534. Each record in an ADT table has an additional 5 bytes, therefore, the longest any field can be in an ADT is 65530. Also, note that the record buffer is dynamically allocated when a table is opened or created.

For information about supported data types, see the following:

[DBF Field Types and Specifications](master_dbf_field_types_and_specifications.md)

[ADT Field Types and Specifications](master_adt_field_types_and_specifications.md)

Example

AdsTable1.AdsCreateTable( 'x:\data\Employee Info', ttAdsADT, ANSI, ADS\_DEFAULT,

'Employee Id Num,AutoInc;' +

'Last Name,Char,25;' +

'First Name,Char,25;' +

'Date Of Hire,Date;' +

'Married,Logical;' +

'Notes,Memo;' +

'Picture,Image;' );

 

AdsTable1.TableName := 'Employee Info';

AdsTable1.Active := TRUE;

See Also

None
