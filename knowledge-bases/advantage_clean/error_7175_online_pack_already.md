---
title: Error 7175 Online Pack Already
slug: error_7175_online_pack_already
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7175_online_pack_already.htm
source: Advantage CHM
tags:
  - error
checksum: 0d39e97223efc0bcc7fdeff77a07e35fe69a110d
---

# Error 7175 Online Pack Already

7175 Online Pack Already Active

7175 Online Pack Already Active

Advantage Error Guide

| 7175 Online Pack Already Active  Advantage Error Guide |  |  |  |  |

Problem: An online pack operation was already active on a table when another online pack operation was requested on the same table.

Solution1: Allow the previous online pack operation to finish before attempting to pack the same table again.

Solution2: Cancel the active online pack operation before attempting to pack the same table again.  Consider specifying a timeout value in the sp\_PackTableOnline call if the operation is taking too long.
