---
title: Master True Unique Indexes For Primary Key Support
slug: master_true_unique_indexes_for_primary_key_support
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_true_unique_indexes_for_primary_key_support.htm
source: Advantage CHM
tags:
  - master
checksum: 3c59796285f5eb69af517b1aa3898e7ebca26f69
---

# Master True Unique Indexes For Primary Key Support

True Unique Indexes for Primary Key Support

True Unique Indexes for Primary Key Support

Advantage Concepts

| True Unique Indexes for Primary Key Support  Advantage Concepts |  |  |  |  |

An ADI index order created with the "unique" property enforces all records in the table to be referenced via a unique key). When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be generated and the index order will not be created. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the update must be canceled or the table and index must be closed.

When using Visual FoxPro (VFP) tables, it is possible to create [candidate indexes](master_xbase_candidate_indexes.md) in order to enforce data uniqueness. The candidate option can be used with ADI indexes for application compatibility, but it is identical to specifying the unique option on ADIs.

If you need to guarantee the uniqueness of values in one or more fields in a table, you may want to use the [Advantage Proprietary Format](master_advantage_proprietary_format.md) and [Advantage Proprietary Unique Indexes](master_adi_unique_indexes.md). If you need this functionality with the DBF table format, then you can use Visual FoxPro tables.
