---
title: Devguide Impressive Backwards Compatibility
slug: devguide_impressive_backwards_compatibility
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_impressive_backwards_compatibility.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 7043700e89a806bb0f69a7c4aad0738ab78ac91c
---

# Devguide Impressive Backwards Compatibility

Impressive Backwards Compatibility

     Impressive Backwards Compatibility

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Impressive Backwards Compatibility  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you have existing Advantage 7.x applications already deployed, you will be pleased to learn that Advantage 8 is largely backwards compatible with 7.x clients. In other words, you do not necessarily have to recompile and redeploy all of your existing applications before you can upgrade to Advantage 8.

For most applications, this means that you can deploy the ADS 8.1 server and then immediately begin to use some of its new features, such as online backup. Then, as time permits, you can update your client applications to take advantage of additional Advantage 8 features, such encrypted indexes.

However, due to the nature of some of the enhancements added to Advantage 8.0 and 8.1, there are some specific instances where upgrading from Advantage 7.x also requires modifications to your client applications. For example, Advantage 8 adds a number of new SQL reserved keywords, including CURSOR, DECLARE, and SAVEPOINT, to name a few. Any existing SQL statements in your client applications that use one of these new reserved keywords as an unquoted field reference must be modified. Similarly, parameters are passed to SQL scripts differently in 7.x and 8. If you used parameters in 7.x SQL scripts, you will probably need to change your applications to reflect the new usage.

Nonetheless, the compatibility between 7.x client and Advantage 8 is remarkable. We recently assisted a client in upgrading from ADS 7.1 to ADS 8 on a production application. The entire process took less than ten minutes, and all client applications, compiled using an Advantage 7.1 driver, restarted without a hiccup.
