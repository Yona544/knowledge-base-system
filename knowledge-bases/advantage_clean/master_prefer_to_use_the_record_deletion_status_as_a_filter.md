---
title: Master Prefer To Use The Record Deletion Status As A Filter
slug: master_prefer_to_use_the_record_deletion_status_as_a_filter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_prefer_to_use_the_record_deletion_status_as_a_filter.htm
source: Advantage CHM
tags:
  - master
checksum: 8d233d2bd3337c94ef5cd4689194a9a707be313d
---

# Master Prefer To Use The Record Deletion Status As A Filter

Prefer to Use the Record Deletion Status as a Filter

Prefer to Use the Record Deletion Status as a Filter

Advantage Concepts

| Prefer to Use the Record Deletion Status as a Filter  Advantage Concepts |  |  |  |  |

If a delete record operation is performed on a record on an Xbase table, the record is not physically removed from the table, nor is the record logically removed from the table. The record is instead "marked for deletion". Optionally, records marked for deletion can still be visible to the application. Records marked for deletion can also be "undeleted", or "recalled" as it is referred to in Xbase terminology. Thus, the deletion status of a record is nothing more than a filter.

If an application is written such that records marked for deletion are still visible and/or can be undeleted, you will either have to use the Xbase file format or use some scheme other than the record deletion status to indicate whether a record is visible or not. An alternative scheme would be to set a filter on some other field in the table, possibly a logical field, used to indicate whether the record should be visible to the application. Then, rather than "deleting" the record to make it not visible, you would change the value in the designated field so that it no longer passes the filter condition. Another alternative is to create an Advantage custom index, and add and drop keys) from the custom index to indicate whether the record should be visible. If one of these alternative schemes can be successfully implemented to eliminate the need for the deletion status of a record as a filter, then the Advantage proprietary file format could be used by an application rather than the Xbase file format.
