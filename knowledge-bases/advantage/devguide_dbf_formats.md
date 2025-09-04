DBF Formats




Advantage Database Server 12  

     DBF Formats

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DBF Formats  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      DBF Formats Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_DBF\_Formats Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > DBF Formats / Dear Support Staff, |  |
| DBF Formats  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

DBF format databases employ tables in DBF format. These tables use indexes in either FoxPro IDX or CDX formats, or the Clipper NTX format. Similarly, memo fields employ the FPT (FoxPro) and DBT (Clipper) memo field files. Because the index and memo files are associated with either FoxPro or Clipper, which format you use depends on the Advantage driver you are employing. For example, you use the Advantage NTX driver to create and work with NTX indexes. By comparison, you use the Advantage CDX driver to use IDX and CDX indexes.

Both the FoxPro and Clipper formats have well-known characteristics and limitations. For example, the maximum field name length is 10 characters, deleted records are merely marked for deletion and can still be accessed up until a table is packed, unique indexes do not enforce record uniqueness, and memo files can include large amounts of wasted space.

In short, except for legacy application support, the use of the DBF file formats is discouraged. In fact, if you are building a new application with no need for backward compatibility with existing Clipper or FoxPro applications, you are much better off using the Advantage proprietary format. For more information on Clipper and FoxPro DBF formats, including their characteristics, refer to the Advantage help or a third-party book on Clipper or FoxPro.