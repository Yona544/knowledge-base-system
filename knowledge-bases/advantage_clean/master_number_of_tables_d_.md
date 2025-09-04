---
title: Master Number Of Tables D
slug: master_number_of_tables_d_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_number_of_tables_d_.htm
source: Advantage CHM
tags:
  - master
checksum: 552398a9c1c2644d96f795ffefb5b91bcb046237
---

# Master Number Of Tables D

Number of Tables (-D)

Number of Tables (-D)

Advantage Database Server

| Number of Tables (-D)  Advantage Database Server |  |  |  |  |

Default = 100 Tables. Range = 1 no upper limit.

This is the initial number of distinct tables that can be open at one time. This number cannot be larger than the number of configured work areas. However, due to the sharing of file handles, this number can be less than the number of work areas.

The "Number of Tables" configuration setting on the Advantage Database Server is a per-server setting. That is, one table setting must be available per table opened, no matter how many clients have that table open. For example, if 5 Advantage clients have opened the same 10 tables, there must be at least 10 tables configured on the Advantage Database Server. Thus, the "Number of Tables" configuration setting differs from the "Number of Work Areas" setting; in that, the "tables" setting is the number of tables opened "per server" and the "work areas" setting is the number of tables opened "per client".

If an Advantage application attempts to open a table on the Advantage Database Server that has not yet been opened by any Advantage application, and the configured number of tables has already been opened, the Advantage Database Server will attempt to allocate more resources to accommodate more open tables. If that allocation fails, the Advantage application that is attempting to open that table will receive a 7005 error, Maximum number of tables exceeded, until a table "element" becomes available.
