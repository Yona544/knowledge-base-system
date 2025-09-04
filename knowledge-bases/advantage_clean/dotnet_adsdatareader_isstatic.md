---
title: Dotnet Adsdatareader Isstatic
slug: dotnet_adsdatareader_isstatic
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_isstatic.htm
source: Advantage CHM
tags:
  - dotnet
checksum: aebadda1f9106df7db99729dc2f669ae79c5cd3d
---

# Dotnet Adsdatareader Isstatic

AdsDataReader.IsStatic

AdsDataReader.IsStatic

Advantage .NET Data Provider

| AdsDataReader.IsStatic  Advantage .NET Data Provider |  |  |  |  |

Indicates whether or not a result set is static (read-only) or live (updateable).

public bool IsStatic { get; }

Remarks

The IsStatic property reflects the type of cursor returned by the SQL statement (or direct table open). There is a one-to-one correlation between this property and the capability to use the [AdsCommandBuilder](dotnet_adscommandbuilder.md) to automatically generate commands for updating a result set. If this property returns False, it is not possible to use AdsCommandBuilder to generate the update commands for the statement. For information about these cursor types, see [Live versus Static Cursors](master_live_versus_static_cursors.md) in the Advantage Help file.

See Also

[AdsCommandBuilder](dotnet_adscommandbuilder.md)
