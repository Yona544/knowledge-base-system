---
title: Ade Tadsaepsessionmgr
slug: ade_tadsaepsessionmgr
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsaepsessionmgr.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f56e8fcf88e3dddcb30228068d5c075b2461f0aa
---

# Ade Tadsaepsessionmgr

TAdsAEPSessionMgr

TAdsAEPSessionMgr

Advantage TDataSet Descendant

| TAdsAEPSessionMgr  Advantage TDataSet Descendant |  |  |  |  |

[Methods](ade_tadsaepsessionmgr_methods.md)

Unit

AdsAEPSessionMgr

Description

TAdsAEPSessionMgr is a simple class to help developers writing Advantage Extended Procedures (AEPs) manage data modules for multiple concurrent users. TAdsAEPSessionMgr maintains a simple list of identifier/DataModule pairs. The class uses a critical section to protect the list it maintains.

A data module can be created in the AEP Startup function (called once for each Advantage connection that uses an AEP container), and a pointer to this data module can be stored in the session manager. The session manager can then be used at the beginning of each procedure to retrieve the user-specific data module instance, and work with that instance throughout the life of the Advantage Extended Procedure.An AEP template that uses the TAdsAEPSessionMgr class is available in the Delphi object repository. To view this project, select New... from the Delphi File menu. Select the Advantage tab and choose the Advantage Extended Procedure project.

Note The TAdsAEPSessionMgr is a very simple session manager. Possible enhancements include modifying the class to also store connection-specific variables, which could be used to maintain state information for multiple AEP connections.

See Also[Advantage Extended Procedures TDataSet Descendant Tutorial](master_advantage_extended_procedures_tdataset_tutorial.md)
