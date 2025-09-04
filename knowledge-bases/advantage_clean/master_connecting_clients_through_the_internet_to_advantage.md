---
title: Master Connecting Clients Through The Internet To Advantage
slug: master_connecting_clients_through_the_internet_to_advantage
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_connecting_clients_through_the_internet_to_advantage.htm
source: Advantage CHM
tags:
  - master
checksum: e0e8a7a836b97695a55557ec1842d53455ac8aa5
---

# Master Connecting Clients Through The Internet To Advantage

Connecting Clients Through the Internet to Advantage

Connecting Clients through the Internet to Advantage

Advantage Database Server

| Connecting Clients through the Internet to Advantage  Advantage Database Server |  |  |  |  |

In order for your application to use the Advantage Internet Server functionality, you must configure your application to use the Advantage Internet Server server type. You must also specify the location of the Internet-enabled Advantage Internet Server. See [Specifying the Advantage Internet Server Location](master_specifying_the_advantage_internet_server_location.md) for details not included in this topic. Specifying the server type is different depending upon which Advantage client you are using. Below describes specification for each client:

Advantage Client Engine API

To connect to an Advantage Database Server over the Internet using the Advantage Client Engine API, you will need to call AdsConnect60 with the full path to the data dictionary and with ADS\_AIS\_SERVER as the second parameter or as part of the second parameter. Example:

ulRetVal = AdsConnect60( "q:\\test.add",

ADS\_AIS\_SERVER,

"User1",

"foobar",

ADS\_DEFAULT,

&hConnect );

Where drive letter "Q" is specified in ADS.INI as the Advantage Database Server you want to connect to over the Internet. See [Specifying the Advantage Internet Server Location](master_specifying_the_advantage_internet_server_location.md) for details on specifying the first parameter (the path to the Advantage Data Dictionary).

Advantage TDataSet Descendant

There are several ways to configure the Advantage Internet Server server type in the Advantage TDataSet Descendant.

- Set your TAdsSettings components AdsServerTypes property to include stADS\_AIS.

- Set your TAdsDictionary components AdsServerTypes property to include stADS\_AIS.

- Set your TAdsConnection components AdsServerTypes property to include stADS\_AIS.

Using the TAdsConnection components AdsServerTypes property is typically the recommended method. Additionally, in your connection path you need to specify the full path to a data dictionary.

Advantage ODBC Driver

The Advantage ODBC Driver can be configured through the Data Sources administrator.

| 1. | Select Internet Server (AIS) from the Available Server Types. |

| 2. | In the Database or Data Dictionary Path field, enter the path to your data dictionary. In this example "Q" is the drive that is specified in ADS.INI to be our "Internet Enabled" Advantage Database Server location. |

When connected, enter a username/password from the Advantage Data Dictionary on the username/password dialog.

Advantage OLE DB Provider

Specify the path to your Advantage Data Dictionary file as the Data Source, where the drive letter is mapped to a server in the ADS.INI file (if using a drive letter). Specify ADS\_AIS\_SERVER for the ServerType, or as part of the ServerType.

Provider=Advantage.OLEDB.1;User ID=adssys;Data Source=q:\foobar.add;Persist Security Info=False;ServerType=ADS\_AIS\_SERVER

Advantage .NET Data Provider

Specify the path to your Advantage Data Dictionary file as the Data Source, where the drive letter is mapped to a server in the ADS.INI file (if using a drive letter). Include ADS\_AIS\_SERVER (or AIS) in the ServerType connection string property. For example:

AdsConnection conn = new AdsConnection( @"data source=\\server:2001\share\data\test.add;servertype=AIS;user id=test;password='passwd'" );

Advantage PHP Extension

To connect to an Advantage Database Server over the Internet using the Advantage PHP Extension, your Advantage Data Dictionary file must be specified as the value of the DataDirectory keyword. In addition, the value of the ServerType keyword must be modified to include Advantage Internet Server, which has a value of 4.

<?

echo "Basic Connect<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\mydictionary.add;ServerTypes=4", "User1", "foobar" );

echo "Connect<br>\n";

ads\_close( $rConn );

echo "Closed<br>\n";

?>

Advantage DBI Driver

To connect to an Advantage Database Server over the Internet using the Advantage DBI Driver, the path to your Advantage Data Dictionary file must be specified as the value of the DataDirectory keyword. In addition, the value of the ServerType keyword must be modified to include Advantage Internet Server, which has a value of 4.

use DBI;

use strict;

 

 

my $dbh1 = DBI->connect(

'dbi:Advantage:DataDirectory=\\server1\share1\data\mydictionary;ServerTypes=4;',"User1",

"foobar", {AutoCommit => 1 } )

or die "Can't Make Connection\n";

 

$dbh1->disconnect or warn "Couldn't disconnect\n";

Advantage CA-Visual Objects RDDs

To connect to an Advantage Data Dictionary, include the ACE.AEF and DBFAXS.AEF libraries in the project. Connect via the Advantage Client Engine API AdsConnect60 (see Advantage Client Engine API above for AIS-specific details for the first and second parameters). Sample code:

LOCAL oDB AS DBServer

LOCAL dwError AS DWORD

LOCAL pacError AS PSZ

LOCAL wLen AS WORD

LOCAL lReturn AS LONGINT

LOCAL hConnect AS LONGINT

 

pacError := MemAlloc( 200 )

wLen := 200

dwError := AE\_SUCCESS

 

/\*

\* HandleErrors is a function you may write to catch and handle

\* connection errors.

\*/

HandleErrors( AdsConnect60( "X:\DATA\TEST.ADD",

ADS\_AIS\_SERVER, "UserName", "Password", ;

ADS\_INC\_USERCOUNT, @hConnect ) )

 

/\* Set the connection handle \*/

AX\_SetConnectionHandle( hConnect )

 

/\*

\* Since a database path is specified in the connection, it does

\* not need to be specified here. No extension to the table name is

\* needed unless the table name in the Data Dictionary includes

\* an extension.

\*/

oDB := DBServer { "MYTABLE", DBShared, , "ADSADT" }

 

AdsGetLastError( @dwError, pacError, @wLen )

IF dwError != AE\_SUCCESS

ErrorBox{, " Advantage error = " + Psz2String(pacError)}:Show()

ENDIF

ErrorBox{ , " SUCCESS" }:Show()

 

/\* Clear the connection handle. It is not required to clear the

\* connection handle unless you no longer want to use hConnect as

\* the connection handle for future table opens.

\*/

AX\_SetConnectionHandle( 0 )

 

oDB:Close()

CA-Clipper

See the Advantage IP for CA-Clipper readme.txt file for information about connecting through the Internet to Advantage Database Server with CA-Clipper.
