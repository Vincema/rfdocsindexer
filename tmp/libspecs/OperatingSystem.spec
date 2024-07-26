<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="OperatingSystem" type="LIBRARY" format="ROBOT" scope="GLOBAL" generated="2024-07-26T11:05:33+00:00" specversion="6" source="C:\Users\maire\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\robot\libraries\OperatingSystem.py" lineno="39">
<version>7.0.1</version>
<doc>A library providing keywords for operating system related tasks.

``OperatingSystem`` is Robot Framework's standard library that
enables various operating system related tasks to be performed in
the system where Robot Framework is running. It can, among other
things, execute commands (e.g. `Run`), create and remove files and
directories (e.g. `Create File`, `Remove Directory`), check
whether files or directories exists or contain something
(e.g. `File Should Exist`, `Directory Should Be Empty`) and
manipulate environment variables (e.g. `Set Environment Variable`).

== Table of contents ==

- `Path separators`
- `Pattern matching`
- `Tilde expansion`
- `pathlib.Path support`
- `Boolean arguments`
- `Example`
- `Keywords`

= Path separators =

Because Robot Framework uses the backslash (``\``) as an escape character
in its data, using a literal backslash requires duplicating it like
in ``c:\\path\\file.txt``. That can be inconvenient especially with
longer Windows paths, and thus all keywords expecting paths as arguments
convert forward slashes to backslashes automatically on Windows. This also
means that paths like ``${CURDIR}/path/file.txt`` are operating system
independent.

Notice that the automatic path separator conversion does not work if
the path is only a part of an argument like with the `Run` keyword.
In these cases the built-in variable ``${/}`` that contains ``\`` or ``/``,
depending on the operating system, can be used instead.

= Pattern matching =

Many keywords accept arguments as either _glob_ or _regular expression_ patterns.

== Glob patterns ==

