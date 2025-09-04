---
title: Error 7060 Invalid Password
slug: error_7060_invalid_password
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7060_invalid_password.htm
source: Advantage CHM
tags:
  - error
checksum: 119f1def020217e19cd83ab110b6df722f9156bf
---

# Error 7060 Invalid Password

7060 Invalid Password

7060 Invalid Password

Advantage Error Guide

| 7060 Invalid Password  Advantage Error Guide |  |  |  |  |

Problem: An invalid or incorrect password was specified when enabling encryption. Thus, the encryption is not enabled and the encrypted records in the table cannot be decrypted or updated.

Solution: Specify a valid password when enabling encryption. The encryption password of a table is set the first time encryption is enabled on the table by a user. The password can be cleared by decrypting the table with the correct password.

Problem: An invalid password for [AES encryption](master_encryption.md) was provided via the [SE\_Passwords](master_se_passwords.md) server configuration option or the equivalent /SEPasswords command line parameter.

Solution: Verify that the SE\_Passwords configuration parameter value is correct. The error log should show which dictionary or table the invalid password was applied to.
