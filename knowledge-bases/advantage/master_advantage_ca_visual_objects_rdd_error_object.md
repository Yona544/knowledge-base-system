Advantage CA-Visual Objects RDD Error Object




Advantage Database Server 12  

Advantage CA-Visual Objects RDD Error Object

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage CA-Visual Objects RDD Error Object  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Advantage CA-Visual Objects RDD Error Object Troubleshooting master\_Advantage\_ca-visual\_objects\_rdd\_error\_object Troubleshooting and Technical Support > Troubleshooting > Advantage CA-Visual Objects RDD Error Object / Dear Support Staff, |  |
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