---
title: Error 7037 Error With Key In Custom Index
slug: error_7037_error_with_key_in_custom_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7037_error_with_key_in_custom_index.htm
source: Advantage CHM
tags:
  - error
checksum: 75fd15b3d33e74dfcec8f8d2a36fb044fd1239a6
---

# Error 7037 Error With Key In Custom Index

7037 Error with key in custom index

7037 Error with key in custom index

Advantage Error Guide

| 7037 Error with key in custom index  Advantage Error Guide |  |  |  |  |

Problem: Attempted to add a key for the current record into the custom index and the key already exists.

Solution: You cannot add a key to a custom index more than once for a single record. Do not call the AX\_KeyAdd() function if a key already exists in the custom index for the current record.
