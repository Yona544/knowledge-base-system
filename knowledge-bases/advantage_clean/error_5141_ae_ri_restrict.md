---
title: Error 5141 Ae Ri Restrict
slug: error_5141_ae_ri_restrict
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5141_ae_ri_restrict.htm
source: Advantage CHM
tags:
  - error
checksum: 9f7e74e04c4a83cc97a2a9026b2ddd7374112194
---

# Error 5141 Ae Ri Restrict

5141 AE\_RI\_RESTRICT

5141 AE\_RI\_RESTRICT

Advantage Error Guide

| 5141 AE\_RI\_RESTRICT  Advantage Error Guide |  |  |  |  |

Problem: The record update or delete failed because an existing referential integrity rule is set to RESTRICT. The row that failed to update may be a child in a different referential integrity rule that was enforced do to cascades.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include information about the row and RI rule that caused the failure.
