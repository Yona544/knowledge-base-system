Advantage PHP PDO Driver




Advantage Database Server 12  

Advantage PHP PDO Driver

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage PHP PDO Driver  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - Advantage PHP PDO Driver Advantage PHP Extension php\_Advantage\_PDO\_Driver Advantage PHP Extension > Advantage PHP PDO Driver / Dear Support Staff, |  |
| Advantage PHP PDO Driver  Advantage PHP Extension |  |  |  |  |

Advantage PHP PDO Driver

The Advantage PHP PDO Driver is a PHP module designed to provide an alternate mechanism for database access from the PHP environment.

PHP Data Objects (PDO) allows for a consistent interface for accessing database in PHP.   More information can be found here: <http://php.net/manual/en/book.pdo.php>

Installation:

Windows:

1] Verify the file version of the compiled extension matches the version of PHP installed on the machine. The default location of the extension is \Program Files\Advantage X.x\PHP\.

The extension is name pdo\_advantage.dll.5.x.y, which should correspond to the version of PHP on the computer.

2] Copy the pdo\_advantage.dll.5.x.y to the PHP extension directory with the name pdo\_advantage.dll.

3] Locate the php.ini file and add the following entry under the Windows Extensions section:

extension=pdo\_advantage.dll

4] Restart the web server.

Linux:

1) Untar and Unzip the PHP source.

#tar -zxvf php-5.x.x.tar.gz

2) Run the Advantage PHP Extension installer.

#setup.pl  
or  
#perl setup.pl

3) Follow the installer prompts.

4) In the PHP source directory type:

#./buildconf

This will include the Advantage PDO Extension in the PHP build and install.

5) Configure PHP with Advantage by using

-with-pdo\_advantage

For example to install the Advantage Extension in Apache with PHP as a DSO type the following:

#./configure --with-pdo\_advantage

6) Make and Install PHP:

#make  
#make install

 

Example:

<?PHP

$pdoDBH = new PDO( "advantage:Data Source=//server:6262/share/;ServerType=Remote;" );

$pdoDBH->setAttribute( PDO::ATTR\_ERRMODE, PDO::ERRMODE\_EXCEPTION );

$pdostmtStatement = $pdoDBH->query( "select \* from testtable" );

$iNumRows = $pdostmtStatement->rowCount();

$aArray = $pdostmtStatement->fetchAll( PDO::FETCH\_ASSOC );

print\_r( $aArray );

$pdostmtStatement->closeCursor();

$pdoDBH = null;

?>