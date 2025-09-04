What's New in Advantage 11.1




Advantage Database Server 12  

What's New in Advantage 11.1

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What's New in Advantage 11.1  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - What's New in Advantage 11.1 Advantage Database Server master\_Whats\_New\_in\_Advantage\_11.1 Advantage Database Server > Introduction > What's New in Advantage 11.1 / Dear Support Staff, |  |
| What's New in Advantage 11.1  Advantage Database Server |  |  |  |  |

Delphi XE6 Support

The Advantage Delphi Components now include support for Delphi XE6. Note that some default behaviors have changed in Delphi XE6.  See topic [Effects of Upgrading](master_effects_of_upgrading_to_version_11_1.htm) for more information.

 

Delphi XE5 Support

The Advantage Delphi Components now include support for Delphi XE5.

Delphi XE4 Support

The Advantage Delphi Components now include support for Delphi XE4.

 

Delphi XE3 Support

The Advantage Delphi Components now include support for Delphi XE3.

Visual Studio 12 Support

The Advantage .NET Data Provider now includes support for Visual Studio 12.

Security Enhancements

A complete security scan of the code has been made. Enhancements were made to improve checks of incoming packet data, prevent DLL injection attacks, perform buffer validation, etc.

New System Procedure

The procedure [sp\_GetTableSizeInfo](master_sp_gettablesizeinfo.htm) was added to be able to return information about physical table and memo files.

SQL Engine Enhancements

Enhancement has been made in the SQL engine to reduce recursion in expression parsing and evaluation. The changes greatly expand the size of the expressions that the SQL engine can evaluate without causing the "recursion depth error", and improve the speed of evaluating some large SQL expressions.

New Platforms

Support has been added for:

|  |  |
| --- | --- |
| · | Windows Server 2012 |

|  |  |
| --- | --- |
| · | Windows Small Business Server |

|  |  |
| --- | --- |
| · | Windows 8 |

New Server Configuration Setting

The configuration setting [Check\_Free\_Table\_Access](master_check_free_table_access.htm) has been added to restrict free table access through data dictionary connections on a server wide basis.

Entity Framework Skip Operator

Added support for the .Skip() operator to the .NET Entity Framework Provider.

New UTC Timestamp Scalar and Expression Engine Function

Added [CURRENT\_TIMESTAMP\_UTC()](master_date_time_functions.htm "CURRENT_TIMESTAMP_UTC()") SQL scalar and [NOW\_UTC()](master_now_utc.htm "NOW_UTC()") expression engine function that return a timestamp value of the current date and time in Coordinated Universal Time (UTC).  UTC is the time zone of London England and widely used by applications that share time data across time zones.

New \_\_rootdd Server-Side Alias

Added a system alias called [\_\_rootdd](master_server_side_aliases.htm) that resolves to the root dictionary path.  This allows applications to connect to the root dictionary without knowing the actual path.  As with any server-side alias, it also allows applications to connect to the root dictionary without having to expose the root dictionary with a network share.  See [server-side aliases](master_server_side_aliases.htm) for more information.

ExtraConnectString Property Available in Advantage Data Architect

The connection repository in Advantage Data Architect has been updated to expose the TAdsConnection ExtraConnectString property, which allows additional connection string properties to be provided for a connection.  As with the other connection properties, this is persisted in the ads.ini file.