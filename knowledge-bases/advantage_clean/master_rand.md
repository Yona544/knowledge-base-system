---
title: Master Rand
slug: master_rand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_rand.htm
source: Advantage CHM
tags:
  - master
checksum: c6c8dad454202f6824dccf23de7d950b7f04138f
---

# Master Rand

RAND()

RAND()

Advantage Concepts

| RAND()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a pseudo-random number.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

RAND( [<nSeed>] ) à SyntaxRetPH

Parameters

| <nSeed> | Optional integer seed value for the random number generator. |

Return Value

Pseudo-random number between 0 and 1.

Remarks

Returns a pseudo-random floating point value between 0 and 1 using <nSeed> as an optional seed value. If zero is specified as the seed value, the current time in milliseconds is used as the seed. Seeding RAND() is not required and RAND() should only be seeded once for the life of the connection. Seeding RAND() multiple times on the same connection can result in poor random number generation.
