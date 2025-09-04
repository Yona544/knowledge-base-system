---
title: Error 5169 Ae Info Copy Made By Client
slug: error_5169_ae_info_copy_made_by_client
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5169_ae_info_copy_made_by_client.htm
source: Advantage CHM
tags:
  - error
checksum: 906327e0aa075057fbff685fdf879d06f6cd54ec
---

# Error 5169 Ae Info Copy Made By Client

5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT

5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT

Advantage Error Guide

| 5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT  Advantage Error Guide |  |  |  |  |

This is an informational error code that can be retrieved by using AdsGetLastError after a call to AdsCopyTable or AdsCopyTableContents. Should this error be retrieved after a call to either of these APIs it does NOT signify that the copy failed. Instead it means that the server could not carry out the copy and the operation had to be scaled back to the client in order to complete. The error string passed to AdsGetLastError will contain specifics as to why the operation had to scale back to the client when AdsGetLastError returns.
