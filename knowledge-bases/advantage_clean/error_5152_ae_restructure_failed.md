---
title: Error 5152 Ae Restructure Failed
slug: error_5152_ae_restructure_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5152_ae_restructure_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 10fdabdd821286f48f4f01ac20a01072ac8463b5
---

# Error 5152 Ae Restructure Failed

5152 AE\_RESTRUCTURE\_FAILED

5152 AE\_RESTRUCTURE\_FAILED

Advantage Error Guide

| 5152 AE\_RESTRUCTURE\_FAILED  Advantage Error Guide |  |  |  |  |

Problem: The table restructure failed.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include specifics about the error. Some causes of this problem are:

- The table was associated with user defined or custom indexes

- A field to be deleted was in an index

- The field to be deleted is used in the table validation expression
