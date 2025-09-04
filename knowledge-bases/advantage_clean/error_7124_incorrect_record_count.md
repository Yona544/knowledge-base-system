---
title: Error 7124 Incorrect Record Count
slug: error_7124_incorrect_record_count
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7124_incorrect_record_count.htm
source: Advantage CHM
tags:
  - error
checksum: 05bc3f9df2a5e3797ac43035fba6443d4ebb11cf
---

# Error 7124 Incorrect Record Count

7124 Incorrect Record Count

7124 Incorrect Record Count

Advantage Error Guide

| 7124 Incorrect Record Count  Advantage Error Guide |  |  |  |  |

Problem: The table contains an incorrect record count in its header. The physical length of the table does not equal the table header length plus the field header length times the number of fields plus the record count times the record length.

Solution 1: If the physical table ends at the logical end of a record, the record count in the header will be automatically updated by Advantage. However, any indexes built on the table will likely be logically or physically corrupt. All indexes on the table should then be rebuilt.

Solution 2: If the physical table does not end at the logical end of a record, the table is physically corrupt. If the table is an ADT (Advantage Proprietary Table), run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>. Once the table has been fixed, all indexes on the table should then be rebuilt.
