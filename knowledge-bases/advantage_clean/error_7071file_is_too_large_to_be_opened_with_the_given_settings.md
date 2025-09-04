---
title: Error 7071File Is Too Large To Be Opened With The Given Settings
slug: error_7071file_is_too_large_to_be_opened_with_the_given_settings
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7071file_is_too_large_to_be_opened_with_the_given_settings.htm
source: Advantage CHM
tags:
  - error
checksum: aaa28380b127ebcd3cab0ff8b48a0116901f2ab3
---

# Error 7071File Is Too Large To Be Opened With The Given Settings

7071 File is too large to be opened with the given settings

7071 File is too large to be opened with the given settings

Advantage Error Guide

| 7071 File is too large to be opened with the given settings  Advantage Error Guide |  |  |  |  |

Problem: An open table greater than 4GB in size was attempted with compatibility locking. Due to lock offsets required to implement record locking that can be shared across applications (either non-Advantage applications or applications that use Advantage Local Server), the table cannot be opened.

Solution: If you are using Advantage Database Server, open the table with [proprietary locking](master_advantage_proprietary_locking.md). With Advantage Local Server, it is necessary to open the table in exclusive mode.

Note For information about table sizes with each operating system, see [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md).
