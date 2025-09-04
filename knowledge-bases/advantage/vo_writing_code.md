Writing Code




Advantage Database Server 12  

Writing Code

Advantage Visual Objects RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Writing Code  Advantage Visual Objects RDD |  |  | Feedback on: Advantage Database Server 12 - Writing Code Advantage Visual Objects RDD vo\_Writing\_code Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Writing Code  Advantage Visual Objects RDD |  |  |  |  |

Specifying an Advantage RDD as the default RDD

If you are writing code to manipulate the database files (rather than generating code with the IDE), specifying the RDD is easy. Simply reference the RDD in your USE VIA command or set the default RDD, using the function [RDDSetDefault(),](vo_using_rddsetdefault_to_specify_the_advantage_rdd.htm) in your code.

Visual Objects will automatically reference the specified RDD. Recompile the application. Once the RDD is specified, it will load and run the Advantage communication library automatically.

Specifying an Advantage RDD as-needed

To access the Advantage RDD on an as-needed basis instead of specifying it as the application default RDD, you may reference the RDD using object-oriented code or with procedural code.

Object-oriented:

If you are modifying a DBServer class, you may modify the code to reference an Advantage RDD. If the SetSelectiveRelation method is to be used, the server class must inherit from AdsDBServer instead of DBServer.

The DBServer:Init method has four parameters. Modify the fourth parameter in the function to an Advantage RDD name.

DBServer:Init( oFileSpec, lShareMode, lReadOnlyMode, "DBFNTXAX" )

If the fourth parameter is not supplied, the DBServer class uses the default RDD.

Procedural:

To specify the Advantage RDD in procedural code, use the VIA clause in your USE command.

For example, if DBFNTX is the default RDD, you can access the Advantage .ntx RDD as follows:

USE test.dbf VIA "DBFNTXAX" SHARED NEW

If the Advantage RDD is the default RDD, you can access DBFNTX or another RDD as follows:

USE test.dbf VIA "DBFNTX" SHARED READONLY NEW