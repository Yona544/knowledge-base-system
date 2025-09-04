Disabling Database Logins




Advantage Database Server 12  

Disabling Database Logins

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Disabling Database Logins  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Disabling Database Logins Advantage Concepts master\_Disabling\_database\_logins Advantage Concepts > Advantage Functionality > Disabling Database Logins / Dear Support Staff, |  |
| Disabling Database Logins  Advantage Concepts |  |  |  |  |

Advantage Data Dictionaries provide the ability to disable database logins. When logins are disabled, only the administrative user is allowed to make [database connections](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)). If other users attempt to login, they will receive an error code and a custom error message (which the administrator specifies when disabling logins).

This functionality can be used in a variety of situations. For example, you might want to disable logins when performing a backup, doing general maintenance, updating a stored procedure or trigger container, etc.

Logins can be disabled via the Advantage Data Architect (ARC) or through a variety of run-time methods such as API calls (AdsDDSetDatabaseProperty) or the stored procedure sp\_ModifyDatabase. The run-time methods allow the developer to embed this functionality into automatic backup programs or general maintenance utilities without requiring any user interaction. See the Advantage Data Architect Help documentation (ARC.hlp or arc.htm) for more information about disabling database logins using ARC. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

Disabling logins will not disconnect existing users. If you want to disable existing users the AdsMgKillUser management API can be used.

Disabling logins is supported with all server types, including the Advantage Database Server, the Advantage Internet Server, and the Advantage Local Server.

Version 7.1 or greater of Advantage clients will display your custom error string to users who attempt a database connection while logins are disabled. If an older client attempts to login, an error code will be returned, but the custom error text will not.

Check the Advantage Developers Zone (http://devzone.advantagedatabase.com) for examples and demos that disable database logins.