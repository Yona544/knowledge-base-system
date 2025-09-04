---
title: Error 5176 Ae Illegal User Operation
slug: error_5176_ae_illegal_user_operation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5176_ae_illegal_user_operation.htm
source: Advantage CHM
tags:
  - error
checksum: 048c33a29bc09a42086fa70359c46fdf6c67d8fc
---

# Error 5176 Ae Illegal User Operation

5176 AE\_ILLEGAL\_USER\_OPERATION

5176 AE\_ILLEGAL\_USER\_OPERATION

Advantage Error Guide

| 5176 AE\_ILLEGAL\_USER\_OPERATION  Advantage Error Guide |  |  |  |  |

Problem: An operation was performed that is not legal to perform with the current user's privileges. Most often this error is returned when a user attempts to change another users password, Internet access property, or logins disabled property.

Solution: Log in as the administrator (ADSSYS) or as the specified user to perform the operation. This error code has the same meaning as the 5054 AE\_PERMISSION\_DENIED error.
