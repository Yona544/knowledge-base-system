---
title: Ade Getapplicationid
slug: ade_getapplicationid
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getapplicationid.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 168fb822f20ee6eb7692a1803f1120cc05b2c651
---

# Ade Getapplicationid

GetApplicationID

TAdsConnection.GetApplicationID

Advantage TDataSet Descendant

| TAdsConnection.GetApplicationID  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Retrieves the Application ID from the server.

Syntax

function GetApplicationID : String;

Description

GetApplicationID returns the ApplicationID as a string from the current connection in the server.

Note: If GetApplicationID was used when it is not connected to the server, then GetApplicationID method will just return whatever value in the property, not in the server.

Example

procedure TForm1.Test();

var

appID : String;

begin

{\* Get the ApplicationID \*}

appID := AdsConnection1.GetApplicationID();

end;

See Also

[TAdsConnection.ApplicationID](ade_applicationid.md)