Some keywords, for example `List Directory`, support so called
[http://en.wikipedia.org/wiki/Glob_(programming)|glob patterns] where:

| ``*``        | matches any string, even an empty string                |
| ``?``        | matches any single character                            |
| ``[chars]``  | matches one character in the bracket                    |
| ``[!chars]`` | matches one character not in the bracket                |
| ``[a-z]``    | matches one character from the range in the bracket     |
| ``[!a-z]``   | matches one character not from the range in the bracket |

Unless otherwise noted, matching is case-insensitive on case-insensitive
operating systems such as Windows.

== Regular expressions ==

Some keywords, for example `Grep File`, support
[http://en.wikipedia.org/wiki/Regular_expression|regular expressions]
that are more powerful but also more complicated that glob patterns.
The regular expression support is implemented using Python's
[http://docs.python.org/library/re.html|re module] and its documentation
should be consulted for more information about the syntax.

Because the backslash character (``\``) is an escape character in
Robot Framework data, possible backslash characters in regular
expressions need to be escaped with another backslash like ``\\d\\w+``.
Strings that may contain special characters but should be handled
as literal strings, can be escaped with the `Regexp Escape` keyword
from the BuiltIn library.

= Tilde expansion =

Paths beginning with ``~`` or ``~username`` are expanded to the current or
specified user's home directory, respectively. The resulting path is
operating system dependent, but typically e.g. ``~/robot`` is expanded to
``C:\Users\&lt;user&gt;\robot`` on Windows and ``/home/&lt;user&gt;/robot`` on Unixes.

= pathlib.Path support =

Starting from Robot Framework 6.0, arguments representing paths can be given
as [https://docs.python.org/3/library/pathlib.html|pathlib.Path] instances
in addition to strings.

All keywords returning paths return them as strings. This may change in
the future so that the return value type matches the argument type.

= Boolean arguments =

Some keywords accept arguments that are handled as Boolean values true or
false. If such an argument is given as a string, it is considered false if
it is an empty string or equal to ``FALSE``, ``NONE``, ``NO``, ``OFF`` or
``0``, case-insensitively. Other strings are considered true regardless
their value, and other argument types are tested using the same
[http://docs.python.org/library/stdtypes.html#truth|rules as in Python].

True examples:
| `Remove Directory` | ${path} | recursive=True    | # Strings are generally true.    |
| `Remove Directory` | ${path} | recursive=yes     | # Same as the above.             |
| `Remove Directory` | ${path} | recursive=${TRUE} | # Python ``True`` is true.       |
| `Remove Directory` | ${path} | recursive=${42}   | # Numbers other than 0 are true. |

False examples:
| `Remove Directory` | ${path} | recursive=False    | # String ``false`` is false.   |
| `Remove Directory` | ${path} | recursive=no       | # Also string ``no`` is false. |
| `Remove Directory` | ${path} | recursive=${EMPTY} | # Empty string is false.       |
| `Remove Directory` | ${path} | recursive=${FALSE} | # Python ``False`` is false.   |

= Example =

| ***** Settings *****
| Library         OperatingSystem
|
| ***** Variables *****
| ${PATH}         ${CURDIR}/example.txt
|
| ***** Test Cases *****
| Example
|     `Create File`          ${PATH}    Some text
|     `File Should Exist`    ${PATH}
|     `Copy File`            ${PATH}    ~/file.txt</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Append To Environment Variable" lineno="983">
<arguments repr="name, *values, **config">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**config">
<name>config</name>
</arg>
</arguments>
<doc>Appends given ``values`` to environment variable ``name``.

If the environment variable already exists, values are added after it,
and otherwise a new environment variable is created.

Values are, by default, joined together using the operating system
path separator (``;`` on Windows, ``:`` elsewhere). This can be changed
by giving a separator after the values like ``separator=value``. No
other configuration parameters are accepted.

Examples (assuming ``NAME`` and ``NAME2`` do not exist initially):
| Append To Environment Variable | NAME     | first  |       |
| Should Be Equal                | %{NAME}  | first  |       |
| Append To Environment Variable | NAME     | second | third |
| Should Be Equal                | %{NAME}  | first${:}second${:}third |
| Append To Environment Variable | NAME2    | first  | separator=-     |
| Should Be Equal                | %{NAME2} | first  |                 |
| Append To Environment Variable | NAME2    | second | separator=-     |
| Should Be Equal                | %{NAME2} | first-second             |</doc>
<shortdoc>Appends given ``values`` to environment variable ``name``.</shortdoc>
</kw>
<kw name="Append To File" lineno="640">
<arguments repr="path, content, encoding=UTF-8">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="content">
<name>content</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
</arguments>
<doc>Appends the given content to the specified file.

If the file exists, the given text is written to its end. If the file
does not exist, it is created.

Other than not overwriting possible existing files, this keyword works
exactly like `Create File`. See its documentation for more details
about the usage.</doc>
<shortdoc>Appends the given content to the specified file.</shortdoc>
</kw>
<kw name="Copy Directory" lineno="912">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>Copies the source directory into the destination.

If the destination exists, the source is copied under it. Otherwise
the destination directory and the possible missing intermediate
directories are created.</doc>
<shortdoc>Copies the source directory into the destination.</shortdoc>
</kw>
<kw name="Copy File" lineno="739">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>Copies the source file into the destination.

Source must be a path to an existing file or a glob pattern (see
`Glob patterns`) that matches exactly one file. How the
destination is interpreted is explained below.

1) If the destination is an existing file, the source file is copied
over it.

2) If the destination is an existing directory, the source file is
copied into it. A possible file with the same name as the source is
overwritten.

3) If the destination does not exist and it ends with a path
separator (``/`` or ``\``), it is considered a directory. That
directory is created and a source file copied into it.
Possible missing intermediate directories are also created.

4) If the destination does not exist and it does not end with a path
separator, it is considered a file. If the path to the file does not
exist, it is created.

The resulting destination path is returned.

See also `Copy Files`, `Move File`, and `Move Files`.</doc>
<shortdoc>Copies the source file into the destination.</shortdoc>
</kw>
<kw name="Copy Files" lineno="865">
<arguments repr="*sources_and_destination">
<arg kind="VAR_POSITIONAL" required="false" repr="*sources_and_destination">
<name>sources_and_destination</name>
</arg>
</arguments>
<doc>Copies specified files to the target directory.

Source files can be given as exact paths and as glob patterns (see
`Glob patterns`). At least one source must be given, but it is
not an error if it is a pattern that does not match anything.

Last argument must be the destination directory. If the destination
does not exist, it will be created.

Examples:
| Copy Files | ${dir}/file1.txt  | ${dir}/file2.txt | ${dir2} |
| Copy Files | ${dir}/file-*.txt | ${dir2}          |         |

See also `Copy File`, `Move File`, and `Move Files`.</doc>
<shortdoc>Copies specified files to the target directory.</shortdoc>
</kw>
<kw name="Count Directories In Directory" lineno="1375">
<arguments repr="path, pattern=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
</arguments>
<doc>Wrapper for `Count Items In Directory` returning only directory count.</doc>
<shortdoc>Wrapper for `Count Items In Directory` returning only directory count.</shortdoc>
</kw>
<kw name="Count Files In Directory" lineno="1369">
<arguments repr="path, pattern=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
</arguments>
<doc>Wrapper for `Count Items In Directory` returning only file count.</doc>
<shortdoc>Wrapper for `Count Items In Directory` returning only file count.</shortdoc>
</kw>
<kw name="Count Items In Directory" lineno="1358">
<arguments repr="path, pattern=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
</arguments>
<doc>Returns and logs the number of all items in the given directory.

The argument ``pattern`` has the same semantics as with `List Directory`
keyword. The count is returned as an integer, so it must be checked e.g.
with the built-in keyword `Should Be Equal As Integers`.</doc>
<shortdoc>Returns and logs the number of all items in the given directory.</shortdoc>
</kw>
<kw name="Create Binary File" lineno="614">
<arguments repr="path, content">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="content">
<name>content</name>
</arg>
</arguments>
<doc>Creates a binary file with the given content.

If content is given as a Unicode string, it is first converted to bytes
character by character. All characters with ordinal below 256 can be
used and are converted to bytes with same values. Using characters
with higher ordinal is an error.

Byte strings, and possible other types, are written to the file as is.

If the directory for the file does not exist, it is created, along
with missing intermediate directories.

Examples:
| Create Binary File | ${dir}/example.png | ${image content} |
| Create Binary File | ${path}            | \x01\x00\xe4\x00 |

Use `Create File` if you want to create a text file using a certain
encoding. `File Should Not Exist` can be used to avoid overwriting
existing files.</doc>
<shortdoc>Creates a binary file with the given content.</shortdoc>
</kw>
<kw name="Create Directory" lineno="697">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Creates the specified directory.

Also possible intermediate directories are created. Passes if the
directory already exists, but fails if the path exists and is not
a directory.</doc>
<shortdoc>Creates the specified directory.</shortdoc>
</kw>
<kw name="Create File" lineno="577">
<arguments repr="path, content=, encoding=UTF-8">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="content=">
<name>content</name>
<default/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
</arguments>
<doc>Creates a file with the given content and encoding.

If the directory where the file is created does not exist, it is
automatically created along with possible missing intermediate
directories. Possible existing file is overwritten.

On Windows newline characters (``\n``) in content are automatically
converted to Windows native newline sequence (``\r\n``).

See `Get File` for more information about possible ``encoding`` values,
including special values ``SYSTEM`` and ``CONSOLE``.

Examples:
| Create File | ${dir}/example.txt | Hello, world!       |         |
| Create File | ${path}            | Hyv\xe4 esimerkki  | Latin-1 |
| Create File | /tmp/foo.txt       | 3\nlines\nhere\n | SYSTEM  |

Use `Append To File` if you want to append to an existing file
and `Create Binary File` if you need to write bytes without encoding.
`File Should Not Exist` can be used to avoid overwriting existing
files.</doc>
<shortdoc>Creates a file with the given content and encoding.</shortdoc>
</kw>
<kw name="Directory Should Be Empty" lineno="524">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the specified directory is empty.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails unless the specified directory is empty.</shortdoc>
</kw>
<kw name="Directory Should Exist" lineno="440">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the given path points to an existing directory.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails unless the given path points to an existing directory.</shortdoc>
</kw>
<kw name="Directory Should Not Be Empty" lineno="536">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the specified directory is empty.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the specified directory is empty.</shortdoc>
</kw>
<kw name="Directory Should Not Exist" lineno="454">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given path points to an existing file.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the given path points to an existing file.</shortdoc>
</kw>
<kw name="Empty Directory" lineno="682">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Deletes all the content from the given directory.

Deletes both files and sub-directories, but the specified directory
itself if not removed. Use `Remove Directory` if you want to remove
the whole directory.</doc>
<shortdoc>Deletes all the content from the given directory.</shortdoc>
</kw>
<kw name="Environment Variable Should Be Set" lineno="1030">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the specified environment variable is not set.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the specified environment variable is not set.</shortdoc>
</kw>
<kw name="Environment Variable Should Not Be Set" lineno="1040">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the specified environment variable is set.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the specified environment variable is set.</shortdoc>
</kw>
<kw name="File Should Be Empty" lineno="548">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the specified file is empty.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails unless the specified file is empty.</shortdoc>
</kw>
<kw name="File Should Exist" lineno="412">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the given ``path`` points to an existing file.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails unless the given ``path`` points to an existing file.</shortdoc>
</kw>
<kw name="File Should Not Be Empty" lineno="562">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the specified file is empty.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the specified file is empty.</shortdoc>
</kw>
<kw name="File Should Not Exist" lineno="426">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given path points to an existing file.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the given path points to an existing file.</shortdoc>
</kw>
<kw name="Get Binary File" lineno="294">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Returns the contents of a specified file.

This keyword reads the specified file and returns the contents as is.
See also `Get File`.</doc>
<shortdoc>Returns the contents of a specified file.</shortdoc>
</kw>
<kw name="Get Environment Variable" lineno="956">
<arguments repr="name, default=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=None">
<name>default</name>
<default>None</default>
</arg>
</arguments>
<doc>Returns the value of an environment variable with the given name.

If no environment variable is found, returns possible default value.
If no default value is given, the keyword fails.

Returned variables are automatically decoded to Unicode using
the system encoding.

Note that you can also access environment variables directly using
the variable syntax ``%{ENV_VAR_NAME}``.</doc>
<shortdoc>Returns the value of an environment variable with the given name.</shortdoc>
</kw>
<kw name="Get Environment Variables" lineno="1051">
<arguments repr="">
</arguments>
<doc>Returns currently available environment variables as a dictionary.

Both keys and values are decoded to Unicode using the system encoding.
Altering the returned dictionary has no effect on the actual environment
variables.</doc>
<shortdoc>Returns currently available environment variables as a dictionary.</shortdoc>
</kw>
<kw name="Get File" lineno="253">
<arguments repr="path, encoding=UTF-8, encoding_errors=strict">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding_errors=strict">
<name>encoding_errors</name>
<default>strict</default>
</arg>
</arguments>
<doc>Returns the contents of a specified file.

This keyword reads the specified file and returns the contents.
Line breaks in content are converted to platform independent form.
See also `Get Binary File`.

``encoding`` defines the encoding of the file. The default value is
``UTF-8``, which means that UTF-8 and ASCII encoded files are read
correctly. In addition to the encodings supported by the underlying
Python implementation, the following special encoding values can be
used:

- ``SYSTEM``: Use the default system encoding.
- ``CONSOLE``: Use the console encoding. Outside Windows this is same
  as the system encoding.

``encoding_errors`` argument controls what to do if decoding some bytes
fails. All values accepted by ``decode`` method in Python are valid, but
in practice the following values are most useful:

- ``strict``: Fail if characters cannot be decoded (default).
- ``ignore``: Ignore characters that cannot be decoded.
- ``replace``: Replace characters that cannot be decoded with
  a replacement character.</doc>
<shortdoc>Returns the contents of a specified file.</shortdoc>
</kw>
<kw name="Get File Size" lineno="1305">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Returns and logs file size as an integer in bytes.</doc>
<shortdoc>Returns and logs file size as an integer in bytes.</shortdoc>
</kw>
<kw name="Get Modified Time" lineno="1216">
<arguments repr="path, format=timestamp">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="format=timestamp">
<name>format</name>
<default>timestamp</default>
</arg>
</arguments>
<doc>Returns the last modification time of a file or directory.

How time is returned is determined based on the given ``format``
string as follows. Note that all checks are case-insensitive.
Returned time is also automatically logged.

1) If ``format`` contains the word ``epoch``, the time is returned
   in seconds after the UNIX epoch. The return value is always
   an integer.

