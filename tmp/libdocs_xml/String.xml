<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="String" type="LIBRARY" format="ROBOT" scope="GLOBAL" generated="2024-07-26T11:05:34+00:00" specversion="6" source="C:\Users\maire\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\robot\libraries\String.py" lineno="28">
<version>7.0.1</version>
<doc>A library for string manipulation and verification.

``String`` is Robot Framework's standard library for manipulating
strings (e.g. `Replace String Using Regexp`, `Split To Lines`) and
verifying their contents (e.g. `Should Be String`).

Following keywords from ``BuiltIn`` library can also be used with strings:

- `Catenate`
- `Get Length`
- `Length Should Be`
- `Should (Not) Be Empty`
- `Should (Not) Be Equal (As Strings/Integers/Numbers)`
- `Should (Not) Match (Regexp)`
- `Should (Not) Contain`
- `Should (Not) Start With`
- `Should (Not) End With`
- `Convert To String`
- `Convert To Bytes`</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Convert To Lower Case" lineno="52">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>Converts string to lower case.

Uses Python's standard
[https://docs.python.org/library/stdtypes.html#str.lower|lower()]
method.

Examples:
| ${str1} = | Convert To Lower Case | ABC |
| ${str2} = | Convert To Lower Case | 1A2c3D |
| Should Be Equal | ${str1} | abc |
| Should Be Equal | ${str2} | 1a2c3d |</doc>
<shortdoc>Converts string to lower case.</shortdoc>
</kw>
<kw name="Convert To Title Case" lineno="83">
<arguments repr="string, exclude=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude=None">
<name>exclude</name>
<default>None</default>
</arg>
</arguments>
<doc>Converts string to title case.

Uses the following algorithm:

- Split the string to words from whitespace characters (spaces,
  newlines, etc.).
- Exclude words that are not all lower case. This preserves,
  for example, "OK" and "iPhone".
- Exclude also words listed in the optional ``exclude`` argument.
- Title case the first alphabetical character of each word that has
  not been excluded.
- Join all words together so that original whitespace is preserved.

Explicitly excluded words can be given as a list or as a string with
words separated by a comma and an optional space. Excluded words are
actually considered to be regular expression patterns, so it is
possible to use something like "example[.!?]?" to match the word
"example" on it own and also if followed by ".", "!" or "?".
See `BuiltIn.Should Match Regexp` for more information about Python
regular expression syntax in general and how to use it in Robot
Framework data in particular.

Examples:
| ${str1} = | Convert To Title Case | hello, world!     |
| ${str2} = | Convert To Title Case | it's an OK iPhone | exclude=a, an, the |
| ${str3} = | Convert To Title Case | distance is 1 km. | exclude=is, km.? |
| Should Be Equal | ${str1} | Hello, World! |
| Should Be Equal | ${str2} | It's an OK iPhone |
| Should Be Equal | ${str3} | Distance is 1 km. |

The reason this keyword does not use Python's standard
[https://docs.python.org/library/stdtypes.html#str.title|title()]
method is that it can yield undesired results, for example, if
strings contain upper case letters or special characters like
apostrophes. It would, for example, convert "it's an OK iPhone"
to "It'S An Ok Iphone".</doc>
<shortdoc>Converts string to title case.</shortdoc>
</kw>
<kw name="Convert To Upper Case" lineno="67">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>Converts string to upper case.

Uses Python's standard
[https://docs.python.org/library/stdtypes.html#str.upper|upper()]
method.

Examples:
| ${str1} = | Convert To Upper Case | abc |
| ${str2} = | Convert To Upper Case | 1a2C3d |
| Should Be Equal | ${str1} | ABC |
| Should Be Equal | ${str2} | 1A2C3D |</doc>
<shortdoc>Converts string to upper case.</shortdoc>
</kw>
<kw name="Decode Bytes To String" lineno="163">
<arguments repr="bytes, encoding, errors=strict">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="bytes">
<name>bytes</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="encoding">
<name>encoding</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="errors=strict">
<name>errors</name>
<default>strict</default>
</arg>
</arguments>
<doc>Decodes the given ``bytes`` to a string using the given ``encoding``.

``errors`` argument controls what to do if decoding some bytes fails.
All values accepted by ``decode`` method in Python are valid, but in
practice the following values are most useful:

- ``strict``: fail if characters cannot be decoded (default)
- ``ignore``: ignore characters that cannot be decoded
- ``replace``: replace characters that cannot be decoded with
  a replacement character

Examples:
| ${string} = | Decode Bytes To String | ${bytes} | UTF-8 |
| ${string} = | Decode Bytes To String | ${bytes} | ASCII | errors=ignore |

Use `Encode String To Bytes` if you need to convert strings to bytes,
and `Convert To String` in ``BuiltIn`` if you need to
convert arbitrary objects to strings.</doc>
<shortdoc>Decodes the given ``bytes`` to a string using the given ``encoding``.</shortdoc>
</kw>
<kw name="Encode String To Bytes" lineno="140">
<arguments repr="string, encoding, errors=strict">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="encoding">
<name>encoding</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="errors=strict">
<name>errors</name>
<default>strict</default>
</arg>
</arguments>
<doc>Encodes the given ``string`` to bytes using the given ``encoding``.

``errors`` argument controls what to do if encoding some characters fails.
All values accepted by ``encode`` method in Python are valid, but in
practice the following values are most useful:

- ``strict``: fail if characters cannot be encoded (default)
- ``ignore``: ignore characters that cannot be encoded
- ``replace``: replace characters that cannot be encoded with
  a replacement character

Examples:
| ${bytes} = | Encode String To Bytes | ${string} | UTF-8 |
| ${bytes} = | Encode String To Bytes | ${string} | ASCII | errors=ignore |

Use `Convert To Bytes` in ``BuiltIn`` if you want to create bytes based
on character or integer sequences. Use `Decode Bytes To String` if you
need to convert bytes to strings and `Convert To String`
in ``BuiltIn`` if you need to convert arbitrary objects to strings.</doc>
<shortdoc>Encodes the given ``string`` to bytes using the given ``encoding``.</shortdoc>
</kw>
<kw name="Fetch From Left" lineno="575">
<arguments repr="string, marker">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="marker">
<name>marker</name>
</arg>
</arguments>
<doc>Returns contents of the ``string`` before the first occurrence of ``marker``.

If the ``marker`` is not found, whole string is returned.

See also `Fetch From Right`, `Split String` and `Split String
From Right`.</doc>
<shortdoc>Returns contents of the ``string`` before the first occurrence of ``marker``.</shortdoc>
</kw>
<kw name="Fetch From Right" lineno="585">
<arguments repr="string, marker">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="marker">
<name>marker</name>
</arg>
</arguments>
<doc>Returns contents of the ``string`` after the last occurrence of ``marker``.

If the ``marker`` is not found, whole string is returned.

See also `Fetch From Left`, `Split String` and `Split String
From Right`.</doc>
<shortdoc>Returns contents of the ``string`` after the last occurrence of ``marker``.</shortdoc>
</kw>
<kw name="Format String" lineno="187">
<arguments repr="template, *positional, **named">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="template">
<name>template</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*positional">
<name>positional</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**named">
<name>named</name>
</arg>
</arguments>
<doc>Formats a ``template`` using the given ``positional`` and ``named`` arguments.

The template can be either be a string or an absolute path to
an existing file. In the latter case the file is read and its contents
are used as the template. If the template file contains non-ASCII
characters, it must be encoded using UTF-8.

The template is formatted using Python's
[https://docs.python.org/library/string.html#format-string-syntax|format
string syntax]. Placeholders are marked using ``{}`` with possible
field name and format specification inside. Literal curly braces
can be inserted by doubling them like `{{` and `}}`.

Examples:
| ${to} = | Format String | To: {} &lt;{}&gt;                    | ${user}      | ${email} |
| ${to} = | Format String | To: {name} &lt;{email}&gt;           | name=${name} | email=${email} |
| ${to} = | Format String | To: {user.name} &lt;{user.email}&gt; | user=${user} |
| ${xx} = | Format String | {:*^30}                        | centered     |
| ${yy} = | Format String | {0:{width}{base}}              | ${42}        | base=X | width=10 |
| ${zz} = | Format String | ${CURDIR}/template.txt         | positional   | named=value |</doc>
<shortdoc>Formats a ``template`` using the given ``positional`` and ``named`` arguments.</shortdoc>
</kw>
<kw name="Generate Random String" lineno="595">
<arguments repr="length=8, chars=[LETTERS][NUMBERS]">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="length=8">
<name>length</name>
<default>8</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="chars=[LETTERS][NUMBERS]">
<name>chars</name>
<default>[LETTERS][NUMBERS]</default>
</arg>
</arguments>
<doc>Generates a string with a desired ``length`` from the given ``chars``.

``length`` can be given as a number, a string representation of a number,
or as a range of numbers, such as ``5-10``. When a range of values is given
the range will be selected by random within the range.

The population sequence ``chars`` contains the characters to use
when generating the random string. It can contain any
characters, and it is possible to use special markers
explained in the table below:

|  = Marker =   |               = Explanation =                   |
| ``[LOWER]``   | Lowercase ASCII characters from ``a`` to ``z``. |
| ``[UPPER]``   | Uppercase ASCII characters from ``A`` to ``Z``. |
| ``[LETTERS]`` | Lowercase and uppercase ASCII characters.       |
| ``[NUMBERS]`` | Numbers from 0 to 9.                            |

Examples:
| ${ret} = | Generate Random String |
| ${low} = | Generate Random String | 12 | [LOWER]         |
| ${bin} = | Generate Random String | 8  | 01              |
| ${hex} = | Generate Random String | 4  | [NUMBERS]abcdef |
| ${rnd} = | Generate Random String | 5-10 | # Generates a string 5 to 10 characters long |

Giving ``length`` as a range of values is new in Robot Framework 5.0.</doc>
<shortdoc>Generates a string with a desired ``length`` from the given ``chars``.</shortdoc>
</kw>
<kw name="Get Line" lineno="250">
<arguments repr="string, line_number">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="line_number">
<name>line_number</name>
</arg>
</arguments>
<doc>Returns the specified line from the given ``string``.

Line numbering starts from 0, and it is possible to use
negative indices to refer to lines from the end. The line is
returned without the newline character.

Examples:
| ${first} =    | Get Line | ${string} | 0  |
| ${2nd last} = | Get Line | ${string} | -2 |

Use `Split To Lines` if all lines are needed.</doc>
<shortdoc>Returns the specified line from the given ``string``.</shortdoc>
</kw>
<kw name="Get Line Count" lineno="217">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>Returns and logs the number of lines in the given string.</doc>
<shortdoc>Returns and logs the number of lines in the given string.</shortdoc>
</kw>
<kw name="Get Lines Containing String" lineno="266">
<arguments repr="string: str, pattern: str, case_insensitive: bool | None = None, ignore_case: bool = False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string: str">
<name>string</name>
<type name="str" typedoc="string"/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern: str">
<name>pattern</name>
<type name="str" typedoc="string"/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive: bool | None = None">
<name>case_insensitive</name>
<type name="Union" union="true">
<type name="bool" typedoc="boolean"/>
<type name="None" typedoc="None"/>
</type>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case: bool = False">
<name>ignore_case</name>
<type name="bool" typedoc="boolean"/>
<default>False</default>
</arg>
</arguments>
<doc>Returns lines of the given ``string`` that contain the ``pattern``.

The ``pattern`` is always considered to be a normal string, not a glob
or regexp pattern. A line matches if the ``pattern`` is found anywhere
on it.

The match is case-sensitive by default, but that can be changed by
giving ``ignore_case`` a true value. This option is new in Robot
Framework 7.0, but with older versions it is possible to use the
nowadays deprecated ``case_insensitive`` argument.

Lines are returned as a string with lines joined together with
a newline. Possible trailing newline is never returned. The number
of matching lines is automatically logged.

Examples:
| ${lines} = | Get Lines Containing String | ${result} | An example |
| ${ret} =   | Get Lines Containing String | ${ret} | FAIL | ignore_case=True |

See `Get Lines Matching Pattern` and `Get Lines Matching Regexp`
if you need more complex pattern matching.</doc>
<shortdoc>Returns lines of the given ``string`` that contain the ``pattern``.</shortdoc>
</kw>
<kw name="Get Lines Matching Pattern" lineno="300">
<arguments repr="string: str, pattern: str, case_insensitive: bool | None = None, ignore_case: bool = False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string: str">
<name>string</name>
<type name="str" typedoc="string"/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern: str">
<name>pattern</name>
<type name="str" typedoc="string"/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive: bool | None = None">
<name>case_insensitive</name>
<type name="Union" union="true">
<type name="bool" typedoc="boolean"/>
<type name="None" typedoc="None"/>
</type>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case: bool = False">
<name>ignore_case</name>
<type name="bool" typedoc="boolean"/>
<default>False</default>
</arg>
</arguments>
<doc>Returns lines of the given ``string`` that match the ``pattern``.

The ``pattern`` is a _glob pattern_ where:
| ``*``        | matches everything |
| ``?``        | matches any single character |
| ``[chars]``  | matches any character inside square brackets (e.g. ``[abc]`` matches either ``a``, ``b`` or ``c``) |
| ``[!chars]`` | matches any character not inside square brackets |

A line matches only if it matches the ``pattern`` fully.

The match is case-sensitive by default, but that can be changed by
giving ``ignore_case`` a true value. This option is new in Robot
Framework 7.0, but with older versions it is possible to use the
nowadays deprecated ``case_insensitive`` argument.

Lines are returned as a string with lines joined together with
a newline. Possible trailing newline is never returned. The number
of matching lines is automatically logged.

Examples:
| ${lines} = | Get Lines Matching Pattern | ${result} | Wild???? example |
| ${ret} = | Get Lines Matching Pattern | ${ret} | FAIL: * | ignore_case=True |

See `Get Lines Matching Regexp` if you need more complex
patterns and `Get Lines Containing String` if searching
literal strings is enough.</doc>
<shortdoc>Returns lines of the given ``string`` that match the ``pattern``.</shortdoc>
</kw>
<kw name="Get Lines Matching Regexp" lineno="339">
<arguments repr="string, pattern, partial_match=False, flags=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="partial_match=False">
<name>partial_match</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="flags=None">
<name>flags</name>
<default>None</default>
</arg>
</arguments>
<doc>Returns lines of the given ``string`` that match the regexp ``pattern``.

See `BuiltIn.Should Match Regexp` for more information about
Python regular expression syntax in general and how to use it
in Robot Framework data in particular.

Lines match only if they match the pattern fully by default, but
partial matching can be enabled by giving the ``partial_match``
argument a true value.

If the pattern is empty, it matches only empty lines by default.
When partial matching is enabled, empty pattern matches all lines.

Possible flags altering how the expression is parsed (e.g. ``re.IGNORECASE``,
``re.VERBOSE``) can be given using the ``flags`` argument (e.g.
``flags=IGNORECASE | VERBOSE``) or embedded to the pattern (e.g.
``(?ix)pattern``).

Lines are returned as one string concatenated back together with
newlines. Possible trailing newline is never returned. The
number of matching lines is automatically logged.

Examples:
| ${lines} = | Get Lines Matching Regexp | ${result} | Reg\\w{3} example |
| ${lines} = | Get Lines Matching Regexp | ${result} | Reg\\w{3} example | partial_match=true |
| ${ret} =   | Get Lines Matching Regexp | ${ret}    | (?i)FAIL: .* |
| ${ret} =   | Get Lines Matching Regexp | ${ret}    | FAIL: .* | flags=IGNORECASE |

See `Get Lines Matching Pattern` and `Get Lines Containing String` if you
do not need the full regular expression powers (and complexity).

The ``flags`` argument is new in Robot Framework 6.0.</doc>
<shortdoc>Returns lines of the given ``string`` that match the regexp ``pattern``.</shortdoc>
</kw>
<kw name="Get Regexp Matches" lineno="383">
<arguments repr="string, pattern, *groups, flags=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*groups">
<name>groups</name>
</arg>
<arg kind="NAMED_ONLY" required="false" repr="flags=None">
<name>flags</name>
<default>None</default>
</arg>
</arguments>
<doc>Returns a list of all non-overlapping matches in the given string.

``string`` is the string to find matches from and ``pattern`` is the
regular expression. See `BuiltIn.Should Match Regexp` for more
information about Python regular expression syntax in general and how
to use it in Robot Framework data in particular.

If no groups are used, the returned list contains full matches. If one
group is used, the list contains only contents of that group. If
multiple groups are used, the list contains tuples that contain
individual group contents. All groups can be given as indexes (starting
from 1) and named groups also as names.

Possible flags altering how the expression is parsed (e.g. ``re.IGNORECASE``,
``re.MULTILINE``) can be given using the ``flags`` argument (e.g.
``flags=IGNORECASE | MULTILINE``) or embedded to the pattern (e.g.
``(?im)pattern``).

Examples:
| ${no match} =    | Get Regexp Matches | the string | xxx     |
| ${matches} =     | Get Regexp Matches | the string | t..     |
| ${matches} =     | Get Regexp Matches | the string | T..     | flags=IGNORECASE |
| ${one group} =   | Get Regexp Matches | the string | t(..)   | 1 |
| ${named group} = | Get Regexp Matches | the string | t(?P&lt;name&gt;..) | name |
| ${two groups} =  | Get Regexp Matches | the string | t(.)(.) | 1 | 2 |
=&gt;
| ${no match} = []
| ${matches} = ['the', 'tri']
| ${one group} = ['he', 'ri']
| ${named group} = ['he', 'ri']
| ${two groups} = [('h', 'e'), ('r', 'i')]

The ``flags`` argument is new in Robot Framework 6.0.</doc>
<shortdoc>Returns a list of all non-overlapping matches in the given string.</shortdoc>
</kw>
<kw name="Get Substring" lineno="638">
<arguments repr="string, start, end=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="start">
<name>start</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="end=None">
<name>end</name>
<default>None</default>
</arg>
</arguments>
<doc>Returns a substring from ``start`` index to ``end`` index.

The ``start`` index is inclusive and ``end`` is exclusive.
Indexing starts from 0, and it is possible to use
negative indices to refer to characters from the end.

Examples:
| ${ignore first} = | Get Substring | ${string} | 1  |    |
| ${ignore last} =  | Get Substring | ${string} | 0  | -1 |
| ${5th to 10th} =  | Get Substring | ${string} | 4  | 10 |
| ${first two} =    | Get Substring | ${string} | 0  | 1  |
| ${last two} =     | Get Substring | ${string} | -2 |    |</doc>
<shortdoc>Returns a substring from ``start`` index to ``end`` index.</shortdoc>
</kw>
<kw name="Remove String" lineno="480">
<arguments repr="string, *removables">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*removables">
<name>removables</name>
</arg>
</arguments>
<doc>Removes all ``removables`` from the given ``string``.

``removables`` are used as literal strings. Each removable will be
matched to a temporary string from which preceding removables have
been already removed. See second example below.

Use `Remove String Using Regexp` if more powerful pattern matching is
needed. If only a certain number of matches should be removed,
`Replace String` or `Replace String Using Regexp` can be used.

A modified version of the string is returned and the original
string is not altered.

Examples:
| ${str} =        | Remove String | Robot Framework | work   |
| Should Be Equal | ${str}        | Robot Frame     |
| ${str} =        | Remove String | Robot Framework | o | bt |
| Should Be Equal | ${str}        | R Framewrk      |</doc>
<shortdoc>Removes all ``removables`` from the given ``string``.</shortdoc>
</kw>
<kw name="Remove String Using Regexp" lineno="504">
<arguments repr="string, *patterns, flags=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*patterns">
<name>patterns</name>
</arg>
<arg kind="NAMED_ONLY" required="false" repr="flags=None">
<name>flags</name>
<default>None</default>
</arg>
</arguments>
<doc>Removes ``patterns`` from the given ``string``.

This keyword is otherwise identical to `Remove String`, but
the ``patterns`` to search for are considered to be a regular
expression. See `Replace String Using Regexp` for more information
about the regular expression syntax. That keyword can also be
used if there is a need to remove only a certain number of
occurrences.

Possible flags altering how the expression is parsed (e.g. ``re.IGNORECASE``,
``re.MULTILINE``) can be given using the ``flags`` argument (e.g.
``flags=IGNORECASE | MULTILINE``) or embedded to the pattern (e.g.
``(?im)pattern``).

The ``flags`` argument is new in Robot Framework 6.0.</doc>
<shortdoc>Removes ``patterns`` from the given ``string``.</shortdoc>
</kw>
<kw name="Replace String" lineno="428">
<arguments repr="string, search_for, replace_with, count=-1">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="search_for">
<name>search_for</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="replace_with">
<name>replace_with</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="count=-1">
<name>count</name>
<default>-1</default>
</arg>
</arguments>
<doc>Replaces ``search_for`` in the given ``string`` with ``replace_with``.

``search_for`` is used as a literal string. See `Replace String
Using Regexp` if more powerful pattern matching is needed.
If you need to just remove a string see `Remove String`.

If the optional argument ``count`` is given, only that many
occurrences from left are replaced. Negative ``count`` means
that all occurrences are replaced (default behaviour) and zero
means that nothing is done.

A modified version of the string is returned and the original
string is not altered.

Examples:
| ${str} =        | Replace String | Hello, world!  | world | tellus   |
| Should Be Equal | ${str}         | Hello, tellus! |       |          |
| ${str} =        | Replace String | Hello, world!  | l     | ${EMPTY} | count=1 |
| Should Be Equal | ${str}         | Helo, world!   |       |          |</doc>
<shortdoc>Replaces ``search_for`` in the given ``string`` with ``replace_with``.</shortdoc>
</kw>
<kw name="Replace String Using Regexp" lineno="452">
<arguments repr="string, pattern, replace_with, count=-1, flags=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="replace_with">
<name>replace_with</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="count=-1">
<name>count</name>
<default>-1</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="flags=None">
<name>flags</name>
<default>None</default>
</arg>
</arguments>
<doc>Replaces ``pattern`` in the given ``string`` with ``replace_with``.

This keyword is otherwise identical to `Replace String`, but
the ``pattern`` to search for is considered to be a regular
expression.  See `BuiltIn.Should Match Regexp` for more
information about Python regular expression syntax in general
and how to use it in Robot Framework data in particular.

Possible flags altering how the expression is parsed (e.g. ``re.IGNORECASE``,
``re.MULTILINE``) can be given using the ``flags`` argument (e.g.
``flags=IGNORECASE | MULTILINE``) or embedded to the pattern (e.g.
``(?im)pattern``).

If you need to just remove a string see `Remove String Using Regexp`.

Examples:
| ${str} = | Replace String Using Regexp | ${str} | 20\\d\\d-\\d\\d-\\d\\d | &lt;DATE&gt; |
| ${str} = | Replace String Using Regexp | ${str} | (Hello|Hi) | ${EMPTY} | count=1 |

The ``flags`` argument is new in Robot Framework 6.0.</doc>
<shortdoc>Replaces ``pattern`` in the given ``string`` with ``replace_with``.</shortdoc>
</kw>
<kw name="Should Be Byte String" lineno="711">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given ``item`` is not a byte string.

Use `Should Be String` if you want to verify the ``item`` is a string.

The default error message can be overridden with the optional ``msg`` argument.</doc>
<shortdoc>Fails if the given ``item`` is not a byte string.</shortdoc>
</kw>
<kw name="Should Be Lower Case" lineno="721">
<arguments repr="string, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given ``string`` is not in lower case.

For example, ``'string'`` and ``'with specials!'`` would pass, and
``'String'``, ``''`` and ``' '`` would fail.

The default error message can be overridden with the optional
``msg`` argument.

See also `Should Be Upper Case` and `Should Be Title Case`.</doc>
<shortdoc>Fails if the given ``string`` is not in lower case.</shortdoc>
</kw>
<kw name="Should Be String" lineno="687">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given ``item`` is not a string.

The default error message can be overridden with the optional ``msg`` argument.</doc>
<shortdoc>Fails if the given ``item`` is not a string.</shortdoc>
</kw>
<kw name="Should Be Title Case" lineno="750">
<arguments repr="string, msg=None, exclude=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude=None">
<name>exclude</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if given ``string`` is not title.

``string`` is a title cased string if there is at least one upper case
letter in each word.

For example, ``'This Is Title'`` and ``'OK, Give Me My iPhone'``
would pass. ``'all words lower'`` and ``'Word In lower'`` would fail.

This logic changed in Robot Framework 4.0 to be compatible with
`Convert to Title Case`. See `Convert to Title Case` for title case
algorithm and reasoning.

The default error message can be overridden with the optional
``msg`` argument.

Words can be explicitly excluded with the optional ``exclude`` argument.

Explicitly excluded words can be given as a list or as a string with
words separated by a comma and an optional space. Excluded words are
actually considered to be regular expression patterns, so it is
possible to use something like "example[.!?]?" to match the word
"example" on it own and also if followed by ".", "!" or "?".
See `BuiltIn.Should Match Regexp` for more information about Python
regular expression syntax in general and how to use it in Robot
Framework data in particular.

See also `Should Be Upper Case` and `Should Be Lower Case`.</doc>
<shortdoc>Fails if given ``string`` is not title.</shortdoc>
</kw>
<kw name="Should Be Unicode String" lineno="703">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given ``item`` is not a Unicode string.

On Python 3 this keyword behaves exactly the same way `Should Be String`.
That keyword should be used instead and this keyword will be deprecated.</doc>
<shortdoc>Fails if the given ``item`` is not a Unicode string.</shortdoc>
</kw>
<kw name="Should Be Upper Case" lineno="735">
<arguments repr="string, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given ``string`` is not in upper case.

For example, ``'STRING'`` and ``'WITH SPECIALS!'`` would pass, and
``'String'``, ``''`` and ``' '`` would fail.

The default error message can be overridden with the optional
``msg`` argument.

See also `Should Be Title Case` and `Should Be Lower Case`.</doc>
<shortdoc>Fails if the given ``string`` is not in upper case.</shortdoc>
</kw>
<kw name="Should Not Be String" lineno="695">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given ``item`` is a string.

The default error message can be overridden with the optional ``msg`` argument.</doc>
<shortdoc>Fails if the given ``item`` is a string.</shortdoc>
</kw>
<kw name="Split String" lineno="526">
<arguments repr="string, separator=None, max_split=-1">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="separator=None">
<name>separator</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="max_split=-1">
<name>max_split</name>
<default>-1</default>
</arg>
</arguments>
<doc>Splits the ``string`` using ``separator`` as a delimiter string.

If a ``separator`` is not given, any whitespace string is a
separator. In that case also possible consecutive whitespace
as well as leading and trailing whitespace is ignored.

Split words are returned as a list. If the optional
``max_split`` is given, at most ``max_split`` splits are done, and
the returned list will have maximum ``max_split + 1`` elements.

Examples:
| @{words} =         | Split String | ${string} |
| @{words} =         | Split String | ${string} | ,${SPACE} |
| ${pre} | ${post} = | Split String | ${string} | ::    | 1 |

See `Split String From Right` if you want to start splitting
from right, and `Fetch From Left` and `Fetch From Right` if
you only want to get first/last part of the string.</doc>
<shortdoc>Splits the ``string`` using ``separator`` as a delimiter string.</shortdoc>
</kw>
<kw name="Split String From Right" lineno="552">
<arguments repr="string, separator=None, max_split=-1">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="separator=None">
<name>separator</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="max_split=-1">
<name>max_split</name>
<default>-1</default>
</arg>
</arguments>
<doc>Splits the ``string`` using ``separator`` starting from right.

Same as `Split String`, but splitting is started from right. This has
an effect only when ``max_split`` is given.

Examples:
| ${first} | ${rest} = | Split String            | ${string} | - | 1 |
| ${rest}  | ${last} = | Split String From Right | ${string} | - | 1 |</doc>
<shortdoc>Splits the ``string`` using ``separator`` starting from right.</shortdoc>
</kw>
<kw name="Split String To Characters" lineno="567">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>Splits the given ``string`` to characters.

Example:
| @{characters} = | Split String To Characters | ${string} |</doc>
<shortdoc>Splits the given ``string`` to characters.</shortdoc>
</kw>
<kw name="Split To Lines" lineno="223">
<arguments repr="string, start=0, end=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="start=0">
<name>start</name>
<default>0</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="end=None">
<name>end</name>
<default>None</default>
</arg>
</arguments>
<doc>Splits the given string to lines.

It is possible to get only a selection of lines from ``start``
to ``end`` so that ``start`` index is inclusive and ``end`` is
exclusive. Line numbering starts from 0, and it is possible to
use negative indices to refer to lines from the end.

Lines are returned without the newlines. The number of
returned lines is automatically logged.

Examples:
| @{lines} =        | Split To Lines | ${manylines} |    |    |
| @{ignore first} = | Split To Lines | ${manylines} | 1  |    |
| @{ignore last} =  | Split To Lines | ${manylines} |    | -1 |
| @{5th to 10th} =  | Split To Lines | ${manylines} | 4  | 10 |
| @{first two} =    | Split To Lines | ${manylines} |    | 1  |
| @{last two} =     | Split To Lines | ${manylines} | -2 |    |

Use `Get Line` if you only need to get a single line.</doc>
<shortdoc>Splits the given string to lines.</shortdoc>
</kw>
<kw name="Strip String" lineno="657">
<arguments repr="string, mode=both, characters=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="mode=both">
<name>mode</name>
<default>both</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="characters=None">
<name>characters</name>
<default>None</default>
</arg>
</arguments>
<doc>Remove leading and/or trailing whitespaces from the given string.

``mode`` is either ``left`` to remove leading characters, ``right`` to
remove trailing characters, ``both`` (default) to remove the
characters from both sides of the string or ``none`` to return the
unmodified string.

If the optional ``characters`` is given, it must be a string and the
characters in the string will be stripped in the string. Please note,
that this is not a substring to be removed but a list of characters,
see the example below.

Examples:
| ${stripped}=  | Strip String | ${SPACE}Hello${SPACE} | |
| Should Be Equal | ${stripped} | Hello | |
| ${stripped}=  | Strip String | ${SPACE}Hello${SPACE} | mode=left |
| Should Be Equal | ${stripped} | Hello${SPACE} | |
| ${stripped}=  | Strip String | aabaHelloeee | characters=abe |
| Should Be Equal | ${stripped} | Hello | |</doc>
<shortdoc>Remove leading and/or trailing whitespaces from the given string.</shortdoc>
</kw>
</keywords>
<typedocs>
<type name="boolean" type="Standard">
<doc>Strings ``TRUE``, ``YES``, ``ON`` and ``1`` are converted to Boolean ``True``,
the empty string as well as strings ``FALSE``, ``NO``, ``OFF`` and ``0``
are converted to Boolean ``False``, and the string ``NONE`` is converted
to the Python ``None`` object. Other strings and other accepted values are
passed as-is, allowing keywords to handle them specially if
needed. All string comparisons are case-insensitive.

Examples: ``TRUE`` (converted to ``True``), ``off`` (converted to ``False``),
``example`` (used as-is)
</doc>
<accepts>
<type>string</type>
<type>integer</type>
<type>float</type>
<type>None</type>
</accepts>
<usages>
<usage>Get Lines Containing String</usage>
<usage>Get Lines Matching Pattern</usage>
</usages>
</type>
<type name="None" type="Standard">
<doc>String ``NONE`` (case-insensitive) is converted to Python ``None`` object.
Other values cause an error.
</doc>
<accepts>
<type>string</type>
</accepts>
<usages>
<usage>Get Lines Containing String</usage>
<usage>Get Lines Matching Pattern</usage>
</usages>
</type>
<type name="string" type="Standard">
<doc>All arguments are converted to Unicode strings.</doc>
<accepts>
<type>Any</type>
</accepts>
<usages>
<usage>Get Lines Containing String</usage>
<usage>Get Lines Matching Pattern</usage>
</usages>
</type>
</typedocs>
</keywordspec>
