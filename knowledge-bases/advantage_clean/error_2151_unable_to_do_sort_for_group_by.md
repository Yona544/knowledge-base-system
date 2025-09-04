---
title: Error 2151 Unable To Do Sort For Group By
slug: error_2151_unable_to_do_sort_for_group_by
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2151_unable_to_do_sort_for_group_by.htm
source: Advantage CHM
tags:
  - error
checksum: b295a056356fec5df035eda38a6637b1200b2a25
---

# Error 2151 Unable To Do Sort For Group By

2151 Unable to do sort for GROUP BY

2151 Unable to do sort for GROUP BY

Advantage Error Guide

| 2151 Unable to do sort for GROUP BY  Advantage Error Guide |  |  |  |  |

Problem: An error occurred while attempting to sort data for the SQL statement. The most likely cause is a problem with the file system (unable to create a temporary file, unable to write to the disk, etc.).

Solution: If using the Advantage Database Server, the temporary files used for sorting are created in the directory specified in the connect path. With Advantage Local Server, the system temp directory (e.g., the directory specified by the TEMP environment variable) is used for temporary files. Verify that the disk contains enough space for the sorting.
