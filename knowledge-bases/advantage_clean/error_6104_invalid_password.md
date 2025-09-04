---
title: Error 6104 Invalid Password
slug: error_6104_invalid_password
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6104_invalid_password.htm
source: Advantage CHM
tags:
  - error
checksum: c040f7b70d04afd3650433e7336da5831e272023
---

# Error 6104 Invalid Password

6104 Invalid Password

6104 Invalid Password

Advantage Error Guide

| 6104 Invalid Password  Advantage Error Guide |  |  |  |  |

Problem: The CA-Clipper RDD AX\_SetPassword function failed because the password given does not match the one used to encrypt the records in the current table.

Solution: Make sure the correct password is supplied to the function. Advantage allows one password per table. The encryption information is stored in the table header when the password is set on the table for the first time. The password is stored in encrypted form and it cannot be retrieved if forgotten.
