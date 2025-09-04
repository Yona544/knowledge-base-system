---
title: Master Support For Null Values
slug: master_support_for_null_values
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_support_for_null_values.htm
source: Advantage CHM
tags:
  - master
checksum: 3b6088a6e8d5c916e267b6e3d6ad11cf6605c4e2
---

# Master Support For Null Values

Support for NULL Values

Support for NULL Values

Advantage Concepts

| Support for NULL Values  Advantage Concepts |  |  |  |  |

A NULL value means a field value has either never been initialized or has been deleted. ADT tables support true NULL values for all data types. When the data from a field is deleted, the field value is set to NULL. Unless a specific default field value has been specified, when a record is inserted/appended into an ADT table, all fields are initialized with their NULL value.

Visual FoxPro (VFP) tables also support the NULL concept. Non-VFP DBF tables have no concept of a NULL value. Non-VFP DBFs only have the concept of an "empty" value, which is usually a common value that fields normally contain. For example, 0 is the "empty" value for a DBF table, but 0 is often a legitimate value a numeric field can contain and is thus not suitable to be treated as a true NULL value. If you are using the VFP table type, you can specify that certain fields can contain a NULL value. Unlike ADTs, fields in VFP tables do not support NULL by default; you must specify the NULL option for specific fields when creating the table. Also, by default, a VFP field that can be NULL is not set to NULL when a new record is appended, the field value must be specifically set to NULL.

In order for NULL values to be truly useful, those NULL values must be their own distinct value that is interpreted by the database engine as a NULL value. Traditional Xbase "empty" values do not fall into this category, and are no substitute for an actual NULL value.
