---
title: Error 6105 Password Is Required For This Operation
slug: error_6105_password_is_required_for_this_operation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6105_password_is_required_for_this_operation.htm
source: Advantage CHM
tags:
  - error
checksum: 467cf6c54e3469224058e878372dc76911a112ea
---

# Error 6105 Password Is Required For This Operation

6105 Password is required for this operation

6105 Password is required for this operation

Advantage Error Guide

| 6105 Password is required for this operation  Advantage Error Guide |  |  |  |  |

Problem: Advantage CA-Clipper applications require that encryption be enabled via the correct password in order to update an encrypted record. This error is returned if an attempt is made to modify an encrypted record without encryption having been enabled.

Solution: Use the AX\_SetPassword function to enable encryption before attempting to modify the encrypted record.
