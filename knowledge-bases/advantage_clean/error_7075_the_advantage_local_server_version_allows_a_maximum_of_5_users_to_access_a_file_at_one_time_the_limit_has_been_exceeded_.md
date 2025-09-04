---
title: Error 7075 The Advantage Local Server Version Allows A Maximum Of 5 Users To Access A File At One Time The Limit Has Been Exceeded
slug: error_7075_the_advantage_local_server_version_allows_a_maximum_of_5_users_to_access_a_file_at_one_time_the_limit_has_been_exceeded_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7075_the_advantage_local_server_version_allows_a_maximum_of_5_users_to_access_a_file_at_one_time_the_limit_has_been_exceeded_.htm
source: Advantage CHM
tags:
  - error
checksum: 268689e3ca075a39aa7b5d732babceca9e72843a
---

# Error 7075 The Advantage Local Server Version Allows A Maximum Of 5 Users To Access A File At One Time The Limit Has Been Exceeded

7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time.

7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time. The limit has been exceeded.

Advantage Error Guide

| 7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time. The limit has been exceeded.  Advantage Error Guide |  |  |  |  |

Problem: The maximum of five (5) licensed users for Advantage Local Server has been exceeded.

Solution 1: A maximum of five concurrent users are allowed to access the Advantage Local Server. Have any users not currently using the Advantage Local Server logout to allow access by another user. To allow more than five concurrent users, contact your Advantage Database Server reseller to expand the number of concurrent users.

Solution 2: If an application does not terminate properly and close each table it has open, the tables it had open may be left with an incorrect open count. To resolve this problem, either open and close the table from the same workstation as the application improperly terminated, or open the table exclusively from any workstation to reset the open count to one.
