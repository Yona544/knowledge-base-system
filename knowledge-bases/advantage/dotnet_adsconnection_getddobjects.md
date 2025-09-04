AdsConnection.GetDDObjects




Advantage Database Server 12  

AdsConnection.GetDDObjects

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.GetDDObjects  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.GetDDObjects Advantage .NET Data Provider dotnet\_Adsconnection\_getddobjects Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.GetDDObjects / Dear Support Staff, |  |
| AdsConnection.GetDDObjects  Advantage .NET Data Provider |  |  |  |  |

Retrieves the names of objects of the specified type from an open data dictionary.

public object[] GetDDObjects( AdsObjectType type, string strParent );

Remarks

GetDDObjects finds objects in the data dictionary matching the specified AdsObjectType and returns the object names in an array. The strParent parameter is the name of the object that is the parent or owner of the objects searched for. This parameter is ignored when searching for table, view, user group or referential integrity objects. When searching for an index file or a field object, strParent should supply the name of the associated table object. When searching for a user, strParent can optionally supply the name of the user group to limit the search result to users who are members of the user group.

Note The AdsConnection must be open on a data dictionary connection when GetDDObjects is called.

See Also

[AdsObjectType](dotnet_adsconnection_adsobjecttype.htm)