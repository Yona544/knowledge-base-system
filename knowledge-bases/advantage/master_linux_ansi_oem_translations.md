Linux ANSI/OEM Translations




Advantage Database Server 12  

Linux ANSI/OEM Translations

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Linux ANSI/OEM Translations  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Linux ANSI/OEM Translations Advantage Concepts master\_Linux\_ansi\_oem\_translations Advantage Concepts > Advantage Linux Development Notes > Linux ANSI/OEM Translations / Dear Support Staff, |  |
| Linux ANSI/OEM Translations  Advantage Concepts |  |  |  |  |

|  |  |
| --- | --- |
| · | This information applies only to tables opened with the OEM character set type. |

When using DBF (ADS\_CDX or ADS\_NTX) tables with the OEM character set type, Advantage must perform translations between ANSI and OEM character values. If a DBF table is opened with the OEM character set type, then the character data in the table is expected to have OEM values. Advantage converts the values to ANSI before returning it to client applications and performs the reverse conversion when storing data in the tables. The conversions must be done at various times in processing. When reading data, for example, the conversions are performed at the client. When performing SQL operations, some of the conversions must occur at the server.

The Advantage Database Server for Linux has translation tables built into it for converting characters between ANSI and OEM character sets. The existing tables are for converting from OEM character set 437 to the ANSI character set 1252 (the common character sets used in the United States). If you use different character sets, then it is possible you may need different conversion tables. For example, ANSI character 165 (in code page 1252) gets converted to OEM character 190 when using OEM code page 850 and to OEM character 157 when using OEM code page 437.

If you use different code pages, you must stamp the corresponding translation tables into the ADS daemon. The utility stampansioem.exe is provided for this purpose. It must be run from a Windows client. When you run it, provide the adsd binary as the command line parameter. The utility will generate the ANSI/OEM translation tables based on the current operating system settings and stamp those tables into the adds binary.

The Advantage Client Engine for Linux reads the ANSI/OEM translation tables from the server when it connects, so it does not require the tables to be stamped into the client. Win32 clients use the translation functions that are built into the Windows operating systems.