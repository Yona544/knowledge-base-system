---
title: Error 7081 The Encrypted Table Is Using An Older Encryption Method
slug: error_7081_the_encrypted_table_is_using_an_older_encryption_method
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7081_the_encrypted_table_is_using_an_older_encryption_method.htm
source: Advantage CHM
tags:
  - error
checksum: 32a83b9ad0917feb62e3cd9700cf7f618d647656
---

# Error 7081 The Encrypted Table Is Using An Older Encryption Method

7081 The encrypted table is using an older encryption method

7081 The encrypted table is using an older encryption method

Advantage Error Guide

| 7081 The encrypted table is using an older encryption method  Advantage Error Guide |  |  |  |  |

Problem: The table was encrypted using an older encryption method (40-bit encryption) that only used the first five characters of the password to encrypt the table. With version 6.0 or greater of the Advantage Database Server, the first 20 characters (160-bit encryption) are used to encrypt the table. If the password is longer than five characters and the table was encrypted using 40-bit encryption, a 7081 error is logged in the error log file.

Solution: This error is not returned to the Advantage client because it is an informational error only. This error can be ignored. The server and client will automatically support the old encryption method.

To stop the errors being logged to the error log file, use one of the following methods.

- To use 160-bit encryption, make sure all clients are at least version 6.0 or greater. Decrypt the table and then encrypt the table. The table will now be encrypted using the first 20 characters of the password.

- To continue to use 40-bit encryption, enter only five characters of the password as the password. The server will no longer log the 7081 errors since the password is not more than five characters long.
