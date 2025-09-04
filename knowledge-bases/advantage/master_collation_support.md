Collation Support




Advantage Database Server 12  

Collation Support

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Collation Support  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Collation Support Advantage Concepts master\_Collation\_support Advantage Concepts > Advantage Development Notes > Collation Support / Dear Support Staff, |  |
| Collation Support  Advantage Concepts |  |  |  |  |

Traditionally, Advantage has been able to use one collation at a time for ordering character data. With Advantage Database Server, a collation for ANSI character data and a collation for OEM character data are stamped into the server binary. These collations came from ansi.chr and extend.chr (for OEM character data). With Advantage Local Server, these collations are specified in the local server configuration file and are loaded at application startup. These are static collations because they cannot be changed at runtime. The character type specified with the table or SQL statement (ADS\_ANSI or ADS\_OEM) specifies if the ANSI collation is used or if the OEM collation is used. Note that ADT tables only use the ANSI collation.

Beginning with version 9.0, additional collation support has been added to provide compatibility with Visual FoxPro tables. These collations are loaded dynamically at runtime as they are needed, which provides for the ability for an application to switch between different collations as desired and for a single table to have indexes built with different collations. The dynamic collations can be used both with Visual FoxPro (VFP) tables and with Advantage Proprietary (ADT) tables.

