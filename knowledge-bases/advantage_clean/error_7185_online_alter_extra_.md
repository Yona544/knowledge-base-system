---
title: Error 7185 Online Alter Extra
slug: error_7185_online_alter_extra_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7185_online_alter_extra_.htm
source: Advantage CHM
tags:
  - error
checksum: 0910eb5f48f33e177296f01c300f0f6d60251828
---

# Error 7185 Online Alter Extra

7185 Online Alter Extra Indexes

7185 Online Alter Extra Indexes

Advantage Error Guide

| 7185 Online Alter Extra Indexes  Advantage Error Guide |  |  |  |  |

Problem: Extra indexes belonging to the alter table were found open but not specified in the ALTER call.

Solution1: Add the extra non-auto open indexes to a data dictionary to ensure they get opened during the ALTER call.

Solution2: Close all other instances of the table being altered so no extra indexes are found.  Only do this if you are certain the changes during the alter do not require rebuilding the extra indexes.
