---
title: Master Sp Getcollations
slug: master_sp_getcollations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getcollations.htm
source: Advantage CHM
tags:
  - master
checksum: 62bba0d8767e47da18633c95516f013d9e5ed7dd
---

# Master Sp Getcollations

sp\_GetCollations

sp\_GetCollations

Advantage SQL Engine

| sp\_GetCollations  Advantage SQL Engine |  |  |  |  |

Retrieve the list of collations that can be loaded dynamically.

Syntax

sp\_GetCollations( Pattern,CICHARACTER,100 )

Parameters

| Pattern (I) | Name pattern that can be used to restrict the result set. For example, if the parameter is general%, all of the collations beginning with the word general would be returned. If an empty string or NULL is given, all collations are returned. |

Output

The sp\_GetCollations procedure will return a result set containing information about available dynamic collations.

| Field Name | Field Type | Field Size | Description |
| Name | CiCharacter | 100 | The collation name. This is the name that should be supplied by the Advantage client either as part of the connection string or as a parameter to ACE functions. A Unicode collation locale name may be appended with '\_ADS\_CI' to denote a case insensitive collation. |
| ShortName | CiCharacter | 8 | The short collation name. For ANSI/OEM collations, this is the name that is used directly in Visual FoxPro. For Unicode collations, this is the language of the collation. |
| Description | Memo | 9 | A text description of the collation. |
| Version | Integer | 4 | The version number of the collation table. |
| CodePage | Integer | 4 | The code page with which the collation table is associated. Rows with CodePage=1202 are Unicode collation locales. |
| FoxCompat | Logical | 1 | Flag indicating if the collation is a Visual FoxPro compatible collation. |
| UnicodeLocale | Character | 16 | Default Unicode collation locale for the corresponding ANSI/OEM collation. |
| AllowMultiple | Logical | 1 | Flag that indicates whether the collation table can be used at the same time as other collation tables on a given DBF or ADT table. |

Remarks

sp\_GetCollations retrieves the list of collations that are currently available for dynamic loading by Advantage Database Server or Advantage Local Server. The ANSI/OEM collations that are returned are the ones currently in the adscollate.adt table. The Unicode collations associated with code page 1202 are dynamically retrieved from aicu32/64.dll. Normally, applications would not need to use this procedure unless it was desired to present a list of collations to the user to choose from.

When supplying a collation name as part of a connection string or a parameter to a call to ACE, the Unicode collation name should follow the ANSI/OEM collation name with a colon : separating the two parts. The following are examples of valid collation specifications: CZECH\_VFP\_CI\_AS\_1250, CZECH\_VFP\_CI\_AS\_1250:en\_US, and :ar\_IQ\_ADS\_CI (note the final example does not specify an ANSI/OEM collation, but can still provide a Unicode locale by starting the specification with a colon character).

Example

The following example will retrieve all available collation tables:

EXECUTE PROCEDURE sp\_GetCollations( NULL );

The next example will retrieve all available Spanish collations:

EXECUTE PROCEDURE sp\_GetCollations( Spanish% );

See Also

[sp\_GetCollationTable](master_sp_getcollationtable.md)

[Dynamic Collation Support](master_collation_support.md)
