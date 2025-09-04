---
title: Devguide Administrative Operations With Ads And Java
slug: devguide_administrative_operations_with_ads_and_java
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_administrative_operations_with_ads_and_java.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 880b84939dea930b855b39593253525f09e2dad9
---

# Devguide Administrative Operations With Ads And Java

Administrative Operations with ADS and Java

     Administrative Operations with ADS and Java

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Administrative Operations with ADS and Java  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While ADS requires little in the way of periodic maintenance to keep it running smoothly, many applications need to provide administrative functionality related to the management of users, groups, and other objects.

This section is designed to provide you with insight into exposing administrative functions in your client applications. Two related, yet different, operations are demonstrated here. In the first, a new table is added to the database and all groups are granted access rights to it. This operation requires that you establish an administrative connection, or a user connection with the appropriate GRANT rights. The second operation involves permitting individual users to modify their own passwords. Especially in the security-conscious world of modern database management, this feature is often considered an essential step to protecting data.
