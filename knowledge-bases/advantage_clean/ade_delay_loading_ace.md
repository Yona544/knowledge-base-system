---
title: Ade Delay Loading Ace
slug: ade_delay_loading_ace
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_delay_loading_ace.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2734f4b6f69f063816e2408e5e2278cb03a49011
---

# Ade Delay Loading Ace

Delay-Loading the Advantage Client Engine

Delay-Loading the Advantage Client Engine

Advantage TDataSet Descendant

| Delay-Loading the Advantage Client Engine  Advantage TDataSet Descendant |  |  |  |  |

The TDataSet Descendant supports the ability to load the Advantage Client Engine (ACE) on-demand.  This functionality requires Delphi 2010 or newer.  (For prior versions of Delphi, the TDataSet Descendant will still load the ACE during the initialization of your application.)

As a result of this feature, an Advantage-enabled application will run without loading ACE (and other Advantage DLLs) until the first time an ACE API is called.  This allows application developers to accomplish some tasks that were very difficult (or impossible) before, including:

- Distributing an application that uses ACE in some configurations, but without always loading ACE.

- Performing initialization code that will execute before ACE is loaded (including altering Windows environment variables).

- Loading ACE from a specific directory (without altering the PATH environment variable).

When ACE is loaded

To fully take advantage of this functionality, it is important to understand exactly when the TDataSet will load ACE. In short, ACE will be loaded as soon as the first ACE API is called.  Due to the number of different code paths that may result in an ACE call, it may be necessary to take precautions to ensure that ACE is not loaded prematurely.  In general, most components can be instantiated and will not load ACE until they establish an Advantage connection.  One can reasonably expect this to happen with the Open method is called or the Active property is set to True. (This does mean that setting the StoreConnected or StoreActive property will cause ACE to be loaded when the form that owns the Advantage component is created.)  The exception is the TAdsSettings component, which begins making ACE calls immediately upon instantiation.

In general, the following guidelines will help delay the load of ACE as long as possible:

- Avoid using a TAdsSettings component.  This component begins making ACE calls immediately upon instantiation.  Many of the settings that required a TAdsSettings component can now be specified using the [TAdsConnection.ExtraConnectString](ade_extraconnectstring_tadscon.md) property.

- Place Advantage components on a DataModule, and avoid instantiating the DataModule until it's explicitly needed.

- Avoid setting the StoreActive (or StoreConnected) properties to true when Active (or Connected) is also true.  (The exception to this guideline is if a DataModule is used, in which case that DataModule should not be instantiated until it's needed.)
