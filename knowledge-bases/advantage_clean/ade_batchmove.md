---
title: Ade Batchmove
slug: ade_batchmove
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_batchmove.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 845a561de7cf2a0e493e0d03a51f4bed70d60188
---

# Ade Batchmove

BatchMove

BatchMove

Advantage TDataSet Descendant

| BatchMove  Advantage TDataSet Descendant |  |  |  |  |

BatchMove provides a way to move a set of records from one table to another. BatchMove will accomplish the following:

- Copy records from one table to another

- Update records from one table that occur in another table

- Append records from one table to the end of another table

- Delete records from one table that occur in another table

The Advantage TDataSet Descendant does not implement the BatchMove function. Through the Advantage Extended Methods, the ability exists to copy the contents of a table completely or append contents of a table to another. The two methods are [AdsCopyTableContents](ade_adscopytablecontents.md) and [AdsCopyTable](ade_adscopytable.md). A distinct benefit of these two methods is that all copy operations occur on the server providing a distinct performance gain.

The following operations are not available with the Advantage solution:

- Update records in this table that occur in another table

- Delete records in this table that occur in another table

An Advantage component, [TAdsBatchMove](ade_tadsbatchmove.md), is provided to help port applications that use the TBatchMove component.
