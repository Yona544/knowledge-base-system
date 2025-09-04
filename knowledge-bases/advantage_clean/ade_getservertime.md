---
title: Ade Getservertime
slug: ade_getservertime
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getservertime.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 601a120feb62b26e02971a51ea166dac771e8b29
---

# Ade Getservertime

GetServerTime

TAdsConnection.GetServerTime

Advantage TDataSet Descendant

| TAdsConnection.GetServerTime  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Retrieves the current time and date from the server via the Advantage Database Server

Syntax

function GetServerTime: TDateTime;

Description

GetServerTime returns the current date and time from the server, which is useful if the Advantage client application is running at a site that is in a different time zone than where the data is located and is being accessed by the Advantage Database Server. When Advantage is used in a WAN environment or is being used with the Advantage Internet Server, the Advantage client and Advantage server will often be located in different time zones. This function allows time, date, and timestamp fields to be populated with a consistent date and time, that is, the date and time of the server location.

Example

procedure TForm1.Test();

var

dtDateTime : TDateTime;

begin

 

{\* Get the server date and time \*}

dtDateTime := MyConnection1.GetServerTime();

 

{\* Display the current server time \*}

lbServerTime.Caption := DateTimeToStr( dtDateTime );

 

end;
