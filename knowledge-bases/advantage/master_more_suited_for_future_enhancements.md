More Suited for Future Enhancements




Advantage Database Server 12  

More Suited for Future Enhancements

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| More Suited for Future Enhancements  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - More Suited for Future Enhancements Advantage Concepts master\_More\_suited\_for\_future\_enhancements Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > More Suited for Future Enhancements / Dear Support Staff, |  |
| More Suited for Future Enhancements  Advantage Concepts |  |  |  |  |

Advantage proprietary ADT tables have information in the table header that will keep the table from being opened if the data dictionary in which field level constraints for the table are defined is not also open. Xbase DBF tables have no such information in the table header. Thus, when Advantage has support for a data dictionary, enforcement of functionality such as field value constraints can be guaranteed in ADT tables, but not necessarily in DBF tables if that DBF table is opened while the corresponding data dictionary is not open.

The Advantage proprietary file format table header has been designed to allow support for field level encryption at the Advantage level. Although this functionality is not yet supported, it is functionality that could not be easily implemented in Xbase file formats.

The Advantage proprietary file format table header has been designed to support up to 65535 different field types. Xbase files can support nowhere near this many field types. If there is ever a need to support many different field types, this will only be possible with the Advantage proprietary file format.