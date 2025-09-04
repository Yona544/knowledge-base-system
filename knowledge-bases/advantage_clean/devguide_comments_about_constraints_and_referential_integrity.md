---
title: Devguide Comments About Constraints And Referential Integrity
slug: devguide_comments_about_constraints_and_referential_integrity
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_comments_about_constraints_and_referential_integrity.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c48f6b4baf043fa12f8b659e36243660d0ecae39
---

# Devguide Comments About Constraints And Referential Integrity

Comments About Constraints and Referential Integrity

 

     Comments About Constraints and Referential Integrity

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Comments About Constraints and Referential Integrity  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As pointed out at the beginning of this chapter, there are a number of benefits to constraints and referential integrity. They are easy to configure, all client applications must abide by them, and they can improve the overall integrity of your data.

But the ease with which constraints can be added to a data dictionary can lead to their overuse. When overused, they can prevent valid data from being entered into your database. And in the case of referential integrity constraints, they can produce an unexpected increase in resource use on the server.

The following sections take a final look at each of the types of constraints provided by a data dictionary. In each case, the limits of each approach are discussed.
