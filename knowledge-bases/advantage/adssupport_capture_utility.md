ADSSupport Capture Utility




Advantage Database Server 12  

Advantage Support Capture Utility

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Support Capture Utility  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Advantage Support Capture Utility Troubleshooting ADSSupport\_Capture\_Utility Troubleshooting and Technical Support > Troubleshooting > ADSSupport Capture Utility / Dear Support Staff, |  |
| Advantage Support Capture Utility  Troubleshooting |  |  |  |  |

The ADS Support Capture Tool (ADSSupportCapture.exe) is a utility designed to gather support files and Advantage Server settings in a quick and simple manor.

The ADS Support Capture Tool will gather the following items and put them into one zip file that can be email to the Advantage Technical Services team.

|  |  |
| --- | --- |
| · | ADS\_ERR.\* files. |

|  |  |
| --- | --- |
| · | Windows Event Logs |

|  |  |
| --- | --- |
| · | [ADS dump file(s)](master_adsdump_files.htm) |

|  |  |
| --- | --- |
| · | A report with various ADS server settings and IP configuration information. |

Optionally, it can:

|  |  |
| --- | --- |
| · | Run ADTFix on a specific folder of tables to check for corruption |

|  |  |
| --- | --- |
| · | Connect to the current Advantage service and get stats and info |

|  |  |
| --- | --- |
| · | Specify the age of dump files to be received |

|  |  |
| --- | --- |
| · | Gather the MSInfo32 information for the system it is run on |

The zip file will be placed in the same folder as the Error and Assert Log path defined in the Advantage Configuration Utility (where the ADS\_ERR.\* files are located).  However, if ADS is installed on Microsoft Vista or newer, the location of the zip file will be: C:\Users\Public\ADS\_SupportCapture.zip

In either case, the location will be displayed to the user when the program has completed.

Usage

ADSSupportCapture.exe [Parameters]

       -p=(path) - For specifying data path

       -x=(password) - For specifying table encryption password passed to ADTFix (not recommended)

       -s - For logging the current server stats

       -i - For logging MSInfo32 information

       -id - For logging MSInfo32 information (Report mode(only if -i fails to work))

       -f - For logging file info of ADS related files

       -d# - For capturing all dump files (# indicates age of files in days)

Known Issues

MSInfo32 is known to hang on some machines.  If you find that it is hanging on your machine, please run with the -id option instead of the -i.  This is a Windows bug and is not reproducible on all machines.