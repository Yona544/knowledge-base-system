Overview of Lazarus Support




Advantage Database Server 12  

Overview of Lazarus Support

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Overview of Lazarus Support  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Overview of Lazarus Support Advantage TDataSet Descendant ade\_Overview\_of\_Lazarus\_Support Advantage TDataSet Descendant > Using the TDataSet with Lazarus > Overview of Lazarus Support / Dear Support Staff, |  |
| Overview of Lazarus Support  Advantage TDataSet Descendant |  |  |  |  |

Lazarus is the open-source graphical RAD IDE for the FreePascal compiler.  The TDataSet Descendant code now builds in version 2.2.4, 2.4.0, and 2.6.0 of the FreePascal compiler, and the TDataSet Descendant components are supported in version 1.0 of the Lazarus IDE.  For more information about Lazarus, see the Lazarus web site at <http://lazarus.freepascal.org>

Supported Platforms

As Lazarus is a cross-platform development platform, the TDataSet Descendant cannot support all platforms that Lazarus does.  The TDataSet Descendant works with the 32-bit Lazarus IDE on Windows and [Linux](ade_using_lazarus_on_linux.htm) (only).

Unsupported Functionality

For various reasons, not all of the functionality of Delphi's TDataSet Descendent can be supported in Lazarus.  Here is a list of currently-unsupported features:

|  |  |
| --- | --- |
| · | IProvider Support.  The Lazarus TDataSet does not implement the IProvider interface.  This means that functionality that relies on a TDataSetProvider (like client datasets) are not supported in Lazarus. |

|  |  |
| --- | --- |
| · | The Advanced Property Editors for TAdsTable (that allows tables to be created/restructured from within the IDE) and TAdsQuery (that allows the use of Advantage Data Architect's SQL Utility from within the IDE) are not supported due to the lack of a required ancestor class in Lazarus. |

|  |  |
| --- | --- |
| · | Lazarus does not provide a built-in login dialog (the LoginPrompt method of the TAdsConnection component has no effect).  As a result, those who need to prompt for authentication information will need to write their own form to collect the login information. |

|  |  |
| --- | --- |
| · | Unicode fields are not currently supported in Lazarus.  (Lazarus does support Unicode fields, but the current implementation of the TDataSet Descendant for Lazarus does not expose this functionality.) |