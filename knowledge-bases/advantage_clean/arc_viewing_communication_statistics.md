---
title: Arc Viewing Communication Statistics
slug: arc_viewing_communication_statistics
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_viewing_communication_statistics.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: a67d3f7c3ce161de8ab35d47f19b0286663578da
---

# Arc Viewing Communication Statistics

Viewing Communication Statistics

Viewing Communication Statistics

Advantage Data Architect

| Viewing Communication Statistics  Advantage Data Architect |  |  |  |  |

The Communication Statistics screen shows the packet and low-level network status.

Field Descriptions

Total Packets Received

This value represents all data packets received from Advantage clients since the Advantage Database Server was loaded/started.

Check-Sum Failures

The number of corrupted packets received over the network. The Advantage Database Server ignores corrupted packets and new packets are sent again from the Advantage client.

Receive Packets Out of Sequence

The number of packets received out of sequence. Communication packets are assigned sequence numbers. These packets are sent between the client and the Advantage Database Server. If a packet is received out of sequence, this value is incremented. Packets may be out of sequence as the result of a packet getting lost on the network, which may cause it to show up after others were received. If a packet is out of sequence, the Advantage Database Server ignores it and waits for the resend.

Receive Requests Out of Sequence

The client is requesting a resend of a packet from the Advantage Database Server but the Advantage Database Server no longer has the packet available. Identify the client that is generating the re-sends. Exit the application and restart it. Monitor the results.

Packet Owner Not Logged In

The Advantage Database Server was unable to communicate with a client properly and closed the connection. This occurs when a request for an operation, such as a Seek, is made before the user is properly connected to the Advantage Database Server. Verify that your application is properly connecting to the Advantage Database Server. This value is incremented when the Advantage Database Server initiates a disconnect, and the client is still generating disconnect requests.

Server Initiated Disconnect

A normal client disconnect consists of two steps initiated by the client: 1) the semaphore connection file is closed, and 2) a disconnect request is made. If a client PC crashes, is turned off without first logging off the network, or if the network goes down, a normal disconnect will not occur. The Advantage Database Server "watch dog" thread determines that the client is gone and disconnects the client automatically. This can also occur on a busy network when step 2 above is not immediately serviced after step 1 occurs.

Removed Partial Connection

When a client connects to the Advantage Database Server, a reply is sent to the client. The Advantage Database Server waits for a response from the client to acknowledge that the reply has been received. If the client does not send a response, the Advantage Database Server terminates the connection. This is a symptom of an extremely busy network.

Invalid Packets

Number of invalid packets received specifically by the Advantage Database Server. These are packets that are smaller or larger than the allowed Advantage packet size.

Recvfrom Errors

Number of errors that occurred when the Advantage Database Server was receiving packets. The specific errors are logged in the error log file by the Advantage Database Server.

Sendto Errors

Number of errors that occurred when the Advantage Database Server was sending packets. The specific errors are logged in the error log file by the Advantage Database Server.

Percent of Total Packets

This is a calculation that is performed on the two fields Total Packets Received and Check Sum Failures. The Percent of Total Packets is the percent of packets that failed in light of the total packets received. For example, if 100 packets were received and the check sum failure was 50, the percent of total packets would be 50%.

Reset All Statistics

By clicking this option, all entries that are being logged in the communication statistics are reset to 0. This is to aid in diagnosing communication problems by being able to reset all communication statistics back to 0.
