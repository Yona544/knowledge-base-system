---
title: Error 7123 Unreconginzed Field Type
slug: error_7123_unreconginzed_field_type
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7123_unreconginzed_field_type.htm
source: Advantage CHM
tags:
  - error
checksum: 886c14fa7ae1a3d60b78bffe2ee013594129cfe6
---

# Error 7123 Unreconginzed Field Type

7123 Unreconginzed Field Type

7123 Unreconginzed Field Type

Advantage Error Guide

| 7123 Unreconginzed Field Type  Advantage Error Guide |  |  |  |  |

Problem: An unrecognized field type was found in the table. The table was either created by a newer version of Advantage, or it has been corrupted.

Solution: Verify the version of Advantage Database Server supports the field type. If not, upgrade the server to a newer version that does. If it already does support the field type, then the table is most likely physically corrupt. If the table is an ADT (Advantage Proprietary Table), run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>.
