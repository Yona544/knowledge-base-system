Effects of Upgrading to Version 9.0




Advantage Database Server 12  

Effects of Upgrading to Version 9.0

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Effects of Upgrading to Version 9.0  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Effects of Upgrading to Version 9.0 Advantage Database Server master\_Effects\_of\_upgrading\_to\_9\_0 Advantage Database Server > Introduction > Effects of Upgrading to Version 9.0 / Dear Support Staff, |  |
| Effects of Upgrading to Version 9.0  Advantage Database Server |  |  |  |  |

The following Advantage functionality changes may affect your applications if you upgrade to Advantage version 9.0.

Effects of Upgrading

Progress information returned during a reindex operation now only goes from 0 to 100 once for the entire operation. Previous versions of Advantage would return progress information from 0 to 100 once for each index tag that was rebuilt.

Data dictionaries created using a version 9.0 or newer client cannot be used by Advantage version 6.0 or 6.1. An error will be returned when trying to open the newer data dictionary with Advantage version 6.0 or 6.1.

The CREATE DATABASE statement can now only be called by the ADSSYS user or a member of the DB:admin group when executed on a dictionary connection.

The character ':' is no longer allowed to be the leading character of the name of a temporary table.

In the past the OEM charset did not always need to be specified in the setup.ini file when performing a silent installation. The OEM charset must now always be specified.

Configuration settings which control the maximum number of tables, indexes, work areas, connections, and locks are no longer maximum values. These values are now initial values and Advantage will allocate additional resources to allow more instances of each type to be used as necessary. See the [Advantage Database Server Configuration Overview](master_advantage_database_server_configuration_overview.htm) topic for more details.

The default client timeout and internet client timeout values have been lowered to 2 minutes. This change will force more frequent keep-alive packets to be sent from clients, decreasing the chance of a firewall or VPN closing the port Advantage clients are using to communicate with the server.

New reserved keywords: AT, TRIGGER, VARCHAR, MERGE, USING

"DEBUG" is no longer a valid variable name in an SQL script.

In addition to the ':' character, the '\_' (underscore) character is no longer allowed to be the leading character of a declared variable in an SQL script.

Integer math now produces 2231 (Numeric result out of range) error if the result is out of the range of a signed 32-bit integer. In previous releases, the result was nondeterministic.

Pre 9.0 version of the Advantage TDataSet Descendant, OLE DB Provider, and ODBC driver may not function properly with a 9.0 or newer version of the Advantage Client Engine (ACE) DLL. The SQL engine may return a VarCharFox field type in static cursors when certain string scalars are used in the SELECT list. The older clients will not recognize this data type. For the TDataset Descendant, if it is desirable to use a newer version of the ACE DLL, you will need to re-compile the application using a 9.0 or newer version of the TDataset Descendant. For OLE DB or ODBC based applications, a 9.0 or newer version of the driver must be used.

When creating referential integrity (RI) rules, the foreign key and primary key fields must be matching lengths. In previous versions, it was possible to relate a 4 byte integer primary key integer to a 2 byte foreign key integer. That could lead to unpredictable behavior and is no longer allowed.

Attempts to create indexes on ADS\_NTX and ADS\_CDX tables with the binary concatenation (;) operator will produce a different error code. In the past, the error was a generic 5011 error. It will now be a specific expression engine error code: 3006, 3106, 3206, 3306, 3406, or 3506 depending on the usage.

The behavior of CONTAINS(\*, search) has been improved. It now searches across multiple fields in a more intuitive fashion. For example, if two fields have FTS indexes, then a search such as CONTAINS(\*, word1 and word2) will find records where word1 is contained in one FTS-indexed field and word2 is in a different FTS-indexed field. Previously, the search would succeed only if both search words were found in the same field. The NEAR operator still requires that the related search terms be in the same field.

AdsDataProvider - All definitions of Advantage handles (ADSHANDLE) have been changed from int or uint to IntPtr. This was necessary to support both 32 and 64 bit platforms with the .NET data provider. Specifically, these object properties were changed: AdsConnection.ConnectionHandle, AdsExtendedReader.ActiveHandle, & AdsExtendedReader.AdsHandle. It is recommended that any references to these properties in your code use the IntPtr variable type.

Dropped Support for Some Platforms and Technologies

Windows NT is no longer a supported platform.

The following Delphi and C++Builder versions will no longer be supported. Most will continue to be available in the installation as a courtesy, but the Advantage Technical Services team will not provide support for them.

|  |  |
| --- | --- |
| · | Delphi 3, 4, 5, 8 and 2005 |

|  |  |
| --- | --- |
| · | C++Builder 3 and 4 |

The Advantage Borland Data Provider (BDP) will no longer be supported. Borland/CodeGear has deprecated this technology.

The following Crystal Reports versions will no longer be supported. The drivers will continue to be available in the installation as a courtesy, but the Advantage Technical Services team will not provide support for them.

|  |  |
| --- | --- |
| · | Crystal Reports version 6.X |

|  |  |
| --- | --- |
| · | Crystal Reports version 7.X |

|  |  |
| --- | --- |
| · | Crystal Reports version 8.X |

See Also

[Effects of Upgrading to Version 8.1](master_effects_of_upgrading_to_advantage_8_1.htm)

[Effects of Upgrading from a Version Prior to v8.0](master_effects_of_upgrading_from_a_version_prior_to_v8_0.htm)