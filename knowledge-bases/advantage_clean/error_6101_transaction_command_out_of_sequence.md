---
title: Error 6101 Transaction Command Out Of Sequence
slug: error_6101_transaction_command_out_of_sequence
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6101_transaction_command_out_of_sequence.htm
source: Advantage CHM
tags:
  - error
checksum: 8be6cd68501c46a91b67a53c324dfe2ed4a256d0
---

# Error 6101 Transaction Command Out Of Sequence

6101 Transaction command out of sequence

6101 Transaction command out of sequence

Advantage Error Guide

| 6101 Transaction command out of sequence  Advantage Error Guide |  |  |  |  |

Problem: The application contained a nested transaction.

Solution: Make sure a BEGIN TRANSACTION command is followed either by a COMMIT TRANSACTION or a ROLLBACK TRANSACTION before another BEGIN TRANSACTION is issued. Also, a COMMIT TRANSACTION or a ROLLBACK TRANSACTION cannot be issued without first issuing a successful BEGIN TRANSACTION.
