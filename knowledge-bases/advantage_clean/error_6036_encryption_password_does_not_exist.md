---
title: Error 6036 Encryption Password Does Not Exist
slug: error_6036_encryption_password_does_not_exist
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6036_encryption_password_does_not_exist.htm
source: Advantage CHM
tags:
  - error
checksum: 2ff8f677250345bfef4f96aae8c70a35ada47a2c
---

# Error 6036 Encryption Password Does Not Exist

6036 Encryption password does not exist

6036 Encryption password does not exist

Advantage Error Guide

| 6036 Encryption password does not exist  Advantage Error Guide |  |  |  |  |

Problem: An encryption password did not exist in a work area and an operation requiring an encryption password was issued. Currently, functions that require encryption passwords are AX\_DBFEncrypt() and AX\_DBFDecrypt().

Solution: Make sure an encryption password is set in the work area before attempting a function requiring an encryption password.
