---
title: Ace Adsgetrecordcrc
slug: ace_adsgetrecordcrc
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetrecordcrc.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 10ef4a540c872622993a713eb39f8709d02ad475
---

# Ace Adsgetrecordcrc

AdsGetRecordCRC

AdsGetRecordCRC

Advantage Client Engine

| AdsGetRecordCRC  Advantage Client Engine |  |  |  |  |

Calculates a 32-bit CRC value using the current record.

Syntax

| UNSIGNED32 | AdsGetRecordCRC (ADSHANDLE hObj, UNSIGNED32 \*pulCRC, UNSIGNED32 ulOptions) |

Parameters

| hObj (I) | Handle of a table or cursor. |
| pulCRC (O) | Pointer to a 32-bit unsigned integer that will hold the CRC value. |
| ulOptions (I) | Options. |

Remarks

AdsGetRecordCRC calculates a 32-bit CRC value using the current record data, including all memo and blob data.

Two options flags are supported and can be passed in the ulOptions parameter:

- ADS\_DEFAULT

- ADS\_CRC\_LOCALLY

If the ADS\_CRC\_LOCALLY option is passed, the CRC will be calculated on the client. If the record contains memo and/or blob data, this data will be read over to the client in order to calculate the CRC value. If there is a substantial amount of memo/blob data this operation can be time consuming.

If the ADS\_DEFAULT option is passed, the API will make a decision on whether to calculate the CRC locally, or to send a server request to calculate the CRC. If the table does not contain any memos or blobs, the CRC will be calculated locally, which can increase performance.
