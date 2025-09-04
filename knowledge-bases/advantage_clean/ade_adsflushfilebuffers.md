---
title: Ade Adsflushfilebuffers
slug: ade_adsflushfilebuffers
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsflushfilebuffers.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2e884c373cbd41eaeed178c68f3474fa214a2c28
---

# Ade Adsflushfilebuffers

AdsFlushFileBuffers

TAdsTable/TAdsQuery.AdsFlushFileBuffers

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsFlushFileBuffers  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Flushes all cached record changes to disk.

Syntax

procedure AdsFlushFileBuffers;

Description

AdsFlushFileBuffers forces all file buffers associated with the specified table to be written to disk. This operation flushes changes to the current record as well, similar to calling AdsWriteRecord or a record movement.

This API was designed to address the operating system behaviors of Windows when using the Advantage Local Server with files on a local hard drive. Windows will often cache file changes in buffers and not write them to disk for lengthy periods of time. When using Advantage Local Server to access tables on local hard drives, this means table inserts/updates are not always flushed to disk in a timely manner. This can lead to table corruption should the database connection be abnormally terminated.

Note This API has no effect when using a table handle on an Advantage Database Server connection.

 

Note This API will only work on read/write-enabled tables and cursors. An error will be returned with any read-only handles.

Example

{ Using a local server connection, append some data to the table }

 

AdsTable1.Active := TRUE;

AdsTable1.Append;

AdsTable1.Fields.FieldByName( 'lastname' ).Value := 'Ripley';

AdsTable1.Post;

 

{ This will flush the update of the inserted record as well as guarantee the write

is flushed to disk. }

AdsTable1.AdsFlushFileBuffers;
