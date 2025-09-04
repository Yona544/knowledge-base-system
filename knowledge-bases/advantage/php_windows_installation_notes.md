Windows Installation Notes




Advantage Database Server 12  

Windows Installation Notes

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Windows Installation Notes  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - Windows Installation Notes Advantage PHP Extension php\_Windows\_installation\_notes Advantage PHP Extension > Windows Installation Notes / Dear Support Staff, |  |
| Windows Installation Notes  Advantage PHP Extension |  |  |  |  |

Compiled versions of the Advantage PHP Extension are provided for the most recent versions of PHP available at the time of the Advantage release. Unfortunately PHP extensions are not forward or backward compatible.

PHP 5

1] Verify the file version of the compiled extension matches the version of PHP installed on the machine. The default location of the extension is \Program Files\Advantage X.x\PHP\.

The extension is name php\_advantage.dll.5.x.y, which should correspond to the version of PHP on the computer.

2] Copy the php\_advantage.dll.5.x.y to the PHP extension directory with the name php\_advantage.dll.

3] Locate the php.ini file and add the following entry under the Windows Extensions section:

extension=php\_advantage.dll

4] Restart the web server.