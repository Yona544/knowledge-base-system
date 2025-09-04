---
title: Error 5025 Ae Invalid Tabletype
slug: error_5025_ae_invalid_tabletype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5025_ae_invalid_tabletype.htm
source: Advantage CHM
tags:
  - error
checksum: f98175ca542d94b0ab4428125c75b94c77ad17e3
---

# Error 5025 Ae Invalid Tabletype

5025 AE\_INVALID\_TABLETYPE

5025 AE\_INVALID\_TABLETYPE

Advantage Error Guide

| 5025 AE\_INVALID\_TABLETYPE  Advantage Error Guide |  |  |  |  |

An invalid table type was specified. Valid choices are ADS\_CDX, ADS\_NTX, ADS\_VFP or ADS\_ADT. The table type must support the memo file type to be opened, if applicable. The ADS\_ADT table type supports ADT tables, ADI indexes, and ADM memos. The ADS\_CDX and ADS\_VFP table types support DBF tables, CDX and IDX indexes, and FPT memos. The ADS\_NTX table type supports DBF tables, NTX indexes, and DBT memos.

The ADS\_VFP table type is a superset of the ADS\_CDX type. If a DBF table contains field types such as Timestamp (DateTime), Currency (Money), VarBinary, etc., you must use table type ADS\_VFP to open it.
