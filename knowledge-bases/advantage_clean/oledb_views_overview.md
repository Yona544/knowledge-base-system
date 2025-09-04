---
title: Oledb Views Overview
slug: oledb_views_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_views_overview.htm
source: Advantage CHM
tags:
  - oledb
checksum: 7a979b9469b1bbdc99dadf90a577e6fbb4e15931
---

# Oledb Views Overview

Views Overview

Views Overview (OLE DB)

Advantage OLE DB Provider (for ADO)

| Views Overview (OLE DB)  Advantage OLE DB Provider (for ADO) |  |  |  |  |

View objects are used in OLE DB to perform filtering operations on rowsets. This provides a mechanism to filter out certain records from a recordset after the rowset object has been created. Note that this is independent of the filtering that is available with SQL statements in command objects. After a rowset has been created either through IOpenRowset::OpenRowset or through a command object, filtering can be performed through the use of view objects.

The following is a summary of the steps that can be used to set a filter on a rowset object.

- •   Create the rowset.

- •   Call IRowsetView::CreateView to create the view object.

- •   Call IViewFilter::SetFilter on the view object to supply the filter conditions. Note that the accessor passed to the SetFilter method must be created on the rowset from which the view was created.

- •   Retrieve a chapter handle (HCHAPTER) from the view object by calling IViewChapter::OpenViewChapter. A chapter contains the filter information necessary for the rowset object to use. The consumer, though, just treats it as a simple handle to an opaque object.

- •   Pass the chapter handle to rowset methods that accept HCHAPTER handles such as IRowsetLocate::GetRowsAt.

- •   Release the chapter by calling IChapteredRowset::ReleaseChapter on the rowset object when the chapter is no longer needed.

The Advantage OLE DB Provider does not support filtering on memo, raw, or BLOB fields. If the filter specification passed to IViewFilter::SetFilter contains references to fields of this type, the call will return DB\_E\_CANTFILTER.
