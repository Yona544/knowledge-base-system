---
title: Ade Adsisserverloaded
slug: ade_adsisserverloaded
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisserverloaded.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3d338be4992fffde1a9ab38943ea1d3481fbaf41
---

# Ade Adsisserverloaded

AdsIsServerLoaded

TAdsTable/TAdsQuery.AdsIsServerLoaded

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsIsServerLoaded  Advantage TDataSet Descendant |  |  |  |  |

Determines if the Advantage server is loaded.

Syntax

function AdsIsServerLoaded( strServer : String ) : Boolean;

Parameter

| strServer | String containing drive letter or server name to check. If the application uses a server name as the parameter, it must include the share name as well. For example, use "\\server\share" or "server\vol:". |

Description

AdsIsServerLoaded is used to check if an Advantage server is loaded on the specified machine. If AdsIsServerLoaded returns non-zero, this results in a connection to the server. If AdsIsServerLoaded returns 0, no server is loaded.

Example

bIsLoaded := AdsTable1.AdsIsServerLoaded( x:\data );

{ bIsLoaded equals TRUE if the Advantage Database Server is loaded on that remote server }

See Also

None.
