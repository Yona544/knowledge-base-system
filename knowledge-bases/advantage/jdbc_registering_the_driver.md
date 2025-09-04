Registering the Driver




Advantage Database Server 12  

Registering the Driver

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Registering the Driver  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - Registering the Driver Advantage JDBC Driver jdbc\_Registering\_the\_driver Advantage JDBC Driver > Registering the Driver / Dear Support Staff, |  |
| Registering the Driver  Advantage JDBC Driver |  |  |  |  |

Registering the driver tells the JDBC driver manager which driver to load. When loading a driver using class.forName(), you must specify the name of the driver:

com.sap.jdbc.advantage.ADSDriver

For example:

Class.forName("com.sap.jdbc.advantage.ADSDriver");