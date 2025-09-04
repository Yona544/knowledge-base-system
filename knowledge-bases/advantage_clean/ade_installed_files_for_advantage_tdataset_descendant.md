---
title: Ade Installed Files For Advantage Tdataset Descendant
slug: ade_installed_files_for_advantage_tdataset_descendant
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_installed_files_for_advantage_tdataset_descendant.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 40128ad75ede52c1b0ec4ca1ece1c7b4e3e0c132
---

# Ade Installed Files For Advantage Tdataset Descendant

Installed Files for Advantage TDataSet Descendant

Installed Files for Advantage TDataSet Descendant

Advantage TDataSet Descendant

| Installed Files for Advantage TDataSet Descendant  Advantage TDataSet Descendant |  |  |  |  |

The files listed in the tables below will be installed in the following directories regardless of the Delphi/C++Builder product selected:

| Location | File Name | File Description |
| \Program Files\Advantage X.x \TDATASET | FILES.TXT | Contains information about what files are installed and their location. |
| \Program Files\Advantage X.x \TDATASET | READ\_ACE.TXT | The Advantage Client Engine readme file. Contains specific release level information about the Advantage Client Engine (ACE) that may not be in the ACE.HLP Help file. |
| \Program Files\Advantage X.x \TDATASET | README.TXT | The Advantage TDataSet Descendant readme file. Contains specific release level information about the Advantage TDataSet Descendant that may not be in the ADE.HLP Help file. |
| \Program Files\Advantage X.x \TDATASET | READ\_LOC.TXT | The Advantage Local Server Readme file. Contains specific information about the [Advantage Local Server](master_advantage_local_server.md). |
| \Program Files\Advantage X.x \HELP | ADVANTAGE.HLP | Advantage master Help file. |
| \Program Files\Advantage X.x \HELP | ADVANTAGE.CNT | Advantage master contents file. ADVANTAGE.CNT must reside in the same location as the ADVANTAGE.HLP file. |
| \Program Files\Advantage X.x \HELP | ADE.HLP | This Help file. |
| \Progam Files\Advantage X.x \HELP | ADE.CNT | Contents file for this Help file (ADE.HLP). ADE.CNT must reside in the same location as the ADE.HLP file. |
| \Program Files\Advantage X.x \HELP | ADSERROR.HLP | The Advantage Error Guide Help file. This file contains error codes and explanations. |
| \Program Files\Advantage X.x \HELP | ADSERROR.CNT | Advantage error codes contents file. ADSERROR.CNT must reside in the same location as the ADSERROR.HLP file. |
| \Program Files\Advantage X.x \TDATASET | LICENSE.TXT | The software license agreement for this product. |
| \Program Files\Advantage X.x \TDATASET | ANSICHR.EXE | Utility for adding an ANSI collation language to ANSI.CHR. |
| \Program Files\Advantage X.x \TDATASET | ENCRYPT.DOC | Microsoft Word document that contains information about the new Advantage 2.5/5.5 encryption algorithm. |
| \Program Files\Advantage X.x \TDATASET | GETSTART.PDF | Documentation on getting started with the Advantage TDataSet Descendant. Use Acrobat Reader to view this file. |
| \Program Files\Advantage X.x \TDATASET | COMPREF.PDF | Documentation of the Properties, Methods, and Events for the Advantage Delphi components. Use Acrobat Reader to view this file. |
| \Program Files\Advantage X.x \TDATASET | INFPOWD4.EXE | Self-extracting executable that contains the Advantage InfoPower components for Delphi 4. This file is optionally installed with the Advantage Delphi 4 components. |
| \Program Files\Advantage X.x \TDATASET | INFPOWD3.EXE | Self-extracting executable that contains the Advantage InfoPower components for Delphi 3. This file is optionally installed with the Advantage Delphi 3 components. |

Sample Data Files

