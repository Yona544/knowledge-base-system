---
title: Ace Adsgetdateformat
slug: ace_adsgetdateformat
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdateformat.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 79d3d6c40ec2eeac4a053bed38c10ce5fb04647c
---

# Ace Adsgetdateformat

AdsGetDateFormat

AdsGetDateFormat

Advantage Client Engine

| AdsGetDateFormat  Advantage Client Engine |  |  |  |  |

Retrieves the current date format

Syntax

| UNSIGNED32 | AdsGetDateFormat (UNSIGNED8 \*pucFormat,  UNSIGNED16 \*pusLen); |

Parameters

| pucFormat (O) | Contains the returned date format string. |
| pusLen (I/O) | Length of the buffer on input, amount of data stored on output. |

Remarks

AdsGetDateFormat returns the current date format or the date format defined by AdsSetDateFormat.

AdsGetDateFormat is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adsgetdateformatexample)

See Also

[AdsGetDate](ace_adsgetdate.md)

[AdsGetDateFormat60](ace_adsgetdateformat60.md)

[AdsGetEpoch](ace_adsgetepoch.md)

[AdsSetDate](ace_adssetdate.md)

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsSetDateFormat60](ace_adssetdateformat60.md)

[AdsSetEpoch](ace_adssetepoch.md)
