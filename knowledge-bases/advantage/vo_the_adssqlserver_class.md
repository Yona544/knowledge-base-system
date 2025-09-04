The AdsSQLServer Class




Advantage Database Server 12  

The AdsSQLServer Class

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The AdsSQLServer Class  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - The AdsSQLServer Class Advantage AXSQL RDDs vo\_The\_adssqlserver\_class Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > The AdsSQLServer Class / Dear Support Staff, |  |
| The AdsSQLServer Class  Advantage AXSQL RDDs |  |  |  |  |

The AdsSQLServer class is a class library that descends from the DBServer class with some additional functionality specific to the AXSQL RDDs. The majority of its methods and properties are exactly the same as the DBServer class. Although the AdsSQLServer class isnt required to use the AXSQL RDDs, only the most basic functionality will be available without it. Therefore it is highly recommended that it is always used with the AXSQL RDDs.

The AdsSQLServer class supports SQL parameters by passing in an array of key-value pairs to the constructor (init) or Refresh methods.  More information about using parameters with AdsSQLServer can be found on the [Parameter Support](vo_axsql_parameters.htm) page