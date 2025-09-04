---
title: Master Math Functions
slug: master_math_functions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_math_functions.htm
source: Advantage CHM
tags:
  - master
checksum: 12c1cb92d0da7f653fb748e7665dfaff9d0f9ac6
---

# Master Math Functions

Math Functions

Math Functions

Advantage SQL Engine

| Math Functions  Advantage SQL Engine |  |  |  |  |

num = Expression or literal resulting in a numeric value.

float = Expression or literal resulting in a floating point value.

int = Expression or literal resulting in a integer value.

 

| [ABS](master_abs.md)( num ) | Returns the absolute value of a numeric. |
| [ACOS](master_acos.md)( float ) | Returns the arc cosine of float as an angle, expressed in radians. |
| [ASIN](master_asin.md)( float ) | Returns the arc sine of float as an angle, expressed in radians. |
| [ATAN](master_atan.md)( float ) | Returns the arc tangent of float as an angle, expressed in radians. |
| [ATAN2](master_atan2.md)( float1, float2 ) | Returns the arc tangent of the x and y coordinates, specified by float1 and float2, as an angle, expressed in radians. |
| [CEILING](master_ceiling.md)( num ) | Returns the smallest integer greater than or equal to num. The return value is of the same data type as the input parameter. |
| [COS](master_cos.md)( float ) | Returns the cosine of float, where float is an angle expressed in radians. |
| [COT](master_cot.md)( float ) | Returns the cotangent of float, where float is an angle expressed in radians. |
| [DEGREES](master_degrees.md)( num ) | Returns the number of degrees converted from radians. |
| [EXP](master_exp.md)( float ) | Returns the exponential value of float. |
| [FLOOR](master_floor.md)( num ) | Returns the largest integer less than or equal to num. The return value is of the same data type as the input parameter. |
| [LOG](master_log.md)( float ) | Returns the natural logarithm of float. |
| [LOG10](master_log10.md)( float ) | Returns the base 10 logarithm of float. |
| [MOD](master_mod.md)( int1, int2 ) | Returns the modulus (remainder) of int1 divided by int2. |
| [PI](master_pi.md)( ) | Returns the value of pi as a floating point value constant. |
| [POWER](master_power.md)( num, int ) | Returns the value of num raised to the power of int. |
| [RADIANS](master_radians.md)( num ) | Returns the number of radians converted from degrees. |
| [RAND](master_rand.md)( [int] ) | Returns a pseudo-random floating point value between 0 and 1 using int as an optional seed value. If zero is specified as the seed value, the current time in milliseconds is used as the seed. Seeding RAND() is not required and RAND() should only be seeded once for the life of the connection. Seeding RAND() multiple times on the same connection can result in poor random number generation. |
| [ROUND](master_round.md)( num, int ) | Returns num rounded to int places to the right of the decimal point. If int is negative, num is rounded to ABS(int) places to the left of the decimal point. |
| [SIGN](master_sign.md)( num ) | If num is less than zero, 1 is returned. If num equals zero, 0 is returned. If num is greater than zero, 1 is returned. |
| [SIN](master_sin.md)( float ) | Returns the sine of the float expression, where float is an angle expressed in radians. |
| [SQRT](master_sqrt.md)( float ) | Returns the square root of float. |
| [TAN](master_tan.md)( float ) | Returns the tangent of float, where float is an angle expressed in radians. |
| [TRUNCATE](master_truncate.md)( num, int ) | Returns num truncated to int places to the right of the decimal point. If int is negative, num is truncated to ABS(int) places to the left of the decimal point. |

See Also

[Supported Scalar Functions](master_supported_scalar_functions.md)

[String Functions](master_string_functions.md)

[Date/Time Functions](master_date_time_functions.md)

[Miscellaneous Functions](master_miscellaneous_functions.md)
