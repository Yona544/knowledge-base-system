Setting the Classpath




Advantage Database Server 12  

Setting the Classpath

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Setting the Classpath  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - Setting the Classpath Advantage JDBC Driver jdbc\_Setting\_the\_classpath Advantage JDBC Driver > Setting the Classpath / Dear Support Staff, |  |
| Setting the Classpath  Advantage JDBC Driver |  |  |  |  |

The Advantage JDBC Driver needs to be defined in your CLASSPATH variable. The CLASSPATH is the search string that your Java Virtual Machine (JVM) uses to locate the JDBC drivers on your computer. If the drivers are not on your CLASSPATH, you receive the error "class not found" when trying to load the driver. Set your system CLASSPATH to include the following entries, where install\_dir is the path to the Advantage JDBC Driver installation directory:

install\_dir/jdbc/adsjdbc.jar

Windows Example

CLASSPATH=.;c:\program files\Advantage\jdbc\adsjdbc.jar

Linux Example

CLASSPATH=.:/usr/local/ads/jdbc/adsjdbc.jar