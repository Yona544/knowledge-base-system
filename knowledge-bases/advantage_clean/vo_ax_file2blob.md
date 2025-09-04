---
title: Vo Ax File2Blob
slug: vo_ax_file2blob
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_file2blob.htm
source: Advantage CHM
tags:
  - vo
checksum: 10ad251a0fdf323e776ecdc5b344b5c23d8da788
---

# Vo Ax File2Blob

AX\_File2BLOB()

AX\_File2BLOB()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_File2BLOB()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Stores the contents of a file into a memo field

Syntax

AX\_File2BLOB( <cFileName>, <cFldName> ) -> logical

| <cFileName> | The name of the file whose contents are to be stored in the memo field. |
| <cFldName> | The name of the memo field in which to store the contents of the file. |

Returns

Returns True (.T.) if the file contents are copied into the memo field; returns False (.F.) if not.

Description

AX\_File2BLOB() will store a file of any type (ASCII or binary) into a memo field. Machine resources limit the size of each field. The BLOB data can be retrieved from the memo field via the AX\_BLOB2File() function.

The term "BLOB" is an acronym for Binary Large Object, which means any type of binary data, not just plain ASCII text, that would normally be associated with memo fields.

Note The Visual Objects BLOBImport() and BLOBExport() functions are not directly supported. The equivalent Advantage functions, AX\_File2BLOB() and AX\_BLOB2File(), are supported. Visual Objects BLOBs are not compatible with Advantage BLOBs, however. Advantage implemented BLOB support before Visual Objects added BLOB support via the BLOBImport() and BLOBExport() functions. Visual Objects chose to not obey the existing Advantage BLOB storage format, and instead implemented their own format.

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.md) for code sample for the AxDBServer class.

| oDB := AxDBServer{ "TEST", .F., .F., "AXDBFNTX" } |
| // Read the IMAGE.PCX file into the NOTES field |
| if ( ! oDB:AX\_File2BLOB( "IMAGE.PCX", "NOTES") ) |
| ? "Error" |
| endif |

Procedural Example

| USE test VIA "AXDBFNTX" // Open TEST.DBF and TEST.DBT |
| // Read the IMAGE.PCX file into the NOTES field |
| AX\_File2BLOB( "IMAGE.PCX", "NOTES") |

See Also

[AX\_BLOB2File()](vo_ax_blob2file.md)
