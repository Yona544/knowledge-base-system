---
title: Devguide Administrative Operations With Ads And Ado Net
slug: devguide_administrative_operations_with_ads_and_ado_net
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_administrative_operations_with_ads_and_ado_net.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 325e6acca76ef6e28a7bac7563976ca1778a0a35
---

# Devguide Administrative Operations With Ads And Ado Net

Administrative Operations with ADS and ADO.NET

     Administrative Operations with ADS and ADO.NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Administrative Operations with ADS and ADO.NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While Advantage requires little in the way of periodic maintenance to keep it running smoothly, many applications need to provide administrative functionality related to the management of users, groups, and objects.

This section is designed to provide you with insight into exposing administrative functions in your client applications. Two related, yet different, operations are demonstrated here. In the first, a new table is added to the database and all groups are granted access rights to it. This operation requires that you establish an administrative connection (or a connection from a user account with GRANT privileges). The second operation involves permitting individual users to modify their own passwords. Especially in the security-conscious world of modern database management, this feature is often considered an essential step to protecting data.
