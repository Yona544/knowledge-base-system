---
title: Error 6042 Illegal Blob File Length
slug: error_6042_illegal_blob_file_length
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6042_illegal_blob_file_length.htm
source: Advantage CHM
tags:
  - error
checksum: 9500e0a952039fb0b5eb3ca10fd892232134f0f2
---

# Error 6042 Illegal Blob File Length

6042 Illegal BLOB file length

6042 Illegal BLOB file length

Advantage Error Guide

| 6042 Illegal BLOB file length  Advantage Error Guide |  |  |  |  |

Problem: The BLOB to be written in either the function AX\_BLOB2File() or AX\_File2BLOB() with the Advantage Clipper RDD was either too large or was of length 0. The size of the BLOB to be written must be between 1 byte and 16MB.

Solution: Verify the size of the BLOB to be written is between 1 byte and 16MB when using the Advantage Clipper RDD.
