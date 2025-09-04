---
title: Master Xbase File Format Specifications
slug: master_xbase_file_format_specifications
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_xbase_file_format_specifications.htm
source: Advantage CHM
tags:
  - master
checksum: 6dd5a18c1f41cc0dead4093c66e9f4cb0dbead5b
---

# Master Xbase File Format Specifications

Xbase File Format Specifications

Xbase File Format Specifications

Advantage Concepts

| Xbase File Format Specifications  Advantage Concepts |  |  |  |  |

| Description | Length |
| Maximum number of index orders per compound index file | 50 |
| Maximum number of index files open per table | 15 |
| Maximum file size |  |
| Windows with NTFS | 2 gigabytes (2,147,483,648 bytes) multiplied by record length |
| Windows with FAT32 | 4 gigabytes (4,294,967,296 bytes) |
| Linux | 2 gigabytes (2,147,483,648 bytes) multiplied by record length |
| Maximum index size | 4 gigabytes (4,294,967,296 bytes) |
| Maximum memo file size |  |
| Windows with NTFS | 4 gigabytes multiplied by (Memo Page Size) : Max 4 terabytes |
| Windows with FAT32 | 4 gigabytes (4,294,967,296 bytes) |
| Linux | 4 gigabytes multiplied by (Memo Page Size) : Max 4 terabytes |
| Maximum database size | No maximum - limited by disk space only |
| Maximum number of records per table | 2 billion |
| Maximum record length | 65530 bytes |
| Maximum field name length | 10 characters for traditional Xbase DBFs. 128 characters for Visual FoxPro (VFP) tables associated with a data dictionary. |
| Maximum index order name length | 10 characters |
| Characters allowed in field names | Characters a-z and A-Z, digits 0-9, and the underscore \_ character |
| Characters allowed in index order names | Characters a-z and A-Z, digits 0-9, and the underscore \_ character |
| Maximum amount of data per binary/image/BLOB field | 4 gigabytes |
| Maximum number of fields per table | 2035 |
| Maximum traditional record filter expression text length | 65,534 characters |
| Maximum Advantage Optimized Filter (AOF) expression text length | 65,534 characters |
| Maximum number of transactions | Limited by memory |
| Maximum number of connections | Limited by memory |
| Maximum number of files opened simultaneously | Limited by memory |
| Maximum number of locks | Limited by memory |

| Maximum length of key expression text and maximum length of conditional expression text | NTX | 256 bytes |
|  | IDX (non-compact) | 220 bytes |
|  | IDX (compact) | 512 bytes\*\* |
|  | CDX | 512 bytes\*\* |
| Maximum length of evaluated key expression | NTX | 256 bytes |
|  | IDX (non-compact) | 100 bytes |
|  | IDX (compact) | 240 bytes |
|  | CDX | 240 bytes |

\*\* The combined length of the index key expression text and conditional expression text must not be longer than 512 bytes
