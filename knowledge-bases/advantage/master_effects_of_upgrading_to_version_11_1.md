Effects of Upgrading to Version 11.1




Advantage Database Server 12  

Effects of Upgrading to Version 11.1

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Effects of Upgrading to Version 11.1  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Effects of Upgrading to Version 11.1 Advantage Database Server master\_Effects\_of\_Upgrading\_to\_Version\_11.1 Advantage Database Server > Introduction > Effects of Upgrading to Version 11.1 / Dear Support Staff, |  |
| Effects of Upgrading to Version 11.1  Advantage Database Server |  |  |  |  |

DLL Search Paths are More Restrictive

As part of the additional security checks added in v11.1, Advantage Database Server is more restrictive in searching for DLLs. In previous versions, Advantage Database Server would load the Advantage Client Engine (ace32/64.dll) using the Windows search path environment variable if it was not found in the folder in which the service executable (ads.exe) existed. Beginning with v11.1, though, that search is no longer performed. Advantage Database Server will only load ace32/64.dll from the folder in which the executable (ads.exe) resides or from the Windows system folder. Note that it is not recommended to put the Advantage DLLs in the Windows system folder, but for legacy reasons, that folder is still searched.  The use of the system directory may be removed in the future. This more restrictive DLL search applies to the following DLLs:

|  |  |
| --- | --- |
| · | ace32/64.dll |

|  |  |
| --- | --- |
| · | axcws32/64.dll |

|  |  |
| --- | --- |
| · | aicu32/64.dll |

|  |  |
| --- | --- |
| · | libeay32.dll |

|  |  |
| --- | --- |
| · | ssleay32.dll |

This more restrictive searching also applies to the Advantage Client Engine DLL when it is running in the context of a client application. It will only load the above DLLs from the ace32/64.dll folder, the client executable folder, or the Windows system folder (in that order).

Note that the [REPLICATION\_LIBRARY](master_replication_library.htm) configuration parameter can still be used to provide a specific path to ace32/64.dll that resides outside the folder of the Advantage Database Server executable.

Auto-updating Rowversion and Modtime Fields in Stored Procedure Input or Output Tables are no Longer Updatable

Rowversion and modtime fields defined in stored procedure input or output tables will be automatically populated in the table.  In other words, these fields will be given new values automatically generated in the input or output tables.  If you need to pass in or out existing rowversion or modtime values, define the input or output field types as numeric or timestamp so the original values are preserved.  Autoinc fields have and will behave this same way.

Non-Automatic Fields created at Runtime in RAD Studio XE6 may not be cleaned up on Table Close.

In RAD Studio (or Delphi) XE6, TField objects that are created at runtime and assigned to a given TDataSet (or a Descendant such as a TAdsTable or TAdsQuery) are not automatically cleaned up when the DataSet is closed.  (They are, however, destroyed when the DataSet object is freed.)  As a result, the effect is only seen when altering fields at runtime.  This can cause various error conditions.  For instance, a "Component Already Exists" error may occur if a lookup field is added and the tabled then opened and closed, then a lookup field of the same name (but potentially different definition) is added to the table.  This is a regression in RAD Studio XE6 reported as QC# 126207 that also affects the BDE and other TDataSet components.  To work around this issue, clear the field definitions when closing the table (if it is to be re-opened) with by calling the DataSet's .Fields.Clear method.  (Alternately, the TDataSet object can be freed and re-instantiated.)