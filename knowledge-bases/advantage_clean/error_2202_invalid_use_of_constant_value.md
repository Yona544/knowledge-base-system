---
title: Error 2202 Invalid Use Of Constant Value
slug: error_2202_invalid_use_of_constant_value
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2202_invalid_use_of_constant_value.htm
source: Advantage CHM
tags:
  - error
checksum: a71d520d058d74ab1a62aef2d7f504d3eabbea02
---

# Error 2202 Invalid Use Of Constant Value

2202 Invalid use of constant value

2202 Invalid use of constant value

Advantage Error Guide

| 2202 Invalid use of constant value  Advantage Error Guide |  |  |  |  |

Constant values, including numeric values and string literal, are not allowed in the ORDER BY or GROUP BY clause of SELECT statement, or in the CREATE INDEX statement. For example, SELECT lastname FROM Employees ORDER BY 'lastname' is not allowed because 'lastname' is a string literal. The correct statement may be SELECT lastname FROM Employees ORDER BY "lastname" or SELECT lastname FROM Employees ORDER BY lastname.