2) If ``format`` contains any of the words ``year``, ``month``,
   ``day``, ``hour``, ``min`` or ``sec``, only the selected parts are
   returned. The order of the returned parts is always the one
   in the previous sentence and the order of the words in
   ``format`` is not significant. The parts are returned as
   zero-padded strings (e.g. May -&gt; ``05``).

3) Otherwise, and by default, the time is returned as a
   timestamp string in the format ``2006-02-24 15:08:31``.

Examples (when the modified time of ``${CURDIR}`` is
2006-03-29 15:06:21):
| ${time} = | Get Modified Time | ${CURDIR} |
| ${secs} = | Get Modified Time | ${CURDIR} | epoch |
| ${year} = | Get Modified Time | ${CURDIR} | return year |
| ${y} | ${d} = | Get Modified Time | ${CURDIR} | year,day |
| @{time} = | Get Modified Time | ${CURDIR} | year,month,day,hour,min,sec |
=&gt;
- ${time} = '2006-03-29 15:06:21'
- ${secs} = 1143637581
- ${year} = '2006'
- ${y} = '2006' &amp; ${d} = '29'
- @{time} = ['2006', '03', '29', '15', '06', '21']</doc>
<shortdoc>Returns the last modification time of a file or directory.</shortdoc>
</kw>
<kw name="Grep File" lineno="305">
<arguments repr="path, pattern, encoding=UTF-8, encoding_errors=strict, regexp=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding_errors=strict">
<name>encoding_errors</name>
<default>strict</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="regexp=False">
<name>regexp</name>
<default>False</default>
</arg>
</arguments>
<doc>Returns the lines of the specified file that match the ``pattern``.

