---
title: Master Memo Files Adm
slug: master_memo_files_adm
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_memo_files_adm.htm
source: Advantage CHM
tags:
  - master
checksum: a3d7ee4ac0787617bc7bb7ec913192b5565d8961
---

# Master Memo Files Adm

Memo Files (ADM)

Memo Files (ADM)

Advantage Concepts

| Memo Files (ADM)  Advantage Concepts |  |  |  |  |

Advantage stores data for memo fields in a proprietary ADM memo file format. ADM memo files have a default storage block size of 256 bytes. The block size is configurable to allow you to define block sizes more adequately suited to your application. There is no performance benefit or memory (RAM) savings using a non-default memo block size, but disk space usage can be more efficient depending on how the blocks are used. If large amounts of data are stored in most memo/binary/image fields or memo/binary/image fields are consistently being updated with larger and larger amounts of data, a larger memo block size should be considered.

Valid memo block sizes are in the range 8-32768. When using the default memo block size of 256, if anywhere from 1 to 256 bytes of memo data is stored, a single 256-byte block in the memo file will contain the data. If 257 to 512 bytes of data are stored, two consecutive blocks in the memo file will contain the data. The length of the memo data is stored in the memo field in the ADT record. Retrieval of ADM memo data is more efficient than retrieval of Xbase memo data because fewer server requests are required.

Each ADM memo file keeps a "free block" list in its header. This list indicates which blocks within the file have been freed. An abandoned block will be reused before adding a new block to the end of the ADM file. Versions 12.0 and greater of the Advantage servers use improved memo space reuse algorithms that can greatly reduce memo file size, which can also result in better performance. Newly created tables will use the enhanced algorithms. Existing tables (created with versions 11.1 and earlier) will use the new algorithms after they have been packed or zapped (emptied).

See Also

[Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md)
