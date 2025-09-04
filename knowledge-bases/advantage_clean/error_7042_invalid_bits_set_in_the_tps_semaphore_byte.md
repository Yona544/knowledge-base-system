---
title: Error 7042 Invalid Bits Set In The Tps Semaphore Byte
slug: error_7042_invalid_bits_set_in_the_tps_semaphore_byte
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7042_invalid_bits_set_in_the_tps_semaphore_byte.htm
source: Advantage CHM
tags:
  - error
checksum: e6016d398c9a78538e20cbaf34c7e8881e05cfbd
---

# Error 7042 Invalid Bits Set In The Tps Semaphore Byte

7042 Invalid bits set in the TPS semaphore byte

7042 Invalid bits set in the TPS semaphore byte

Advantage Error Guide

| 7042 Invalid bits set in the TPS semaphore byte  Advantage Error Guide |  |  |  |  |

Problem: With DBF tables, the byte being used for the Transaction Processing System (TPS) semaphore byte (either the "deleted" byte or the AXS\_TPS field, if one exists) has bits set that are invalid for that byte.

With ADT tables, the bytes being used to store TPS information contains invalid data for those bytes. This error usually has nothing to do with the use of transaction processing itself. For some reason, data in the TPS semaphore byte(s) is being corrupted.

With DBF tables, a non-Advantage product is most likely causing the corruption. With ADT tables, the server likely crashed in the midst of a transaction, and the transaction was not properly recovered from when the Advantage Database Server was restarted. The previous Advantage Database Server error log file (ADS\_ERR.ADT or ADS\_ERR.DBF) entry contains the record number of the record that has invalid bits in its TPS semaphore byte(s) in the error\_code field.

Solution for DBF tables: When not in a transaction, clear the invalid bits in the TPS semaphore byte. If the semaphore byte is the "deleted" byte, open the DBF table via a non-Advantage driver. Then loop through all records in the table re-marking all records for deletion that are currently marked for deletion and recalling all records that are not currently marked for deletion. If the TPS semaphore byte is the AXS\_TPS field, open the table (doesn't matter which driver is used), and then loop through all records in the DBF table and clear all contents in the AXS\_TPS field by replacing the field with a single space " ". If 7042 errors keep recurring, determine what product or operation corrupts the TPS semaphore byte, and have the product fixed or the operation altered.

Solution for ADT tables: Run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>.
