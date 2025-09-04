---
title: Master More Suited For Future Enhancements
slug: master_more_suited_for_future_enhancements
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_more_suited_for_future_enhancements.htm
source: Advantage CHM
tags:
  - master
checksum: bc8d0d12057cb168b1f74bcaabc5d33a212efb8d
---

# Master More Suited For Future Enhancements

More Suited for Future Enhancements

More Suited for Future Enhancements

Advantage Concepts

| More Suited for Future Enhancements  Advantage Concepts |  |  |  |  |

Advantage proprietary ADT tables have information in the table header that will keep the table from being opened if the data dictionary in which field level constraints for the table are defined is not also open. Xbase DBF tables have no such information in the table header. Thus, when Advantage has support for a data dictionary, enforcement of functionality such as field value constraints can be guaranteed in ADT tables, but not necessarily in DBF tables if that DBF table is opened while the corresponding data dictionary is not open.

The Advantage proprietary file format table header has been designed to allow support for field level encryption at the Advantage level. Although this functionality is not yet supported, it is functionality that could not be easily implemented in Xbase file formats.

The Advantage proprietary file format table header has been designed to support up to 65535 different field types. Xbase files can support nowhere near this many field types. If there is ever a need to support many different field types, this will only be possible with the Advantage proprietary file format.
