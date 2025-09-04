Automatic Version Checking




Advantage Database Server 12  

Automatic Version Checking

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Automatic Version Checking  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Automatic Version Checking Troubleshooting master\_Automatic\_version\_checking Troubleshooting and Technical Support > Troubleshooting > Automatic Version Checking / Dear Support Staff, |  |
| Automatic Version Checking  Troubleshooting |  |  |  |  |

Automatic version checking currently exists in the Advantage Client Engine DLLs. At initialization time, each DLL checks to verify that the DLLs it is using are of the same version. If the DLLs do not have matching versions, a message will be displayed indicating a specific DLL is newer or older than another. The only result of the version mismatch is the message box. If one of these messages is displayed, the DLL will attempt to continue working. It is meant to be a warning to make the user aware of the problem and to encourage the user to get matching DLLs.

The Advantage TDataSet Descendent does not check the Advantage Client Engine DLLs, however, the DLLs do perform the internal checking at load time to make sure they all match.