File Requirements




Advantage Database Server 12  

File Requirements

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| File Requirements  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - File Requirements Advantage Visual Objects and Vulcan.NET RDD vo\_File\_requirements Advantage Visual Objects and Vulcan.NET RDD > Introduction > File Requirements / Dear Support Staff, |  |
| File Requirements  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Required Files

The following list of files will be installed into the following directory structure beneath the Visual Objects directory specified during setup (the default Visual Objects directory is C:\CAVO28 or C:\Program Files\CAVO26, etc) or in the Advantage install directory for Vulcan.NET (the default being C:\Program Files\Advantage X.x):

|  |  |
| --- | --- |
| BIN\ADSADT.RDD | The Advantage ADT/ADI/ADM RDD. A DLL for use with Visual Objects. |
| BIN\AXDBFCDX.RDD | The Advantage DBF/CDX/FPT RDD. A DLL for use with Visual Objects. |
| BIN\AXDBFNTX.RDD | The Advantage DBF/NTX/DBT RDD. A DLL for use with Visual Objects. |
| BIN\AXDBFVFP.RDD | The Advantage DBF/CDX/FPT Visual FoxPro RDD. A DLL for use with Visual Objects. |
| BIN\AXSQLADT.RDD | The Advantage ADT/ADI/ADM SQL RDD. A DLL for use with Visual Objects. |
| BIN\AXSQLVFP.RDD | The Advantage Visual FoxPro DBF/CDX/FPT SQL RDD. A DLL for use with Visual Objects. |
| BIN\AXSQLCDX.RDD | The Advantage DBF/CDX/FPT SQL RDD. A DLL for use with Visual Objects. |
| BIN\AXSQLNTX.RDD | The Advantage DBF/NTX/DBT SQL RDD. A DLL for use with Visual Objects. |
| Vulcan.NET\AdvantageRDD.dll | The Advantage Vulcan.NET RDD.  A .NET assembly containing all the Advantage RDDs for Vulcan.NET. |
| ADS\ADSSQLSERVER.AEF | The Visual Objects Application Export File (AEF) that provides a DBServer implementation for use with the SQL RDDs. |
| ADS\ACE.AEF | The Visual Objects Application Export File (AEF) that provides the API prototypes for the Advantage Client Engine advanced functionality. |
| ADS\DBFAXS.AEF | The Visual Objects Application Export File (AEF) that provides access to Advantage advanced functionality. |
| ADS\ADSDBSER.AEF | The Visual Objects Application Export File (AEF) that fixes a bug with the DBServer class and early versions of Visual Objects. |
| VULCAN.NET\ADSSQLSERVER.PRG | The AdsSQLServer class library for Vulcan.NET. |
| VULCAN.NET\DBFAXS.PRG | The DBFAXS extended functions library for Vulcan.NET. |
| VULCAN.NET\DBFAXS.VH | The DBFAXS library constants for Vulcan.NET. |
| ADS\ADS.INI | Windows initialization file to override specific default settings such as the Advantage Server type and the Advantage Collation language. |
| WINDOWS\SYSTEM\ACE32.DLL | The Advantage Client Engine DLL used by the Advantage RDDs. |
| WINDOWS\SYSTEM\AXCWS32.DLL | The Advantage communication layer DLL required if accessing the Advantage Database Server. |
| WINDOWS\SYSTEM\ADSLOC32.DLL | Advantage Local Server DLL necessary if accessing the Advantage Local Server. |
| WINDOWS\SYSTEM\ADSLOCAL.CFG | Advantage Local Server configuration file. |
| WINDOWS\SYSTEM\EXTEND.CHR | OEM collation sequences. This file is needed if non-USA OEM character sets are to be used with the Advantage Local Server. |
| WINDOWS\SYSTEM\ANSI.CHR | ANSI collation sequences. This file may be needed if non-English ANSI character sets are to be used with the Advantage Local Server. |

The following list of VO support files will be installed into the Advantage Support files directory specified during installation (the default Advantage Support files directory is C:\Program Files\Advantage X.x\VO).

|  |  |
| --- | --- |
| VO\ADS.REG | Advantage registry file. Used to set registry settings during installation. |
| VO\LICENSE.TXT or  VULCAN.NET\LICENSE.TXT | The software license agreement for this product. |

The Advantage help file will be installed into the Advantage Help file directory specified during installation (the default Advantage Help file directory is C:\Program Files\Advantage X.x\HELP).

|  |  |
| --- | --- |
| ADVANTAGE.CHM | Advantage master Help file. |

For more information about which files are necessary to distribute with an Advantage Visual Objects application, see [Distributing Advantage Visual Objects Applications](vo_distributing_advantage_ca_visual_objects_applications.htm).