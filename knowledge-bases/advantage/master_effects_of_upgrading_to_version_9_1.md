Effects of Upgrading to Version 9.1




Advantage Database Server 12  

Effects of Upgrading to Version 9.1

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Effects of Upgrading to Version 9.1  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Effects of Upgrading to Version 9.1 Advantage Database Server master\_Effects\_of\_upgrading\_to\_version\_9\_1 Advantage Database Server > Introduction > Effects of Upgrading to Version 9.1 / Dear Support Staff, |  |
| Effects of Upgrading to Version 9.1  Advantage Database Server |  |  |  |  |

In addition to the [Effects of Upgrading to Version 9.0,](master_effects_of_upgrading_to_9_0.htm) the following Advantage functionality changes may affect your applications if you upgrade to Advantage version 9.1.

Effects of Upgrading

General

In older versions of Advantage, proprietary locking did not open files using an exclusive mode, instead it used a "deny write" open mode. While this would allow non-Advantage applications access to the data files, it could also lead to index corruption. Non-Advantage applications could still lock bytes in the files causing Advantage read and write operations to fail. For this reason the default proprietary open mode was changed. If, however, you require other non-Advantage enabled applications (such as backup software or reporting software) to open files in a shared, read-only mode, a server option is available to revert to older behavior. For details, see the [Non-Exclusive Proprietary Locking](master_non_exclusive_proprietary_locking.htm) configuration option.

Version 9.1 fixes an issue where differential backups were not correctly managing recycled memo pages, which could lead to memo corruption in a restored database image. It is recommended that anyone using differential backups re-initialize their backup image after installing this service update.