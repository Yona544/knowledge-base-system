The Advantage Proprietary (ADT) Format




Advantage Database Server 12  

     The Advantage Proprietary (ADT) Format

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The Advantage Proprietary (ADT) Format  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      The Advantage Proprietary (ADT) Format Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_The\_Advantage\_Proprietary\_ADT\_Format Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > The Advantage Proprietary (ADT) Format / Dear Support Staff, |  |
| The Advantage Proprietary (ADT) Format  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As noted in the preceding section, the traditional DBF format has well-documented limitations, making its use less attractive than many of the alternatives available today. In response to these limitations, the Advantage team introduced a new, proprietary format in 1998. This format is referred to as the ADT format.

Tables of the ADT format employ the .adt file extension, with the associated memo file and structural index having the same filename, but with the .adm and .adi file extensions, respectively. Among the enhancements introduced with the ADT format are long field names, superior memo file space utilization, improved index options, many more field types (19 in all), and more flexible table structures. Also, whereas FoxPro and Clipper field names are limited to alpha characters, 09, and underscore (\_), ADS table field names can include all but null values, semicolons, and commas.

Table 2-1 lists some of the basic ADT table specifications. For more information, refer to the Advantage documentation, which is available with the Advantage Database Server (see Appendix A) or at the Advantage Developer Zone Web site at:

http://devzone.advantagedatabase.com/