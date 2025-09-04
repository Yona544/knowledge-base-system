---
title: Master Cast
slug: master_cast
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_cast.htm
source: Advantage CHM
tags:
  - master
checksum: 9ff256b7a51c62b8dc9ea80f233eaa1c446969fb
---

# Master Cast

CAST()

CAST ()

Advantage Concepts

| CAST ()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to convert a value from one type to another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CAST ( <expr> AS data-type [( <precision> [, <scale> ] ) ] ) à result

Parameters

| <expr> | The value to convert |
| data-type | SQL\_BINARY, SQL\_VARBINARY, SQL\_BIT (logical), SQL\_LONGVARCHAR, SQL\_VARCHAR, SQL\_CHAR, SQL\_WLONGVARCHAR, SQL\_WVARCHAR, SQL\_WCHAR, SQL\_DATE, SQL\_NUMERIC, SQL\_DOUBLE, SQL\_INTEGER, SQL\_TIMESTAMP, SQL\_TIME, or SQL\_MONEY |
| <precision> | Optional precision for numeric conversion |
| <scale> | Optional scale for numeric conversion |

Return Value

This function returns <expr> convert to a value of the specified data type.

Remarks

Only SQL\_BINARY, SQL\_VARBINARY, SQL\_VARCHAR, SQL\_CHAR, and SQL\_NUMERIC support the precision parameter and only SQL\_NUMERIC supports the scale parameter.

See Also

[CONVERT()](master_convert.md)

[STR()](master_str.md)

[VAL()](master_val.md)
