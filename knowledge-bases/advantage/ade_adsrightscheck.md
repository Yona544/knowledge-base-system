AdsRightsCheck




Advantage Database Server 12  

AdsTableOptions.AdsRightsCheck

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsRightsCheck  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsRightsCheck Advantage TDataSet Descendant ade\_Adsrightscheck Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsRightsCheck  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Indicates if the Advantage Database Server should perform network operating system access rights checking during file opens for [free connections](javascript:hhpopuplink.TextPopup(popid_233455464X,FontFace,-1,-1,-1,-1)).

Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.htm).

Syntax

property AdsTableOptions.AdsRightsCheck;

Description

Indicates if the client should perform file access rights checking during file opens for free connections. Options are True and False. If True is given, the client will check to see if the client workstation has visibility to the file path when creating or opening a file. If the user does not have rights to the directory or server, then the operation will fail. If AdsRightsCheck is False, the client will not perform the existence check. This allows an application developer to allow only Advantage-based applications to access specific data. See [Database Security](master_database_security.htm) for more information on rights checking.

AdsRightsCheck is ignored when used with Advantage Local Server. AdsRightsCheck is effectively treated as if it is set to True.

AdsRightsCheck is ignored with database connections. User Account database security is used for [database connections](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1)). See the "Flexible User Access Control" section in [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.