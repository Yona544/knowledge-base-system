Online Backup Permissions




Advantage Database Server 12  

Online Backup Permissions

Advantage Tech Tips

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Online Backup Permissions  Advantage Tech Tips |  |  | Feedback on: Advantage Database Server 12 - Online Backup Permissions Advantage Tech Tips master\_Online\_Backup\_Permissions Tech Tips > Best Practices > Online Backup Permissions / Dear Support Staff, |  |
| Online Backup Permissions  Advantage Tech Tips |  |  |  |  |

Online backup is a powerful feature that was added to Advantage Database Server in version 8.0. This feature allows administrators and members of the DB:Backup group to make backups of free tables or an entire database when users are actively using the data. This can be particularly useful when the data is accessed from the internet or in another 24X7 implementation.

Although configuring online backup is relatively easy it does require the proper permissions. When backing up a database (ADD) you must be a member of the DB:Admin or DB:Backup group to initiate a backup. Additionally the Advantage service must have full permission to the location where the file is to be backed up.

Configuring Share Permissions for Windows

When performing an online backup you specify a path to a target destination. For a local path, physical or mapped drive, you should not need to specify any special permissions. If you your target is a shared folder you must ensure that the share permissions are correct.

Advantage runs using the System user account by default. This account has full access permission to all of the local drives on the system. It does not have any rights on any network shares by default. In a Windows Domain or Active Directory you can grant share permissions to the local system account by adding the machine name to the permissions list.

Another option is to create a service account which can be used by the Advantage service. This works best when the computer running Advantage and the share are part of a domain. Create a domain account and configure the Advantage service to use this account. Once this is done simply assign full control permissions on the target share to the new service account. The service account is configured on the service properties page on the Log On tab.

Generally service account passwords do not change which may be against the company password policy. You may have to change the account password periodically. Whenever this password changes you must re-enter the password on the service property pages.

Configuring Share Permissions for Linux

The Advantage Daemon runs as the advantage user which is a member of the advantage group which is created by the setup script. All backup targets must allow read and write access to the advantage user and group. This can be done by using the chmod command.

 Chmod R ug+rw backupdir/

In most cases it is easier to simply make the advantage user the owner of the directory and change the group to advantage using the following commands.

 Chown advantage <file-list>

 Chgrp advantage <file-list>

Accessing a remote share with Linux is more difficult. The easiest thing to do is to mount a share as a drive on the system. The mounted drive will take care of the network permissions. Once the drive is mounted you can assign the proper rights to the drive for the advantage user and group using the chmod command.

You can also access a network share by mounting an NFS volume. You can mount an NFS volume using the mount command. Provide the network path you wish to mount and the name of the mount point on your local system.

 mount master.foo.com:/data /mnt/data

You can also mount a share at runtime by modifying the etc/fstab file. You can also specify the permissions within this file. An example NFS volume entry is below.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| # device | mountpoint | fs-type | options | dump | fsckorder |
| ... |  |  |  |  |  |
| master.foo.com/data | /mnt/data | nfs | rw | 0 | 0 |
| ... |  |  |  |  |  |

Backup and Restore System Procedure Permissions

Backup and restores are initiated by calling system procedures. For free tables use sp\_BackupFreeTables and sp\_RestoreFreeTables. These system procedures do not require any authentication to be run. When working with dictionary (database) tables use sp\_BackupDatabase and sp\_RestoreDatabase. These system procedures can only be run by an administrator or a member of the DB:Backup group.

When using the adsbackup utility you can specify the username with the y option. If no username is specified the adssys account is used.

When restoring a database you must supply the adssys password for the database as one of the parameters for the sp\_RestoreDatabase system procedure. For example:

EXECUTE PROCEDURE sp\_RestoreDatabase( 'C:\Backup\20090610\MyAdd.add', 'password', 'C:\Data\MyApp\MyAdd.add', NULL )

Version 9.x and newer of Advantage will allow members of the DB:Backup and DB:Admin group to restore a data dictionary.

Summary

Advantage online backup is designed to provide a safe and robust mechanism for backing up your data without worrying about users being logged into the system. Although the backup process is very simple to invoke it may require some network configuration. Since the Advantage service is creating the backup and writing the files it must have the proper permissions to the target location. With a little bit of prior planning this is easily accomplished.