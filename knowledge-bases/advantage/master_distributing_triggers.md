Distributing Triggers




Advantage Database Server 12  

Distributing Triggers

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Distributing Triggers  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Distributing Triggers Advantage Concepts master\_Distributing\_triggers Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Distributing Triggers  Advantage Concepts |  |  |  |  |

Script triggers are stored inside the database and require no extra distribution efforts.

Other trigger containers need to be distributed along with the database (the .add file).

WIN32 DLLs and Linux shared objects should be distributed with the .add file. Place them on the disk using the same relative path as when they were registered.

COM containers and .NET Assemblies can be installed anywhere on the server machine. These containers must be registered using either regsvr32.exe (for COM containers) or regasm (for .NET assemblies). See the documentation that came with your development environment for registration details.