Beginning with version 10.0, Unicode collation support has been added to provide sorting, indexing and comparing of Unicode character data based on a specific collation locale. The Unicode collation support is based on the open source components from the ICU project (<http://site.icu-project.org/>). The Unicode collations are loaded at runtime by the aicu32/64.dll or aicu.so libraries as needed. The Unicode collation is applied to Unicode data only and does not affect ANSI/OEM encoded character data. The supported Unicode collation locale names may be retrieved using the system procedure [sp\_GetCollations](master_sp_getcollations.htm). If a specific Unicode collation locale is not specified for the table or query, a default Unicode locale corresponding to the tables or querys ANSI/OEM collation will be used for Unicode characters. The default Unicode collation locale name for a supported ANSI/OEM collation may also be viewed using the [sp\_GetCollations](master_sp_getcollations.htm) procedure.

Using a different collation allows for data to be sorted according to the rules of a certain locale, and it allows for string comparisons (e.g., in filters, and SQL WHERE clauses) to match according to different rules. The static collations that are stamped into the server or specified in the local server configuration file provide a one-to-one mapping of characters to unique collation values. Each of the 256 character values maps to a different collation value. The dynamic collations provide for more flexibility in collation. For example, the German collation for code page 1252 (GERMAN\_VFP\_CI\_AS\_1252) accounts for expansion characters such as æ and ß, which will collate the same as the corresponding two-character sequences ae and ss. This means, for example, that the words Strasse and Straße are considered equivalent for comparison and sorting purposes (a filter with one of those values will find records containing either value). Also, contraction character sequences in collations such as SPANISH\_VFP\_CI\_AS\_850 are handled correctly. For example, the character pair ch is treated as a single collation element for sorting purposes (it collates between c and d).

In addition, accented characters are treated differently in some of the dynamic collations. The accented characters have unique collation values from the non-accented characters, but they are differentiated with secondary collation weights, which provides for a more logical sorting of data. For example, with a single-byte static collation, the following words would be sorted:

resume, resumes, resumé, resumés

A dynamic collation such as GENERAL\_VFP\_CI\_AS\_1252 will order the words as:

resume, resumé, resumes, resumés

Many of the new Visual FoxPro-compatible collations require two bytes of collation data per character. This means that an index built with one of these collations will take more space, although the extra space may not be significant because of the index compression techniques that are used.

The collation names provide information about the collation itself. They are based on the names used by Visual FoxPro with an appended \_VFP\_ in the name to indicate that it is compatible with Visual FoxPro. Collations with \_CI\_ in the name are case-insensitive; \_CS\_ indicates it is case-sensitive. If the name contains \_AS\_, the collation is accent sensitive, and \_AI\_ indicates it is accent-insensitive, although the copy of adscollate.adt available with version 9.0 does not yet have any accent-insensitive collations. The final part of the name is the codepage for which the collation is intended. The "machine" collations (e.g., MACHINE\_VFP\_BIN\_1252) are single-byte collations that all order data in byte order based on the ASCII value of the character. The \_BIN\_ in the name signifies raw binary sorting. The machine collations are both case-sensitive and accent-sensitive.

The currently available Visual FoxPro-compatible collations include CZECH, DUTCH, GENERAL, GERMAN, GREEK, HUNGARY, ICELAND, MACHINE, NORDAN, POLISH, RUSSIAN, SLOVAK, SPANISH, SWEFIN, TURKISH, and UNIQWT. They include support for code pages 437, 620, 737, 850, 852, 857, 861, 865, 866, 895, 1250, 1251, 1252, 1253, and 1254. At this point none of the collations for multi-byte character sets are supported. Specifically, collations built in Visual FoxPro that use the National Language Support (NLS) will not be compatible with Advantage.

The collations are physically stored in the files adscollate.adt and adscollate.adm. The file adscollate.adt is a standard Advantage proprietary format (ADT) table that can be opened the same as any other ADT table. However, you can use the system procedure [sp\_GetCollations](master_sp_getcollations.htm) to retrieve the list of available collations along with short text descriptions and other information. In order to use these dynamic collations, adscollate.adt and the associated memo file adscollate.adm must be available for Advantage Database Server or Advantage Local Server to load at runtime. When using Advantage Database Server the file is expected to reside in the same directory as the ADS binary (e.g., ads.exe, libadsd.so). With Advantage Local Server, the file must be available in the search path; for example, it would normally be in the same directory as the adslocal.cfg file.

Using Collations

In order to use one of the dynamically loaded collations, you must specify the collation name at run time. In general, the collation name is specified instead of the existing ADS\_ANSI or ADS\_OEM character set choice. The method depends on the development environment you are using. When using one of the connection-string oriented clients such as JDBC, OLE DB, ADO.NET, etc. the application should specify the collation name in the connection string. For example, specifying chartype=general\_vfp\_ci\_as\_1252 in the connection string when using the Advantage .NET Data Provider will cause all operations in that connection to use the GENERAL collation for codepage 1252. A Delphi application, for example, can specify one of these collations via the AdsCharType property.

The Unicode collation locale name may be specified after the ANSI/OEM collation name with a colon separating them. For example, specifying chartype=general\_vfp\_ci\_as\_1252:en\_CA\_ADS\_CI in the connection string when using the Advantage .NET data provider will cause all Unicode related operations to use the case insensitive Canadian English locale.

In general, choosing ANSI (ADS\_ANSI) or OEM (ADS\_OEM) chooses one of the static single-byte collations that is stamped in the Advantage Database Server or specified in adslocal.cfg. Choosing another name specifies that the named collation is to be loaded dynamically at runtime from adscollate.adt.

There are some runtime differences between the traditional static collations and the dynamic collations. Aside from being able to choose different collations at runtime, the primary difference is that indexes built with the dynamic collations will be maintained no matter which collation is currently active in the application. If an index is built with a static collation, then that collation must always be the one available in the server, otherwise the index must be rebuilt to avoid logical index corruption.

A benefit to using a static collation is that you can install a version of Advantage Database Server with the desired collation language and rebuild all indexes (or use the [auto-creation](master_advantage_data_dictionary.htm) option), and your application will automatically use that new collation. In other words, some of the localization can be handled at install time. In contrast, an index built with one of the dynamic collations must be dropped and created again in order to use a different collation. With dynamic collations, the name of the collation is stored in the index header in the index file itself.

Advantage will only use a dynamic collation for optimization purposes if the collation matches the currently chosen collation. For example, if the collation currently in use for an SQL statement is HUNGARY\_VFP\_CI\_AS\_1250, then it will only use an index built on a character field for optimizing an ORDER BY clause or a filter if the index was built with that same collation. Note that in a development environment that allows you to choose indexes directly for ordering results (e.g., with Delphi and the TAdsTable component), you can choose any index to be the active index even if it does not match the current collation.

The handling of [Full Text Search](master_full_text_search.htm) (FTS) indexes is a little different. When using the CONTAINS() function to do an FTS search, Advantage will use any FTS index available even if it was built with a different collation. Another difference with FTS indexes is that accent information is not stored when a dynamic collation with secondary weight information is used. For example, if the collation GENERAL\_VFP\_CI\_AS\_1252 is used for building an FTS index, the accent information for characters such as á, è, ö, etc. is not stored in the index. This means that a search such as CONTAINS(\*, resume) will find resumé. If this is not desired, then it is necessary to use a static collation or use one of the MACHINE dynamic collations.

Because of the fact that multiple dynamic collations can be specified and in use at any one time, it presents the possibility of silently hiding optimization problems. For example, if you write an SQL query in Advantage Data Architect and look at the optimization plan, you might see that it is desirable to add a new index. If your application specifies a dynamic collation that is not currently chosen in Advantage Data Architect, then the new index will be built with a collation that is not used by the application. If you then run the query in your application, it might not be optimized because the collation would not match that of the new index.

To help make developers aware of this potential issue, Advantage will, by default, produce a 5209 error when a table is opened that has indexes built with collations that do not match the currently specified collation.

If you want to be able to use multiple collations concurrently on a single table, you can use the system procedure [sp\_AllowMultipleCollations](master_sp_allowmultiplecollations.htm) to turn off the 5209 error. The information that controls whether this error is generated is contained in the adscollate.adt collation table repository. This means that if you turn off the 5209 error for one or more collations, it will turn it off for all applications that are using that same collation repository.

Codepages

Advantage does not currently perform data conversions between any two different codepages. Visual FoxPro DBF tables contain a codepage in the header. In Visual FoxPro, you can specify the active codepage. When Visual FoxPro reads and writes to a DBF that has a different codepage, it will translate the data appropriately. Currently, the only conversion that Advantage performs is between ANSI and OEM codepages that are the current ones defined on the PC. If the DBF has an OEM codepage, then Advantage will convert the data to the applications ANSI codepage.

If you create a new DBF table when using one of the FoxPro-compatible collations, Advantage will store the codepage for that collation in the DBF header for use by Visual FoxPro. If you are not using the FoxPro-compatible collations, Advantage will not store the codepage in the DBF header.