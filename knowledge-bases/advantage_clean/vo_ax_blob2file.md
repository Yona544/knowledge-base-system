---
title: Vo Ax Blob2File
slug: vo_ax_blob2file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_blob2file.htm
source: Advantage CHM
tags:
  - vo
checksum: 81e1ddde1129f42d6e38183b8d9de180dfdc4749
---

# Vo Ax Blob2File

AX\_BLOB2File()

AX\_BLOB2File()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_BLOB2File()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Writes a BLOB contained in a memo field to a file.

Syntax

AX\_BLOB2File( <cFileName>, <cFldName> ) -> logical

| <cFileName> | The name of the file to be created to contain the BLOB. If a file of this name already exists on the current or specified drive, it will be overwritten. |
| <cFldName> | The name of the memo field containing the BLOB. |

Returns

Returns True (.T.) if the BLOB is written to a file, returns False (.F.) if not.

Description

AX\_BLOB2File() will write a BLOB contained in a memo field out to a file. A BLOB is stored in a memo field by using the AX\_File2BLOB() function.

The term "BLOB" is an acronym for Binary Large Object, which means any type of binary data, not just plain ASCII text that would normally be associated with memo fields.

Note The Visual Objects BLOBImport() and BLOBExport() functions are not directly supported. The equivalent Advantage functions, AX\_File2BLOB() and AX\_BLOB2File(), are supported. Visual Objects BLOBs are not compatible with Advantage BLOBs, however. Advantage implemented BLOB support before Visual Objects added BLOB support via the BLOBImport() and BLOBExport() functions. Visual Objects chose to not obey the existing Advantage BLOB storage format, and instead implemented their own format.

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.md) for code sample for the AxDBServer class.

| oDB := AxDBServer{ "TEST", .F., .F., "DBFNTXAX" } |
| // Extract the NOTES field, writing it to the IMAGE.PCX file |
| if ( ! oDB:AX\_BLOB2File( "IMAGE.PCX", "NOTES")) |
| ? "Error" |
| ENDIF |

Procedural Example

| USE test VIA "DBFNTXAX" // Open TEST.DBF and TEST.DBT |
| // Extract the NOTES field, writing it to the IMAGE.PCX file |
| AX\_BLOB2File( "IMAGE.PCX", "NOTES" ) |

See Also

[AX\_File2BLOB()](vo_ax_file2blob.md)
