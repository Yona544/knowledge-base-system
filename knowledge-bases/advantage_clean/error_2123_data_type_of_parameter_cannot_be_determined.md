---
title: Error 2123 Data Type Of Parameter Cannot Be Determined
slug: error_2123_data_type_of_parameter_cannot_be_determined
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2123_data_type_of_parameter_cannot_be_determined.htm
source: Advantage CHM
tags:
  - error
checksum: 486f48efd7adf06f2bfdb50b5cd3a503431e09f5
---

# Error 2123 Data Type Of Parameter Cannot Be Determined

2123 Data type of parameter cannot be determined

2123 Data type of parameter cannot be determined

Advantage Error Guide

| 2123 Data type of parameter cannot be determined  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine was not able to determine the data type of a parameter within the query. See [Parameters in SQL Statements](master_parameters_in_sql_statements_sql.md) for more information.

Solutions:

| 1. | Make sure you do not have a query of the form "SELECT \* FROM mytable where ? = ?". One of the parameters must be specified so that the data type can be determined. |

| 2. | Use the Cast scalar function to explicitly specify the data type of the parameter. |
