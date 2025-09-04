---
title: Error 7107 The Client S Memo Data Is Out Of Sync With The Server
slug: error_7107_the_client_s_memo_data_is_out_of_sync_with_the_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7107_the_client_s_memo_data_is_out_of_sync_with_the_server.htm
source: Advantage CHM
tags:
  - error
checksum: 9b6ac2d7cb5e422ce0d472a5b1a15d94d1d9f9ab
---

# Error 7107 The Client S Memo Data Is Out Of Sync With The Server

7107 The client's memo data is out of sync with the server

7107 The client's memo data is out of sync with the server

Advantage Error Guide

| 7107 The client's memo data is out of sync with the server  Advantage Error Guide |  |  |  |  |

Problem: Advantage server detected a mismatch between the client's expected memo or blob data length and the amount of actual available data. This error is possible with the Advantage thin clients, such as JDBC driver, when live/updateable result set (cursor) is used.

Solution: Refresh the client's record data after receiving this error to make it in sync with the server. To avoid this error, use static cursor.
