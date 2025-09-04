UserGroups




Advantage Database Server 12  

TAdsConnection.UserGroups

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.UserGroups  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.UserGroups Advantage TDataSet Descendant ade\_Usergroups\_tadsconnection\_prop Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.UserGroups  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

String list of groups the current user belongs to.

Syntax

property UserGroups: TStringList;

Description

UserGroups is a list of groups the current user belongs to. The UserGroups property is only supported in Delphi/C++Builder versions 5 or greater. If using an older version of Delphi or C++Builder, use the [UserGroupsString](ade_usergroupsstring_tadsconnection_prop.htm) property.

The UserGroups is only applicable to [database connections](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1)), and will be empty if called on a [free connection](javascript:hhpopuplink.TextPopup(popid_233455464X,FontFace,-1,-1,-1,-1)). If called on an inactive connection, UserGroups will be empty.

See Also

[UserGroupsString](ade_usergroupsstring_tadsconnection_prop.htm)

[Username](ade_username_tadsconnection.htm)