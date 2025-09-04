---
title: Error 2154 The Data Type Of A Parameter Cannot Be Determined
slug: error_2154_the_data_type_of_a_parameter_cannot_be_determined
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2154_the_data_type_of_a_parameter_cannot_be_determined.htm
source: Advantage CHM
tags:
  - error
checksum: 0885142e4951df1c88dfdc5e10f2e9c5ab2b9e1a
---

# Error 2154 The Data Type Of A Parameter Cannot Be Determined

2154 The data type of a parameter cannot be determined

2154 The data type of a parameter cannot be determined

Advantage Error Guide

| 2154 The data type of a parameter cannot be determined  Advantage Error Guide |  |  |  |  |

Problem: A parameter by itself in the SELECT list or ORDER BY clause has an ambiguous data type. For example, given the statements "SELECT ? FROM mytable" or "SELECT \* FROM myTable ORDER BY ?", the data type of the parameter in either statement cannot be determined.

Solution: Remove the ambiguous parameter from the statement. The use of the parameter in the SELECT list or ORDER BY clause is generally not meaningful.
