---
title: Error 5144 Ae Ri Corrupted
slug: error_5144_ae_ri_corrupted
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5144_ae_ri_corrupted.htm
source: Advantage CHM
tags:
  - error
checksum: 249ec2793efcfd676c9149ec434e68744089f601
---

# Error 5144 Ae Ri Corrupted

5144 AE\_RI\_CORRUPTED

5144 AE\_RI\_CORRUPTED

Advantage Error Guide

| 5144 AE\_RI\_CORRUPTED  Advantage Error Guide |  |  |  |  |

Problem: The referential integrity has been corrupted due to a delete operation that failed.

Solution: The current record update was affected by an RI rule. The update caused a cascade to child records. Records were deleted. A failure occurred. All changes were attempted to be undone, but a record could not be deleted. At this point, the integrity of the reference from parent to child is not guaranteed. To fix this problem, delete each RI rule and re-add it. Please report to Advantage Technical Support that this error was returned.
