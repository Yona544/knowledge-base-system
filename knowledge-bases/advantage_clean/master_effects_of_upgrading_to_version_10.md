---
title: Master Effects Of Upgrading To Version 10
slug: master_effects_of_upgrading_to_version_10
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_effects_of_upgrading_to_version_10.htm
source: Advantage CHM
tags:
  - master
checksum: 5c66735cc4fe3e121ff85bb7a39c0c3774439bfb
---

# Master Effects Of Upgrading To Version 10

Effects of Upgrading to Version 10

Effects of Upgrading to Version 10

Advantage Database Server

| Effects of Upgrading to Version 10  Advantage Database Server |  |  |  |  |

Check Rights is no Longer the Default

The default behavior for rights checking has been changed. The new default behavior is to ignore the rights checking setting for table opens and creations and always ignore the client rights check. Free table opens in most clients would previously default to do rights checking; the client would do an existence check for a table before attempting to open it. For most applications, this was an unnecessary and potentially expensive check that could result in long timeouts on the client. And if a developer did not explicitly turn off rights checking, then their application would be penalized without them realizing it. Note that this only affects direct free table opens; it has no affect on SQL statements or opening of data dictionary-bound tables.

In order to restore the previous (pre-version 10.0) behavior to your application, it is necessary to call the Advantage Client Engine API [AdsSetRightsChecking](ace_adssetrightschecking.md).  This new behavior requires the v10.0 client. Older clients are not affected by this change in behavior.

5004 Errors Opening Static Cursors from ACE 2.7/5.7 and Older Clients

Rights checking must be disabled on 5.7 and older clients when using an Advantage version 10 server. Version 10 uses a combination of data caching and temporary file handle pooling, and these technologies are not compatible with 5.7 and older clients as they attempt to verify the existence of the physical temporary file when opening a static cursor.

 

Delphi for .NET No Longer Supported

Delphi for .NET is no longer supported, and Advantage version 10 components for Delphi for .NET will not be shipped. Older versions will still continue to work against newer servers, however. Also note that this only applies to the Delphi for .NET product line (TDataSet.NET). Delphi Prism is still fully supported via the Advantage ADO.NET provider.

Crystal Reports Driver Settings

In version 10 we have added per-alias Crystal Reports settings instead of only providing global settings (for options like Collation, LockingMode, ShowDeleted, etc). As a side-effect, if these new per-alias settings already exist in the ads.ini file (and they might, as they use the same format as the Advantage Data Architect connection repository settings), they will now be used instead of the global settings in the [Crystal] section.

SQL LIKE Operator Escape Characters

Prior to version 10 release, if the '%' or '\_' character was specified as the escape character for an SQL LIKE comparison, the SQL statement would execute successfully but the comparison performed might not be intended by the user. For example, the expression "Column LIKE 'ab%%%' ESCAPE '%'" would only match columns that where exactly 'ab' instead of columns with the prefix 'ab'. Starting with version 10, an error will be returned if '%' or '\_' is being specified as the escape character for the LIKE comparison. If the application receives an error message "ESCAPE clause must be a single ASCII character that is not '%' or '\_'", the SQL statement must be rewritten to avoid such usage.

Different Variable Data Type in SQL Scripts

In SQL scripts, a variable declared as a STRING is now treat as equivalent to the SQL\_VARCHAR type instead of the SQL\_LONGVARCHAR type. This change makes internal processing of the STRING variables in the SQL script more efficient. The effect of this change is that when the variable is being returned in the SELECT list of a SQL query such as "SELECT StringVar FROM system.iota", the corresponding column type for the variable in the Advantage Client Engine (ACE) will be ADS\_VARCHARFOX instead of the MEMO type. Normally, this will make processing the cursor more efficient for the application and it should have little effect on the application built using clients that encapsulates the ACE functionality, such as the ADS TDataSet Descendant for Delphi or the Advantage .NET Data Provider. However, if this change is undesirable, the work around is to declare the variable as the SQL\_LONGVARCHAR type instead of the STRING type.

Column name in SQL cursor may be different

In version 10, the column names for the values based on declared variables in the SQL scripts are the names of the variables, instead of the generated names of "EXPR", "EXPR\_1", etc. For example, given the following SQL script:

DECLARE Var1 String;

DECLARE Var2 Integer;

Var1 = 'abc';

Var2 = 1;

SELECT Var1, Var2, Var2 + 1 FROM system.iota

In ADS 10, the returned cursor will have the three columns named "Var1", "Var2", and "EXPR". While in previous releases, the columns would have the names "EXPR", "EXPR\_1", and "EXPR\_2". In general, one should not rely on the names generated by the server as it may change in the future. It is a good practice to always alias the columns that may not have explicit names to avoid potential problem. For example, the SELECT statement above may be changed to: SELECT Var1 AS Var1, Var2 AS Var2, Var2 + 1 AS MyCalc FROM system.iota to remove any potential ambiguity.

64 bit ACE DLL Name Change

In order to allow the Advantage ADO.NET provider to work on 32 and 64 bit platforms, the 64 bit ACE DLL in prior versions was named ace32.dll. In version 10 the file now uses the more appropriate name ACE64.DLL. The Advantage ADO.NET provider has been modified to detect the platform at runtime and load the correct ACE DLL based on that information.

Unicode Field Types in System Views

The system views for data dictionary metadata now return Unicode fields for some properties.  When connecting with clients older than 10.0 ANSI fields will always be returned in the system views.  For clients that cannot handle Unicode strings pre-pending "ansi\_" onto the view name will force the system view to return ANSI fields.

Invalid Floating Point Values are Prevented from being Stored

Note: This change is in v10.0.0.3.  The handling of floating point values has been changed to detect when attempts are made to store invalid IEEE 8-byte double values.  If an attempt is made to store an invalid double (e.g., NaN), either through the Advantage Client Engine API or through SQL, a 5101 (AE\_INVALID\_VALUE) error will be returned. This change does not affect existing values stored in tables.
