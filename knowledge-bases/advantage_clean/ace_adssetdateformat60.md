---
title: Ace Adssetdateformat60
slug: ace_adssetdateformat60
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetdateformat60.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f2be2acf38ee11512490c3aa3a7cbb233b9be677
---

# Ace Adssetdateformat60

AdsSetDateFormat60

AdsSetDateFormat60

Advantage Client Engine

| AdsSetDateFormat60  Advantage Client Engine |  |  |  |  |

Specifies the date format for dates represented as character strings for a given connection.

Syntax

| UNSIGNED32 | AdsSetDateFormat60( ADSHANDLE hConn, UNSIGNED8 \*pucFormat ); |

Parameters

| hConn (I) | Handle of connection to set the date format on. If this is 0, it is the same as calling [AdsSetDateFormat](ace_adssetdateformat.md). |
| pucFormat (I) | Specifies the date format to be set. The date format must contain two or more occurrences of the letters D, M, and Y respectively (e.g., "MMDDYYYY"). The default value is "MM/DD/YYYY". |

Remarks

AdsSetDateFormat60 can be used to set the date format for a specific connection. This setting affects how the Advantage Client Engine interprets date strings passed to the Advantage Client Engine from the calling application. It also defines how the Advantage Client Engine formats dates passed back from the Advantage Client Engine to the calling application. AdsSetDateFormat60 can be used to specify separators in the date format. For example, "DD/MM/YYYY" and "YYYY-MM-DD" are both valid date formats.

See Also

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsGetDateFormat60](ace_adsgetdateformat60.md)

[AdsSetEpoch](ace_adssetepoch.md)

[AdsGetDate](ace_adsgetdate.md)

[AdsGetField](ace_adsgetfield.md)

[AdsSetField](ace_adssetfield.md)

[AdsSeek](ace_adsseek.md)

[AdsSetScope](ace_adssetscope.md)

[AdsSetDate](ace_adssetdate.md)
