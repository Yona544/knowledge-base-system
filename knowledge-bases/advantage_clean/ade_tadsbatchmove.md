---
title: Ade Tadsbatchmove
slug: ade_tadsbatchmove
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsbatchmove.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9138281786126bd59b324bc1f10cf0799ab4a29f
---

# Ade Tadsbatchmove

TAdsBatchMove

TAdsBatchMove

Advantage TDataSet Descendant

| TAdsBatchMove  Advantage TDataSet Descendant |  |  |  |  |

| [Properties](ade_tadsbatchmove_properties.md) | [Methods](ade_tadsbatchmove_methods.md) |  |

 

TAdsBatchMove is a component provided to help users convert existing applications that make use of the BDE TBatchMove component.

It should be noted that the TAdsBatchMove component is not always the most efficient method to move a batch of records when using Advantage. The TAdsBatchMove component is provided as a tool to make porting existing applications easier. The majority of the functionality this component provides must be performed on the client. This client-side processing has a significant affect on performance.

Currently the batCopy mode is the only mode that will make the most efficient use of Advantage. If your application uses other modes (for example, batUpdate) it is recommended you use the TAdsBatchMove when porting your application, but later revisit this component and replace its usage with a more efficient approach.

Developers writing new functionality are encouraged to find another means to move a batch of records. Alternatives include:

- The INSERT INTO statement, via SQL

- The SELECT INTO statement, via SQL

- The AdsCopyTable function (which exists in TAdsTable, TAdsQuery, and as an ACE API)

- The AdsCopyTableContents function (which exists in TAdsTable, TAdsQuery, and as an ACE API)
