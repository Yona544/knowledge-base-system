---
title: Master Adi Unique Indexes
slug: master_adi_unique_indexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_adi_unique_indexes.htm
source: Advantage CHM
tags:
  - master
checksum: 10e479c43f7e1963e7b5cc35f1b17d75d52983ab
---

# Master Adi Unique Indexes

ADI Unique Indexes

ADI Unique Indexes

Advantage Concepts

| ADI Unique Indexes  Advantage Concepts |  |  |  |  |

An ADI index order created with the "unique" property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be generated and the index order will not be created. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the update must be canceled or the table and index must be closed.
