Custom TDataSet Versions




Advantage Database Server 12  

Custom TDataSet Versions

Advantage TDataSet Descendant

Managing Multiple Versions

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Custom TDataSet Versions  Advantage TDataSet Descendant  Managing Multiple Versions |  |  | Feedback on: Advantage Database Server 12 - Custom TDataSet Versions Advantage TDataSet Descendant Managing Multiple Versions ade\_Custom\_tdataset\_versions Advantage TDataSet Descendant > Managing Multiple Versions > Custom TDataSet Versions / Dear Support Staff, |  |
| Custom TDataSet Versions  Advantage TDataSet Descendant  Managing Multiple Versions |  |  |  |  |

Custom TDataSet Versions allow developers to configure the utility to be able to detect their own TDataSet classes that descend from the Advantage TDataSet Descendants as well as versions of the Advantage TDataSet Descendant prior to version 7.1.

To access this functionality, click on the "Configure Custom Versions" button on the main TDataSet Switch form. The menu that is displayed allows you to configure a TDataSet Descendant name and installation path. The configured TDataSet installation path should point to a directory structure that mirrors the TDataSet install directory. Specifically, this directory needs to contain "DelphiX" and "CBlderX" directories corresponding to each version of Delphi/C++ Builder that can use this version of the TDataSet. Additionally, the directory should contain a "Redistribute" directory that contains the ACE DLL files (ace32.dll, axcws32.dll, and adsloc32.dll) for this version of the TDataSet Descendant.

For instance, if Delphi 2006 and C++Builder 2007 are present for a given version of the TDataSet Descendant, the configured path should point to a directory that contains the following directories:

TDataSet\

TDataSet\Delphi2006\

TDataSet\CBlder2007\

TDataSet\Redistribute\