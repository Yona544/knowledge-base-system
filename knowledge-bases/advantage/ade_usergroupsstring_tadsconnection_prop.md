UserGroupsString




Advantage Database Server 12  

TAdsConnection.UserGroupsString

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.UserGroupsString  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.UserGroupsString Advantage TDataSet Descendant ade\_Usergroupsstring\_tadsconnection\_prop Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.UserGroupsString  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Semi-colon delimited list of groups the current user belongs to.

Syntax

property UserGroupsString: string;

Description

UserGroupsString contains a semi-colon delimited list of groups the current user belongs to. If you are using Delphi/C++Builder version 5 or greater, use the [UserGroups](ade_usergroups_tadsconnection_prop.htm) property.

This string can either be used directly, or modified to contain coma delimiters instead of semi-colon delimiters and placed into a TStringList object. Beware that colons are valid characters in user names.

The UserGroupsString is only applicable to [database connections](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1)), and will be empty if called on a [free connection](javascript:hhpopuplink.TextPopup(popid_233455464X,FontFace,-1,-1,-1,-1)). If called on an inactive connection, UserGroupsString will return an empty string.

See Also

[UserGroups](ade_usergroups_tadsconnection_prop.htm)

[Username](ade_username_tadsconnection.htm)