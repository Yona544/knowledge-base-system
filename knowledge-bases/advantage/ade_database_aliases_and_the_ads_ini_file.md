Database Aliases and the ads.ini File




Advantage Database Server 12  

Database Aliases and the ads.ini File

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Database Aliases and the ads.ini File  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Database Aliases and the ads.ini File Advantage TDataSet Descendant ade\_Database\_aliases\_and\_the\_ads\_ini\_file Advantage TDataSet Descendant > Developing and Distributing Applications > Database Aliases and the ADS.INI File / Dear Support Staff, |  |
| Database Aliases and the ads.ini File  Advantage TDataSet Descendant |  |  |  |  |

The Advantage TDataSet Descendant supports database aliases. The database alias is used by Advantage components to reference a database directory on disk. The alias is associated to a path and may change when the data files are moved to different directories, drives, or file servers. The alias name must be established prior to being used by the application.

Database aliases and their values are read from a file named ads.ini. See [ads.ini File Support](master_ads_ini_file_support.htm) for details on where the ads.ini file can reside.

The alias file must be of this format:

[Databases]

ALIASNAME=c:\path;x

where x is N, C, A, V, or D.

N=ttAdsNTX

C=ttAdsCDX

A=ttAdsADT

V=ttAdsVFP

D=Advantage Data Dictionary connection

Examples:

[Databases]

TEST\_NTX=X:\data;N

TEST\_CDX=X:\data;C

TEST\_ADT=X:\data;A

TEST\_VFP=X:\data;V

TEST\_DICTIONARY=X:\data\mydictionary.add;D

Aliases may be used in the following ways:

|  |  |
| --- | --- |
| · | You may use a TAdsConnection component. The [TAdsConnection.ConnectPath](ade_connectpath_tadsconnection.htm) property and the new [TAdsConnection.AliasName](ade_aliasname_tadsconnection.htm) property are mutually exclusive. If you enter data into one property, the other will be cleared automatically. Once the AliasName property is filled in, all TAdsTable instances that are connected to this TAdsConnection component that have blank TAdsTable.DatabaseName properties will use the alias. The TAdsTable.TableType properties will be changed to use the table type associated with the alias. |

|  |  |
| --- | --- |
| · | Regardless if a TAdsTable instance uses a TAdsConnection component, the [TAdsTable.DatabaseName](ade_databasename.htm) property may be filled in with a path or an alias, or left blank. If left blank, the alias information from the TAdsConnection listed in the TAdsTable.AdsConnection property will be used. This would be the suggested use of aliases. If an alias or path is entered in the TAdsTable.DatabaseName property, the alias information from the TAdsConnection will be overridden. If an alias is entered, the TAdsTable.TableType property will be changed to use the table type associated with that alias. |

|  |  |
| --- | --- |
| · | If the path specified in the alias is to an Advantage Data Dictionary file all Advantage components attached to the connection can access the tables, views, and stored procedures defined in the dictionary. See [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm). |