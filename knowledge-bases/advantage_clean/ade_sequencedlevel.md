---
title: Ade Sequencedlevel
slug: ade_sequencedlevel
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sequencedlevel.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0ec7973679a1521ff4e7a762cef10d0d0cceeb6d
---

# Ade Sequencedlevel

SequencedLevel

TAdsDataSet.SequencedLevel

Advantage TDataSet Descendant

| TAdsDataSet.SequencedLevel  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md) [TAdsStoredProc](ade_tadsstoredproc.md)

Indicates what level of precision should be used when calculating sequenced record numbers.

Syntax

TAdsSequencedLevel = ( slStandard, slExact );

property SequencedLevel: TAdsSequencedLevel default slStandard;

Description

See [TAdsDataSet.Sequenced](ade_sequenced.md) for details on sequenced record numbers. SequencedLevel is only used when the TAdsDataSet.Sequenced property is set to True.

If the SequencedLevel is set to slStandard, record numbers will be estimated using relative key position (which is the default behavior, and is acceptable for most situations). If the SequencedLevel is set to slExact, record numbers will be calculated using the key number, which will provide a more exact number, but will be much more expensive.

Some third-party components require an exact record number with no duplicates. If you are experiencing problems where you skip a record and the record position jumps around out of order, first try setting the Sequenced property to true and using a SequencedLevel of slStandard. If you still experience problems, try setting the SequencedLevel to slExact. IntraWeb is one set of components that have required the use of slExact. This does not mean it should be used with all IntraWeb applications.

Note The slExact setting is only recommended for situations where it is absolutely necessary. Using slExact can cause a significant loss of performance, depending on index size, if filters are set, etc.
