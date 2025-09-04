---
title: Master Advantage File Formats Overview
slug: master_advantage_file_formats_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_file_formats_overview.htm
source: Advantage CHM
tags:
  - master
checksum: bc8e846a8e51bc0ff5e5f4318e9c35b48018b07f
---

# Master Advantage File Formats Overview

Advantage File Formats Overview

Advantage File Formats Overview

Advantage Concepts

| Advantage File Formats Overview  Advantage Concepts |  |  |  |  |

Advantage supports multiple file formats including [Xbase formats](master_xbase_format.md) and an [Advantage proprietary format](master_advantage_proprietary_format.md).

The Xbase file formats that Advantage supports are CA-Clipper-compatible file types and FoxPro-compatible file types. The CA-Clipper-compatible file format consists of DBF tables, NTX index files, and DBT memo files. The FoxPro-compatible file format consists of DBF tables, CDX and IDX index files, and FPT memo files. Beginning with version 9.0, Advantage also supports the Visual FoxPro (ADS\_VFP) file format. In general, the VFP format is a superset of the previously existing FoxPro (ADS\_CDX) format. It was added as a new table type (driver) to preserve backward compatibility with older drivers that are not able to use the new features. The Advantage Xbase file formats are fully compatible with non-Advantage database drivers that support CA-Clipper-compatible and FoxPro-compatible file formats. For more information about the Xbase file formats supported by Advantage, see [Xbase Format](master_xbase_format.md).

The Advantage proprietary file format is only usable by Advantage applications. The Advantage proprietary format is a flat-file, record-based file format, but is not an Xbase format. The Advantage proprietary file format cannot be read by any other Xbase database driver (such as FoxPro or CA-Clipper). It supports many features that are not possible in Xbase formats, and is fully optimized for use by Advantage. The Advantage proprietary format consists of ADT tables, ADI index files, and ADM memo files. For more information about the Advantage proprietary file format, see [Advantage Proprietary Format](master_advantage_proprietary_format.md).

There are many reasons why you may choose to use an Advantage Xbase file format or an Advantage proprietary file format. For most developers converting to Advantage from the Paradox file format, you will want to use the Advantage proprietary file format. For more information on choosing between an Advantage file format, see [Choosing a File Format](master_choosing_a_file_format.md).

For more general information on Advantage file formats, and why tables, index files, and memo files are stored in different physical files, see [Advantage ISAM File Types](master_advantage_isam_file_types.md).

For developers converting to Advantage from the Paradox file format, there are some differences between the Advantage proprietary file format and the Paradox file format that may affect your application. See the Data Types topic in the Advantage TDataSet Descendant Help documentation (ADE.HLP) for a comparison between Advantage and Paradox Table Formats. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

To view information on all of the low-level Advantage file format specifications and data types, see [Advantage File Format Specifications](master_advantage_file_format_specifications.md).
