Performing Simple Upgrades, Expansions and Replication Activation




Advantage Database Server 12  

Performing Simple Upgrades, Expansions and Replication Activation

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Performing Simple Upgrades, Expansions and Replication Activation  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Performing Simple Upgrades, Expansions and Replication Activation Advantage Database Server master\_Performing\_simple\_advantage\_database\_server\_upgrades\_and\_expansions Advantage Database Server > Installing the Advantage Database Server > Performing Simple Upgrades, Expansions and Replication Activation / Dear Support Staff, |  |
| Performing Simple Upgrades, Expansions and Replication Activation  Advantage Database Server |  |  |  |  |

A utility is provided, adsstamp.exe, which allows upgrades and expansions of the Advantage Database Server. The upgrade functionality is useful for upgrading to a new maintenance release (i.e., a new .x release) of the Advantage Database Server without having to re-run the Advantage Database Server installation program. The expansion functionality is useful to expand the Advantage Database Server to a greater number of users (given a new validation code) without having to re-run the Advantage Database Server installation program. This utility also allows the ANSI/OEM collation language and other product information that is currently being used by the Advantage Database Server to be modified.

For best results, while using a computer running a Windows operating system, run the adsstamp.exe utility from the directory in which the Advantage Database Server is installed. For example, if the Advantage Database Server is installed in the e:\Program Files\Advantage X.x\Server directory, change your current directory to e:\Program Files\Advantage X.x\Server and run adsstamp.exe.

Important Note Stop or unload the Advantage Database Server before running the adsstamp.exe utility. If you are embedding adsstamp.exe into your own application or are installing and running a Windows operating system, execute the "net stop advantage" system command to programmatically stop the Advantage Database Server".

Advantage Database Server Upgrades (to a newer version)

From the opening dialog in the adsstamp.exe, choose the Upgrade option to upgrade to a new minor (.x) version of the Advantage Database Server. On the next dialog, enter the path to the new Advantage Database Server binary (ads.exe for Windows) or use the Browse button to browse to the location of the new binary. Upon clicking the Finish button, the new version of the Advantage Database Server will be installed with the product information from the existing version of the Advantage Database Server (if new licensing or language settings are desired, choose the Languages or License option from the main dialog after the upgrade is complete). Upon a successful upgrade, the old version of the Advantage Database Server binary will be renamed ads.old.

A command line parameter of "-silent" can be passed to adsstamp.exe to suppress all dialogs when upgrading to a newer version. This option can be useful if you are embedding adsstamp.exe into your own program or installation. This option requires the new server binary to be named ads.new and to be present in the same directory as adsstamp.exe and the current server binary.

Example: adsstamp.exe -silent

If you need to change the serial number, validation code, or replication code during a silent upgrade, you can specify the new values using the sn, vc, and rc options. If new SN/VC/RP values are specified, adsstamp will use them when upgrading the existing ADS binary with the ads.new binary. If the ads.new binary is not found, adsstamp will update the existing ADS binary with the new values.

Example: adsstamp.exe silent sn:1234567 vc:ABCDE rc:ABCDE

Advantage Database Server upgrade functionality does not work with the Advantage Database Server for Linux. The upgrade functionality works with all other versions of the Advantage Database Server.

 

The adsstamp.exe utility is designed for upgrading minor (.x) versions of the Advantage Database Server, such as from Advantage Database Server v9.0 to Advantage Database Server v9.1. If upgrading to a new major (x.) version, such as upgrading from Advantage Database Server v9.1 to Advantage Database Server v10.0, it is recommended that the adsstamp.exe not be used. Run the full Advantage Database Server installation program if updating to a new major version of the Advantage Database Server.

When upgrading to a minor (.x) version of the Advantage Database Server for Windows, if Advantage Extended Procedures (AEPs) or Triggers are being used by the Advantage Database Server, the newer versions of the ACE32/ACE64.DLL and AXCWS32/AXCWS64.DLL  should be manually copied to the Advantage Database Server installation directory. The adsstamp.exe does not handle upgrading these DLLs.

Expansions, Language Selection, Product Information Modification (of an existing version), and Replication Activation

To change the current ANSI and/or OEM language setting of the Advantage Database Server, choose the Languages option from the opening dialog of the adsstamp utility. The ANSI Character Set and OEM Character Set dialogs will be displayed for you to select which languages you would like to use.

To change the current licensing information, registered owner, or startup setting (Windows only) of the Advantage Database Server, choose the License option from the opening dialog of the adsstamp utility. On the Product Information dialog, you may then change the serial number and validation code or authorization code, the registered owner, or the startup setting. Entering a new validation code with the existing serial number allows for expansion of the Advantage Database Server to a higher number of users, such as from a 10-user version of the Advantage Database Server to a 25-user version. Entering a replication code with the existing serial number enables Advantage Replication.

Note Advantage Database Server expansion and product information modification via adsstamp.exe does not work with the Advantage Database Server for Linux. It only works with the Advantage Database Server for Windows. To perform simple Advantage Database Server for Linux expansion and product information modifications, see the install.txt file that is installed with the Advantage Database Server for Linux for detailed instructions.