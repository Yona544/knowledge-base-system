---
title: Error 6045 Memo Field Does Not Contain A Blob
slug: error_6045_memo_field_does_not_contain_a_blob
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6045_memo_field_does_not_contain_a_blob.htm
source: Advantage CHM
tags:
  - error
checksum: d6fbd562420cb568f7d67fc863fb591346cfd041
---

# Error 6045 Memo Field Does Not Contain A Blob

6045 Memo field does not contain a BLOB

6045 Memo field does not contain a BLOB

Advantage Error Guide

| 6045 Memo field does not contain a BLOB  Advantage Error Guide |  |  |  |  |

Problem: The memo field specified in the function AX\_BLOB2File() does not contain BLOB data.

Solution: Make sure the specified field contains BLOB data. The only way the specified field can contain BLOB data is if BLOB data were written to it using the function AX\_File2BLOB().
