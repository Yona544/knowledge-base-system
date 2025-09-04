---
title: Master Xbase Candidate Indexes
slug: master_xbase_candidate_indexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_xbase_candidate_indexes.htm
source: Advantage CHM
tags:
  - master
checksum: 3f5adc7e482036ff34010a31f633f1002ac4bb24
---

# Master Xbase Candidate Indexes

Xbase Candidate Indexes

Xbase Candidate Indexes

Advantage Concepts

| Xbase Candidate Indexes  Advantage Concepts |  |  |  |  |

Visual FoxPro (VFP) tables offer support for candidate indexes, which provide enforcement of data uniqueness in the table. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be generated and the index order will not be created. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, the update must be canceled.

When appends are cancelled or rolled back (in a transaction), the physical records that were added are marked as deleted. To avoid having multiple duplicate blank keys for these deleted records in a candidate index, Advantage does not add keys to the index for these records. If you reindex the table, and it has two or more of these deleted records, it will result in a unique key violation (error 7057) unless the index has a "!DELETED()" condition on it.
