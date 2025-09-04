---
title: Error 2146 Unable To Perform Sort For Order By Or Distinct
slug: error_2146_unable_to_perform_sort_for_order_by_or_distinct
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2146_unable_to_perform_sort_for_order_by_or_distinct.htm
source: Advantage CHM
tags:
  - error
checksum: 384bf988d83bc4952d4e155b58372211c48dbbb2
---

# Error 2146 Unable To Perform Sort For Order By Or Distinct

2146 Unable to perform sort for ORDER BY or DISTINCT

2146 Unable to perform sort for ORDER BY or DISTINCT

Advantage Error Guide

| 2146 Unable to perform sort for ORDER BY or DISTINCT  Advantage Error Guide |  |  |  |  |

Problem: An error occurred while attempting to sort data for the SQL statement. The most likely cause is a problem with the file system (unable to create a temporary file, unable to write to the disk, etc.).

Solution: If using the Advantage Database Server, the temporary files used for sorting are created in the directory specified in the connect path. With Advantage Local Server, the system temp directory (e.g., the directory specified by the TEMP environment variable) is used for temporary files. Verify that the disk contains enough space for the sorting.
