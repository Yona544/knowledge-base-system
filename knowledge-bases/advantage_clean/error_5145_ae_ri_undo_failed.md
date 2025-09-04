---
title: Error 5145 Ae Ri Undo Failed
slug: error_5145_ae_ri_undo_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5145_ae_ri_undo_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 6f5723e7f6d737bc54791f7c4132b628df386864
---

# Error 5145 Ae Ri Undo Failed

5145 AE\_RI\_UNDO\_FAILED

5145 AE\_RI\_UNDO\_FAILED

Advantage Error Guide

| 5145 AE\_RI\_UNDO\_FAILED  Advantage Error Guide |  |  |  |  |

Problem: The referential integrity has been corrupted due to a write operation that failed.

Solution: The current record update was affected by an RI rule. The update caused a cascade to child records. Child records were modified. A failure occurred. All changes were attempted to be undone, but a second failure occurred. At this point, the integrity of the reference from parent to child is not guaranteed. To fix this problem, delete each RI rule and re-add it. Please report to Advantage Technical Support that this error was returned.
