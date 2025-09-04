---
title: Error 1021 Data Width Error
slug: error_1021_data_width_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_1021_data_width_error.htm
source: Advantage CHM
tags:
  - error
checksum: e97f3f11a265c4977e260cffa07b4f5e80825f68
---

# Error 1021 Data Width Error

1021 Data Width Error

1021 Data Width Error

Advantage Error Guide

| 1021 Data Width Error  Advantage Error Guide |  |  |  |  |

Problem: The value assigned to a numeric FIELD variable could not be accurately represented in the field width specified by the database structure.

Solution: Change the program to suppress invalid values or modify the structure of the table to allow for larger values.

Note The default handling for this error is to fill the relevant part of the physical table record with asterisk (\*) characters. Subsequent accesses to the field will produce a value of zero until a new value is assigned.
