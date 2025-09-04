---
title: Ace Adssetdateformat
slug: ace_adssetdateformat
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetdateformat.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7fc4b37d6398c406c64c169b3af8d98e3d747e15
---

# Ace Adssetdateformat

AdsSetDateFormat

AdsSetDateFormat

Advantage Client Engine

| AdsSetDateFormat  Advantage Client Engine |  |  |  |  |

Specifies the date format for dates represented as character strings

Syntax

| UNSIGNED32 | AdsSetDateFormat (UNSIGNED8 \*pucFormat); |

Parameters

| pucFormat (I) | Specifies the date format to be set. The date format must contain two or more occurrences of the letters D, M, and Y respectively (e.g., "MMDDYYYY"). The default value is "MM/DD/YYYY". |

Remarks

AdsSetDateFormat analyzes the format specified by pucFormat and determines the placement as well as the correct number of digits for the day, month, and year.

AdsSetDateFormat is a global setting that affects the behavior of the entire application. This allows control of date formatting for applications being used internationally.

This setting affects how the Advantage Client Engine interprets all date strings passed to the Advantage Client Engine from the calling application. It also defines how the Advantage Client Engine formats all dates passed back from the Advantage Client Engine to the calling application. AdsSetDateFormat can also be used to specify separators in the date format. For example, "DD/MM/YYYY" and "DD-MM-YYYY" are both valid date formats.

Example

[Click Here](ace_examples.md#adssetdateformatexample)

See Also

[AdsGetDateFormat](ace_adsgetdateformat.md)

[AdsGetDate](ace_adsgetdate.md)

[AdsGetField](ace_adsgetfield.md)

[AdsSetField](ace_adssetfield.md)

[AdsSeek](ace_adsseek.md)

[AdsSetScope](ace_adssetscope.md)

[AdsSetDate](ace_adssetdate.md)

[AdsSetDateFormat60](ace_adssetdateformat60.md)

[AdsSetEpoch](ace_adssetepoch.md)
