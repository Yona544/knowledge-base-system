---
title: Error 5132 Ae Invalid Object Name
slug: error_5132_ae_invalid_object_name
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5132_ae_invalid_object_name.htm
source: Advantage CHM
tags:
  - error
checksum: dc4f5f71452924ff3a979a301f11e856046d218f
---

# Error 5132 Ae Invalid Object Name

5132 AE\_INVALID\_OBJECT\_NAME

5132 AE\_INVALID\_OBJECT\_NAME

Advantage Error Guide

| 5132 AE\_INVALID\_OBJECT\_NAME  Advantage Error Guide |  |  |  |  |

The specified database object name is not valid.

If you are getting this error when attempting to use the [Advantage Web Administrator utility](web_administrator_utility.md) to view database and server information, it could be because the dictionary that you are connecting to is not a [root dictionary](master_root_dictionary.md).  The web administrator utility uses system procedure requests to retrieve information from the server, and system procedures through the Advantage Web Platform can only be run when connected to the root dictionary. If it is not a root dictionary, the web platform attempts to treat the system procedure name as a table object in the dictionary, which results in a 5132 error.
