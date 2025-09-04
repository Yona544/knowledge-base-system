ADS Supported Table Types




Advantage Database Server 12  

 

     ADS Supported Table Types

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS Supported Table Types  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       ADS Supported Table Types Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_ADS\_Supported\_Table\_Types Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > ADS Supported Table Types / Dear Support Staff, |  |
| ADS Supported Table Types  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Database Server supports three different table formats: Clipper and FoxPro DBF formats (compatible with dBASE III + format), and a proprietary ADT format. The two DBF formats are useful for developers who want to maintain backward compatibility with legacy applications, particularly those still running in DOS. In this book, the Advantage-supported formats are referred to collectively as Advantage tables.

The ADT format, on the other hand, is the preferred Advantage format for Advantage-based applications that no longer need to maintain backward compatibility. This is because the ADT format provides superior features, flexibility, and performance.

While there are still quite a few legacy Clipper and FoxPro applications out there that can benefit from the stability and performance offered by Advantage, most developers using ADS should use the ADT format if at all possible.