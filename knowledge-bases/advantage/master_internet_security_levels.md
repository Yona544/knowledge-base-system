Internet Security Levels




Advantage Database Server 12  

Internet Security Levels

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Internet Security Levels  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Internet Security Levels Advantage Database Server master\_Internet\_security\_levels Advantage Database Server > Advantage Internet Server > Advantage Internet Server Security > Internet Security Levels / Dear Support Staff, |  |
| Internet Security Levels  Advantage Database Server |  |  |  |  |

The Advantage Database Server (ADS) offers three levels of Internet security. The security level is specified per database (Advantage Data Dictionary). The security level chosen applies to all users connecting to that database via Advantage Internet Server functionality.

Level 0

This level provides no authentication or encryption. This might be the choice if Advantage Internet Server were being used in an intranet environment. Users are not prompted to enter a user ID and password on the database application startup.

Level 1

Level 1 requires users to authenticate but no encryption is used. Users are prompted on database application startup to enter a user ID and password. User access to database files is limited according to the user rights in the [Advantage Data Dictionary](master_advantage_data_dictionary.htm).

Level 2

Level 2 requires users to authenticate and encrypts all data during the session. Users are prompted on database application startup to enter a user ID and password. The encryption algorithm is an industry-standard stream cipher that uses 160-bit keys.

Security level 2 might be the best choice when using Internet connections so data is not transferred in the "clear" over the Internet.

To configure Security, you will need to set the level in your data dictionary. With the security level in the Data Dictionary, different levels of security can be maintained depending on which Data Dictionary is being used. Security levels can be set using [Advantage Data Architect](master_advantage_data_architect.htm) or the Advantage Client Engine APIs. See [Enabling Internet Access in the Data Dictionary](master_enabling_internet_access_in_the_data_dictionary.htm).

With security level 1 and 2, upon starting your Advantage client application, you will be prompted for a user name and password for authentication.

Note When using modems in connections to the Advantage Database Server, it is probably best to use [communications compression](master_communications_compression.htm). When ADS security Level 2 is used, the encrypted data cannot be compressed well by modems. It is best, therefore, to use the compression support provided by Advantage because the data is compressed prior to encryption.

Note The more restrictive authentication requirement between this Internet Security Level setting and the Logins Required property of the Advantage Data Dictionary is used. For example, if Logins Required is True and the Internet Security Level is level 0, a login (authentication) is required. The contrary is also true. If Logins Required is False and the Internet Security Level is 1 or 2, a login (authentication) is required.