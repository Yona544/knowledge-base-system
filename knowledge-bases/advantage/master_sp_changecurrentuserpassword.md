sp\_ChangeCurrentUserPassword




Advantage Database Server 12  

sp\_ChangeCurrentUserPassword

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ChangeCurrentUserPassword  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ChangeCurrentUserPassword Advantage SQL Engine Master\_sp\_ChangeCurrentUserPassword Advantage SQL > System Procedures > Procedures > sp\_ChangeCurrentUserPassword / Dear Support Staff, |  |
| sp\_ChangeCurrentUserPassword  Advantage SQL Engine |  |  |  |  |

Changes the current connected user's data dictionary password.

Syntax

sp\_ChangeCurrentUserPassword(

 OldPassword Char(20),

      NewPassword Char(20)  );

Parameters

|  |  |
| --- | --- |
| OldPassword (I) | The user's current password. |
| NewPassword(I) | The new password to change to. |

Output

None.

Remarks

sp\_ChangeCurrentUserPassword changes the current connected user's data dictionary password to the NewPassword. By default, the user's current password must be supplied in the OldPassword parameter for the stored procedure to execute successfully. If no OldPassword is specified, or the OldPassword does not match, an 5097 (AE\_INVALID\_PASSWORD) will be returned. However, if the user is set up to not require old password when changing existing password, then the value supplied by the OldPassword is ignored.

See Also

[sp\_ModifyUserProperty](master_sp_modifyuserproperty.htm)