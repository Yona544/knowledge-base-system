Linux Case Sensitivity




Advantage Database Server 12  

Linux Case Sensitivity

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Linux Case Sensitivity  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Linux Case Sensitivity Advantage Concepts master\_Linux\_case\_sensitivity Advantage Concepts > Advantage Linux Development Notes > Linux Case Sensitivity / Dear Support Staff, |  |
| Linux Case Sensitivity  Advantage Concepts |  |  |  |  |

Because Linux uses a case-sensitive file system, all connection paths and table names must match the case of the file on disk exactly. This can often be a problem when the client kit (CA Clipper, for example) modifies the case of strings typed in by the user or developer.

The Advantage Database Server provides a configuration option (LOWERCASE\_ALL\_PATHS) in the ads.conf file that can be used to change all paths to lowercase before attempting to access them on disk. The Advantage Local Server for Linux also provides this functionality through an option in the adslocal.cfg configuration file.

If this option is enabled, Advantage will convert all paths to lowercase for all users/connections. This means the file names (and the directory names in the path) on disk must contain all lower-case characters.

The following command can be used to change all filenames in a directory to lower-case. The text below encompasses one single command; type all of the text before pressing "enter".

find -type f | while read i; do j="`echo $i | tr [[:upper:]] [[:lower:]]`"; [ "$j" != "$i" ] && { mv "$i" "$j" || echo "ERROR: $i"; } ; done

 

Important Note Always back up all files before running the command provided above.