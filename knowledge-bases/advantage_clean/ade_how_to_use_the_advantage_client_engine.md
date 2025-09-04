---
title: Ade How To Use The Advantage Client Engine
slug: ade_how_to_use_the_advantage_client_engine
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_how_to_use_the_advantage_client_engine.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f730a69f075075ce7f674c65f110fb2c302e66ea
---

# Ade How To Use The Advantage Client Engine

How to Use the Advantage Client Engine

How to Use the Advantage Client Engine

Advantage TDataSet Descendant

| How to Use the Advantage Client Engine  Advantage TDataSet Descendant |  |  |  |  |

The Advantage Client Engine uses handles to identify every connection, table, and index. The Advantage TDataSet Descendant components wrap the handle values. Therefore, you do not need to access the handles unless you plan to call the Advantage Client Engine directly. To retrieve the handle for a specific object, use the Advantage extended methods [GetAceTableHandle](ade_getacetablehandle.md), [GetAceIndexHandle](ade_getaceindexhandle.md), [GetAceOrderHandle](ade_getaceorderhandle.md), and [GetAceConnectionHandle](ade_getaceorderhandle.md).These methods return connection, table, and/or index handles associated with an AdsDataSet instance. Once these handles are obtained, they can be used to call Advantage Client Engine APIs directly.

All available Advantage Client Engine APIs are documented in the Advantage Client Engine Help (ACE.HLP). (Note that each of the Advantage products and their corresponding Help files are installed separately.)

The prototype syntax in this Help file is in 'C'. To see the prototype syntax in Delphi/Pascal, find the function prototype in ACE.PAS, which is installed with the Advantage TDataSet Descendant.

To use Advantage Client Engine APIs directly in your code, add ACE.PAS to the "uses" clause. Then prefix the Advantage Client Engine API call with "ACE.". For example:

ulRetVal := ACE.AdsMgGetUserNames( hMgmtHandle, pchar( AdsTable1.TableName ), 0, @astUserInfo, @usArrayLen, @usSize );

The source code for the Advantage TDataSet Descendant extended methods is provided in the ADSFUNC.PAS file. This source code is an excellent example of how to use the Advantage Client Engine API.

Note It is possible to change the state of the Advantage Client Engine by calling the Advantage Client Engine APIs directly. The TAdsTable instances may make certain assumptions about the state of the Advantage Client Engine that can cause problems. The TDataSet method CheckBrowseMode is useful for synchronizing the state of the components and the underlying engine.