This keyword reads a file from the file system using the defined
``path``, ``encoding`` and ``encoding_errors`` similarly as `Get File`.
A difference is that only the lines that match the given ``pattern`` are
returned. Lines are returned as a single string concatenated back together
with newlines and the number of matched lines is automatically logged.
Possible trailing newline is never returned.

A line matches if it contains the ``pattern`` anywhere in it i.e. it does
not need to match the pattern fully. There are two supported pattern types:

- By default the pattern is considered a _glob_ pattern where, for example,
  ``*`` and ``?`` can be used as wildcards.
- If the ``regexp`` argument is given a true value, the pattern is
  considered to be a _regular expression_. These patterns are more
  powerful but also more complicated than glob patterns. They often use
  the backslash character and it needs to be escaped in Robot Framework
  date like `\\`.

For more information about glob and regular expression syntax, see
the `Pattern matching` section. With this keyword matching is always
case-sensitive.

Examples:
| ${errors} = | Grep File | /var/log/myapp.log | ERROR |
| ${ret} = | Grep File | ${CURDIR}/file.txt | [Ww]ildc??d ex*ple |
| ${ret} = | Grep File | ${CURDIR}/file.txt | [Ww]ildc\\w+d ex.*ple | regexp=True |

Special encoding values ``SYSTEM`` and ``CONSOLE`` that `Get File` supports
are supported by this keyword only with Robot Framework 4.0 and newer.

