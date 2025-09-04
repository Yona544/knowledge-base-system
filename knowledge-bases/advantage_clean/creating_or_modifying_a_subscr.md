---
title: Creating Or Modifying A Subscr
slug: creating_or_modifying_a_subscr
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: creating_or_modifying_a_subscr.htm
source: Advantage CHM
tags:
  - creating
checksum: 526322937f3d1f1e3a5c7341d56dd29b97bdc642
---

# Creating Or Modifying A Subscr

Creating or Modifying a Subscription

Creating or Modifying a Subscription

Advantage Data Architect

| Creating or Modifying a Subscription  Advantage Data Architect |  |  |  |  |

This defines where a specific publication is to be replicated. It includes the publication name, replication target, user ID and password for the target data dictionary, and various options that control the replication actions. Note that because Advantage implements push replication, the subscription is defined at the source database; not the target/subscriber.

To create or modify a Subscription, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with CREATE SUBSCRIPTION or ALTER permissions on the specific subscription in order to add or modify Subscriptions in a database.

To add a new Subscription, from the tree view within the Connection Repository, right-click the SUBSCRIPTIONS icon and select Create.

To modify an existing Subscription's properties, from the tree view within the Connection Repository, right-click the Subscription's name icon and select Properties.

Subscription Field Descriptions

Name (required)

Name of the subscription.

Publication (required)

Publication to subscribe to.

Target Database (required)

Database to update with changes.

User Name (required)

User Name for target database.

Password (required)

Password for target database.

Disable Subscription (optional)

Disable replication of records.  Records will not be queued for later replication.

Pause Subscription (optional)

Pauses replication of records.  Records will be appended to the queue for later replication.

Queue Table (optional)

Path to the queue table used for replication.

Static Path (optional)

True if a static path should be used.

Target Connection Type (optional)

Whether to use Remote or Advantage Internet Server.

Communication Type (optional)

Type of communication to use with target server.

Options (optional)

Connection string options to when making connection to target server.

Ignore Replication Failures (optional)

If checked replication will not stop when an error is encountered.

Log Data for Failed Replication Updates (optional)

If a replication update fails, this option will cause data to be logged with it.

Forward Replicated Records (optional)

If true replicated records will be forwarded onto other replication servers.

Description (optional)

Description for the publication.
