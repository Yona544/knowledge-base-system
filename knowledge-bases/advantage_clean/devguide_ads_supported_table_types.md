---
title: Devguide Ads Supported Table Types
slug: devguide_ads_supported_table_types
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_ads_supported_table_types.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c6e43367d9ccedbad0d37c4d18266684bd5c3026
---

# Devguide Ads Supported Table Types

ADS Supported Table Types

 

     ADS Supported Table Types

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| ADS Supported Table Types  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Database Server supports three different table formats: Clipper and FoxPro DBF formats (compatible with dBASE III + format), and a proprietary ADT format. The two DBF formats are useful for developers who want to maintain backward compatibility with legacy applications, particularly those still running in DOS. In this book, the Advantage-supported formats are referred to collectively as Advantage tables.

The ADT format, on the other hand, is the preferred Advantage format for Advantage-based applications that no longer need to maintain backward compatibility. This is because the ADT format provides superior features, flexibility, and performance.

While there are still quite a few legacy Clipper and FoxPro applications out there that can benefit from the stability and performance offered by Advantage, most developers using ADS should use the ADT format if at all possible.