Support for regular expressions is new in Robot Framework 5.0.</doc>
<shortdoc>Returns the lines of the specified file that match the ``pattern``.</shortdoc>
</kw>
<kw name="Join Path" lineno="1073">
<arguments repr="base, *parts">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="base">
<name>base</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*parts">
<name>parts</name>
</arg>
</arguments>
<doc>Joins the given path part(s) to the given base path.

The path separator (``/`` or ``\``) is inserted when needed and
the possible absolute paths handled as expected. The resulted
path is also normalized.

Examples:
| ${path} = | Join Path | my        | path  |
| ${p2} =   | Join Path | my/       | path/ |
| ${p3} =   | Join Path | my        | path  | my | file.txt |
| ${p4} =   | Join Path | my        | /path |
| ${p5} =   | Join Path | /my/path/ | ..    | path2 |
=&gt;
- ${path} = 'my/path'
- ${p2} = 'my/path'
- ${p3} = 'my/path/my/file.txt'
- ${p4} = '/path'
- ${p5} = '/my/path2'</doc>
<shortdoc>Joins the given path part(s) to the given base path.</shortdoc>
</kw>
<kw name="Join Paths" lineno="1097">
<arguments repr="base, *paths">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="base">
<name>base</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*paths">
<name>paths</name>
</arg>
</arguments>
<doc>Joins given paths with base and returns resulted paths.

See `Join Path` for more information.

Examples:
| @{p1} = | Join Paths | base     | example       | other |          |
| @{p2} = | Join Paths | /my/base | /example      | other |          |
| @{p3} = | Join Paths | my/base  | example/path/ | other | one/more |
=&gt;
- @{p1} = ['base/example', 'base/other']
- @{p2} = ['/example', '/my/base/other']
- @{p3} = ['my/base/example/path', 'my/base/other', 'my/base/one/more']</doc>
<shortdoc>Joins given paths with base and returns resulted paths.</shortdoc>
</kw>
<kw name="List Directories In Directory" lineno="1350">
<arguments repr="path, pattern=None, absolute=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="absolute=False">
<name>absolute</name>
<default>False</default>
</arg>
</arguments>
<doc>Wrapper for `List Directory` that returns only directories.</doc>
<shortdoc>Wrapper for `List Directory` that returns only directories.</shortdoc>
</kw>
<kw name="List Directory" lineno="1315">
<arguments repr="path, pattern=None, absolute=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="absolute=False">
<name>absolute</name>
<default>False</default>
</arg>
</arguments>
<doc>Returns and logs items in a directory, optionally filtered with ``pattern``.

File and directory names are returned in case-sensitive alphabetical
order, e.g. ``['A Name', 'Second', 'a lower case name', 'one more']``.
Implicit directories ``.`` and ``..`` are not returned. The returned
items are automatically logged.

File and directory names are returned relative to the given path
(e.g. ``'file.txt'``) by default. If you want them be returned in
absolute format (e.g. ``'/home/robot/file.txt'``), give the ``absolute``
argument a true value (see `Boolean arguments`).

If ``pattern`` is given, only items matching it are returned. The pattern
is considered to be a _glob pattern_ and the full syntax is explained in
the `Glob patterns` section. With this keyword matching is always
case-sensitive.

Examples (using also other `List Directory` variants):
| @{items} = | List Directory           | ${TEMPDIR} |
| @{files} = | List Files In Directory  | /tmp | *.txt | absolute |
| ${count} = | Count Files In Directory | ${CURDIR} | ??? |</doc>
<shortdoc>Returns and logs items in a directory, optionally filtered with ``pattern``.</shortdoc>
</kw>
<kw name="List Files In Directory" lineno="1343">
<arguments repr="path, pattern=None, absolute=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="absolute=False">
<name>absolute</name>
<default>False</default>
</arg>
</arguments>
<doc>Wrapper for `List Directory` that returns only files.</doc>
<shortdoc>Wrapper for `List Directory` that returns only files.</shortdoc>
</kw>
<kw name="Log Environment Variables" lineno="1060">
<arguments repr="level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>Logs all environment variables using the given log level.

Environment variables are also returned the same way as with
`Get Environment Variables` keyword.</doc>
<shortdoc>Logs all environment variables using the given log level.</shortdoc>
</kw>
<kw name="Log File" lineno="358">
<arguments repr="path, encoding=UTF-8, encoding_errors=strict">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding_errors=strict">
<name>encoding_errors</name>
<default>strict</default>
</arg>
</arguments>
<doc>Wrapper for `Get File` that also logs the returned file.

The file is logged with the INFO level. If you want something else,
just use `Get File` and the built-in keyword `Log` with the desired
level.

See `Get File` for more information about ``encoding`` and
``encoding_errors`` arguments.</doc>
<shortdoc>Wrapper for `Get File` that also logs the returned file.</shortdoc>
</kw>
<kw name="Move Directory" lineno="941">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>Moves the source directory into a destination.

