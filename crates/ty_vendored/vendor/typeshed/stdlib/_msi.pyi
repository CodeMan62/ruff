"""Documentation"""

import sys

if sys.platform == "win32":
    class MSIError(Exception): ...
    # Actual typename View, not exposed by the implementation
    class _View:
        def Execute(self, params: _Record | None = ...) -> None: ...
        def GetColumnInfo(self, kind: int) -> _Record: ...
        def Fetch(self) -> _Record: ...
        def Modify(self, mode: int, record: _Record) -> None: ...
        def Close(self) -> None: ...
        # Don't exist at runtime
        __new__: None  # type: ignore[assignment]
        __init__: None  # type: ignore[assignment]

    # Actual typename SummaryInformation, not exposed by the implementation
    class _SummaryInformation:
        def GetProperty(self, field: int) -> int | bytes | None: ...
        def GetPropertyCount(self) -> int: ...
        def SetProperty(self, field: int, value: int | str) -> None: ...
        def Persist(self) -> None: ...
        # Don't exist at runtime
        __new__: None  # type: ignore[assignment]
        __init__: None  # type: ignore[assignment]

    # Actual typename Database, not exposed by the implementation
    class _Database:
        def OpenView(self, sql: str) -> _View: ...
        def Commit(self) -> None: ...
        def GetSummaryInformation(self, updateCount: int) -> _SummaryInformation: ...
        def Close(self) -> None: ...
        # Don't exist at runtime
        __new__: None  # type: ignore[assignment]
        __init__: None  # type: ignore[assignment]

    # Actual typename Record, not exposed by the implementation
    class _Record:
        def GetFieldCount(self) -> int: ...
        def GetInteger(self, field: int) -> int: ...
        def GetString(self, field: int) -> str: ...
        def SetString(self, field: int, str: str) -> None: ...
        def SetStream(self, field: int, stream: str) -> None: ...
        def SetInteger(self, field: int, int: int) -> None: ...
        def ClearData(self) -> None: ...
        # Don't exist at runtime
        __new__: None  # type: ignore[assignment]
        __init__: None  # type: ignore[assignment]

    def UuidCreate() -> str:
        """Return the string representation of a new unique identifier."""

    def FCICreate(cabname: str, files: list[str], /) -> None:
        """Create a new CAB file.

        cabname
          the name of the CAB file
        files
          a list of tuples, each containing the name of the file on disk,
          and the name of the file inside the CAB file
        """

    def OpenDatabase(path: str, persist: int, /) -> _Database:
        """Return a new database object.

        path
          the file name of the MSI file
        persist
          the persistence mode
        """

    def CreateRecord(count: int, /) -> _Record:
        """Return a new record object.

        count
          the number of fields of the record
        """
    MSICOLINFO_NAMES: int
    MSICOLINFO_TYPES: int
    MSIDBOPEN_CREATE: int
    MSIDBOPEN_CREATEDIRECT: int
    MSIDBOPEN_DIRECT: int
    MSIDBOPEN_PATCHFILE: int
    MSIDBOPEN_READONLY: int
    MSIDBOPEN_TRANSACT: int
    MSIMODIFY_ASSIGN: int
    MSIMODIFY_DELETE: int
    MSIMODIFY_INSERT: int
    MSIMODIFY_INSERT_TEMPORARY: int
    MSIMODIFY_MERGE: int
    MSIMODIFY_REFRESH: int
    MSIMODIFY_REPLACE: int
    MSIMODIFY_SEEK: int
    MSIMODIFY_UPDATE: int
    MSIMODIFY_VALIDATE: int
    MSIMODIFY_VALIDATE_DELETE: int
    MSIMODIFY_VALIDATE_FIELD: int
    MSIMODIFY_VALIDATE_NEW: int

    PID_APPNAME: int
    PID_AUTHOR: int
    PID_CHARCOUNT: int
    PID_CODEPAGE: int
    PID_COMMENTS: int
    PID_CREATE_DTM: int
    PID_KEYWORDS: int
    PID_LASTAUTHOR: int
    PID_LASTPRINTED: int
    PID_LASTSAVE_DTM: int
    PID_PAGECOUNT: int
    PID_REVNUMBER: int
    PID_SECURITY: int
    PID_SUBJECT: int
    PID_TEMPLATE: int
    PID_TITLE: int
    PID_WORDCOUNT: int
