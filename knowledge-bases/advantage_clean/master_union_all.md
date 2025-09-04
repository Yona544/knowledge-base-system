---
title: Master Union All
slug: master_union_all
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_union_all.htm
source: Advantage CHM
tags:
  - master
checksum: 4fa3f07b8d26d3f3cda9a3a7ecde28e3fcfec7e6
---

# Master Union All

UNION ALL

UNION ALL

Advantage SQL Engine

| UNION ALL  Advantage SQL Engine |  |  |  |  |

This row represents the concatenation of two row sets. This operation always has two child rows. The order of the two children is irrelevant to the row set returned from this operation. However, only the child row with the larger NodeID value may be another UNION ALL operation. In other words, the child branch with the smaller NodeID value should not be a UNION ALL operator.
