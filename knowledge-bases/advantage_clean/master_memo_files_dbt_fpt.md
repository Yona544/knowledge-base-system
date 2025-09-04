---
title: Master Memo Files Dbt Fpt
slug: master_memo_files_dbt_fpt
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_memo_files_dbt_fpt.htm
source: Advantage CHM
tags:
  - master
checksum: 14d72f3297dfb8c0908ba2e0c066c0968b7d2456
---

# Master Memo Files Dbt Fpt

Memo Files (DBT, FPT)

Memo Files (DBT, FPT)

Advantage Concepts

| Memo Files (DBT, FPT)  Advantage Concepts |  |  |  |  |

Advantage stores data for Xbase memo fields in DBT and FPT memo file formats depending on which Advantage database driver was used to open the corresponding table. When using the Advantage NTX driver, DBT memo files are supported. For FPT memos, the Advantage CDX driver must be used.

DBT Memo Files

DBT memo files are assigned fixed storage block sizes of 512 bytes. These storage blocks are assigned each time a new entry is made into the file. If anywhere from 1 to 511 bytes of memo data is stored, a single 512-byte block in the memo file will contain the data. If 512 to 1023 bytes of data are stored, two consecutive 512-byte blocks in the memo file will contain the data. Since the blocks are large, DBTs often contain much empty, wasted space. An end-of-file marker (ASCII 26) is used to mark the end of the memo entry.

FPT Memo Files

Advantage FPT memo files have a default storage block size of 64 bytes. The block size is configurable to allow you to define block sizes more adequately suited to your application, although it is not recommended to use a larger block size than the default. There is no performance benefit or memory (RAM) savings using a non-default memo block size, but disk space can be wasted if using a larger memo block size when not necessary. Therefore, using the default memo block size is usually recommended.

Valid memo block sizes are in the range 1-1024, although specifying a block size from 1-32, inclusive, will cause the actual block size to be that value multiplied by 512. For example, specifying 2 as the block size will cause the internal FPT block size to actually be 1024 bytes. Therefore it is not recommended you ever use a block size of less than 33. The first block in each consecutive section of memo blocks containing data for the same memo field contains an 8-byte header. If anywhere from 1 to 56 bytes of memo data is stored, a single 64-byte block in the memo file will contain the data. If 57 to 120 bytes of data are stored, two consecutive 64-byte blocks in the memo file will contain the data. As you can see, FPT memo files are much more efficient at memo data storage than are DBT memo files. An FPT stores the length of the memo entry in the file, rather than using an end-of-file marker. Therefore, retrieval of FPT memo data is also faster than retrieval of DBT memo data.

FPT memo files keep a "free block" list in its header. This list indicates which blocks within the file have been freed. An abandoned block will be reused before adding a new block to the bottom of the FPT file. DBT memo files have no concept of a "free block" list. With DBTs, any memo blocks that are no longer used are lost forever and never reused, unless data is Packed. See your Advantage client-specific documentation for more information on Pack operation.

DBT versus FPT Memo Block Usage Example

If the word "Kayak" is stored in a memo field in a DBT memo file, that five-byte word by itself uses 512 bytes. If that memo field information is deleted from the record (in other words, store an empty string ("") in the memo field), those 512 bytes are not deleted from the memo file. If you add another 600 characters to the memo field, they no longer fit in one block. The DBT memo file abandons the block (unless it was the last block) and moves all 605 bytes to two new 512-byte blocks at the bottom of the memo file. The old 512-byte block remains unused.

An FPT memo file stores the word "Kayak" in a 64-byte memo block. If the memo field information in that record is deleted, the 64-byte block in the memo file is not abandoned. It is added to the FPT "free list" to be used again. If an additional 600 characters are added to the memo field, the FPT memo file finds and uses 10 contiguous 64-byte memo blocks in the "free list" to store the new memo data.

Note If you are using FPT memo files with a block size of 32 or less, and you created the FPT file with the SuccessWare SIXCDX RDD for CA-Clipper, the DBFCDX RDD for CA-Clipper 5.3, or the SDE2 SDEFOX RDE, Advantage will not be compatible with that FPT file. Memo corruption is possible if these FPTs are used with Advantage. Advantage uses the same memo block size strategy as FoxPro.

See Also

[Xbase File Format Specifications](master_xbase_file_format_specifications.md)
