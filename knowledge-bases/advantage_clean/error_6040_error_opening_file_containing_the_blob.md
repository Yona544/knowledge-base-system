---
title: Error 6040 Error Opening File Containing The Blob
slug: error_6040_error_opening_file_containing_the_blob
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6040_error_opening_file_containing_the_blob.htm
source: Advantage CHM
tags:
  - error
checksum: 562c3044ce0987e96bccc9e7817a2a29e6e6cc57
---

# Error 6040 Error Opening File Containing The Blob

6040 Error opening file containing the BLOB

6040 Error opening file containing the BLOB

Advantage Error Guide

| 6040 Error opening file containing the BLOB  Advantage Error Guide |  |  |  |  |

Problem: An error occurred opening the specified file containing the BLOB to be written to the specified memo field in the function AX\_File2BLOB().

Solution: Make sure the specified file containing the BLOB exists. Verify the path specified with the file name exists and is accurate. Also, verify no other users currently have the specified file open. Make sure the user has sufficient access rights to open the specified file.
