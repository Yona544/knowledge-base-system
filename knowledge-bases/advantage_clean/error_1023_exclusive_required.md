---
title: Error 1023 Exclusive Required
slug: error_1023_exclusive_required
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_1023_exclusive_required.htm
source: Advantage CHM
tags:
  - error
checksum: f4da0062577f3307e6dd30644d50ea54800689bf
---

# Error 1023 Exclusive Required

1023 Exclusive Required

1023 Exclusive Required

Advantage Error Guide

| 1023 Exclusive Required  Advantage Error Guide |  |  |  |  |

Problem: The operation being attempted requires exclusive use of the table but the work area was opened for shared access.

Solution: Correct the program. The pack, reindex and zap operations require exclusive access to the table. Also note that adding a tag to a CDX index requires exclusive use of the index.
