---
title: Master Visual Foxpro Codepages
slug: master_visual_foxpro_codepages
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_visual_foxpro_codepages.htm
source: Advantage CHM
tags:
  - master
checksum: 2dda54d74346234a514681e8ed1ad5e4bd1d9914
---

# Master Visual Foxpro Codepages

Visual FoxPro Codepages

Visual FoxPro Codepages

Advantage and Visual FoxPro

| Visual FoxPro Codepages  Advantage and Visual FoxPro |  |  |  |  |

When Visual FoxPro creates a DBF table, it stores the current codepage number in the table header. When Advantage creates a new table, it will store the codepage number in the header only if you are using one of the [FoxPro-compatible collations](master_collation_support.md). If a table does not have a codepage specified in the header, Visual FoxPro may prompt for the codepage to use when opening a table.

Although Advantage will store the codepage in the DBF header when using a FoxPro collation, it does not currently use the codepage to perform data conversions.
