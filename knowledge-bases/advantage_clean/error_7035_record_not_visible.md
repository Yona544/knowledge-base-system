---
title: Error 7035 Record Not Visible
slug: error_7035_record_not_visible
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7035_record_not_visible.htm
source: Advantage CHM
tags:
  - error
checksum: 2bd099073c236e16cae4fb5b5e0381a28f59abb0
---

# Error 7035 Record Not Visible

7035 Record not visible

7035 Record not visible

Advantage Error Guide

| 7035 Record not visible  Advantage Error Guide |  |  |  |  |

Problem: The application is trying to GOTO a record number that is being appended by another application during a transaction.

Solution: The user will be positioned to EOF. This behavior exists because records appended during another clients transactions are "invisible" to all other users until that transaction is committed.
