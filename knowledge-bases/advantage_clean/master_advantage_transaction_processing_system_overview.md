---
title: Master Advantage Transaction Processing System Overview
slug: master_advantage_transaction_processing_system_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_transaction_processing_system_overview.htm
source: Advantage CHM
tags:
  - master
checksum: 06e698b14e46758f7e140cbc6940e9719d190341
---

# Master Advantage Transaction Processing System Overview

Advantage Transaction Processing System Overview

Advantage Transaction Processing System Overview

Advantage Concepts

| Advantage Transaction Processing System Overview  Advantage Concepts |  |  |  |  |

In networked environments, tables and their associated indexes are susceptible to corruption if a workstation crashes or a network failure occurs while the tables and index files are being updated. Building an audit trail to monitor these failures is difficult. Developing a method to recover from incomplete updates is even more difficult. Advantage TPS eliminates these problems and protects database integrity by automatically undoing any updates that were performed in the event of workstation or network failure. This leaves a database exactly as it was before a transaction began. Advantage brings this functionality, which is not available in non-client/server products, to your network database applications.

If an application is halfway through a series of updates and the decision is made, for whatever reason, to not continue, the Advantage TPS will abort all updates. Advantage will "undo" the changes that are marked in your application as a transaction. By "undoing" the changes, your database will be in a state exactly as it was before the transaction began.

While updates are being made within a transaction, the Advantage TPS hides the updates from other users until the data is committed. The uncommitted data is visible only to the application performing the transaction. The other applications view the data as it was before the transaction began. If the transaction is rolled back, the uncommitted data is never seen by any users other than the one who was performing the transaction. If the transaction is committed, the updated data becomes visible all at once. This hiding of uncommitted data is not available in existing non-client/server applications.

Example of a Transaction

To better illustrate a "transaction", consider the following example. A programmer is developing an order processing module. The module allows users to input a customer order, asking for customer information and parts to be ordered. The order information is entered by the user on the screen.

For this example, three items are being purchased by one customer. When the order is completed, four tables and their associated indexes are to be updated. The tables to be updated are: an Order Table, a Customer Table, a Parts List Table, and an Inventory Table. The order of database changes occur as follows:

| 1. | The order is inserted into the Order Table. |

| 2. | The customer name and address is updated in the Customer Table, if necessary. |

| 3. | Each ordered part is inserted into the Parts List Table. |

| 4. | Part quantities are adjusted in the Inventory Table. |

For this order, a total of eight records are either inserted or updated in these tables. A record is inserted into the Order Table containing the order information. A Customer Table record is updated with the new address information. Three parts are being ordered, so three records are inserted into the Parts Table and three records are updated in the Inventory Table. All of these insertions and updates also cause updates to the associated index files.

With the Advantage TPS, the insertions and updates in the above scenario are considered one transaction. The Advantage TPS logs the insertions and updates to a transaction log file. At any time during the transaction, the insertions and updates can be aborted by issuing a statement to roll back the transaction. To save all of the information in the transaction, issue a commit transaction statement, and all the changes to the tables and associated indexes will be written at one time. Without the Advantage TPS, there is the possibility that only some of these table and index updates are successfully completed. If only a portion of these updates are successful, the tables and index files are logically corrupt since the data is not consistent in all locations. By using the Advantage TPS, the programmer can ensure that all inserts and updates to the tables and indexes are either completely updated or not updated at all.
