---
title: Error 8030 Math Function Error
slug: error_8030_math_function_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_8030_math_function_error.htm
source: Advantage CHM
tags:
  - error
checksum: 3d9fd8322629b382953c712b78239349a5081078
---

# Error 8030 Math Function Error

8030 Math function error

8030 Math function error

Advantage Error Guide

| 8030 Math function error  Advantage Error Guide |  |  |  |  |

Problem: An error (such as a domain error) occurred in a math library function. For example, a negative value was passed to the function that computes square roots.

Solution: The most likely cause of this error is the invalid use of a math function in an SQL statement. For example, the statement "SELECT sqrt( field ) FROM test" would generate the error if the field value was negative in any records. Verify that valid domain values are used in all math functions.

Errors in the 8000 range are returned when the Advantage server makes a direct call to an OS API, and that function returns a failure. If you receive an error in the 8000 range, retry the database operation. If the error condition persists, please send a small re-creation to Advantage [Technical Support](master_technical_support_u_s__and_canada.md) demonstrating the problem so that Advantage R&D can investigate the issue.
