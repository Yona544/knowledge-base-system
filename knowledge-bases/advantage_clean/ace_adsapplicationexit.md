---
title: Ace Adsapplicationexit
slug: ace_adsapplicationexit
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsapplicationexit.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5d7b1f15cf2dc9d92aff6b847fd0fa93e2c9888b
---

# Ace Adsapplicationexit

AdsApplicationExit

AdsApplicationExit

Advantage Client Engine

| AdsApplicationExit  Advantage Client Engine |  |  |  |  |

Closes all tables and cleans up all open Advantage connections

Syntax

| UNSIGNED32 | AdsApplicationExit (); |

Parameters

None.

Remarks

AdsApplicationExit is used to ensure the Advantage Client Engine is unloaded completely and cleanly, and that all open indexes, tables, and connections are closed. Calling this function will roll back any open transactions.

Call AdsApplicationExit when exiting an application and all function calls into the Advantage Client Engine are complete.

Example

[Click Here](ace_examples.md#adsapplicationexitexample)

See Also

[AdsThreadExit](ace_adsthreadexit.md)
