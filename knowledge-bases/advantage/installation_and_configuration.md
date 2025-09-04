Installation and Configuration




Advantage Database Server 12  

Installation and Configuration

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Installation and Configuration |  |  | Feedback on: Advantage Database Server 12 - Installation and Configuration Installation\_and\_Configuration Advantage Web Development > Advantage Delphi OData Client > Installation and Configuration / Dear Support Staff, |  |
| Installation and Configuration |  |  |  |  |

To use this product, you will first need to install [Advantage Web Platform](web_advantage_web_platform.htm) and do the appropriate settings. Please read its documentation for additional information on the OData component.

Installation

The Advantage Delphi OData is a BDE replacement, that allows you to create and distribute a database application that does not require BDE. The installed files for Advantage Delphi OData client are:

|  |  |
| --- | --- |
| · | ODataSet.pas |

|  |  |
| --- | --- |
| · | ODataClient.pas |

|  |  |
| --- | --- |
| · | ODataAPIDesign.pas |

|  |  |
| --- | --- |
| · | ODataAdaptor.pas |

|  |  |
| --- | --- |
| · | BatchRequest.pas |

|  |  |
| --- | --- |
| · | Versions.inc |

Configuration

After installing Delphi OData client, add source path to the RAD studio as:

Go to Tools --> Options

Select Library under Delphi Options

 Add the Delphi OData installation path. i.e:

 "<INSTALLDIR>\Advantage 12.00\DelphiOData\DelphiODataXE8\Win32\Source" and

 "<INSTALLDIR>\Advantage 12.00\DelphiOData\DelphiODataXE8\Win64\Source" to the Library Path.

Un-installation

Performing the following steps can uninstall the Advantage DelphiOData:

1.        Click the Start button on the Task Bar.

2.        Select Settings, Control Panel.

3.        Select Add/Remove Programs. The name of the Advantage software will depend on what Delphi product was installed.

4.        Locate the software to uninstall. Highlight it and click on the Add/Remove button. This will remove all the installed files except ads.ini and the files written to the SYSTEM directory.

---

 Note This method of uninstalling the Advantage DelphiOData will not remove the ads.ini file and the files written to the SYSTEM directory because they could be shared with other Advantage-enabled applications. If Advantage will no longer be used on this system, then it is safe to delete these files. The uninstall will remove the Advantage DelphiOData package but it will not remove the source path from the library path.

---

To remove the Advantage directory from the library path:

 1. Start the IDE and select Tools then Environment Options.

 2. Click the Library  under Delphi Options tab. Locate the <INSTALLDIR>\Advantage     X.x\DelphiOData\ path in Library Path and delete it from the library path

To remove other Advantage files:

 1.  Delete the <INSTALLDIR>\Advantage X.x\DelphiOData\<Delphi\_product> directory.

 2. If the Advantage DelphiOData is the only Advantage product installed, delete the <INSTALLDIR>\Advantage X.x directory and all of its subdirectories.

 3. Remove the Advantage package and source path.