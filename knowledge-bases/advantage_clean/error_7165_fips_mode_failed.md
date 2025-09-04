---
title: Error 7165 Fips Mode Failed
slug: error_7165_fips_mode_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7165_fips_mode_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 7ed86cc6999b7b54beb1e10dcfc331b8087e083a
---

# Error 7165 Fips Mode Failed

7165 FIPS Mode Failed

7165 FIPS Mode Failed

Advantage Error Guide

| 7165 FIPS Mode Failed  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to enable [FIPS mode](master_fips.md) when starting up.

Solution: If FIPS mode is not desired, verify that the [FIPS configuration parameter](master_fips_config.md) is not specified with a value of 1. If FIPS mode is desired, check the error log for more detailed information on the exact nature of the error.

The OpenSSL libraries are required in order to use FIPS mode. If there was an error loading the libraries, the error log should have a [7160](error_7160_unable_to_load_ssl.md), [7161](error_7161_unable_to_verify_si.md), [7162](error_7162_unable_to_load_ssl_.md) error that may indicate why they could not be loaded.

It is also possible for the internal FIPS mode verification performed at startup to fail. If this happened, the error log should contain additional information.
