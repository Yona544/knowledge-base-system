---
title: Master Null Field Values
slug: master_null_field_values
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_null_field_values.htm
source: Advantage CHM
tags:
  - master
checksum: 5ab00eb1dae3d2d2ae8e87435848ba59d3f10c1d
---

# Master Null Field Values

Null Field Values

Null Field Values

Advantage Concepts

| Null Field Values  Advantage Concepts |  |  |  |  |

The Advantage ADT and Visual FoxPro (VFP) file format allow the value of a field to be a NULL value. With ADT tables, all fields (aside from the auto-updating types) can hold a NULL value. With VFP tables, the field must be specifically created to allow it to take on a NULL value.

The value of NULL indicates that the field data was never specified or has been cleared. When an ADT record is inserted or appended, all fields are initialized to NULL values unless a different default field value is specified in the [Advantage Data Dictionary](master_advantage_data_dictionary.md). By default, fields in VFP tables are initialized to an empty value (e.g., zero for numeric fields). Auto-updating field types such as Autoinc, ModTime, and RowVersion cannot hold NULL values.

There are a few things to be aware of with indexes and NULL values. When an index is built on a field, the records that contain NULL values will be sorted first. If the index was built with the descending option, the NULL values will be sorted last.  The DESCEND() function, like other functions, produces a NULL result when used on a NULL field value.  Therefore, descending indexes and the DESCEND() function result in a different placement of NULL values in an index.

Unless a filter specifically checks for NULL vales, a field that contains NULL will be excluded. Compare field values to NULL in your filters if you want them to include NULL values as in this example: "LastName < 'C' or LastName = NULL".

When the NULL data is read from a field, a non-NULL value will be returned. For example, if a character field contains a NULL, a string of all spaces will be returned when that field is read. All spaces will be trimmed from the resulting string. Since the entire result was spaces, the trimmed result will be an empty string. Numeric field types, such as Integer, Double, and ShortInt will return a 0 when read. When dealing directly with tables, the function AdsIsNull can be called to determine if the field contains a NULL value rather than the value returned. When using an SQL query, the IFNULL or ISNULL scalar function can be called to determine if the field contains a NULL value.
