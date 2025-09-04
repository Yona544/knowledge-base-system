---
title: Devguide Advantage Ansi Collation Utility
slug: devguide_advantage_ansi_collation_utility
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_advantage_ansi_collation_utility.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6625e1766d7b76ec1f2dc6659940f8a0c08a93d5
---

# Devguide Advantage Ansi Collation Utility

Advantage ANSI Collation Utility

     Advantage ANSI Collation Utility

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Advantage ANSI Collation Utility  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Data Architect ships with the Advantage ANSI Collation Utility, shown in Figure 1-12, a tool that permits you to create custom ANSI collations. The ANSI (American National Standards Institute) character set is a standard mapping of characters to numeric values. These characters include printable characters and special control characters, such as tabs and carriage returns. An ANSI collation sequence defines the order, or precedence, of characters for the purpose of making string comparisons.

Figure 1-12: The Advantage ANSI Collation Utility

To access the Advantage ANSI Collation Utility, run ANSICHR.EXE, which is located in the same directory in which the Advantage Data Architect is located. By default, this directory is c:\Program Files\Extended Systems\Advantage 8.1\ARC.

Few developers will ever need to use the Advantage ANSI Collation Utility. For most applications that use the English language, you will install one of the provided English collation sequences. Similarly, for most non-English applications, Sybase iAnywhere provides localized character sets that ensure proper string comparisons.

For those nonEnglish speaking developers for whom there is no localized character set, the Advantage ANSI Collation Utility is an essential tool for defining character precedence.

When installing ADS or ALS, you will choose either a localized character set or an ANSI collation sequence. Which options you have depend on the version of the Advantage Database Server that you are installing. For example, if you are installing the domestic version of ADS, you will be able to select only between an American English collation, a Canadian English collation, and a French Canadian collation.

Regardless of which character set or collation sequence you install, keep one very important issue in mind. The server and each of its client connections must use the same character set or collation sequence. Doing so ensures that the server and its clients agree on how strings are compared.

Because both client and server must use the same character set or ANSI collation sequence, it is particularly important for non-English applications to use the ANSI character set provided by Sybase iAnywhere, instead of choosing "default on machine." This is especially important for Advantage Local Server users. Each version of Windows (95, 98, NT, 2000, XP, and so on) has different "default on machine" ANSI collation sequences, even when the same language is configured. Consequently, if one ALS client is using Windows 98 and another is using Windows 2000, collation mismatch errors will result.

   
CAUTION: If you change the character set or collation sequence being used by your clients and server, you must rebuild all indexes before you access any of your tables.
