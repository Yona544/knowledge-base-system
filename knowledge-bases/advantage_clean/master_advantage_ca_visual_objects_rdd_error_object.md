---
title: Master Advantage Ca Visual Objects Rdd Error Object
slug: master_advantage_ca_visual_objects_rdd_error_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_ca_visual_objects_rdd_error_object.htm
source: Advantage CHM
tags:
  - master
checksum: ff8b4ade07a2895f81f4c59fd0d624c31ccefaac
---

# Master Advantage Ca Visual Objects Rdd Error Object

Advantage CA-Visual Objects RDD Error Object

Advantage CA-Visual Objects RDD Error Object

Troubleshooting

| Advantage CA-Visual Objects RDD Error Object  Troubleshooting |  |  |  |  |

In most cases, run-time errors can be detected by your code. When an error is encountered, an error message is generated and passed to an error object in your CA-Visual Objects error handler or a screen will pop up with an error code.

If a run-time error occurs, identify the error class and specific message. Advantage will use the instance variable, "OSCode", in the CA-Visual Objects error object. You may see error codes in the OSCode field. Advantage error codes are listed in the Advantage Error Guide Help File.

CAUTION When opening a table, the error object is no longer populated if an error occurs. This is because the error object was triggering the default error handler to be called even if the error was handled within the application. This was implemented to provide the ability to control error handling without the resulting default message box being displayed.

The example code below can be used for determining if an error occurred while attempting to open a table:

LOCAL oDB AS DBServer

LOCAL dwError AS DWORD

LOCAL pacError AS PSZ

LOCAL wLen AS WORD

LOCAL lReturn AS LONGINT

pacError := MemAlloc( 200 )

wLen := 200

RDDSETDEFAULT("AXDBFCDX")

oDB := DBServer {"d:\demo10.dbf", DBShared,, "AXDBFCDX"}

lReturn := AdsGetLastError( @dwError, pacError, @wLen)

IF lReturn != AE\_SUCCESS

ErrorBox{ , "Failed to get last error" }:Show()

ELSEIF dwError != AE\_SUCCESS

ErrorBox{ , " Advantage error = " + pacError }:Show()

ENDIF
