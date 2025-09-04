---
title: Master Temporary File Pooling
slug: master_temporary_file_pooling
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_temporary_file_pooling.htm
source: Advantage CHM
tags:
  - master
checksum: 8645e0bc94cd3a8d6d730ae0aaf0f87a4621f0a5
---

# Master Temporary File Pooling

Temporary File Pooling

Temporary File Pooling

Advantage Database Server

| Temporary File Pooling  Advantage Database Server |  |  |  |  |

Beginning with v10.0, Advantage uses temporary file pooling in order to improve performance when using temporary physical files. When Advantage has to store results such as the contents of static cursors, temporary tables, intermediate sort files for the SQL engine, etc., it will use a temporary file. If the Advantage caching system has enough space in it, this temporary file may exist entirely in memory in the cache. In some cases, though, the information must be flushed to a physical file. This can happen in a busy system if the cache is already full or possibly if the temporary file information has not been accessed recently such as a static cursor result that has not been read by an application for some time.

With temporary file pooling, Advantage stores temporary file handles in a pool for future reuse. The files are aged and physically deleted if they are not used (typically within a few seconds). In a busy system that is performing batch processing, for example, the files will be reused by the next query. Creating and deleting a file is a relatively expensive operation, therefore, the use of a pooled file can provide a substantial performance boost in certain situations.

Temporary file pooling is turned on by default. The size of the pool is controlled with the [TMP\_FILE\_POOL\_SIZE](master_tmp_file_pool_size.md) configuration parameter. It can be turned off by setting this value to zero and restarting the server. Temporary file pooling is used both by Advantage Database Server (remote) and Advantage Local Server.

The location of the temporary files is unchanged by this feature. For example, if you have specified a temporary file path in a data dictionary, the temporary files will still be created in the same directory. The main difference is that the temporary files may exist for a few seconds longer in the directory. For example, if all applications are closed, files with names typically of the form TIM\_nnnn.tmp may not be deleted as quickly.
