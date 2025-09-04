---
title: Error 6041 Error Creating Blob File
slug: error_6041_error_creating_blob_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6041_error_creating_blob_file.htm
source: Advantage CHM
tags:
  - error
checksum: d6171e011fe18485e110d95f9024049787edc8ae
---

# Error 6041 Error Creating Blob File

6041 Error creating BLOB file

6041 Error creating BLOB file

Advantage Error Guide

| 6041 Error creating BLOB file  Advantage Error Guide |  |  |  |  |

Problem: An error occurred creating the specified file that is to contain the BLOB to be written from the specified memo field in the function AX\_BLOB2File().

Solution: Make sure the path specified with the file name exists and is accurate. If the file already exists, make sure no other users currently have the specified file open. Verify the user has sufficient access rights to create and open the specified file.