Uses `Copy Directory` keyword internally, and ``source`` and
``destination`` arguments have exactly same semantics as with
that keyword.</doc>
<shortdoc>Moves the source directory into a destination.</shortdoc>
</kw>
<kw name="Move File" lineno="846">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>Moves the source file into the destination.

Arguments have exactly same semantics as with `Copy File` keyword.
Destination file path is returned.

If the source and destination are on the same filesystem, rename
operation is used. Otherwise file is copied to the destination
filesystem and then removed from the original filesystem.

See also `Move Files`, `Copy File`, and `Copy Files`.</doc>
<shortdoc>Moves the source file into the destination.</shortdoc>
</kw>
<kw name="Move Files" lineno="900">
<arguments repr="*sources_and_destination">
<arg kind="VAR_POSITIONAL" required="false" repr="*sources_and_destination">
<name>sources_and_destination</name>
</arg>
</arguments>
<doc>Moves specified files to the target directory.

Arguments have exactly same semantics as with `Copy Files` keyword.

See also `Move File`, `Copy File`, and `Copy Files`.</doc>
<shortdoc>Moves specified files to the target directory.</shortdoc>
</kw>
<kw name="Normalize Path" lineno="1113">
<arguments repr="path, case_normalize=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_normalize=False">
<name>case_normalize</name>
<default>False</default>
</arg>
</arguments>
<doc>Normalizes the given path.

- Collapses redundant separators and up-level references.
- Converts ``/`` to ``\`` on Windows.
- Replaces initial ``~`` or ``~user`` by that user's home directory.
- If ``case_normalize`` is given a true value (see `Boolean arguments`)
  on Windows, converts the path to all lowercase.
- Converts ``pathlib.Path`` instances to ``str``.

Examples:
| ${path1} = | Normalize Path | abc/           |
| ${path2} = | Normalize Path | abc/../def     |
| ${path3} = | Normalize Path | abc/./def//ghi |
| ${path4} = | Normalize Path | ~robot/stuff   |
=&gt;
- ${path1} = 'abc'
- ${path2} = 'def'
- ${path3} = 'abc/def/ghi'
- ${path4} = '/home/robot/stuff'

On Windows result would use ``\`` instead of ``/`` and home directory
would be different.</doc>
<shortdoc>Normalizes the given path.</shortdoc>
</kw>
<kw name="Remove Directory" lineno="713">
<arguments repr="path, recursive=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="recursive=False">
<name>recursive</name>
<default>False</default>
</arg>
</arguments>
<doc>Removes the directory pointed to by the given ``path``.

If the second argument ``recursive`` is given a true value (see
`Boolean arguments`), the directory is removed recursively. Otherwise
removing fails if the directory is not empty.

If the directory pointed to by the ``path`` does not exist, the keyword
passes, but it fails, if the ``path`` points to a file.</doc>
<shortdoc>Removes the directory pointed to by the given ``path``.</shortdoc>
</kw>
<kw name="Remove Environment Variable" lineno="1015">
<arguments repr="*names">
<arg kind="VAR_POSITIONAL" required="false" repr="*names">
<name>names</name>
</arg>
</arguments>
<doc>Deletes the specified environment variable.

Does nothing if the environment variable is not set.

It is possible to remove multiple variables by passing them to this
keyword as separate arguments.</doc>
<shortdoc>Deletes the specified environment variable.</shortdoc>
</kw>
<kw name="Remove File" lineno="653">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Removes a file with the given path.

Passes if the file does not exist, but fails if the path does
not point to a regular file (e.g. it points to a directory).

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.
If the path is a pattern, all files matching it are removed.</doc>
<shortdoc>Removes a file with the given path.</shortdoc>
</kw>
<kw name="Remove Files" lineno="673">
<arguments repr="*paths">
<arg kind="VAR_POSITIONAL" required="false" repr="*paths">
<name>paths</name>
</arg>
</arguments>
<doc>Uses `Remove File` to remove multiple files one-by-one.

Example:
| Remove Files | ${TEMPDIR}${/}foo.txt | ${TEMPDIR}${/}bar.txt | ${TEMPDIR}${/}zap.txt |</doc>
<shortdoc>Uses `Remove File` to remove multiple files one-by-one.</shortdoc>
</kw>
<kw name="Run" lineno="159">
<arguments repr="command">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
</arguments>
<doc>Runs the given command in the system and returns the output.

The execution status of the command *is not checked* by this
keyword, and it must be done separately based on the returned
output. If the execution return code is needed, either `Run
And Return RC` or `Run And Return RC And Output` can be used.

The standard error stream is automatically redirected to the standard
output stream by adding ``2&gt;&amp;1`` after the executed command. This
automatic redirection is done only when the executed command does not
contain additional output redirections. You can thus freely forward
the standard error somewhere else, for example, like
``my_command 2&gt;stderr.txt``.

The returned output contains everything written into the standard
output or error streams by the command (unless either of them
is redirected explicitly). Many commands add an extra newline
(``\n``) after the output to make it easier to read in the
console. To ease processing the returned output, this possible
trailing newline is stripped by this keyword.

