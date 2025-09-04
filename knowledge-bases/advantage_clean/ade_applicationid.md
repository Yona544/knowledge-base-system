---
title: Ade Applicationid
slug: ade_applicationid
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_applicationid.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fc45b2049d92b4ad75b768730eaa1e0722a1359f
---

# Ade Applicationid

ApplicationID

TAdsConnection.ApplicationID

Advantage TDataSet Descendant

| TAdsConnection.ApplicationID  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the Application ID for the connection. If this property is left empty, the Application ID is initialized to be the file name of the application (executable) that created the connection.

For efficiency, this property is only used to specify the ApplicationID, it is not automatically populated on connection. To read the ApplicationID of an active connection, call the TAdsConnection.GetApplicationID method.

This property is not used internally by Advantage, but provided strictly for use by application developers. The ApplicationID is often used for auditing purposes.

The ApplicationID is a wrapper around the canned procedures sp\_SetApplicationID and sp\_GetApplicationID.

Syntax

property ApplicationID: String;

Description

Provide a value in the ApplicationID property.

See Also

[TAdsConnection.GetApplicationID](ade_getapplicationid.md)
