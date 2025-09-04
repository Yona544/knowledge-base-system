Unicode Support




Advantage Database Server 12  

Unicode Support

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Unicode Support  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Unicode Support Advantage Database Server master\_Unicode\_Support Advantage Concepts > Advantage Functionality > Unicode Support / Dear Support Staff, |  |
| Unicode Support  Advantage Database Server |  |  |  |  |

Beginning with version 10, processing of Unicode character text is supported by the Advantage Windows and Linux servers and all Advantage clients. Unicode character data can be stored in three new field types, NCHAR, NVARCHAR and NMEMO. These new field types are available in all table types supported by the Advantage. There are new APIs in the Advantage Client Engine allowing reading and writing Unicode text directly using UTF16 encoding. Unicode characters can also be supplied directly in SQL statements and filter expression. Unicode columns may be sorted or indexed using various collation locales. See [Collation Support](master_collation_support.htm) for additional information on Unicode collations.

The Unicode characters stored on disk and represented internally are UTF-16LE encoded.

Unicode collation and searching capability is supplied through a customized dynamically loaded library that is based on the open source ICU components (<http://site.icu-project.org/>). To fully enable Unicode processing in an Advantage application, the files aicu32/64.dll in Windows or aicu.so in Linux, and icudt40l.dat must be deployed with both the server and the client.

For applications that do not use Unicode field types, it is not necessary to distribute the aicu.dll and icudt40l.dat files. Most Advantage Windows development environments, such as ODBC, OLE DB and ADO.NET, and Delphi 2010 now use Unicode natively. When a conversion from Unicode characters to code page characters is needed, Advantage will use Windows APIs to perform the conversion so the ICU library is not required. However, if the application receives Unicode input that cannot be converted into code page characters, then the ICU library must be present to avoid errors. For example, consider an application that uses input from the user to construct the following filter expression:  lastname > '黄', where 黄is a Chinese character that cannot be converted into a code page string. Even though the lastname column is not a Unicode column, the ICU library is still required to evaluate this comparison expression.