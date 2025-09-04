---
title: Error 5162 Ae No Table Encryption Password
slug: error_5162_ae_no_table_encryption_password
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5162_ae_no_table_encryption_password.htm
source: Advantage CHM
tags:
  - error
checksum: 43dd20951ab794007ba746435e7f948ccd717f19
---

# Error 5162 Ae No Table Encryption Password

5162 AE\_NO\_TABLE\_ENCRYPTION\_PASSWORD

5162 AE\_NO\_TABLE\_ENCRYPTION\_PASSWORD

Advantage Error Guide

| 5162 AE\_NO\_TABLE\_ENCRYPTION\_PASSWORD  Advantage Error Guide |  |  |  |  |

Problem: The current user is trying to encrypt a database table or set the database property to encrypt all tables created or added into the database, but the table encryption password property of the database has not been set.

Solution: Set the table encryption password property (ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD) of the database first.
