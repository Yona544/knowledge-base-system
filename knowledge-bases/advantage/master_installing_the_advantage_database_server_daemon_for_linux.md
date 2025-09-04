Installing the Advantage Database Server Daemon for Linux




Advantage Database Server 12  

Installing the Advantage Database Server Daemon for Linux

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Installing the Advantage Database Server Daemon for Linux  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Installing the Advantage Database Server Daemon for Linux Advantage Database Server master\_Installing\_the\_advantage\_database\_server\_daemon\_for\_linux Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Installing the Advantage Database Server Daemon for Linux  Advantage Database Server |  |  |  |  |

Note You must have superuser privileges to install the Advantage Database Server.

|  |  |
| --- | --- |
| 1. | Log in as superuser using the "su " command. This will set up the appropriate paths so the Advantage installation can find all utilities necessary during the installation. |

|  |  |
| --- | --- |
| 2. | Extract the contents of the Advantage tar distribution into a temporary directory using the command "tar xvzf adslinuxXX.tar.gz", where XX is the version of Advantage being installed. |

|  |  |
| --- | --- |
| 3. | Read the contents of both the README and INSTALL text files. |

|  |  |
| --- | --- |
| 4. | Start the installation by typing "./setup.pl". |

|  |  |
| --- | --- |
| 5. | Follow the on-screen prompts to complete the installation. |

|  |  |
| --- | --- |
| 6. | To properly perform string comparisons when using ANSI collation, Advantage provides ANSI character sets to match your country's language requirements. If your Advantage application uses ANSI character sets, select an ANSI character set to be used on the Advantage Database Server. Selecting a specific ANSI language for all Advantage installs (including Advantage Local Server) will guarantee the ANSI character sets used by all Advantage applications will be the same. |

|  |  |
| --- | --- |
| 7. | To properly perform string comparisons with local languages, Advantage provides OEM/localized character sets to match your country's language requirements. If your Advantage application uses OEM/localized character sets, select the character set that matches your Advantage client applications. Selecting a specific OEM/Localized character set for all Advantage installs (including Advantage Local Server) will guarantee the OEM/Localized character sets used by all Advantage applications will be the same. |

|  |  |
| --- | --- |
| 8. | Enter your serial number, validation code, and the optional replication code. |

To start the Advantage Database Server Daemon, go to the installation destination directory and type "./adsd". You can use the command "ps A" to verify the new adsd threads appear in the process list. See [Understanding Linux Daemons](master_understanding_linux_daemons.htm) for more information on how to start and stop the Advantage Database Server for Linux.