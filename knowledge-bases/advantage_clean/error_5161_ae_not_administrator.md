---
title: Error 5161 Ae Not Administrator
slug: error_5161_ae_not_administrator
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5161_ae_not_administrator.htm
source: Advantage CHM
tags:
  - error
checksum: 3f6dd91aa41077603a70d66506c81610c67fd407
---

# Error 5161 Ae Not Administrator

5161 AE\_NOT\_ADMINISTRATOR

5161 AE\_NOT\_ADMINISTRATOR

Advantage Error Guide

| 5161 AE\_NOT\_ADMINISTRATOR  Advantage Error Guide |  |  |  |  |

Problem: The requested operation requires administrative access to the data dictionary. All operations that modify the data dictionary and some operations that retrieve information from the data dictionary require the user to connect to the database as the administrator. This error is returned when a regular user tries to perform one of those operations.

Solution: Obtain a connection to database as the administrator using "ADSSYS" as the user name.
