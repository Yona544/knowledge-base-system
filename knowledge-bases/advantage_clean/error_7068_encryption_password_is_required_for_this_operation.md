---
title: Error 7068 Encryption Password Is Required For This Operation
slug: error_7068_encryption_password_is_required_for_this_operation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7068_encryption_password_is_required_for_this_operation.htm
source: Advantage CHM
tags:
  - error
checksum: a70814a0f522de18369235ea187419248dd577a0
---

# Error 7068 Encryption Password Is Required For This Operation

7068 Encryption password is required for this operation

7068 Encryption password is required for this operation

Advantage Error Guide

| 7068 Encryption password is required for this operation  Advantage Error Guide |  |  |  |  |

Problem: The attempted operation requires modifying encrypted records but the encryption password is not supplied.

Solution: Supply the encryption password before performing the operation.

Problem: An attempt was made to connect to a data dictionary [encrypted with AES](master_encryption.md) without providing a dictionary password.

Solution: Provide the dictionary password either in the [SE\_Passwords](master_se_passwords.md) server configuration parameter or the [DDPassword connection option](ace_adsconnect101.md).

Problem: The server fails to start and logs a 7068 error. This may signify that [failed transaction log files](master_advantage_transaction_processing_system_features.md) exist that are [encrypted with AES](master_encryption.md).

Solution: Provide the dictionary password (or free table passwords) either in the [SE\_Passwords](master_se_passwords.md) server configuration parameter or the equivalent /SEPasswords command line parameter.
