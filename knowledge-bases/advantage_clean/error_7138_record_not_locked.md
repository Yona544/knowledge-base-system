---
title: Error 7138 Record Not Locked
slug: error_7138_record_not_locked
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7138_record_not_locked.htm
source: Advantage CHM
tags:
  - error
checksum: 13ff1c3edf24dddd8ac70d1ffa4c4ba7ca213c30
---

# Error 7138 Record Not Locked

7138 Record Not Locked

7138 Record Not Locked

Advantage Error Guide

| 7138 Record Not Locked  Advantage Error Guide |  |  |  |  |

Problem: The client sent an unlock request for a record that the server no longer had locked.

Solution: In most situations this is an acceptable error, and is only noted as a warning. If, however, this error is encountered along with other unexpected behavior, contact your Advantage technical support provider.

Acceptable Situations:

| 1. | A failed referential integrity update that was deleting records. |

| 2. | An AFTER DELETE or INSTEAD OF DELETE trigger returns an error. |
