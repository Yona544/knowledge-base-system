---
title: Devguide Basic Replication Strategies
slug: devguide_basic_replication_strategies
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_basic_replication_strategies.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6402d54c766beb45c92044cda29dc113b4b47941
---

# Devguide Basic Replication Strategies

Basic Replication Strategies

 

     Basic Replication Strategies

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Basic Replication Strategies  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Replication can be quite simple or it can be complex. Which it will be depends on the goal you are attempting to achieve through replication.

If you are simply trying to maintain an up-to-date, offsite copy of your records, replication is pretty simple. On the other hand, if you are trying to coordinate updates from multiple satellite databases while maintaining a master central database, the architecture can be pretty complex.

In most cases, however, replication strategies can be reduced down to three basic architectures. These are unidirectional, bi-directional, and spoke and hub.

While these three approaches represent alternative ways of configuring replication, they are not mutually exclusive. Specifically, based on your needs, your replication strategy might employ a combination of two or all three of these strategies.

Nonetheless, each of these strategies represents a combination of requirements and benefits. As a result, each of them will be considered separately in the following sections.
