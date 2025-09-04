---
title: Devguide Administrative Operations With Advantage And Delphi
slug: devguide_administrative_operations_with_advantage_and_delphi
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_administrative_operations_with_advantage_and_delphi.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: fa8b93cfae0c05465a1171c86fac95381d794e14
---

# Devguide Administrative Operations With Advantage And Delphi

Administrative Operations with Advantage and Delphi

     Administrative Operations with Advantage and Delphi

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Administrative Operations with Advantage and Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While Advantage requires little in the way of periodic maintenance to keep it running smoothly, many applications need to provide administrative functionality related to the management of users, groups, and objects.

This section is designed to provide you with insight into exposing administrative functions in your client applications. Two related, yet different, operations are demonstrated here. In the first, a new table is added to the database and all groups are granted access rights to it. This operation requires that you establish an administrative connection (or a user connection that has the appropriate WITH GRANT privileges).

The second operation involves permitting individual users to modify their own passwords. Especially in the security-conscious world of modern database management, this feature is often considered an essential step to protecting data.

Like many of the other operations described in this chapter, Delphi provides a variety of different means for implementing these features. An obvious solution is to use SQL queries to perform these tasks. This approach is demonstrated in other chapters in this part of the book, and in many of those cases represents the only mechanism available.

Since the SQL approach is shown elsewhere in Chapters 1618, the following sections demonstrate how to implement these operations using methods of the AdsTable, AdsConnection, and AdsDictionary components. While this approach is sometimes more involved than the SQL approach, it is nonetheless valuable in that it demonstrates the utility of the various TDataSet descendant components. If you prefer to use the SQL approach in your Delphi applications, refer to the SQL statements used in Chapters 16‑18.

   
NOTE: Although the AdsDictionary does enable you to perform the tasks we describe in this section, and we sincerely believe that it is interesting to know how this interface differs from the SQL-based interface, there is an additional reason to consider the SQL versions of these operations as presented in Chapters 1618. The AdsDictionary is deprecated. Some of the newest administrative operations in Advantage cannot be performed with the AdsDictionary. In order to perform these tasks, you will have to use SQL.