Examples:
| ${output} =        | Run       | ls -lhF /tmp |
| Log                | ${output} |
| ${result} =        | Run       | ${CURDIR}${/}tester.py arg1 arg2 |
| Should Not Contain | ${result} | FAIL |
| ${stdout} =        | Run       | /opt/script.sh 2&gt;/tmp/stderr.txt |
| Should Be Equal    | ${stdout} | TEST PASSED |
| File Should Be Empty | /tmp/stderr.txt |

*TIP:* `Run Process` keyword provided by the
[http://robotframework.org/robotframework/latest/libraries/Process.html|
Process library] supports better process configuration and is generally
recommended as a replacement for this keyword.</doc>
<shortdoc>Runs the given command in the system and returns the output.</shortdoc>
</kw>
<kw name="Run And Return Rc" lineno="197">
<arguments repr="command">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
</arguments>
<doc>Runs the given command in the system and returns the return code.

The return code (RC) is returned as a positive integer in
range from 0 to 255 as returned by the executed command. On
some operating systems (notable Windows) original return codes
can be something else, but this keyword always maps them to
the 0-255 range. Since the RC is an integer, it must be
checked e.g. with the keyword `Should Be Equal As Integers`
instead of `Should Be Equal` (both are built-in keywords).

Examples:
| ${rc} = | Run and Return RC | ${CURDIR}${/}script.py arg |
| Should Be Equal As Integers | ${rc} | 0 |
| ${rc} = | Run and Return RC | /path/to/example.rb arg1 arg2 |
| Should Be True | 0 &lt; ${rc} &lt; 42 |

See `Run` and `Run And Return RC And Output` if you need to get the
output of the executed command.

*TIP:* `Run Process` keyword provided by the
[http://robotframework.org/robotframework/latest/libraries/Process.html|
Process library] supports better process configuration and is generally
recommended as a replacement for this keyword.</doc>
<shortdoc>Runs the given command in the system and returns the return code.</shortdoc>
</kw>
<kw name="Run And Return Rc And Output" lineno="224">
<arguments repr="command">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
</arguments>
<doc>Runs the given command in the system and returns the RC and output.

The return code (RC) is returned similarly as with `Run And Return RC`
and the output similarly as with `Run`.

Examples:
| ${rc} | ${output} =  | Run and Return RC and Output | ${CURDIR}${/}mytool |
| Should Be Equal As Integers | ${rc}    | 0    |
| Should Not Contain   | ${output}       | FAIL |
| ${rc} | ${stdout} =  | Run and Return RC and Output | /opt/script.sh 2&gt;/tmp/stderr.txt |
| Should Be True       | ${rc} &gt; 42      |
| Should Be Equal      | ${stdout}       | TEST PASSED |
| File Should Be Empty | /tmp/stderr.txt |

*TIP:* `Run Process` keyword provided by the
[http://robotframework.org/robotframework/latest/libraries/Process.html|
Process library] supports better process configuration and is generally
recommended as a replacement for this keyword.</doc>
<shortdoc>Runs the given command in the system and returns the RC and output.</shortdoc>
</kw>
<kw name="Set Environment Variable" lineno="973">
<arguments repr="name, value">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
</arguments>
<doc>Sets an environment variable to a specified value.

Values are converted to strings automatically. Set variables are
automatically encoded using the system encoding.</doc>
<shortdoc>Sets an environment variable to a specified value.</shortdoc>
</kw>
<kw name="Set Modified Time" lineno="1258">
<arguments repr="path, mtime">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="mtime">
<name>mtime</name>
</arg>
</arguments>
<doc>Sets the file modification and access times.

Changes the modification and access times of the given file to
the value determined by ``mtime``. The time can be given in
different formats described below. Note that all checks
involving strings are case-insensitive. Modified time can only
be set to regular files.

1) If ``mtime`` is a number, or a string that can be converted
   to a number, it is interpreted as seconds since the UNIX
   epoch (1970-01-01 00:00:00 UTC). This documentation was
   originally written about 1177654467 seconds after the epoch.

2) If ``mtime`` is a timestamp, that time will be used. Valid
   timestamp formats are ``YYYY-MM-DD hh:mm:ss`` and
   ``YYYYMMDD hhmmss``.

3) If ``mtime`` is equal to ``NOW``, the current local time is used.

4) If ``mtime`` is equal to ``UTC``, the current time in
   [http://en.wikipedia.org/wiki/Coordinated_Universal_Time|UTC]
   is used.

5) If ``mtime`` is in the format like ``NOW - 1 day`` or ``UTC + 1
   hour 30 min``, the current local/UTC time plus/minus the time
   specified with the time string is used. The time string format
   is described in an appendix of Robot Framework User Guide.

