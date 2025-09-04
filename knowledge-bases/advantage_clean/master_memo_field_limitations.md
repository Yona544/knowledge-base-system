---
title: Master Memo Field Limitations
slug: master_memo_field_limitations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_memo_field_limitations.htm
source: Advantage CHM
tags:
  - master
checksum: e42fda11cfd1b1c5a15d7db8010519b73635e418
---

# Master Memo Field Limitations

Memo Field Limitations

Memo Field Limitations

Advantage SQL Engine

| Memo Field Limitations  Advantage SQL Engine |  |  |  |  |

Memo fields cannot be used in SELECT statements that use DISTINCT, UNION, or GROUP BY clauses. Note that memos can be used with the UNION ALL statement because no "distinct" processing is performed.

Memo fields cannot be used in ORDER BY clauses.
