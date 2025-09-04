Referencing the Advantage .NET Data Provider




Advantage Database Server 12  

Referencing the Advantage .NET Data Provider

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Referencing the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Referencing the Advantage .NET Data Provider Advantage .NET Data Provider dotnet\_Referencing\_the\_advantage\_net\_data\_provider Advantage .NET Data Provider > Introduction > Referencing the Advantage .NET Data Provider / Dear Support Staff, |  |
| Referencing the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  |  |  |

To use the Advantage .NET Data Provider, a reference to it must be added to the project. Normally, this can be done by choosing the "Add Reference" option from the Project menu (e.g., in Visual Studio .NET). The .NET component list should contain an entry called Advantage.Data.Provider, which you can select.

The Advantage .NET Data Provider installer makes the necessary registry update so that Visual Studio .NET will find the assembly. If you do not use the installer and want the assembly to be listed, add a registry key. For the .NET Framework v1.x (e.g, Visual Studio 2003), add this key:

KEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\.NETFramework\AssemblyFolders\Advantage .NET

For the .NET Framework v2.x (e.g., Visual Studio 2005), add this key:

HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\.NETFramework\<framework version>\AssemblyFoldersEx\Advantage .NET

Use the correct framework version (in place of <frameworkversion>). For example:

HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\.NETFramework\ v2.0.50727\AssemblyFoldersEx\Advantage .NET

Set the default value of the registry key to name the directory where the Advantage .NET Data Provider assembly (advantage.data.provider.dll) resides. You may need to restart Visual Studio .NET in order for the change to be recognized.

If you want it to be visible only for a specific user instead of all users, add the key to HKEY\_CURRENT\_USER instead of HKEY\_LOCAL\_MACHINE.