Examples:
| Set Modified Time | /path/file | 1177654467         | # Time given as epoch seconds |
| Set Modified Time | /path/file | 2007-04-27 9:14:27 | # Time given as a timestamp   |
| Set Modified Time | /path/file | NOW                | # The local time of execution |
| Set Modified Time | /path/file | NOW - 1 day        | # 1 day subtracted from the local time |
| Set Modified Time | /path/file | UTC + 1h 2min 3s   | # 1h 2min 3s added to the UTC time |</doc>
<shortdoc>Sets the file modification and access times.</shortdoc>
</kw>
<kw name="Should Exist" lineno="374">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the given path (file or directory) exists.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails unless the given path (file or directory) exists.</shortdoc>
</kw>
<kw name="Should Not Exist" lineno="387">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given path (file or directory) exists.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.

The default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Fails if the given path (file or directory) exists.</shortdoc>
</kw>
<kw name="Split Extension" lineno="1169">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Splits the extension from the given path.

The given path is first normalized (e.g. possible trailing
path separators removed, special directories ``..`` and ``.``
removed). The base path and extension are returned as separate
components so that the dot used as an extension separator is
removed. If the path contains no extension, an empty string is
returned for it. Possible leading and trailing dots in the file
name are never considered to be extension separators.

Examples:
| ${path} | ${ext} = | Split Extension | file.extension    |
| ${p2}   | ${e2} =  | Split Extension | path/file.ext     |
| ${p3}   | ${e3} =  | Split Extension | path/file         |
| ${p4}   | ${e4} =  | Split Extension | p1/../p2/file.ext |
| ${p5}   | ${e5} =  | Split Extension | path/.file.ext    |
| ${p6}   | ${e6} =  | Split Extension | path/.file        |
=&gt;
- ${path} = 'file' &amp; ${ext} = 'extension'
- ${p2} = 'path/file' &amp; ${e2} = 'ext'
- ${p3} = 'path/file' &amp; ${e3} = ''
- ${p4} = 'p2/file' &amp; ${e4} = 'ext'
- ${p5} = 'path/.file' &amp; ${e5} = 'ext'
- ${p6} = 'path/.file' &amp; ${e6} = ''</doc>
<shortdoc>Splits the extension from the given path.</shortdoc>
</kw>
<kw name="Split Path" lineno="1150">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Splits the given path from the last path separator (``/`` or ``\``).

The given path is first normalized (e.g. a possible trailing
path separator is removed, special directories ``..`` and ``.``
removed). The parts that are split are returned as separate
components.

Examples:
| ${path1} | ${dir} =  | Split Path | abc/def         |
| ${path2} | ${file} = | Split Path | abc/def/ghi.txt |
| ${path3} | ${d2}  =  | Split Path | abc/../def/ghi/ |
=&gt;
- ${path1} = 'abc' &amp; ${dir} = 'def'
- ${path2} = 'abc/def' &amp; ${file} = 'ghi.txt'
- ${path3} = 'def' &amp; ${d2} = 'ghi'</doc>
<shortdoc>Splits the given path from the last path separator (``/`` or ``\``).</shortdoc>
</kw>
<kw name="Touch" lineno="1403">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Emulates the UNIX touch command.

Creates a file, if it does not exist. Otherwise changes its access and
modification times to the current time.

Fails if used with the directories or the parent directory of the given
file does not exist.</doc>
<shortdoc>Emulates the UNIX touch command.</shortdoc>
</kw>
<kw name="Wait Until Created" lineno="496">
<arguments repr="path, timeout=1 minute">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=1 minute">
<name>timeout</name>
<default>1 minute</default>
</arg>
</arguments>
<doc>Waits until the given file or directory is created.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.
If the path is a pattern, the keyword returns when an item matching
it is created.

The optional ``timeout`` can be used to control the maximum time of
waiting. The timeout is given as a timeout string, e.g. in a format
``15 seconds``, ``1min 10s`` or just ``10``. The time string format is
described in an appendix of Robot Framework User Guide.

If the timeout is negative, the keyword is never timed-out. The keyword
returns immediately, if the path already exists.</doc>
<shortdoc>Waits until the given file or directory is created.</shortdoc>
</kw>
<kw name="Wait Until Removed" lineno="470">
<arguments repr="path, timeout=1 minute">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=1 minute">
<name>timeout</name>
<default>1 minute</default>
</arg>
</arguments>
<doc>Waits until the given file or directory is removed.

The path can be given as an exact path or as a glob pattern.
See the `Glob patterns` section for details about the supported syntax.
If the path is a pattern, the keyword waits until all matching
items are removed.

The optional ``timeout`` can be used to control the maximum time of
waiting. The timeout is given as a timeout string, e.g. in a format
``15 seconds``, ``1min 10s`` or just ``10``. The time string format is
described in an appendix of Robot Framework User Guide.

If the timeout is negative, the keyword is never timed-out. The keyword
returns immediately, if the path does not exist in the first place.</doc>
<shortdoc>Waits until the given file or directory is removed.</shortdoc>
</kw>
</keywords>
<typedocs>
</typedocs>
</keywordspec>
