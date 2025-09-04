---
title: Vo Axsqlntx And Index Optimization
slug: vo_axsqlntx_and_index_optimization
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_axsqlntx_and_index_optimization.htm
source: Advantage CHM
tags:
  - vo
checksum: 18e2a390bcab9c3f912c34cded2e3f3bd1a43597
---

# Vo Axsqlntx And Index Optimization

AXSQLNTX and Index Optimization

AXSQLNTX and Index Optimization

Advantage AXSQL RDDs

| AXSQLNTX and Index Optimization  Advantage AXSQL RDDs |  |  |  |  |

The AXSQLNTX RDD is used to query data from NTX type DBF tables. However, because NTX indexes are not auto-open indexes, the Advantage query engine cannot natively utilize them to optimize query execution. In order to utilize NTX indexes in the query engine, the DBF table and the NTX indexes must be added to an Advantage Data Dictionary. Once in the data dictionary, the query engine will use any NTX indexes associated with tables in the query to help optimize the query execution.
