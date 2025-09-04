---
title: Ace Adscreatesavepoint
slug: ace_adscreatesavepoint
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscreatesavepoint.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 12876858a4e62d208e04310fc5babbed7cbef7de
---

# Ace Adscreatesavepoint

AdsCreateSavepoint

AdsCreateSavepoint

Advantage Client Engine

| AdsCreateSavepoint  Advantage Client Engine |  |  |  |  |

Creates a savepoint in the current transaction.

Syntax

UNSIGNED32 AdsCreateSavepoint (ADSHANDLE hConnect,

UNSIGNED8 \*pucSavepoint,

UNSIGNED32 ulOptions );

Parameters

| hConnect (I) | Connection handle with an active transaction to create a savepoint on. |
| pucSavepoint(I) | The name of the savepoint to be created. |
| ulOptions(I) | Options for the command. At this time there are no options. |

Remarks

AdsCreateSavepoint creates a savepoint on the active transaction to which the transaction can be rolled back. Rolling back to a savepoint does not end the transaction and only undoes the work performed after the savepoint was created. After rolling back to a savepoint, the savepoint continues to exist and can be rolled back to multiple times. Creating a savepoint with the same name as an existing savepoint destroys the existing savepoint and creates a new savepoint in the transaction at the current location.

Note AdsBeginTransaction has no effect when used with the Advantage Local Server.

See Also

[AdsCommitTransaction](ace_adscommittransaction.md)

[AdsRollbackTransaction](ace_adsrollbacktransaction.md)

[AdsRollbackTransaction80](ace_adsrollbacktransaction80.md)

[AdsFailedTransactionRecovery](ace_adsfailedtransactionrecovery.md)

[AdsConnect](ace_adsconnect.md)

[AdsInTransaction](ace_adsintransaction.md)
