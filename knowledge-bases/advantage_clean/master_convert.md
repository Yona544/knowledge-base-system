---
title: Master Convert
slug: master_convert
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_convert.htm
source: Advantage CHM
tags:
  - master
checksum: 634e5a4bed3ccd2112126e769e733150aa320c9c
---

# Master Convert

CONVERT()

CONVERT()

Advantage Concepts

| CONVERT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a value from one type to another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CONVERT( <expr>, data-type ) à result

Parameters

| <expr> | The value to convert |
| data-type | SQL\_BINARY, SQL\_VARBINARY, SQL\_BIT (logical), SQL\_LONGVARCHAR, SQL\_VARCHAR, SQL\_CHAR, SQL\_WLONGVARCHAR, SQL\_WVARCHAR, SQL\_WCHAR, SQL\_DATE, SQL\_DOUBLE, SQL\_INTEGER, SQL\_NUMERIC, SQL\_TIME, SQL\_TIMESTAMP, or SQL\_MONEY. |

Return Value

This function returns <expr> convert to a value of the specified data type.

See Also

[CAST()](master_cast.md)

[STR()](master_str.md)

[VAL()](master_val.md)
