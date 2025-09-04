ADS and Java




Advantage Database Server 12  

     ADS and Java

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS and Java  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      ADS and Java Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_ADS\_and\_Java\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 16 - Advantage and Java > ADS and Java / Dear Support Staff, |  |
| ADS and Java  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

JDBC (Java database connectivity) is the core technology for accessing data from Java applications, applets, and servlets. Furthermore, using the JDBC Connector, available from Sun Microsystems, you can use this JDBC driver with any J2EE-compliant server. The Advantage JDBC Driver, named ADSDriver, is located in the com.extendedsystems.jdbc.advantage namespace. Once you have registered this driver and obtained a connection from the DriverManager, you access your Advantage data using the classes and interfaces of the java.sql namespace.

The Advantage JDBC Driver is a class 4 JDBC driver. Unlike class 1, class 2, and class 3 JDBC drivers, a class 4 driver requires no additional libraries, beyond the Java driver itself, to connect to the underlying data. With the Advantage JDBC Driver, the connection to ADS is accomplished using sockets. Unlike the other Advantage data access mechanisms, the Advantage JDBC Driver does not require the services of the Advantage Client Engine (ace32.dll and libace.so are the ACE libraries for Windows and Linux, respectively).

   
NOTE: Class 4 JDBC drivers connect directly to a server without requiring the installation of client drivers. Consequently, you can only use the Advantage JDBC Driver with ADS (since ALS is not a server).  
 

The Advantage JDBC Driver communicates with ADS using TCP/IP port 6262 by default. If you need to communicate with ADS using a different port number on the server, you must change the server configuration. See the Advantage help for information on how to configure your TCP/IP (transmission control protocol/Internet protocol) port number for the version of the ADS server that you are using.

Before you can use the Advantage JDBC Driver, you must install the adsjdbc.jar file and add it to your CLASSPATH environment variable. Java uses CLASSPATH to locate Java classes and other resources at runtime. The Advantage JDBC Driver installation will automatically install the JAR file. Depending on which environment you install the driver on, you may have to add the JAR file location to your CLASSPATH variable manually.

This chapter shows you how to access ADS using the Advantage JDBC Driver. This discussion is divided into three major sections. The first section describes common tasks, such as connecting to ADS, executing queries, and calling stored procedures. The second section shows you how to perform basic navigation with JDBC, and the third section demonstrates several basic administrative tasks, such as creating tables and granting rights to them.

The use of the Advantage JDBC Driver is demonstrated in this chapter using Borland's JBuilder, a popular Java IDE (integrated development environment). Figure 16-1 shows the AdsJava.jpx project opened in JBuilder 2006, with the public JFrame class (named MainFrame) displayed in the JBuilder designer.

Figure 16-1: The MainFrame JFrame class in the JBuilder designer

   
NOTE: This same project can be created with almost any version of Java. Many earlier versions of JBuilder can also be used, as well as Java projects created with other development environments.  
 

 

   
CODE DOWNLOAD: The sample code in this chapter can be found in the JBuilder project named AdsJava.jpx, available with this book's code download (see Appendix A).  
 

Even if you do not have a copy of JBuilder, you can still explore this project using the JDK (Java Development Kit) available from Sun Microsystems. Simply compile the two Java source files named Application1.java and MainFrame.java using javac.exe, the Java compiler. Once you have compiled these .java files into byte-code class files, launch the application by running the Application1.class file using java.exe, the Java runtime launcher. The Application1 class contains the public, static main method entry point.