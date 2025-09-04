---
title: Error 5205 Ae Not Vfp Nullable Field
slug: error_5205_ae_not_vfp_nullable_field
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5205_ae_not_vfp_nullable_field.htm
source: Advantage CHM
tags:
  - error
checksum: 207b5fa92760e56b536d3067b07f8e28a2155998
---

# Error 5205 Ae Not Vfp Nullable Field

5205 AE\_NOT\_VFP\_NULLABLE\_FIELD

5205 AE\_NOT\_VFP\_NULLABLE\_FIELD

Advantage Error Guide

| 5205 AE\_NOT\_VFP\_NULLABLE\_FIELD  Advantage Error Guide |  |  |  |  |

Problem: An operation was performed that requires a nullable field. For example, this error can occur if AdsSetNull is called for a field that cannot be set to NULL. This error may also occur when executing an UPDATE or INSERT statement with a NUL parameter that results in an attempt to set a Visual FoxPro field to NULL. For example, using the Advantage Client Engine API AdsSetEmpty on an SQL parameter will cause a NULL value to be used.

Solution: Verify that the application is specifying the correct field. If necessary, restructure the Visual FoxPro table so that the field can be set to NULL.
