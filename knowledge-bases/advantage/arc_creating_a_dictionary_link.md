Creating a Dictionary Link




Advantage Database Server 12  

Creating a Dictionary Link

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Dictionary Link  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Creating a Dictionary Link Advantage Data Architect arc\_Creating\_a\_dictionary\_link Advantage Data Architect > Databases > Links > Creating a Dictionary Link / Dear Support Staff, |  |
| Creating a Dictionary Link  Advantage Data Architect |  |  |  |  |

To create a data dictionary link, open a database. See [Opening a Database](arc_opening_a_database2.htm) for details. You must login to the database as a user with CREATE LINK permissions in order to add data dictionary links in a database.

To add a new data dictionary link within the Connection Repository, right-click the LINKS icon and select Create.

To view a data dictionary links properties, from the tree view within the Connection Repository, right-click the data dictionary links name and select Properties.

Dictionary Links Field Descriptions

Alias (required)

Name of the data dictionary link.

Linked Data Dictionary (Required)

Path to and file name of the target data dictionary of the link.

Options

Static Path

The full UNC path to the target data dictionary will be stored rather than the relative path to the data dictionary.

Authenticate Active User

Specifies that the user name and password of the current connection should be used to authenticate to the data dictionary.

User

Name

When Authenticate Active User is not checked this is the user name, which should be used for authentication.

Password

When Authenticate Active User is not checked this is the password, which should be used for authentication.

OK

Creates the data dictionary link.

Cancel

Cancels the creation process and exits the screen.