Important Notes




Advantage Database Server 12  

Important Notes

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Important Notes  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Important Notes Advantage .NET Data Provider dotnet\_Important\_notes Advantage .NET Data Provider > Introduction > Important Notes / Dear Support Staff, |  |
| Important Notes  Advantage .NET Data Provider |  |  |  |  |

"Object Reference not set" Error

If you receive "Object reference not set to an instance of an object" errors when dropping AdsCommand or AdsDataAdapter objects onto a form in the Visual Studio IDE, it may be helpful to put the Advantage .NET Data Provider assembly into the Global Assembly Cache (GAC) during development. The IDE sometimes copies assemblies to temporary directories and then loads copies from the temporary directory. If the designer loads the assembly from a different location, it is unable to use the object instance created by the IDE and will result in this error. When the assembly is in the GAC, it will always be loaded from that location.

To put the assembly in the GAC, use the Microsoft-supplied utility gacutil.exe. The following command will install the assembly in the Global Assembly Cache:

gacutil /i advantage.data.provider.dll

To remove it from the Global Assembly Cache, use this command:

gacutil /u advantage.data.provider

As an alternative to putting the assembly in the GAC, you can also sometimes avoid this error by setting the CopyLocal option of the Advantage.Data.Provider assembly to False.