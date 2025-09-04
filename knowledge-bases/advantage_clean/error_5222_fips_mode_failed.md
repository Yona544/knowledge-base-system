---
title: Error 5222 Fips Mode Failed
slug: error_5222_fips_mode_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5222_fips_mode_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 4ce77729bf24c4cc2b89ee40d817eb68a4630451
---

# Error 5222 Fips Mode Failed

5222 FIPS Mode Failed

5222 FIPS Mode Failed

Advantage Error Guide

| 5222 FIPS Mode Failed  Advantage Error Guide |  |  |  |  |

Problem: The Advantage client was not able to enable [FIPS mode](master_fips.md) when starting up.

Solution: If FIPS mode is not desired, verify that the [FIPS connection option](ace_adsconnect101.md) is not specified. If FIPS mode is desired, the error text associated with this error should contain addition information on identifying the problem. The internal FIPS mode verification performed at startup may have failed.
