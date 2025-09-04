---
title: Odbc Character Sets
slug: odbc_character_sets
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_character_sets.htm
source: Advantage CHM
tags:
  - odbc
checksum: 596e509602b5ed20c61b14d4ea0c966c3b22837f
---

# Odbc Character Sets

Character Sets

Character Sets

Advantage ODBC Driver

| Character Sets  Advantage ODBC Driver |  |  |  |  |

Character Sets are important when using the Advantage ODBC Driver in international environments. They are used to determine what characters are available in the chosen language and are used to properly sort indexes based on the chosen languages collation sequence. The Advantage Database Server must also be installed with the correct language collation sequence. When installing the Advantage Database Server, the language support is outlined to properly select the character set you wish to use with your applications.

There are key differences between database and index files created with Windows database applications and DOS database applications. This is due to the underlying character sets defined in Windows and DOS. The character set definitions are not the same in both environments, even with English.

Beginning with version 9.0, the Advantage ODBC driver can make use of additional collation sequences that can be loaded dynamically at run time. See [dynamic collations](master_collation_support.md) for more information.

ANSI Character Sets

ANSI is the definition of character sets as established by Microsoft Windows. When ANSI is chosen as the character set type, it specifies that the ANSI collation stamped into Advantage Database Server (or specified in the adslocal.cfg file for Advantage Local Server) will be used. Any database and index files created by Windows applications are defined with ANSI character sets. When using the Advantage ODBC Driver, you are most likely accessing the Driver from a Windows environment. To access and properly maintain existing indexes, ANSI must be selected in your Data Source as the Character Set. This then assumes the Windows language setting. All changes made to the database and index files, in addition to building new indexes, assume the ANSI option is selected.

When the Advantage proprietary data type is selected, all sorting uses the ANSI character sets.

OEM Character Sets

DOS applications use an OEM character set definition. For database and index files created with a DOS application, such as CA-Clipper, use the OEM character set to sort and maintain indexes. If OEM is selected as the Character Set, it specifies that the OEM collation stamped into Advantage Database Server (or specified in the adslocal.cfg file for Advantage Local Server) will be used.

If OEM is selected, the Advantage ODBC Driver performs OEM to ANSI conversions. Since the ODBC Driver is used from a Windows environment, it assumes that the Windows settings are set up to use the proper collation sequence. The Windows setup information is sufficient to let OemToAnsi and AnsiToOem functions correctly convert data that is in the database.

Conversions

The Advantage ODBC Driver must work with ANSI data, therefore, the Driver must convert OEM database and index files to ANSI. When converting characters, it is possible that some may not properly convert to an expected character.

The Advantage ODBC Driver uses the Windows keyboard driver to figure out the OEM code page. This allows the Driver to use the installed Windows character set to convert the OEM data to ANSI.

For example, the Windows ANSI character È (Windows character 200) in codepage 1252 has no equivalent OEM character in codepage 437. This has several consequences:

- If you create a table with ANSI character 200 in the name, DOS automatically will convert it to a plain E.

- If you create a table with the lower case version è (character 232), the same conversion happens.

- Data in a character field that has character 200 will get converted to E in the AnsiToOem function call made before data is stored in the DBF table. The small character version (232) will convert correctly because code page 437 contains that character.

Field and Path Names

When creating DBF files, the Advantage ODBC Driver creates columns with field names containing only 0-9, \_, A-Z, and a-z characters. Thus, international characters cannot be used in a field name. This is necessary for compatibility with the Advantage Expression Engine. If a table already exists with field names using characters other than 0-9, \_, A-Z, and a-z, the ODBC Driver can access the fields. The maximum length of a DBF field name is typically 10 characters. However, when using Visual FoxPro (VFP) tables in a data dictionary, the names can be up to 128 characters.

Advantage proprietary files allow any character from character code 1-255 to be in a field name, except for ; and , characters. Field names can be up to 128 bytes in length.

Character sets (and collation orders) used by the Driver are based on the information from the ODBC registry entry for a given Data Source. This means that a table accessed through a full path (e.g., "x:\dbdir\table") is assumed by the Driver to have the same character set as the initial connection. Internally, the table is stored as a different "database" under a single "connection". This also applies to the "USE x:\dbdir" extended grammar SQL statement.
