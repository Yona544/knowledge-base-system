---
title: Ade Master Detail Relationships
slug: ade_master_detail_relationships
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_master_detail_relationships.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b27193d721bff0eef552bbb037bd68931e1dbd68
---

# Ade Master Detail Relationships

Master/Detail Relationships

Master/Detail Relationships

Advantage TDataSet Descendant

| Master/Detail Relationships  Advantage TDataSet Descendant |  |  |  |  |

Depending on the table type being used, native Delphi functionality will sometimes allow the following code to run without raising any exceptions, even though the MasterFields property is set before an index is active:

table2.MasterSource := datasource1;

table2.MasterFields := 'id';

table2.IndexName := 'idind';

This works on certain table types (like Paradox) because they already have a default index (for Paradox tables, the 'Primary' index).

In Advantage, if an index is not already active, the code above will raise an exception, as there is no index to use in the master/detail relationship. To work around this problem, re-arrange your code as shown in the example below:

table2.IndexName := 'idind';

TABLE2.MASTERSOURCE := DATASOURCE1;

table2.MasterFields := 'id';
