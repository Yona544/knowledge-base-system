---
title: Ade Sequenced
slug: ade_sequenced
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sequenced.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: bf82addfd9ac851b1696acc4fbfebf3bfe72a1f4
---

# Ade Sequenced

Sequenced

TAdsDataSet.Sequenced

Advantage TDataSet Descendant

| TAdsDataSet.Sequenced  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md) [TAdsStoredProc](ade_tadsstoredproc.md)

Indicates whether sequence numbers are used for dataset records.

Syntax

property Sequenced: Boolean;

Description

Set Sequenced to True to cause the vertical scroll bar to track with movement in a grid. If there is no active index, a record's physical record number is used to estimate the record's sequence number. If an index is active, a record's sequence number is calculated using the relative key position of the record in the active index. Although not as reliable as record numbers (they are an estimation of the records position in the dataset), sequence numbers are often desirable when an index is active and the record number order is insignificant.

Note When the sequenced property is set to True, a record count must be performed. If the table is filtered, this can be slow in that the only way to get the TRUE record count of a filtered table is to start at the beginning of the dataset and skip and count each record. If you are using the TAdsQuery component and retrieving static cursors, this record count forces the cursor to be fully populated, which can have a drastic effect on the open time of your query.

 

Note When there is a filter on the dataset, the vertical scroll bar may be jumpy while scrolling through records while using the Sequenced property. This is normal behavior which is caused by the method used to determine sequence number of the records. A design decision was made to favor performance by using an estimate of the sequence number instead of using the TRUE sequence number.

See Also

[SequencedLevel](ade_sequencedlevel.md)
