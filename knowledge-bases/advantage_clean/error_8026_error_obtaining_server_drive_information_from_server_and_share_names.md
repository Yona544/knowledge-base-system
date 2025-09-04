---
title: Error 8026 Error Obtaining Server Drive Information From Server And Share Names
slug: error_8026_error_obtaining_server_drive_information_from_server_and_share_names
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_8026_error_obtaining_server_drive_information_from_server_and_share_names.htm
source: Advantage CHM
tags:
  - error
checksum: 3e40f32554835059768a13bb81c62ff513430284
---

# Error 8026 Error Obtaining Server Drive Information From Server And Share Names

8026 Error obtaining server drive information from server and share names

8026 Error obtaining server drive information from server and share names

Advantage Error Guide

| 8026 Error obtaining server drive information from server and share names  Advantage Error Guide |  |  |  |  |

Possible Problem: This error can sometimes occur when using [server-side aliases](master_server_side_aliases.md). For example, if you use a server-side alias like:

myalias=c:\test\_drive\data\orders

and connect to this database using the connection string \\servername\myalias\order\_db.add.

If the order\_db database specifies a relative path to any files (temp file path, index file paths, etc), and if that path is "behind" the .add file (for example, "..\tempdir"), you will receive an 8026 error.

Solution: Modify the alias path so it includes any portions of the path that will be required to convert relative paths stored in the data dictionary. In the example above, the alias can be converted to:

myalias=c:\test\_drive\data

and the connection path can be changed to \\servername\myalias\orders\order\_db.add

Errors in the 8000 range are returned when the Advantage server makes a direct call to an OS API, and that function returns a failure. If you receive an error in the 8000 range, retry the database operation. If the error condition persists, please send a small re-creation to Advantage [Technical Support](master_technical_support_u_s__and_canada.md) demonstrating the problem so that Advantage R&D can investigate the issue.
