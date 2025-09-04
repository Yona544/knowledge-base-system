---
title: Devguide The Advantage Proprietary Adt Format
slug: devguide_the_advantage_proprietary_adt_format
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_advantage_proprietary_adt_format.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2772c53a80b9410d921eb5a231e3fbbd3bbb694d
---

# Devguide The Advantage Proprietary Adt Format

The Advantage Proprietary (ADT) Format

     The Advantage Proprietary (ADT) Format

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The Advantage Proprietary (ADT) Format  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As noted in the preceding section, the traditional DBF format has well-documented limitations, making its use less attractive than many of the alternatives available today. In response to these limitations, the Advantage team introduced a new, proprietary format in 1998. This format is referred to as the ADT format.

Tables of the ADT format employ the .adt file extension, with the associated memo file and structural index having the same filename, but with the .adm and .adi file extensions, respectively. Among the enhancements introduced with the ADT format are long field names, superior memo file space utilization, improved index options, many more field types (19 in all), and more flexible table structures. Also, whereas FoxPro and Clipper field names are limited to alpha characters, 09, and underscore (\_), ADS table field names can include all but null values, semicolons, and commas.

Table 2-1 lists some of the basic ADT table specifications. For more information, refer to the Advantage documentation, which is available with the Advantage Database Server (see Appendix A) or at the Advantage Developer Zone Web site at:

http://devzone.advantagedatabase.com/
