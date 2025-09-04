Task 2: Create Your AEP Source File




Advantage Database Server 12  

Task 2: Create Your AEP Source File

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 2: Create Your AEP Source File  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 2: Create Your AEP Source File Advantage Concepts master\_Task\_2\_create\_your\_aep\_source\_file Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > TDataSet Descendant Tutorial > Task 2:  Create Your AEP Source File / Dear Support Staff, |  |
| Task 2: Create Your AEP Source File  Advantage Concepts |  |  |  |  |

Because an AEP (Advantage Extended Procedure) container is either a Windows DLL, COM DLLs, .NET assembly, or a Linux shared object, there are many different methods in which you can create your source project. This tutorial will use Delphi/Kylix, and help you by providing a template you can use in all of your AEP development. Keep in mind an AEP can be written using any development environment that supports the generation of Windows Dynamic Link Libraries (DLLs), COM DLLs, .NET assemblies, or Linux shared objects.

Start a new AEP Project:

|  |  |
| --- | --- |
| 1. | Open Delphi/Kylix and select File->New(File->New->Other if using a newer version of Delphi/Kylix) |

|  |  |
| --- | --- |
| 2. | Select Advantage Extended Procedure from the Project tab in the New Items dialog. |

|  |  |
| --- | --- |
| 3. | When prompted, Windows users enter X:\data as the destination directory. Linux users should enter ~/data as the destination directory. |

|  |  |
| --- | --- |
| 4. | Click the OK button. |

Name and Save Your AEP Container:

You will be presented with a template AEP project. Lets name this AEP container and save it to disk.

|  |  |
| --- | --- |
| 1. | Select Save As from the File menu. |

|  |  |
| --- | --- |
| 2. | Windows users: save your project file as x:\data\MyFirstAEP.dpr. Linux users: save your project file as ~/data/MyFirstAEP.dpr. |