Sample data files are installed to the \Program Files\Advantage X.x\ADS\_DATA directory. The data files are installed one directory up from the specified install path in the ADS\_DATA directory. Two aliases are created during the installation that can be used with the sample data files. These aliases are called ADTDemoData and DBFDemoData.

An Advantage referential integrity example is installed to the \Program Files\Advantage X.x\TDataSet\RI directory. This is a simple example that does the following:

| 1. | Creates a data dictionary from code using the TAdsDictionary component. |

| 2. | Adds a referential integrity constraint to the database. |

| 3. | Allows you to modify data in the tables and see the effects of the RI constraints. |

An Advantage view example is installed to the \Program Files\Advantage X.x\TDataSet\Views Directory. This is a simple example that does the following:

| 1. | Creates a data dictionary from code using the TAdsDictionary component. |

| 2. | Adds a view to the database. |

| 3. | Shows how a view can be opened as a table. |

| 4. | Shows how a view can be used in an SQL statement. |

The following files are installed and needed with all Advantage for Delphi/C++Builder products.

| Location | File Name | File Description |
| Your Windows system directory. | ACE32.DLL | Advantage Client Engine DLL. Contains the core Advantage Windows client functionality. |
| Your Windows system directory. | AXCWS32.DLL | Advantage remote communication library used when accessing data via the Advantage Database Server. Also used when accessing data via international versions of the Advantage Internet Server. This file is not necessary if using the Advantage Local Server only. |
| Your Windows system directory. | ADSLOC32.DLL | Advantage Local Server DLL. Contains the core local server functionality. This file is not necessary if using the Advantage Database Server and/or Advantage Internet Server only. |
| Your Windows system directory. | ADSLOCAL.CFG | [Advantage Local Server Configuration](master_advantage_local_server_configuration.md). This file is only necessary if using the Advantage Local Server and you wish to use Local Server settings other than the default. |
| Your Windows system directory. | EXTEND.CHR | This file is needed for international OEM language support with the Advantage Local Server. This file is only necessary if using a non-USA OEM character set with the Advantage Local Server. |
| Your Windows system directory. | ANSI.CHR | This file may be needed for ANSI language support with the Advantage Local Server. This file is only necessary if not using a specified ANSI character set with the Advantage Local Server. |

The following files will be installed regardless of the Delphi/C++Builder product selected.

| Location | File Name | File Description |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ACE.PAS | The entry points to ACE32.DLL. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ACEUNPUB.PAS | The header file for unpublished APIs for internal use. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSCNNCT.PAS | The resource file for the TAdsConnection component. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSCNNCT.DCR | The compiled resource file for TAdsConnection. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSDATA.PAS | The TAdsDataSet component file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSDESIGN.PAS | The design-time file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSDICTIONARY. DCR | The compiled resource file for TAdsDictionary. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSDICTIONARY. PAS | The TAdsDictionary component file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSFUNC.PAS | The Advantage extended methods file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSSET.PAS | The TAdsSettings component file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSSET.DCR | The compiled resource file for TAdsSettings. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSSTRNG.PAS | The string utilities file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSTABLE.DCR | The compiled resource file for TAdsTable. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSTABLE.PAS | The TAdsTable file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | ADSVER.PAS | The version information file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | INDEXDLG.DFM | The form file for the index dialog. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | INDEXDLG.PAS | The index dialog file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | INFOEXP.PAS | The expression dialog file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | INFOEXP.DFM | The form file for the expression dialog. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | INFOSTRU.PAS | The table structure dialog file. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | INFOSTRU.DFM | The form file for the table structure dialog. |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | N/A | Bitmap image for the Component Palette |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | N/A | Bitmap image for the Component Palette |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | N/A | Bitmap image for the Component Palette |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | N/A | Bitmap image for the Component Palette |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | N/A | Bitmap image for the Component Palette |
| \Program Files\Advantage X.x \TDataSet\<Delphi/C++Builder Product Name> | VERSIONS.INC | The file that sets the pre-defined constants for each environment. |
