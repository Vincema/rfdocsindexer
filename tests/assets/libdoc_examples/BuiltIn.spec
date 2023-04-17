<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="BuiltIn" type="LIBRARY" format="ROBOT" scope="GLOBAL" generated="2023-04-17T12:52:22+00:00" specversion="4" source="/home/kali/Code/rfdocsindexer/.venv/lib/python3.10/site-packages/robot/libraries/BuiltIn.py" lineno="3668">
<version>6.0.2</version>
<doc>An always available standard library with often needed keywords.

``BuiltIn`` is Robot Framework's standard library that provides a set
of generic keywords needed often. It is imported automatically and
thus always available. The provided keywords can be used, for example,
for verifications (e.g. `Should Be Equal`, `Should Contain`),
conversions (e.g. `Convert To Integer`) and for various other purposes
(e.g. `Log`, `Sleep`, `Run Keyword If`, `Set Global Variable`).

== Table of contents ==

- `HTML error messages`
- `Using variables with keywords creating or accessing variables`
- `Evaluating expressions`
- `Boolean arguments`
- `Pattern matching`
- `Multiline string comparison`
- `String representations`
- `Keywords`

= HTML error messages =

Many of the keywords accept an optional error message to use if the keyword
fails, and it is possible to use HTML in these messages by prefixing them
with ``*HTML*``. See `Fail` keyword for a usage example. Notice that using
HTML in messages is not limited to BuiltIn library but works with any
error message.

= Using variables with keywords creating or accessing variables =

This library has special keywords `Set Global Variable`, `Set Suite Variable`,
`Set Test Variable` and `Set Local Variable` for creating variables in
different scopes. These keywords take the variable name and its value as
arguments. The name can be given using the normal ``${variable}`` syntax or
in escaped format either like ``$variable`` or ``\${variable}``. For example,
these are typically equivalent and create new suite level variable
``${name}`` with value ``value``:

| Set Suite Variable    ${name}     value
| Set Suite Variable    $name       value
| Set Suite Variable    \${name}    value

A problem with using the normal ``${variable}`` syntax is that these
keywords cannot easily know is the idea to create a variable with exactly
that name or does that variable actually contain the name of the variable
to create. If the variable does not initially exist, it will always be
created. If it exists and its value is a variable name either in the normal
or in the escaped syntax, variable with _that_ name is created instead.
For example, if ``${name}`` variable would exist and contain value
``$example``, these examples would create different variables:

| Set Suite Variable    ${name}     value    # Creates ${example}.
| Set Suite Variable    $name       value    # Creates ${name}.
| Set Suite Variable    \${name}    value    # Creates ${name}.

Because the behavior when using the normal ``${variable}`` syntax depends
on the possible existing value of the variable, it is *highly recommended
to use the escaped ``$variable`` or ``\${variable}`` format instead*.

This same problem occurs also with special keywords for accessing variables
`Get Variable Value`, `Variable Should Exist` and `Variable Should Not Exist`.

= Evaluating expressions =

Many keywords, such as `Evaluate`, `Run Keyword If` and `Should Be True`,
accept an expression that is evaluated in Python.

== Evaluation namespace ==

Expressions are evaluated using Python's
[http://docs.python.org/library/functions.html#eval|eval] function so
that all Python built-ins like ``len()`` and ``int()`` are available.
In addition to that, all unrecognized variables are considered to be
modules that are automatically imported. It is possible to use all
available Python modules, including the standard modules and the installed
third party modules.

Examples:
| `Should Be True`    len('${result}') &gt; 3
| `Run Keyword If`    os.sep == '/'    Non-Windows Keyword
| ${version} =    `Evaluate`    robot.__version__

`Evaluate` also allows configuring the execution namespace with a custom
namespace and with custom modules to be imported. The latter functionality
is useful in special cases where the automatic module import does not work
such as when using nested modules like ``rootmod.submod`` or list
comprehensions. See the documentation of the `Evaluate` keyword for mode
details.

== Variables in expressions ==

When a variable is used in the expressing using the normal ``${variable}``
syntax, its value is replaced before the expression is evaluated. This
means that the value used in the expression will be the string
representation of the variable value, not the variable value itself.
This is not a problem with numbers and other objects that have a string
representation that can be evaluated directly, but with other objects
the behavior depends on the string representation. Most importantly,
strings must always be quoted, and if they can contain newlines, they must
be triple quoted.

Examples:
| `Should Be True`    ${rc} &lt; 10                   Return code greater than 10
| `Run Keyword If`    '${status}' == 'PASS'        Log    Passed
| `Run Keyword If`    'FAIL' in '''${output}'''    Log    Output contains FAIL

Actual variables values are also available in the evaluation namespace.
They can be accessed using special variable syntax without the curly
braces like ``$variable``. These variables should never be quoted.

Examples:
| `Should Be True`    $rc &lt; 10             Return code greater than 10
| `Run Keyword If`    $status == 'PASS'    `Log`    Passed
| `Run Keyword If`    'FAIL' in $output    `Log`    Output contains FAIL
| `Should Be True`    len($result) &gt; 1 and $result[1] == 'OK'
| `Should Be True`    $result is not None

Using the ``$variable`` syntax slows down expression evaluation a little.
This should not typically matter, but should be taken into account if
complex expressions are evaluated often and there are strict time
constrains.

Notice that instead of creating complicated expressions, it is often better
to move the logic into a library. That eases maintenance and can also
enhance execution speed.

= Boolean arguments =

Some keywords accept arguments that are handled as Boolean values true or
false. If such an argument is given as a string, it is considered false if
it is an empty string or equal to ``FALSE``, ``NONE``, ``NO``, ``OFF`` or
``0``, case-insensitively. Keywords verifying something that allow dropping
actual and expected values from the possible error message also consider
string ``no values`` to be false. Other strings are considered true unless
the keyword documentation explicitly states otherwise, and other argument
types are tested using the same
[http://docs.python.org/library/stdtypes.html#truth|rules as in Python].

True examples:
| `Should Be Equal`    ${x}    ${y}    Custom error    values=True         # Strings are generally true.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=yes          # Same as the above.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=${TRUE}      # Python ``True`` is true.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=${42}        # Numbers other than 0 are true.

False examples:
| `Should Be Equal`    ${x}    ${y}    Custom error    values=False        # String ``false`` is false.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=no           # Also string ``no`` is false.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=${EMPTY}     # Empty string is false.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=${FALSE}     # Python ``False`` is false.
| `Should Be Equal`    ${x}    ${y}    Custom error    values=no values    # ``no values`` works with ``values`` argument

= Pattern matching =

Many keywords accept arguments as either glob or regular expression patterns.

== Glob patterns ==

Some keywords, for example `Should Match`, support so called
[http://en.wikipedia.org/wiki/Glob_(programming)|glob patterns] where:

| ``*``        | matches any string, even an empty string                |
| ``?``        | matches any single character                            |
| ``[chars]``  | matches one character in the bracket                    |
| ``[!chars]`` | matches one character not in the bracket                |
| ``[a-z]``    | matches one character from the range in the bracket     |
| ``[!a-z]``   | matches one character not from the range in the bracket |

Unlike with glob patterns normally, path separator characters ``/`` and
``\`` and the newline character ``\n`` are matches by the above
wildcards.

== Regular expressions ==

Some keywords, for example `Should Match Regexp`, support
[http://en.wikipedia.org/wiki/Regular_expression|regular expressions]
that are more powerful but also more complicated that glob patterns.
The regular expression support is implemented using Python's
[http://docs.python.org/library/re.html|re module] and its documentation
should be consulted for more information about the syntax.

Because the backslash character (``\``) is an escape character in
Robot Framework test data, possible backslash characters in regular
expressions need to be escaped with another backslash like ``\\d\\w+``.
Strings that may contain special characters but should be handled
as literal strings, can be escaped with the `Regexp Escape` keyword.

= Multiline string comparison =

`Should Be Equal` and `Should Be Equal As Strings` report the failures using
[http://en.wikipedia.org/wiki/Diff_utility#Unified_format|unified diff
format] if both strings have more than two lines.

Example:
| ${first} =     `Catenate`    SEPARATOR=\n    Not in second    Same    Differs    Same
| ${second} =    `Catenate`    SEPARATOR=\n    Same    Differs2    Same    Not in first
| `Should Be Equal`    ${first}    ${second}

Results in the following error message:

| Multiline strings are different:
| --- first
| +++ second
| @@ -1,4 +1,4 @@
| -Not in second
|  Same
| -Differs
| +Differs2
|  Same
| +Not in first

= String representations =

Several keywords log values explicitly (e.g. `Log`) or implicitly (e.g.
`Should Be Equal` when there are failures). By default, keywords log values
using human-readable string representation, which means that strings
like ``Hello`` and numbers like ``42`` are logged as-is. Most of the time
this is the desired behavior, but there are some problems as well:

- It is not possible to see difference between different objects that
  have the same string representation like string ``42`` and integer ``42``.
  `Should Be Equal` and some other keywords add the type information to
  the error message in these cases, though.

- Non-printable characters such as the null byte are not visible.

- Trailing whitespace is not visible.

- Different newlines (``\r\n`` on Windows, ``\n`` elsewhere) cannot
  be separated from each others.

- There are several Unicode characters that are different but look the
  same. One example is the Latin ``a`` (``\u0061``) and the Cyrillic
  ``а`` (``\u0430``). Error messages like ``a != а`` are not very helpful.

- Some Unicode characters can be represented using
  [https://en.wikipedia.org/wiki/Unicode_equivalence|different forms].
  For example, ``ä`` can be represented either as a single code point
  ``\u00e4`` or using two combined code points ``\u0061`` and ``\u0308``.
  Such forms are considered canonically equivalent, but strings
  containing them are not considered equal when compared in Python. Error
  messages like ``ä != ä`` are not that helpful either.

- Containers such as lists and dictionaries are formatted into a single
  line making it hard to see individual items they contain.

To overcome the above problems, some keywords such as `Log` and
`Should Be Equal` have an optional ``formatter`` argument that can be
used to configure the string representation. The supported values are
``str`` (default), ``repr``, and ``ascii`` that work similarly as
[https://docs.python.org/library/functions.html|Python built-in functions]
with same names. More detailed semantics are explained below.

== str ==

Use the human-readable string representation. Equivalent to using ``str()``
in Python. This is the default.

== repr ==

Use the machine-readable string representation. Similar to using ``repr()``
in Python, which means that strings like ``Hello`` are logged like
``'Hello'``, newlines and non-printable characters are escaped like ``\n``
and ``\x00``, and so on. Non-ASCII characters are shown as-is like ``ä``.

In this mode bigger lists, dictionaries and other containers are
pretty-printed so that there is one item per row.

== ascii ==

Same as using ``ascii()`` in Python. Similar to using ``repr`` explained above
but with the following differences:

- Non-ASCII characters are escaped like ``\xe4`` instead of
  showing them as-is like ``ä``. This makes it easier to see differences
  between Unicode characters that look the same but are not equal.
- Containers are not pretty-printed.</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Call Method" lineno="3416">
<arguments repr="object, method_name, *args, **kwargs">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="object">
<name>object</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="method_name">
<name>method_name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**kwargs">
<name>kwargs</name>
</arg>
</arguments>
<doc>Calls the named method of the given object with the provided arguments.

The possible return value from the method is returned and can be
assigned to a variable. Keyword fails both if the object does not have
a method with the given name or if executing the method raises an
exception.

Possible equal signs in arguments must be escaped with a backslash
like ``\=``.

Examples:
| Call Method      | ${hashtable} | put          | myname  | myvalue |
| ${isempty} =     | Call Method  | ${hashtable} | isEmpty |         |
| Should Not Be True | ${isempty} |              |         |         |
| ${value} =       | Call Method  | ${hashtable} | get     | myname  |
| Should Be Equal  | ${value}     | myvalue      |         |         |
| Call Method      | ${object}    | kwargs    | name=value | foo=bar |
| Call Method      | ${object}    | positional   | escaped\=equals  |</doc>
<shortdoc>Calls the named method of the given object with the provided arguments.</shortdoc>
</kw>
<kw name="Catenate" lineno="2925">
<arguments repr="*items">
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
</arguments>
<doc>Catenates the given items together and returns the resulted string.

By default, items are catenated with spaces, but if the first item
contains the string ``SEPARATOR=&lt;sep&gt;``, the separator ``&lt;sep&gt;`` is
used instead. Items are converted into strings when necessary.

Examples:
| ${str1} = | Catenate | Hello         | world |       |
| ${str2} = | Catenate | SEPARATOR=--- | Hello | world |
| ${str3} = | Catenate | SEPARATOR=    | Hello | world |
=&gt;
| ${str1} = 'Hello world'
| ${str2} = 'Hello---world'
| ${str3} = 'Helloworld'</doc>
<shortdoc>Catenates the given items together and returns the resulted string.</shortdoc>
</kw>
<kw name="Comment" lineno="3090">
<arguments repr="*messages">
<arg kind="VAR_POSITIONAL" required="false" repr="*messages">
<name>messages</name>
</arg>
</arguments>
<doc>Displays the given messages in the log file as keyword arguments.

This keyword does nothing with the arguments it receives, but as they
are visible in the log, this keyword can be used to display simple
messages. Given arguments are ignored so thoroughly that they can even
contain non-existing variables. If you are interested about variable
values, you can use the `Log` or `Log Many` keywords.</doc>
<shortdoc>Displays the given messages in the log file as keyword arguments.</shortdoc>
</kw>
<kw name="Continue For Loop" lineno="2528">
<arguments repr="">
</arguments>
<doc>Skips the current FOR loop iteration and continues from the next.

---

*NOTE:* Robot Framework 5.0 added support for native ``CONTINUE`` statement that
is recommended over this keyword. In the examples below, ``Continue For Loop``
can simply be replaced with ``CONTINUE``. In addition to that, native ``IF``
syntax (new in RF 4.0) or inline ``IF`` syntax (new in RF 5.0) can be used
instead of ``Run Keyword If``. For example, the first example below could be
written like this instead:

| IF    '${var}' == 'CONTINUE'    CONTINUE

This keyword will eventually be deprecated and removed.

---

Skips the remaining keywords in the current FOR loop iteration and
continues from the next one. Starting from Robot Framework 5.0, this
keyword can only be used inside a loop, not in a keyword used in a loop.

Example:
| FOR | ${var}         | IN                     | @{VALUES}         |
|     | Run Keyword If | '${var}' == 'CONTINUE' | Continue For Loop |
|     | Do Something   | ${var}                 |
| END |

See `Continue For Loop If` to conditionally continue a FOR loop without
using `Run Keyword If` or other wrapper keywords.</doc>
<shortdoc>Skips the current FOR loop iteration and continues from the next.</shortdoc>
</kw>
<kw name="Continue For Loop If" lineno="2564">
<arguments repr="condition">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
</arguments>
<doc>Skips the current FOR loop iteration if the ``condition`` is true.

---

*NOTE:* Robot Framework 5.0 added support for native ``CONTINUE`` statement
and for inline ``IF``, and that combination should be used instead of this
keyword. For example, ``Continue For Loop If`` usage in the example below
could be replaced with

| IF    '${var}' == 'CONTINUE'    CONTINUE

This keyword will eventually be deprecated and removed.

---

A wrapper for `Continue For Loop` to continue a FOR loop based on
the given condition. The condition is evaluated using the same
semantics as with `Should Be True` keyword.

Example:
| FOR | ${var}               | IN                     | @{VALUES} |
|     | Continue For Loop If | '${var}' == 'CONTINUE' |
|     | Do Something         | ${var}                 |
| END |</doc>
<shortdoc>Skips the current FOR loop iteration if the ``condition`` is true.</shortdoc>
</kw>
<kw name="Convert To Binary" lineno="151">
<arguments repr="item, base=None, prefix=None, length=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prefix=None">
<name>prefix</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="length=None">
<name>length</name>
<default>None</default>
</arg>
</arguments>
<doc>Converts the given item to a binary string.

The ``item``, with an optional ``base``, is first converted to an
integer using `Convert To Integer` internally. After that it
is converted to a binary number (base 2) represented as a
string such as ``1011``.

The returned value can contain an optional ``prefix`` and can be
required to be of minimum ``length`` (excluding the prefix and a
possible minus sign). If the value is initially shorter than
the required length, it is padded with zeros.

Examples:
| ${result} = | Convert To Binary | 10 |         |           | # Result is 1010   |
| ${result} = | Convert To Binary | F  | base=16 | prefix=0b | # Result is 0b1111 |
| ${result} = | Convert To Binary | -2 | prefix=B | length=4 | # Result is -B0010 |

See also `Convert To Integer`, `Convert To Octal` and `Convert To Hex`.</doc>
<shortdoc>Converts the given item to a binary string.</shortdoc>
</kw>
<kw name="Convert To Boolean" lineno="298">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>Converts the given item to Boolean true or false.

Handles strings ``True`` and ``False`` (case-insensitive) as expected,
otherwise returns item's
[http://docs.python.org/library/stdtypes.html#truth|truth value]
using Python's ``bool()`` method.</doc>
<shortdoc>Converts the given item to Boolean true or false.</shortdoc>
</kw>
<kw name="Convert To Bytes" lineno="314">
<arguments repr="input, input_type=text">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="input">
<name>input</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="input_type=text">
<name>input_type</name>
<default>text</default>
</arg>
</arguments>
<doc>Converts the given ``input`` to bytes according to the ``input_type``.

Valid input types are listed below:

- ``text:`` Converts text to bytes character by character. All
  characters with ordinal below 256 can be used and are converted to
  bytes with same values. Many characters are easiest to represent
  using escapes like ``\x00`` or ``\xff``. Supports both Unicode
  strings and bytes.

- ``int:`` Converts integers separated by spaces to bytes. Similarly as
  with `Convert To Integer`, it is possible to use binary, octal, or
  hex values by prefixing the values with ``0b``, ``0o``, or ``0x``,
  respectively.

- ``hex:`` Converts hexadecimal values to bytes. Single byte is always
  two characters long (e.g. ``01`` or ``FF``). Spaces are ignored and
  can be used freely as a visual separator.

- ``bin:`` Converts binary values to bytes. Single byte is always eight
  characters long (e.g. ``00001010``). Spaces are ignored and can be
  used freely as a visual separator.

In addition to giving the input as a string, it is possible to use
lists or other iterables containing individual characters or numbers.
In that case numbers do not need to be padded to certain length and
they cannot contain extra spaces.

Examples (last column shows returned bytes):
| ${bytes} = | Convert To Bytes | hyvä      |     | # hyv\xe4      |
| ${bytes} = | Convert To Bytes | hyv\xe4   |     | # hyv\xe4      |
| ${bytes} = | Convert To Bytes | \xff\x07  |     | # \xff\x07     |
| ${bytes} = | Convert To Bytes | 82 70     | int | # RF           |
| ${bytes} = | Convert To Bytes | 0b10 0x10 | int | # \x02\x10     |
| ${bytes} = | Convert To Bytes | ff 00 07  | hex | # \xff\x00\x07 |
| ${bytes} = | Convert To Bytes | 52462121  | hex | # RF!!         |
| ${bytes} = | Convert To Bytes | 0000 1000 | bin | # \x08         |
| ${input} = | Create List      | 1         | 2   | 12             |
| ${bytes} = | Convert To Bytes | ${input}  | int | # \x01\x02\x0c |
| ${bytes} = | Convert To Bytes | ${input}  | hex | # \x01\x02\x12 |

Use `Encode String To Bytes` in ``String`` library if you need to
convert text to bytes using a certain encoding.</doc>
<shortdoc>Converts the given ``input`` to bytes according to the ``input_type``.</shortdoc>
</kw>
<kw name="Convert To Hex" lineno="195">
<arguments repr="item, base=None, prefix=None, length=None, lowercase=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prefix=None">
<name>prefix</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="length=None">
<name>length</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="lowercase=False">
<name>lowercase</name>
<default>False</default>
</arg>
</arguments>
<doc>Converts the given item to a hexadecimal string.

The ``item``, with an optional ``base``, is first converted to an
integer using `Convert To Integer` internally. After that it
is converted to a hexadecimal number (base 16) represented as
a string such as ``FF0A``.

The returned value can contain an optional ``prefix`` and can be
required to be of minimum ``length`` (excluding the prefix and a
possible minus sign). If the value is initially shorter than
the required length, it is padded with zeros.

By default the value is returned as an upper case string, but the
``lowercase`` argument a true value (see `Boolean arguments`) turns
the value (but not the given prefix) to lower case.

Examples:
| ${result} = | Convert To Hex | 255 |           |              | # Result is FF    |
| ${result} = | Convert To Hex | -10 | prefix=0x | length=2     | # Result is -0x0A |
| ${result} = | Convert To Hex | 255 | prefix=X | lowercase=yes | # Result is Xff   |

See also `Convert To Integer`, `Convert To Binary` and `Convert To Octal`.</doc>
<shortdoc>Converts the given item to a hexadecimal string.</shortdoc>
</kw>
<kw name="Convert To Integer" lineno="98">
<arguments repr="item, base=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
</arguments>
<doc>Converts the given item to an integer number.

If the given item is a string, it is by default expected to be an
integer in base 10. There are two ways to convert from other bases:

- Give base explicitly to the keyword as ``base`` argument.

- Prefix the given string with the base so that ``0b`` means binary
  (base 2), ``0o`` means octal (base 8), and ``0x`` means hex (base 16).
  The prefix is considered only when ``base`` argument is not given and
  may itself be prefixed with a plus or minus sign.

The syntax is case-insensitive and possible spaces are ignored.

Examples:
| ${result} = | Convert To Integer | 100    |    | # Result is 100   |
| ${result} = | Convert To Integer | FF AA  | 16 | # Result is 65450 |
| ${result} = | Convert To Integer | 100    | 8  | # Result is 64    |
| ${result} = | Convert To Integer | -100   | 2  | # Result is -4    |
| ${result} = | Convert To Integer | 0b100  |    | # Result is 4     |
| ${result} = | Convert To Integer | -0x100 |    | # Result is -256  |

See also `Convert To Number`, `Convert To Binary`, `Convert To Octal`,
`Convert To Hex`, and `Convert To Bytes`.</doc>
<shortdoc>Converts the given item to an integer number.</shortdoc>
</kw>
<kw name="Convert To Number" lineno="234">
<arguments repr="item, precision=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="precision=None">
<name>precision</name>
<default>None</default>
</arg>
</arguments>
<doc>Converts the given item to a floating point number.

If the optional ``precision`` is positive or zero, the returned number
is rounded to that number of decimal digits. Negative precision means
that the number is rounded to the closest multiple of 10 to the power
of the absolute precision. If a number is equally close to a certain
precision, it is always rounded away from zero.

Examples:
| ${result} = | Convert To Number | 42.512 |    | # Result is 42.512 |
| ${result} = | Convert To Number | 42.512 | 1  | # Result is 42.5   |
| ${result} = | Convert To Number | 42.512 | 0  | # Result is 43.0   |
| ${result} = | Convert To Number | 42.512 | -1 | # Result is 40.0   |

Notice that machines generally cannot store floating point numbers
accurately. This may cause surprises with these numbers in general
and also when they are rounded. For more information see, for example,
these resources:

- http://docs.python.org/tutorial/floatingpoint.html
- http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition

If you want to avoid possible problems with floating point numbers,
you can implement custom keywords using Python's
[http://docs.python.org/library/decimal.html|decimal] or
[http://docs.python.org/library/fractions.html|fractions] modules.

If you need an integer number, use `Convert To Integer` instead.</doc>
<shortdoc>Converts the given item to a floating point number.</shortdoc>
</kw>
<kw name="Convert To Octal" lineno="173">
<arguments repr="item, base=None, prefix=None, length=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prefix=None">
<name>prefix</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="length=None">
<name>length</name>
<default>None</default>
</arg>
</arguments>
<doc>Converts the given item to an octal string.

The ``item``, with an optional ``base``, is first converted to an
integer using `Convert To Integer` internally. After that it
is converted to an octal number (base 8) represented as a
string such as ``775``.

The returned value can contain an optional ``prefix`` and can be
required to be of minimum ``length`` (excluding the prefix and a
possible minus sign). If the value is initially shorter than
the required length, it is padded with zeros.

Examples:
| ${result} = | Convert To Octal | 10 |            |          | # Result is 12      |
| ${result} = | Convert To Octal | -F | base=16    | prefix=0 | # Result is -017    |
| ${result} = | Convert To Octal | 16 | prefix=oct | length=4 | # Result is oct0020 |

See also `Convert To Integer`, `Convert To Binary` and `Convert To Hex`.</doc>
<shortdoc>Converts the given item to an octal string.</shortdoc>
</kw>
<kw name="Convert To String" lineno="284">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>Converts the given item to a Unicode string.

Strings are also [http://www.macchiato.com/unicode/nfc-faq|
NFC normalized].

Use `Encode String To Bytes` and `Decode Bytes To String` keywords
in ``String`` library if you need to convert between Unicode and byte
strings using different encodings. Use `Convert To Bytes` if you just
want to create byte strings.</doc>
<shortdoc>Converts the given item to a Unicode string.</shortdoc>
</kw>
<kw name="Create Dictionary" lineno="420">
<arguments repr="*items">
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
</arguments>
<doc>Creates and returns a dictionary based on the given ``items``.

Items are typically given using the ``key=value`` syntax same way as
``&amp;{dictionary}`` variables are created in the Variable table. Both
keys and values can contain variables, and possible equal sign in key
can be escaped with a backslash like ``escaped\=key=value``. It is
also possible to get items from existing dictionaries by simply using
them like ``&amp;{dict}``.

Alternatively items can be specified so that keys and values are given
separately. This and the ``key=value`` syntax can even be combined,
but separately given items must be first. If same key is used multiple
times, the last value has precedence.

The returned dictionary is ordered, and values with strings as keys
can also be accessed using a convenient dot-access syntax like
``${dict.key}``. Technically the returned dictionary is Robot
Framework's own ``DotDict`` instance. If there is a need, it can be
converted into a regular Python ``dict`` instance by using the
`Convert To Dictionary` keyword from the Collections library.

Examples:
| &amp;{dict} = | Create Dictionary | key=value | foo=bar | | | # key=value syntax |
| Should Be True | ${dict} == {'key': 'value', 'foo': 'bar'} |
| &amp;{dict2} = | Create Dictionary | key | value | foo | bar | # separate key and value |
| Should Be Equal | ${dict} | ${dict2} |
| &amp;{dict} = | Create Dictionary | ${1}=${2} | &amp;{dict} | foo=new | | # using variables |
| Should Be True | ${dict} == {1: 2, 'key': 'value', 'foo': 'new'} |
| Should Be Equal | ${dict.key} | value | | | | # dot-access |</doc>
<shortdoc>Creates and returns a dictionary based on the given ``items``.</shortdoc>
</kw>
<kw name="Create List" lineno="406">
<arguments repr="*items">
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
</arguments>
<doc>Returns a list containing given items.

The returned list can be assigned both to ``${scalar}`` and ``@{list}``
variables.

Examples:
| @{list} =   | Create List | a    | b    | c    |
| ${scalar} = | Create List | a    | b    | c    |
| ${ints} =   | Create List | ${1} | ${2} | ${3} |</doc>
<shortdoc>Returns a list containing given items.</shortdoc>
</kw>
<kw name="Evaluate" lineno="3360">
<arguments repr="expression, modules=None, namespace=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expression">
<name>expression</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="modules=None">
<name>modules</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="namespace=None">
<name>namespace</name>
<default>None</default>
</arg>
</arguments>
<doc>Evaluates the given expression in Python and returns the result.

``expression`` is evaluated in Python as explained in the
`Evaluating expressions` section.

``modules`` argument can be used to specify a comma separated
list of Python modules to be imported and added to the evaluation
namespace.

``namespace`` argument can be used to pass a custom evaluation
namespace as a dictionary. Possible ``modules`` are added to this
namespace.

Variables used like ``${variable}`` are replaced in the expression
before evaluation. Variables are also available in the evaluation
namespace and can be accessed using the special ``$variable`` syntax
as explained in the `Evaluating expressions` section.

Starting from Robot Framework 3.2, modules used in the expression are
imported automatically. There are, however, two cases where they need to
be explicitly specified using the ``modules`` argument:

- When nested modules like ``rootmod.submod`` are implemented so that
  the root module does not automatically import sub modules. This is
  illustrated by the ``selenium.webdriver`` example below.

- When using a module in the expression part of a list comprehension.
  This is illustrated by the ``json`` example below.

Examples (expecting ``${result}`` is number 3.14):
| ${status} =  | Evaluate | 0 &lt; ${result} &lt; 10 | # Would also work with string '3.14' |
| ${status} =  | Evaluate | 0 &lt; $result &lt; 10   | # Using variable itself, not string representation |
| ${random} =  | Evaluate | random.randint(0, sys.maxsize) |
| ${options} = | Evaluate | selenium.webdriver.ChromeOptions() | modules=selenium.webdriver |
| ${items} =   | Evaluate | [json.loads(item) for item in ('1', '"b"')] | modules=json |
| ${ns} =      | Create Dictionary | x=${4}    | y=${2}              |
| ${result} =  | Evaluate | x*10 + y           | namespace=${ns}     |
=&gt;
| ${status} = True
| ${random} = &lt;random integer&gt;
| ${options} = ChromeOptions instance
| ${items} = [1, 'b']
| ${result} = 42

*NOTE*: Prior to Robot Framework 3.2 using ``modules=rootmod.submod``
was not enough to make the root module itself available in the
evaluation namespace. It needed to be taken into use explicitly like
``modules=rootmod, rootmod.submod``.</doc>
<shortdoc>Evaluates the given expression in Python and returns the result.</shortdoc>
</kw>
<kw name="Exit For Loop" lineno="2595">
<arguments repr="">
</arguments>
<doc>Stops executing the enclosing FOR loop.

---

*NOTE:* Robot Framework 5.0 added support for native ``BREAK`` statement that
is recommended over this keyword. In the examples below, ``Exit For Loop``
can simply be replaced with ``BREAK``. In addition to that, native ``IF``
syntax (new in RF 4.0) or inline ``IF`` syntax (new in RF 5.0) can be used
instead of ``Run Keyword If``. For example, the first example below could be
written like this instead:

| IF    '${var}' == 'EXIT'    BREAK

This keyword will eventually be deprecated and removed.

---

Exits the enclosing FOR loop and continues execution after it. Starting
from Robot Framework 5.0, this keyword can only be used inside a loop,
not in a keyword used in a loop.

Example:
| FOR | ${var}         | IN                 | @{VALUES}     |
|     | Run Keyword If | '${var}' == 'EXIT' | Exit For Loop |
|     | Do Something   | ${var} |
| END |

See `Exit For Loop If` to conditionally exit a FOR loop without
using `Run Keyword If` or other wrapper keywords.</doc>
<shortdoc>Stops executing the enclosing FOR loop.</shortdoc>
</kw>
<kw name="Exit For Loop If" lineno="2631">
<arguments repr="condition">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
</arguments>
<doc>Stops executing the enclosing FOR loop if the ``condition`` is true.

---

*NOTE:* Robot Framework 5.0 added support for native ``BREAK`` statement
and for inline ``IF``, and that combination should be used instead of this
keyword. For example, ``Exit For Loop If`` usage in the example below
could be replaced with

| IF    '${var}' == 'EXIT'    BREAK

This keyword will eventually be deprecated and removed.

---

A wrapper for `Exit For Loop` to exit a FOR loop based on
the given condition. The condition is evaluated using the same
semantics as with `Should Be True` keyword.

Example:
| FOR | ${var}           | IN                 | @{VALUES} |
|     | Exit For Loop If | '${var}' == 'EXIT' |
|     | Do Something     | ${var}             |
| END |</doc>
<shortdoc>Stops executing the enclosing FOR loop if the ``condition`` is true.</shortdoc>
</kw>
<kw name="Fail" lineno="484">
<arguments repr="msg=None, *tags">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>Fails the test with the given message and optionally alters its tags.

The error message is specified using the ``msg`` argument.
It is possible to use HTML in the given error message, similarly
as with any other keyword accepting an error message, by prefixing
the error with ``*HTML*``.

It is possible to modify tags of the current test case by passing tags
after the message. Tags starting with a hyphen (e.g. ``-regression``)
are removed and others added. Tags are modified using `Set Tags` and
`Remove Tags` internally, and the semantics setting and removing them
are the same as with these keywords.

Examples:
| Fail | Test not ready   |             | | # Fails with the given message.    |
| Fail | *HTML*&lt;b&gt;Test not ready&lt;/b&gt; | | | # Fails using HTML in the message. |
| Fail | Test not ready   | not-ready   | | # Fails and adds 'not-ready' tag.  |
| Fail | OS not supported | -regression | | # Removes tag 'regression'.        |
| Fail | My message       | tag    | -t*  | # Removes all tags starting with 't' except the newly added 'tag'. |

See `Fatal Error` if you need to stop the whole test execution.</doc>
<shortdoc>Fails the test with the given message and optionally alters its tags.</shortdoc>
</kw>
<kw name="Fatal Error" lineno="510">
<arguments repr="msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Stops the whole test execution.

The test or suite where this keyword is used fails with the provided
message, and subsequent tests fail with a canned message.
Possible teardowns will nevertheless be executed.

See `Fail` if you only want to stop one test case unconditionally.</doc>
<shortdoc>Stops the whole test execution.</shortdoc>
</kw>
<kw name="Get Count" lineno="1251">
<arguments repr="container, item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>Returns and logs how many times ``item`` is found from ``container``.

This keyword works with Python strings and lists and all objects
that either have ``count`` method or can be converted to Python lists.

Example:
| ${count} = | Get Count | ${some item} | interesting value |
| Should Be True | 5 &lt; ${count} &lt; 10 |</doc>
<shortdoc>Returns and logs how many times ``item`` is found from ``container``.</shortdoc>
</kw>
<kw name="Get Length" lineno="1366">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>Returns and logs the length of the given item as an integer.

The item can be anything that has a length, for example, a string,
a list, or a mapping. The keyword first tries to get the length with
the Python function ``len``, which calls the  item's ``__len__`` method
internally. If that fails, the keyword tries to call the item's
possible ``length`` and ``size`` methods directly. The final attempt is
trying to get the value of the item's ``length`` attribute. If all
these attempts are unsuccessful, the keyword fails.

Examples:
| ${length} = | Get Length    | Hello, world! |        |
| Should Be Equal As Integers | ${length}     | 13     |
| @{list} =   | Create List   | Hello,        | world! |
| ${length} = | Get Length    | ${list}       |        |
| Should Be Equal As Integers | ${length}     | 2      |

See also `Length Should Be`, `Should Be Empty` and `Should Not Be
Empty`.</doc>
<shortdoc>Returns and logs the length of the given item as an integer.</shortdoc>
</kw>
<kw name="Get Library Instance" lineno="3633">
<arguments repr="name=None, all=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="name=None">
<name>name</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="all=False">
<name>all</name>
<default>False</default>
</arg>
</arguments>
<doc>Returns the currently active instance of the specified library.

This keyword makes it easy for libraries to interact with
other libraries that have state. This is illustrated by
the Python example below:

| from robot.libraries.BuiltIn import BuiltIn
|
| def title_should_start_with(expected):
|     seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
|     title = seleniumlib.get_title()
|     if not title.startswith(expected):
|         raise AssertionError("Title '%s' did not start with '%s'"
|                              % (title, expected))

It is also possible to use this keyword in the test data and
pass the returned library instance to another keyword. If a
library is imported with a custom name, the ``name`` used to get
the instance must be that name and not the original library name.

If the optional argument ``all`` is given a true value, then a
dictionary mapping all library names to instances will be returned.

Example:
| &amp;{all libs} = | Get library instance | all=True |</doc>
<shortdoc>Returns the currently active instance of the specified library.</shortdoc>
</kw>
<kw name="Get Time" lineno="3277">
<arguments repr="format=timestamp, time_=NOW">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="format=timestamp">
<name>format</name>
<default>timestamp</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="time_=NOW">
<name>time_</name>
<default>NOW</default>
</arg>
</arguments>
<doc>Returns the given time in the requested format.

*NOTE:* DateTime library contains much more flexible keywords for
getting the current date and time and for date and time handling in
general.

How time is returned is determined based on the given ``format``
string as follows. Note that all checks are case-insensitive.

1) If ``format`` contains the word ``epoch``, the time is returned
   in seconds after the UNIX epoch (1970-01-01 00:00:00 UTC).
   The return value is always an integer.

2) If ``format`` contains any of the words ``year``, ``month``,
   ``day``, ``hour``, ``min``, or ``sec``, only the selected parts are
   returned. The order of the returned parts is always the one
   in the previous sentence and the order of words in ``format``
   is not significant. The parts are returned as zero-padded
   strings (e.g. May -&gt; ``05``).

3) Otherwise (and by default) the time is returned as a
   timestamp string in the format ``2006-02-24 15:08:31``.

By default this keyword returns the current local time, but
that can be altered using ``time`` argument as explained below.
Note that all checks involving strings are case-insensitive.

1) If ``time`` is a number, or a string that can be converted to
   a number, it is interpreted as seconds since the UNIX epoch.
   This documentation was originally written about 1177654467
   seconds after the epoch.

2) If ``time`` is a timestamp, that time will be used. Valid
   timestamp formats are ``YYYY-MM-DD hh:mm:ss`` and
   ``YYYYMMDD hhmmss``.

3) If ``time`` is equal to ``NOW`` (default), the current local
   time is used.

4) If ``time`` is equal to ``UTC``, the current time in
   [http://en.wikipedia.org/wiki/Coordinated_Universal_Time|UTC]
   is used.

5) If ``time`` is in the format like ``NOW - 1 day`` or ``UTC + 1 hour
   30 min``, the current local/UTC time plus/minus the time
   specified with the time string is used. The time string format
   is described in an appendix of Robot Framework User Guide.

Examples (expecting the current local time is 2006-03-29 15:06:21):
| ${time} = | Get Time |             |  |  |
| ${secs} = | Get Time | epoch       |  |  |
| ${year} = | Get Time | return year |  |  |
| ${yyyy}   | ${mm}    | ${dd} =     | Get Time | year,month,day |
| @{time} = | Get Time | year month day hour min sec |  |  |
| ${y}      | ${s} =   | Get Time    | seconds and year |  |
=&gt;
| ${time} = '2006-03-29 15:06:21'
| ${secs} = 1143637581
| ${year} = '2006'
| ${yyyy} = '2006', ${mm} = '03', ${dd} = '29'
| @{time} = ['2006', '03', '29', '15', '06', '21']
| ${y} = '2006'
| ${s} = '21'

Examples (expecting the current local time is 2006-03-29 15:06:21 and
UTC time is 2006-03-29 12:06:21):
| ${time} = | Get Time |              | 1177654467          | # Time given as epoch seconds        |
| ${secs} = | Get Time | sec          | 2007-04-27 09:14:27 | # Time given as a timestamp          |
| ${year} = | Get Time | year         | NOW                 | # The local time of execution        |
| @{time} = | Get Time | hour min sec | NOW + 1h 2min 3s    | # 1h 2min 3s added to the local time |
| @{utc} =  | Get Time | hour min sec | UTC                 | # The UTC time of execution          |
| ${hour} = | Get Time | hour         | UTC - 1 hour        | # 1h subtracted from the UTC  time   |
=&gt;
| ${time} = '2007-04-27 09:14:27'
| ${secs} = 27
| ${year} = '2006'
| @{time} = ['16', '08', '24']
| @{utc} = ['12', '06', '21']
| ${hour} = '11'</doc>
<shortdoc>Returns the given time in the requested format.</shortdoc>
</kw>
<kw name="Get Variable Value" lineno="1488">
<arguments repr="name, default=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=None">
<name>default</name>
<default>None</default>
</arg>
</arguments>
<doc>Returns variable value or ``default`` if the variable does not exist.

The name of the variable can be given either as a normal variable name
like ``${name}`` or in escaped format like ``$name`` or ``\${name}``.
For the reasons explained in the `Using variables with keywords creating
or accessing variables` section, using the escaped format is recommended.

Examples:
| ${x} =    `Get Variable Value`    $a    default
| ${y} =    `Get Variable Value`    $a    ${b}
| ${z} =    `Get Variable Value`    $z
=&gt;
- ``${x}`` gets value of ``${a}`` if ``${a}`` exists and string ``default`` otherwise
- ``${y}`` gets value of ``${a}`` if ``${a}`` exists and value of ``${b}`` otherwise
- ``${z}`` is set to Python ``None`` if it does not exist previously</doc>
<shortdoc>Returns variable value or ``default`` if the variable does not exist.</shortdoc>
</kw>
<kw name="Get Variables" lineno="1458">
<arguments repr="no_decoration=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="no_decoration=False">
<name>no_decoration</name>
<default>False</default>
</arg>
</arguments>
<doc>Returns a dictionary containing all variables in the current scope.

Variables are returned as a special dictionary that allows accessing
variables in space, case, and underscore insensitive manner similarly
as accessing variables in the test data. This dictionary supports all
same operations as normal Python dictionaries and, for example,
Collections library can be used to access or modify it. Modifying the
returned dictionary has no effect on the variables available in the
current scope.

By default variables are returned with ``${}``, ``@{}`` or ``&amp;{}``
decoration based on variable types. Giving a true value (see `Boolean
arguments`) to the optional argument ``no_decoration`` will return
the variables without the decoration.

Example:
| ${example_variable} =         | Set Variable | example value         |
| ${variables} =                | Get Variables |                      |
| Dictionary Should Contain Key | ${variables} | \${example_variable} |
| Dictionary Should Contain Key | ${variables} | \${ExampleVariable}  |
| Set To Dictionary             | ${variables} | \${name} | value     |
| Variable Should Not Exist     | \${name}    |           |           |
| ${no decoration} =            | Get Variables | no_decoration=Yes |
| Dictionary Should Contain Key | ${no decoration} | example_variable |</doc>
<shortdoc>Returns a dictionary containing all variables in the current scope.</shortdoc>
</kw>
<kw name="Import Library" lineno="3134">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Imports a library with the given name and optional arguments.

This functionality allows dynamic importing of libraries while tests
are running. That may be necessary, if the library itself is dynamic
and not yet available when test data is processed. In a normal case,
libraries should be imported using the Library setting in the Setting
section.

This keyword supports importing libraries both using library
names and physical paths. When paths are used, they must be
given in absolute format or found from
[http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#module-search-path|
search path]. Forward slashes can be used as path separators in all
operating systems.

It is possible to pass arguments to the imported library and also
named argument syntax works if the library supports it. ``WITH NAME``
syntax can be used to give a custom name to the imported library.

Examples:
| Import Library | MyLibrary |
| Import Library | ${CURDIR}/Lib.py | arg1 | named=arg2 | WITH NAME | Custom |</doc>
<shortdoc>Imports a library with the given name and optional arguments.</shortdoc>
</kw>
<kw name="Import Resource" lineno="3195">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>Imports a resource file with the given path.

Resources imported with this keyword are set into the test suite scope
similarly when importing them in the Setting table using the Resource
setting.

The given path must be absolute or found from
[http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#module-search-path|search path].
Forward slashes can be used as path separator regardless
the operating system.

Examples:
| Import Resource | ${CURDIR}/resource.txt |
| Import Resource | ${CURDIR}/../resources/resource.html |
| Import Resource | found_from_pythonpath.robot |</doc>
<shortdoc>Imports a resource file with the given path.</shortdoc>
</kw>
<kw name="Import Variables" lineno="3170">
<arguments repr="path, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Imports a variable file with the given path and optional arguments.

Variables imported with this keyword are set into the test suite scope
similarly when importing them in the Setting table using the Variables
setting. These variables override possible existing variables with
the same names. This functionality can thus be used to import new
variables, for example, for each test in a test suite.

The given path must be absolute or found from
[http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html##module-search-path|search path].
Forward slashes can be used as path separator regardless
the operating system.

Examples:
| Import Variables | ${CURDIR}/variables.py   |      |      |
| Import Variables | ${CURDIR}/../vars/env.py | arg1 | arg2 |
| Import Variables | file_from_pythonpath.py  |      |      |</doc>
<shortdoc>Imports a variable file with the given path and optional arguments.</shortdoc>
</kw>
<kw name="Keyword Should Exist" lineno="3259">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the given keyword exists in the current scope.

Fails also if there is more than one keyword with the same name.
Works both with the short name (e.g. ``Log``) and the full name
(e.g. ``BuiltIn.Log``).

The default error message can be overridden with the ``msg`` argument.

See also `Variable Should Exist`.</doc>
<shortdoc>Fails unless the given keyword exists in the current scope.</shortdoc>
</kw>
<kw name="Length Should Be" lineno="1414">
<arguments repr="item, length, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="length">
<name>length</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Verifies that the length of the given item is correct.

The length of the item is got using the `Get Length` keyword. The
default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Verifies that the length of the given item is correct.</shortdoc>
</kw>
<kw name="Log" lineno="2951">
<arguments repr="message, level=INFO, html=False, console=False, repr=DEPRECATED, formatter=str">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="html=False">
<name>html</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="console=False">
<name>console</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="repr=DEPRECATED">
<name>repr</name>
<default>DEPRECATED</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="formatter=str">
<name>formatter</name>
<default>str</default>
</arg>
</arguments>
<doc>Logs the given message with the given level.

Valid levels are TRACE, DEBUG, INFO (default), HTML, WARN, and ERROR.
Messages below the current active log level are ignored. See
`Set Log Level` keyword and ``--loglevel`` command line option
for more details about setting the level.

Messages logged with the WARN or ERROR levels will be automatically
visible also in the console and in the Test Execution Errors section
in the log file.

If the ``html`` argument is given a true value (see `Boolean
arguments`), the message will be considered HTML and special characters
such as ``&lt;`` are not escaped. For example, logging
``&lt;img src="image.png"&gt;`` creates an image when ``html`` is true, but
otherwise the message is that exact string. An alternative to using
the ``html`` argument is using the HTML pseudo log level. It logs
the message as HTML using the INFO level.

If the ``console`` argument is true, the message will be written to
the console where test execution was started from in addition to
the log file. This keyword always uses the standard output stream
and adds a newline after the written message. Use `Log To Console`
instead if either of these is undesirable,

The ``formatter`` argument controls how to format the string
representation of the message. Possible values are ``str`` (default),
``repr``, ``ascii``, ``len``, and ``type``. They work similarly to
Python built-in functions with same names. When using ``repr``, bigger
lists, dictionaries and other containers are also pretty-printed so
that there is one item per row. For more details see `String
representations`.

The old way to control string representation was using the ``repr``
argument. This argument has been deprecated and ``formatter=repr``
should be used instead.

Examples:
| Log | Hello, world!        |          |   | # Normal INFO message.   |
| Log | Warning, world!      | WARN     |   | # Warning.               |
| Log | &lt;b&gt;Hello&lt;/b&gt;, world! | html=yes |   | # INFO message as HTML.  |
| Log | &lt;b&gt;Hello&lt;/b&gt;, world! | HTML     |   | # Same as above.         |
| Log | &lt;b&gt;Hello&lt;/b&gt;, world! | DEBUG    | html=true | # DEBUG as HTML. |
| Log | Hello, console!   | console=yes | | # Log also to the console. |
| Log | Null is \x00    | formatter=repr | | # Log ``'Null is \x00'``. |

See `Log Many` if you want to log multiple messages in one go, and
`Log To Console` if you only want to write to the console.

Formatter options ``type`` and ``log`` are new in Robot Framework 5.0.</doc>
<shortdoc>Logs the given message with the given level.</shortdoc>
</kw>
<kw name="Log Many" lineno="3028">
<arguments repr="*messages">
<arg kind="VAR_POSITIONAL" required="false" repr="*messages">
<name>messages</name>
</arg>
</arguments>
<doc>Logs the given messages as separate entries using the INFO level.

Supports also logging list and dictionary variable items individually.

Examples:
| Log Many | Hello   | ${var}  |
| Log Many | @{list} | &amp;{dict} |

See `Log` and `Log To Console` keywords if you want to use alternative
log levels, use HTML, or log to the console.</doc>
<shortdoc>Logs the given messages as separate entries using the INFO level.</shortdoc>
</kw>
<kw name="Log To Console" lineno="3056">
<arguments repr="message, stream=STDOUT, no_newline=False, format=">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="stream=STDOUT">
<name>stream</name>
<default>STDOUT</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="no_newline=False">
<name>no_newline</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="format=">
<name>format</name>
<default/>
</arg>
</arguments>
<doc>Logs the given message to the console.

By default uses the standard output stream. Using the standard error
stream is possible by giving the ``stream`` argument value ``STDERR``
(case-insensitive).

By default appends a newline to the logged message. This can be
disabled by giving the ``no_newline`` argument a true value (see
`Boolean arguments`).

By default adds no alignment formatting. The ``format`` argument allows,
for example, alignment and customized padding of the log message. Please see the
[https://docs.python.org/3/library/string.html#formatspec|format specification] for
detailed alignment possibilities. This argument is new in Robot
Framework 5.0.

Examples:
| Log To Console | Hello, console!             |                 |
| Log To Console | Hello, stderr!              | STDERR          |
| Log To Console | Message starts here and is  | no_newline=true |
| Log To Console | continued without newline.  |                 |
| Log To Console | center message with * pad   | format=*^60     |
| Log To Console | 30 spaces before msg starts | format=&gt;30      |

This keyword does not log the message to the normal log file. Use
`Log` keyword, possibly with argument ``console``, if that is desired.</doc>
<shortdoc>Logs the given message to the console.</shortdoc>
</kw>
<kw name="Log Variables" lineno="1511">
<arguments repr="level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>Logs all variables in the current scope with given log level.</doc>
<shortdoc>Logs all variables in the current scope with given log level.</shortdoc>
</kw>
<kw name="No Operation" lineno="2885">
<arguments repr="">
</arguments>
<doc>Does absolutely nothing.</doc>
<shortdoc>Does absolutely nothing.</shortdoc>
</kw>
<kw name="Pass Execution" lineno="2811">
<arguments repr="message, *tags">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>Skips rest of the current test, setup, or teardown with PASS status.

This keyword can be used anywhere in the test data, but the place where
used affects the behavior:

- When used in any setup or teardown (suite, test or keyword), passes
  that setup or teardown. Possible keyword teardowns of the started
  keywords are executed. Does not affect execution or statuses
  otherwise.
- When used in a test outside setup or teardown, passes that particular
  test case. Possible test and keyword teardowns are executed.

Possible continuable failures before this keyword is used, as well as
failures in executed teardowns, will fail the execution.

It is mandatory to give a message explaining why execution was passed.
By default the message is considered plain text, but starting it with
``*HTML*`` allows using HTML formatting.

It is also possible to modify test tags passing tags after the message
similarly as with `Fail` keyword. Tags starting with a hyphen
(e.g. ``-regression``) are removed and others added. Tags are modified
using `Set Tags` and `Remove Tags` internally, and the semantics
setting and removing them are the same as with these keywords.

Examples:
| Pass Execution | All features available in this version tested. |
| Pass Execution | Deprecated test. | deprecated | -regression    |

This keyword is typically wrapped to some other keyword, such as
`Run Keyword If`, to pass based on a condition. The most common case
can be handled also with `Pass Execution If`:

| Run Keyword If    | ${rc} &lt; 0 | Pass Execution | Negative values are cool. |
| Pass Execution If | ${rc} &lt; 0 | Negative values are cool. |

Passing execution in the middle of a test, setup or teardown should be
used with care. In the worst case it leads to tests that skip all the
parts that could actually uncover problems in the tested application.
In cases where execution cannot continue do to external factors,
it is often safer to fail the test case and make it non-critical.</doc>
<shortdoc>Skips rest of the current test, setup, or teardown with PASS status.</shortdoc>
</kw>
<kw name="Pass Execution If" lineno="2863">
<arguments repr="condition, message, *tags">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>Conditionally skips rest of the current test, setup, or teardown with PASS status.

A wrapper for `Pass Execution` to skip rest of the current test,
setup or teardown based the given ``condition``. The condition is
evaluated similarly as with `Should Be True` keyword, and ``message``
and ``*tags`` have same semantics as with `Pass Execution`.

Example:
| FOR | ${var}            | IN                     | @{VALUES}               |
|     | Pass Execution If | '${var}' == 'EXPECTED' | Correct value was found |
|     | Do Something      | ${var}                 |
| END |</doc>
<shortdoc>Conditionally skips rest of the current test, setup, or teardown with PASS status.</shortdoc>
</kw>
<kw name="Regexp Escape" lineno="3447">
<arguments repr="*patterns">
<arg kind="VAR_POSITIONAL" required="false" repr="*patterns">
<name>patterns</name>
</arg>
</arguments>
<doc>Returns each argument string escaped for use as a regular expression.

This keyword can be used to escape strings to be used with
`Should Match Regexp` and `Should Not Match Regexp` keywords.

Escaping is done with Python's ``re.escape()`` function.

Examples:
| ${escaped} = | Regexp Escape | ${original} |
| @{strings} = | Regexp Escape | @{strings}  |</doc>
<shortdoc>Returns each argument string escaped for use as a regular expression.</shortdoc>
</kw>
<kw name="Reload Library" lineno="3119">
<arguments repr="name_or_instance">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name_or_instance">
<name>name_or_instance</name>
</arg>
</arguments>
<doc>Rechecks what keywords the specified library provides.

Can be called explicitly in the test data or by a library itself
when keywords it provides have changed.

The library can be specified by its name or as the active instance of
the library. The latter is especially useful if the library itself
calls this keyword as a method.</doc>
<shortdoc>Rechecks what keywords the specified library provides.</shortdoc>
</kw>
<kw name="Remove Tags" lineno="3605">
<arguments repr="*tags">
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>Removes given ``tags`` from the current test or all tests in a suite.

Tags can be given exactly or using a pattern with ``*``, ``?`` and
``[chars]`` acting as wildcards. See the `Glob patterns` section
for more information.

This keyword can affect either one test case or all test cases in a
test suite similarly as `Set Tags` keyword.

The current tags are available as a built-in variable ``@{TEST TAGS}``.

Example:
| Remove Tags | mytag | something-* | ?ython |

See `Set Tags` if you want to add certain tags and `Fail` if you want
to fail the test case after setting and/or removing tags.</doc>
<shortdoc>Removes given ``tags`` from the current test or all tests in a suite.</shortdoc>
</kw>
<kw name="Repeat Keyword" lineno="2205">
<arguments repr="repeat, name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="repeat">
<name>repeat</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Executes the specified keyword multiple times.

``name`` and ``args`` define the keyword that is executed similarly as
with `Run Keyword`. ``repeat`` specifies how many times (as a count) or
how long time (as a timeout) the keyword should be executed.

If ``repeat`` is given as count, it specifies how many times the
keyword should be executed. ``repeat`` can be given as an integer or
as a string that can be converted to an integer. If it is a string,
it can have postfix ``times`` or ``x`` (case and space insensitive)
to make the expression more explicit.

If ``repeat`` is given as timeout, it must be in Robot Framework's
time format (e.g. ``1 minute``, ``2 min 3 s``). Using a number alone
(e.g. ``1`` or ``1.5``) does not work in this context.

If ``repeat`` is zero or negative, the keyword is not executed at
all. This keyword fails immediately if any of the execution
rounds fails.

Examples:
| Repeat Keyword | 5 times   | Go to Previous Page |
| Repeat Keyword | ${var}    | Some Keyword | arg1 | arg2 |
| Repeat Keyword | 2 minutes | Some Keyword | arg1 | arg2 |</doc>
<shortdoc>Executes the specified keyword multiple times.</shortdoc>
</kw>
<kw name="Replace Variables" lineno="1574">
<arguments repr="text">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="text">
<name>text</name>
</arg>
</arguments>
<doc>Replaces variables in the given text with their current values.

If the text contains undefined variables, this keyword fails.
If the given ``text`` contains only a single variable, its value is
returned as-is and it can be any object. Otherwise this keyword
always returns a string.

Example:

The file ``template.txt`` contains ``Hello ${NAME}!`` and variable
``${NAME}`` has the value ``Robot``.

| ${template} =   | Get File          | ${CURDIR}/template.txt |
| ${message} =    | Replace Variables | ${template}            |
| Should Be Equal | ${message}        | Hello Robot!           |</doc>
<shortdoc>Replaces variables in the given text with their current values.</shortdoc>
</kw>
<kw name="Return From Keyword" lineno="2663">
<arguments repr="*return_values">
<arg kind="VAR_POSITIONAL" required="false" repr="*return_values">
<name>return_values</name>
</arg>
</arguments>
<doc>Returns from the enclosing user keyword.

---

*NOTE:* Robot Framework 5.0 added support for native ``RETURN`` statement that
is recommended over this keyword. In the examples below, ``Return From Keyword``
can simply be replaced with ``RETURN``. In addition to that, native ``IF``
syntax (new in RF 4.0) or inline ``IF`` syntax (new in RF 5.0) can be used
instead of ``Run Keyword If``. For example, the first example below could be
written like this instead:

| IF    ${rc} &lt; 0    RETURN

This keyword will eventually be deprecated and removed.

---

This keyword can be used to return from a user keyword with PASS status
without executing it fully. It is also possible to return values
similarly as with the ``[Return]`` setting. For more detailed information
about working with the return values, see the User Guide.

This keyword is typically wrapped to some other keyword, such as
`Run Keyword If`, to return based on a condition:

| Run Keyword If    ${rc} &lt; 0    Return From Keyword

It is possible to use this keyword to return from a keyword also inside
a for loop. That, as well as returning values, is demonstrated by the
`Find Index` keyword in the following somewhat advanced example.
Notice that it is often a good idea to move this kind of complicated
logic into a library.

| ***** Variables *****
| @{LIST} =    foo    baz
|
| ***** Test Cases *****
| Example
|     ${index} =    Find Index    baz    @{LIST}
|     Should Be Equal    ${index}    ${1}
|     ${index} =    Find Index    non existing    @{LIST}
|     Should Be Equal    ${index}    ${-1}
|
| ***** Keywords *****
| Find Index
|    [Arguments]    ${element}    @{items}
|    ${index} =    Set Variable    ${0}
|    FOR    ${item}    IN    @{items}
|        Run Keyword If    '${item}' == '${element}'    Return From Keyword    ${index}
|        ${index} =    Set Variable    ${index + 1}
|    END
|    Return From Keyword    ${-1}

The most common use case, returning based on an expression, can be
accomplished directly with `Return From Keyword If`. See also
`Run Keyword And Return` and `Run Keyword And Return If`.</doc>
<shortdoc>Returns from the enclosing user keyword.</shortdoc>
</kw>
<kw name="Return From Keyword If" lineno="2728">
<arguments repr="condition, *return_values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*return_values">
<name>return_values</name>
</arg>
</arguments>
<doc>Returns from the enclosing user keyword if ``condition`` is true.

---

*NOTE:* Robot Framework 5.0 added support for native ``RETURN`` statement
and for inline ``IF``, and that combination should be used instead of this
keyword. For example, ``Return From Keyword`` usage in the example below
could be replaced with

| IF    '${item}' == '${element}'    RETURN    ${index}

This keyword will eventually be deprecated and removed.

---

A wrapper for `Return From Keyword` to return based on the given
condition. The condition is evaluated using the same semantics as
with `Should Be True` keyword.

Given the same example as in `Return From Keyword`, we can rewrite the
`Find Index` keyword as follows:

| ***** Keywords *****
| Find Index
|    [Arguments]    ${element}    @{items}
|    ${index} =    Set Variable    ${0}
|    FOR    ${item}    IN    @{items}
|        Return From Keyword If    '${item}' == '${element}'    ${index}
|        ${index} =    Set Variable    ${index + 1}
|    END
|    Return From Keyword    ${-1}

See also `Run Keyword And Return` and `Run Keyword And Return If`.</doc>
<shortdoc>Returns from the enclosing user keyword if ``condition`` is true.</shortdoc>
</kw>
<kw name="Run Keyword" lineno="1839">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Executes the given keyword with the given arguments.

Because the name of the keyword to execute is given as an argument, it
can be a variable and thus set dynamically, e.g. from a return value of
another keyword or from the command line.</doc>
<shortdoc>Executes the given keyword with the given arguments.</shortdoc>
</kw>
<kw name="Run Keyword And Continue On Failure" lineno="2109">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the keyword and continues execution even if a failure occurs.

The keyword name and arguments work as with `Run Keyword`.

Example:
| Run Keyword And Continue On Failure | Fail | This is a stupid example |
| Log | This keyword is executed |

The execution is not continued if the failure is caused by invalid syntax,
timeout, or fatal exception.</doc>
<shortdoc>Runs the keyword and continues execution even if a failure occurs.</shortdoc>
</kw>
<kw name="Run Keyword And Expect Error" lineno="2129">
<arguments repr="expected_error, name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected_error">
<name>expected_error</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the keyword and checks that the expected error occurred.

The keyword to execute and its arguments are specified using ``name``
and ``*args`` exactly like with `Run Keyword`.

The expected error must be given in the same format as in Robot Framework
reports. By default it is interpreted as a glob pattern with ``*``, ``?``
and ``[chars]`` as wildcards, but that can be changed by using various
prefixes explained in the table below. Prefixes are case-sensitive and
they must be separated from the actual message with a colon and an
optional space like ``PREFIX: Message`` or ``PREFIX:Message``.

| = Prefix = | = Explanation = |
| ``EQUALS`` | Exact match. Especially useful if the error contains glob wildcards. |
| ``STARTS`` | Error must start with the specified error. |
| ``REGEXP`` | Regular expression match. |
| ``GLOB``   | Same as the default behavior. |

See the `Pattern matching` section for more information about glob
patterns and regular expressions.

If the expected error occurs, the error message is returned and it can
be further processed or tested if needed. If there is no error, or the
error does not match the expected error, this keyword fails.

Examples:
| Run Keyword And Expect Error | My error            | Keyword | arg |
| Run Keyword And Expect Error | ValueError: *       | Some Keyword  |
| Run Keyword And Expect Error | STARTS: ValueError: | Some Keyword  |
| Run Keyword And Expect Error | EQUALS:No match for '//input[@type="text"]' |
| ...                          | Find Element | //input[@type="text"] |
| ${msg} =                     | Run Keyword And Expect Error | * |
| ...                          | Keyword | arg1 | arg2 |
| Log To Console | ${msg} |

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword.

*NOTE:* Regular expression matching used to require only the beginning
of the error to match the given pattern. That was changed in Robot
Framework 5.0 and nowadays the pattern must match the error fully.
To match only the beginning, add ``.*`` at the end of the pattern like
``REGEXP: Start.*``.

*NOTE:* Robot Framework 5.0 introduced native TRY/EXCEPT functionality
that is generally recommended for error handling. It supports same
pattern matching syntax as this keyword.</doc>
<shortdoc>Runs the keyword and checks that the expected error occurred.</shortdoc>
</kw>
<kw name="Run Keyword And Ignore Error" lineno="2043">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with the given arguments and ignores possible error.

This keyword returns two values, so that the first is either string
``PASS`` or ``FAIL``, depending on the status of the executed keyword.
The second value is either the return value of the keyword or the
received error message. See `Run Keyword And Return Status` If you are
only interested in the execution status.

The keyword name and arguments work as in `Run Keyword`. See
`Run Keyword If` for a usage example.

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword. Otherwise this keyword itself never fails.

*NOTE:* Robot Framework 5.0 introduced native TRY/EXCEPT functionality
that is generally recommended for error handling.</doc>
<shortdoc>Runs the given keyword with the given arguments and ignores possible error.</shortdoc>
</kw>
<kw name="Run Keyword And Return" lineno="2767">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the specified keyword and returns from the enclosing user keyword.

The keyword to execute is defined with ``name`` and ``*args`` exactly
like with `Run Keyword`. After running the keyword, returns from the
enclosing user keyword and passes possible return value from the
executed keyword further. Returning from a keyword has exactly same
semantics as with `Return From Keyword`.

Example:
| `Run Keyword And Return`  | `My Keyword` | arg1 | arg2 |
| # Above is equivalent to: |
| ${result} =               | `My Keyword` | arg1 | arg2 |
| `Return From Keyword`     | ${result}    |      |      |

Use `Run Keyword And Return If` if you want to run keyword and return
based on a condition.</doc>
<shortdoc>Runs the specified keyword and returns from the enclosing user keyword.</shortdoc>
</kw>
<kw name="Run Keyword And Return If" lineno="2793">
<arguments repr="condition, name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the specified keyword and returns from the enclosing user keyword.

A wrapper for `Run Keyword And Return` to run and return based on
the given ``condition``. The condition is evaluated using the same
semantics as with `Should Be True` keyword.

Example:
| `Run Keyword And Return If` | ${rc} &gt; 0 | `My Keyword` | arg1 | arg2 |
| # Above is equivalent to:   |
| `Run Keyword If`            | ${rc} &gt; 0 | `Run Keyword And Return` | `My Keyword ` | arg1 | arg2 |

Use `Return From Keyword If` if you want to return a certain value
based on a condition.</doc>
<shortdoc>Runs the specified keyword and returns from the enclosing user keyword.</shortdoc>
</kw>
<kw name="Run Keyword And Return Status" lineno="2088">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with given arguments and returns the status as a Boolean value.

This keyword returns Boolean ``True`` if the keyword that is executed
succeeds and ``False`` if it fails. This is useful, for example, in
combination with `Run Keyword If`. If you are interested in the error
message or return value, use `Run Keyword And Ignore Error` instead.

The keyword name and arguments work as in `Run Keyword`.

Example:
| ${passed} = | `Run Keyword And Return Status` | Keyword | args |
| `Run Keyword If` | ${passed} | Another keyword |

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword. Otherwise this keyword itself never fails.</doc>
<shortdoc>Runs the given keyword with given arguments and returns the status as a Boolean value.</shortdoc>
</kw>
<kw name="Run Keyword And Warn On Failure" lineno="2069">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the specified keyword logs a warning if the keyword fails.

This keyword is similar to `Run Keyword And Ignore Error` but if the executed
keyword fails, the error message is logged as a warning to make it more
visible. Returns status and possible return value or error message exactly
like `Run Keyword And Ignore Error` does.

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword. Otherwise this keyword itself never fails.

New in Robot Framework 4.0.</doc>
<shortdoc>Runs the specified keyword logs a warning if the keyword fails.</shortdoc>
</kw>
<kw name="Run Keyword If" lineno="1949">
<arguments repr="condition, name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with the given arguments, if ``condition`` is true.

*NOTE:* Robot Framework 4.0 introduced built-in IF/ELSE support and using
that is generally recommended over using this keyword.

The given ``condition`` is evaluated in Python as explained in the
`Evaluating expressions` section, and ``name`` and ``*args`` have same
semantics as with `Run Keyword`.

Example, a simple if/else construct:
| `Run Keyword If` | '${status}' == 'OK' | Some Action    | arg |
| `Run Keyword If` | '${status}' != 'OK' | Another Action |

In this example, only either ``Some Action`` or ``Another Action`` is
executed, based on the value of the ``${status}`` variable.

Variables used like ``${variable}``, as in the examples above, are
replaced in the expression before evaluation. Variables are also
available in the evaluation namespace and can be accessed using special
``$variable`` syntax as explained in the `Evaluating expressions` section.

Example:
| `Run Keyword If` | $result is None or $result == 'FAIL' | Keyword |

This keyword supports also optional ELSE and ELSE IF branches. Both
of them are defined in ``*args`` and must use exactly format ``ELSE``
or ``ELSE IF``, respectively. ELSE branches must contain first the
name of the keyword to execute and then its possible arguments. ELSE
IF branches must first contain a condition, like the first argument
to this keyword, and then the keyword to execute and its possible
arguments. It is possible to have ELSE branch after ELSE IF and to
have multiple ELSE IF branches. Nested `Run Keyword If` usage is not
supported when using ELSE and/or ELSE IF branches.

Given previous example, if/else construct can also be created like this:
| `Run Keyword If` | '${status}' == 'PASS' | Some Action | arg | ELSE | Another Action |

The return value of this keyword is the return value of the actually
executed keyword or Python ``None`` if no keyword was executed (i.e.
if ``condition`` was false). Hence, it is recommended to use ELSE
and/or ELSE IF branches to conditionally assign return values from
keyword to variables (see `Set Variable If` you need to set fixed
values conditionally). This is illustrated by the example below:

| ${var1} =   | `Run Keyword If` | ${rc} == 0     | Some keyword returning a value |
| ...         | ELSE IF          | 0 &lt; ${rc} &lt; 42 | Another keyword |
| ...         | ELSE IF          | ${rc} &lt; 0      | Another keyword with args | ${rc} | arg2 |
| ...         | ELSE             | Final keyword to handle abnormal cases | ${rc} |
| ${var2} =   | `Run Keyword If` | ${condition}  | Some keyword |

In this example, ${var2} will be set to ``None`` if ${condition} is
false.

Notice that ``ELSE`` and ``ELSE IF`` control words must be used
explicitly and thus cannot come from variables. If you need to use
literal ``ELSE`` and ``ELSE IF`` strings as arguments, you can escape
them with a backslash like ``\ELSE`` and ``\ELSE IF``.</doc>
<shortdoc>Runs the given keyword with the given arguments, if ``condition`` is true.</shortdoc>
</kw>
<kw name="Run Keyword If All Tests Passed" lineno="2472">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with the given arguments, if all tests passed.

This keyword can only be used in a suite teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.</doc>
<shortdoc>Runs the given keyword with the given arguments, if all tests passed.</shortdoc>
</kw>
<kw name="Run Keyword If Any Tests Failed" lineno="2486">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with the given arguments, if one or more tests failed.

This keyword can only be used in a suite teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.</doc>
<shortdoc>Runs the given keyword with the given arguments, if one or more tests failed.</shortdoc>
</kw>
<kw name="Run Keyword If Test Failed" lineno="2424">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with the given arguments, if the test failed.

This keyword can only be used in a test teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.</doc>
<shortdoc>Runs the given keyword with the given arguments, if the test failed.</shortdoc>
</kw>
<kw name="Run Keyword If Test Passed" lineno="2438">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword with the given arguments, if the test passed.

This keyword can only be used in a test teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.</doc>
<shortdoc>Runs the given keyword with the given arguments, if the test passed.</shortdoc>
</kw>
<kw name="Run Keyword If Timeout Occurred" lineno="2452">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the given keyword if either a test or a keyword timeout has occurred.

This keyword can only be used in a test teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.</doc>
<shortdoc>Runs the given keyword if either a test or a keyword timeout has occurred.</shortdoc>
</kw>
<kw name="Run Keyword Unless" deprecated="true" lineno="2031">
<arguments repr="condition, name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>*DEPRECATED since RF 5.0. Use Native IF/ELSE or `Run Keyword If` instead.*

Runs the given keyword with the given arguments if ``condition`` is false.

See `Run Keyword If` for more information and an example. Notice that this
keyword does not support ELSE or ELSE IF branches like `Run Keyword If` does.</doc>
<shortdoc>*DEPRECATED since RF 5.0. Use Native IF/ELSE or `Run Keyword If` instead.*</shortdoc>
</kw>
<kw name="Run Keywords" lineno="1871">
<arguments repr="*keywords">
<arg kind="VAR_POSITIONAL" required="false" repr="*keywords">
<name>keywords</name>
</arg>
</arguments>
<doc>Executes all the given keywords in a sequence.

This keyword is mainly useful in setups and teardowns when they need
to take care of multiple actions and creating a new higher level user
keyword would be an overkill.

By default all arguments are expected to be keywords to be executed.

Examples:
| `Run Keywords` | `Initialize database` | `Start servers` | `Clear logs` |
| `Run Keywords` | ${KW 1} | ${KW 2} |
| `Run Keywords` | @{KEYWORDS} |

Keywords can also be run with arguments using upper case ``AND`` as
a separator between keywords. The keywords are executed so that the
first argument is the first keyword and proceeding arguments until
the first ``AND`` are arguments to it. First argument after the first
``AND`` is the second keyword and proceeding arguments until the next
``AND`` are its arguments. And so on.

Examples:
| `Run Keywords` | `Initialize database` | db1 | AND | `Start servers` | server1 | server2 |
| `Run Keywords` | `Initialize database` | ${DB NAME} | AND | `Start servers` | @{SERVERS} | AND | `Clear logs` |
| `Run Keywords` | ${KW} | AND | @{KW WITH ARGS} |

Notice that the ``AND`` control argument must be used explicitly and
cannot itself come from a variable. If you need to use literal ``AND``
string as argument, you can either use variables or escape it with
a backslash like ``\AND``.</doc>
<shortdoc>Executes all the given keywords in a sequence.</shortdoc>
</kw>
<kw name="Set Global Variable" lineno="1754">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Makes a variable available globally in all tests and suites.

Variables set with this keyword are globally available in all
subsequent test suites, test cases and user keywords. Also variables
created Variables sections are overridden. Variables assigned locally
based on keyword return values or by using `Set Suite Variable`,
`Set Test Variable` or `Set Local Variable` override these variables
in that scope, but the global value is not changed in those cases.

In practice setting variables with this keyword has the same effect
as using command line options ``--variable`` and ``--variablefile``.
Because this keyword can change variables everywhere, it should be
used with care.

See `Set Suite Variable` for more information and usage examples. See
also the `Using variables with keywords creating or accessing variables`
section for information why it is recommended to give the variable name
in escaped format like ``$name`` or ``\${name}`` instead of the normal
``${name}``.</doc>
<shortdoc>Makes a variable available globally in all tests and suites.</shortdoc>
</kw>
<kw name="Set Library Search Order" lineno="3217">
<arguments repr="*search_order">
<arg kind="VAR_POSITIONAL" required="false" repr="*search_order">
<name>search_order</name>
</arg>
</arguments>
<doc>Sets the resolution order to use when a name matches multiple keywords.

The library search order is used to resolve conflicts when a keyword name
that is used matches multiple keyword implementations. The first library
(or resource, see below) containing the keyword is selected and that
keyword implementation used. If the keyword is not found from any library
(or resource), execution fails the same way as when the search order is
not set.

When this keyword is used, there is no need to use the long
``LibraryName.Keyword Name`` notation.  For example, instead of
having

| MyLibrary.Keyword | arg |
| MyLibrary.Another Keyword |
| MyLibrary.Keyword | xxx |

you can have

| Set Library Search Order | MyLibrary |
| Keyword | arg |
| Another Keyword |
| Keyword | xxx |

This keyword can be used also to set the order of keywords in different
resource files. In this case resource names must be given without paths
or extensions like:

| Set Library Search Order | resource | another_resource |

*NOTE:*
- The search order is valid only in the suite where this keyword is used.
- Keywords in resources always have higher priority than
  keywords in libraries regardless the search order.
- The old order is returned and can be used to reset the search order later.
- Calling this keyword without arguments removes possible search order.
- Library and resource names in the search order are both case and space
  insensitive.</doc>
<shortdoc>Sets the resolution order to use when a name matches multiple keywords.</shortdoc>
</kw>
<kw name="Set Local Variable" lineno="1621">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Makes a variable available everywhere within the local scope.

Variables set with this keyword are available within the
local scope of the currently executed test case or in the local scope
of the keyword in which they are defined. For example, if you set a
variable in a user keyword, it is available only in that keyword. Other
test cases or keywords will not see variables set with this keyword.

This keyword is equivalent to a normal variable assignment based on a
keyword return value. For example,

| ${var} =    `Set Variable`    value
| @{list} =    `Create List`    item1    item2    item3

are equivalent with

| `Set Local Variable`    @var    value
| `Set Local Variable`    @list    item1    item2    item3

The main use case for this keyword is creating local variables in
libraries.

See `Set Suite Variable` for more information and usage examples. See
also the `Using variables with keywords creating or accessing variables`
section for information why it is recommended to give the variable name
in escaped format like ``$name`` or ``\${name}`` instead of the normal
``${name}``.

See also `Set Global Variable` and `Set Test Variable`.</doc>
<shortdoc>Makes a variable available everywhere within the local scope.</shortdoc>
</kw>
<kw name="Set Log Level" lineno="3101">
<arguments repr="level">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="level">
<name>level</name>
</arg>
</arguments>
<doc>Sets the log threshold to the specified level and returns the old level.

Messages below the level will not logged. The default logging level is
INFO, but it can be overridden with the command line option
``--loglevel``.

The available levels: TRACE, DEBUG, INFO (default), WARN, ERROR and NONE (no
logging).</doc>
<shortdoc>Sets the log threshold to the specified level and returns the old level.</shortdoc>
</kw>
<kw name="Set Suite Documentation" lineno="3537">
<arguments repr="doc, append=False, top=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="doc">
<name>doc</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="append=False">
<name>append</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="top=False">
<name>top</name>
<default>False</default>
</arg>
</arguments>
<doc>Sets documentation for the current test suite.

By default the possible existing documentation is overwritten, but
this can be changed using the optional ``append`` argument similarly
as with `Set Test Message` keyword.

This keyword sets the documentation of the current suite by default.
If the optional ``top`` argument is given a true value (see `Boolean
arguments`), the documentation of the top level suite is altered
instead.

The documentation of the current suite is available as a built-in
variable ``${SUITE DOCUMENTATION}``.</doc>
<shortdoc>Sets documentation for the current test suite.</shortdoc>
</kw>
<kw name="Set Suite Metadata" lineno="3557">
<arguments repr="name, value, append=False, top=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="append=False">
<name>append</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="top=False">
<name>top</name>
<default>False</default>
</arg>
</arguments>
<doc>Sets metadata for the current test suite.

By default possible existing metadata values are overwritten, but
this can be changed using the optional ``append`` argument similarly
as with `Set Test Message` keyword.

This keyword sets the metadata of the current suite by default.
If the optional ``top`` argument is given a true value (see `Boolean
arguments`), the metadata of the top level suite is altered instead.

The metadata of the current suite is available as a built-in variable
``${SUITE METADATA}`` in a Python dictionary. Notice that modifying this
variable directly has no effect on the actual metadata the suite has.</doc>
<shortdoc>Sets metadata for the current test suite.</shortdoc>
</kw>
<kw name="Set Suite Variable" lineno="1693">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Makes a variable available everywhere within the scope of the current suite.

Variables set with this keyword are available everywhere within the
scope of the currently executed test suite. Setting variables with this
keyword thus has the same effect as creating them using the Variables
section in the data file or importing them from variable files.

Possible child test suites do not see variables set with this keyword
by default, but that can be controlled by using ``children=&lt;option&gt;``
as the last argument. If the specified ``&lt;option&gt;`` is given a true value
(see `Boolean arguments`), the variable is set also to the child
suites. Parent and sibling suites will never see variables set with
this keyword.

The name of the variable can be given either as a normal variable name
like ``${NAME}`` or in escaped format as ``\${NAME}`` or ``$NAME``.
For the reasons explained in the `Using variables with keywords creating
or accessing variables` section, *using the escaped format is highly
recommended*.

Variable value can be specified using the same syntax as when variables
are created in the Variables section. Same way as in that section,
it is possible to create scalar values, lists and dictionaries.
The type is got from the variable name prefix ``$``, ``@`` and ``&amp;``,
respectively.

If a variable already exists within the new scope, its value will be
overwritten. If a variable already exists within the current scope,
the value can be left empty and the variable within the new scope gets
the value within the current scope.

Examples:
| Set Suite Variable    $SCALAR    Hello, world!
| Set Suite Variable    $SCALAR    Hello, world!    children=True
| Set Suite Variable    @LIST      First item       Second item
| Set Suite Variable    &amp;DICT      key=value        foo=bar
| ${ID} =    Get ID
| Set Suite Variable    $ID

To override an existing value with an empty value, use built-in
variables ``${EMPTY}``, ``@{EMPTY}`` or ``&amp;{EMPTY}``:

| Set Suite Variable    $SCALAR    ${EMPTY}
| Set Suite Variable    @LIST      @{EMPTY}
| Set Suite Variable    &amp;DICT      &amp;{EMPTY}

See also `Set Global Variable`, `Set Test Variable` and `Set Local Variable`.</doc>
<shortdoc>Makes a variable available everywhere within the scope of the current suite.</shortdoc>
</kw>
<kw name="Set Tags" lineno="3580">
<arguments repr="*tags">
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>Adds given ``tags`` for the current test or all tests in a suite.

When this keyword is used inside a test case, that test gets
the specified tags and other tests are not affected.

If this keyword is used in a suite setup, all test cases in
that suite, recursively, gets the given tags. It is a failure
to use this keyword in a suite teardown.

The current tags are available as a built-in variable ``@{TEST TAGS}``.

See `Remove Tags` if you want to remove certain tags and `Fail` if
you want to fail the test case after setting and/or removing tags.</doc>
<shortdoc>Adds given ``tags`` for the current test or all tests in a suite.</shortdoc>
</kw>
<kw name="Set Task Variable" lineno="1684">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Makes a variable available everywhere within the scope of the current task.

This is an alias for `Set Test Variable` that is more applicable when
creating tasks, not tests.</doc>
<shortdoc>Makes a variable available everywhere within the scope of the current task.</shortdoc>
</kw>
<kw name="Set Test Documentation" lineno="3518">
<arguments repr="doc, append=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="doc">
<name>doc</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="append=False">
<name>append</name>
<default>False</default>
</arg>
</arguments>
<doc>Sets documentation for the current test case.

By default the possible existing documentation is overwritten, but
this can be changed using the optional ``append`` argument similarly
as with `Set Test Message` keyword.

The current test documentation is available as a built-in variable
``${TEST DOCUMENTATION}``. This keyword can not be used in suite
setup or suite teardown.</doc>
<shortdoc>Sets documentation for the current test case.</shortdoc>
</kw>
<kw name="Set Test Message" lineno="3465">
<arguments repr="message, append=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="append=False">
<name>append</name>
<default>False</default>
</arg>
</arguments>
<doc>Sets message for the current test case.

If the optional ``append`` argument is given a true value (see `Boolean
arguments`), the given ``message`` is added after the possible earlier
message by joining the messages with a space.

In test teardown this keyword can alter the possible failure message,
but otherwise failures override messages set by this keyword. Notice
that in teardown the message is available as a built-in variable
``${TEST MESSAGE}``.

It is possible to use HTML format in the message by starting the message
with ``*HTML*``.

Examples:
| Set Test Message | My message           |                          |
| Set Test Message | is continued.        | append=yes               |
| Should Be Equal  | ${TEST MESSAGE}      | My message is continued. |
| Set Test Message | `*`HTML`*` &lt;b&gt;Hello!&lt;/b&gt; |                      |

This keyword can not be used in suite setup or suite teardown.</doc>
<shortdoc>Sets message for the current test case.</shortdoc>
</kw>
<kw name="Set Test Variable" lineno="1658">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Makes a variable available everywhere within the scope of the current test.

Variables set with this keyword are available everywhere within the
scope of the currently executed test case. For example, if you set a
variable in a user keyword, it is available both in the test case level
and also in all other user keywords used in the current test. Other
test cases will not see variables set with this keyword.
It is an error to call `Set Test Variable` outside the
scope of a test (e.g. in a Suite Setup or Teardown).

See `Set Suite Variable` for more information and usage examples. See
also the `Using variables with keywords creating or accessing variables`
section for information why it is recommended to give the variable name
in escaped format like ``$name`` or ``\${name}`` instead of the normal
``${name}``.

When creating automated tasks, not tests, it is possible to use `Set
Task Variable`. See also `Set Global Variable` and `Set Local Variable`.</doc>
<shortdoc>Makes a variable available everywhere within the scope of the current test.</shortdoc>
</kw>
<kw name="Set Variable" lineno="1593">
<arguments repr="*values">
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Returns the given values which can then be assigned to a variables.

This keyword is mainly used for setting scalar variables.
Additionally it can be used for converting a scalar variable
containing a list to a list variable or to multiple scalar variables.
It is recommended to use `Create List` when creating new lists.

Examples:
| ${hi} =   | Set Variable | Hello, world! |
| ${hi2} =  | Set Variable | I said: ${hi} |
| ${var1}   | ${var2} =    | Set Variable | Hello | world |
| @{list} = | Set Variable | ${list with some items} |
| ${item1}  | ${item2} =   | Set Variable  | ${list with 2 items} |

Variables created with this keyword are available only in the
scope where they are created. See `Set Global Variable`,
`Set Test Variable` and `Set Suite Variable` for information on how to
set variables so that they are available also in a larger scope.</doc>
<shortdoc>Returns the given values which can then be assigned to a variables.</shortdoc>
</kw>
<kw name="Set Variable If" lineno="2366">
<arguments repr="condition, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Sets variable based on the given condition.

The basic usage is giving a condition and two values. The
given condition is first evaluated the same way as with the
`Should Be True` keyword. If the condition is true, then the
first value is returned, and otherwise the second value is
returned. The second value can also be omitted, in which case
it has a default value None. This usage is illustrated in the
examples below, where ``${rc}`` is assumed to be zero.

| ${var1} = | Set Variable If | ${rc} == 0 | zero     | nonzero |
| ${var2} = | Set Variable If | ${rc} &gt; 0  | value1   | value2  |
| ${var3} = | Set Variable If | ${rc} &gt; 0  | whatever |         |
=&gt;
| ${var1} = 'zero'
| ${var2} = 'value2'
| ${var3} = None

It is also possible to have 'else if' support by replacing the
second value with another condition, and having two new values
after it. If the first condition is not true, the second is
evaluated and one of the values after it is returned based on
its truth value. This can be continued by adding more
conditions without a limit.

| ${var} = | Set Variable If | ${rc} == 0        | zero           |
| ...      | ${rc} &gt; 0       | greater than zero | less then zero |
|          |
| ${var} = | Set Variable If |
| ...      | ${rc} == 0      | zero              |
| ...      | ${rc} == 1      | one               |
| ...      | ${rc} == 2      | two               |
| ...      | ${rc} &gt; 2       | greater than two  |
| ...      | ${rc} &lt; 0       | less than zero    |

Use `Get Variable Value` if you need to set variables
dynamically based on whether a variable exist or not.</doc>
<shortdoc>Sets variable based on the given condition.</shortdoc>
</kw>
<kw name="Should Be Empty" lineno="1426">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Verifies that the given item is empty.

The length of the item is got using the `Get Length` keyword. The
default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Verifies that the given item is empty.</shortdoc>
</kw>
<kw name="Should Be Equal" lineno="563">
<arguments repr="first, second, msg=None, values=True, ignore_case=False, formatter=str, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="formatter=str">
<name>formatter</name>
<default>str</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the given objects are unequal.

Optional ``msg``, ``values`` and ``formatter`` arguments specify how
to construct the error message if this keyword fails:

- If ``msg`` is not given, the error message is ``&lt;first&gt; != &lt;second&gt;``.
- If ``msg`` is given and ``values`` gets a true value (default),
  the error message is ``&lt;msg&gt;: &lt;first&gt; != &lt;second&gt;``.
- If ``msg`` is given and ``values`` gets a false value (see
  `Boolean arguments`), the error message is simply ``&lt;msg&gt;``.
- ``formatter`` controls how to format the values. Possible values are
  ``str`` (default), ``repr`` and ``ascii``, and they work similarly
  as Python built-in functions with same names. See `String
  representations` for more details.

If ``ignore_case`` is given a true value (see `Boolean arguments`) and
both arguments are strings, comparison is done case-insensitively.
If both arguments are multiline strings, this keyword uses
`multiline string comparison`.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

Examples:
| Should Be Equal | ${x} | expected |
| Should Be Equal | ${x} | expected | Custom error message |
| Should Be Equal | ${x} | expected | Custom message | values=False |
| Should Be Equal | ${x} | expected | ignore_case=True | formatter=repr |

``strip_spaces`` is new in Robot Framework 4.0 and
``collapse_spaces`` is new in Robot Framework 4.1.</doc>
<shortdoc>Fails if the given objects are unequal.</shortdoc>
</kw>
<kw name="Should Be Equal As Integers" lineno="720">
<arguments repr="first, second, msg=None, values=True, base=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if objects are unequal after converting them to integers.

See `Convert To Integer` for information how to convert integers from
other bases than 10 using ``base`` argument or ``0b/0o/0x`` prefixes.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

Examples:
| Should Be Equal As Integers | 42   | ${42} | Error message |
| Should Be Equal As Integers | ABCD | abcd  | base=16 |
| Should Be Equal As Integers | 0b1011 | 11  |</doc>
<shortdoc>Fails if objects are unequal after converting them to integers.</shortdoc>
</kw>
<kw name="Should Be Equal As Numbers" lineno="757">
<arguments repr="first, second, msg=None, values=True, precision=6">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="precision=6">
<name>precision</name>
<default>6</default>
</arg>
</arguments>
<doc>Fails if objects are unequal after converting them to real numbers.

The conversion is done with `Convert To Number` keyword using the
given ``precision``.

Examples:
| Should Be Equal As Numbers | ${x} | 1.1 | | # Passes if ${x} is 1.1 |
| Should Be Equal As Numbers | 1.123 | 1.1 | precision=1  | # Passes |
| Should Be Equal As Numbers | 1.123 | 1.4 | precision=0  | # Passes |
| Should Be Equal As Numbers | 112.3 | 75  | precision=-2 | # Passes |

As discussed in the documentation of `Convert To Number`, machines
generally cannot store floating point numbers accurately. Because of
this limitation, comparing floats for equality is problematic and
a correct approach to use depends on the context. This keyword uses
a very naive approach of rounding the numbers before comparing them,
which is both prone to rounding errors and does not work very well if
numbers are really big or small. For more information about comparing
floats, and ideas on how to implement your own context specific
comparison algorithm, see
http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/.

If you want to avoid possible problems with floating point numbers,
you can implement custom keywords using Python's
[http://docs.python.org/library/decimal.html|decimal] or
[http://docs.python.org/library/fractions.html|fractions] modules.

See `Should Not Be Equal As Numbers` for a negative version of this
keyword and `Should Be Equal` for an explanation on how to override
the default error message with ``msg`` and ``values``.</doc>
<shortdoc>Fails if objects are unequal after converting them to real numbers.</shortdoc>
</kw>
<kw name="Should Be Equal As Strings" lineno="836">
<arguments repr="first, second, msg=None, values=True, ignore_case=False, strip_spaces=False, formatter=str, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="formatter=str">
<name>formatter</name>
<default>str</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if objects are unequal after converting them to strings.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg``, ``values`` and ``formatter``.

If ``ignore_case`` is given a true value (see `Boolean arguments`),
comparison is done case-insensitively. If both arguments are
multiline strings, this keyword uses `multiline string comparison`.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

Strings are always [http://www.macchiato.com/unicode/nfc-faq| NFC normalized].

``strip_spaces`` is new in Robot Framework 4.0
and ``collapse_spaces`` is new in Robot Framework 4.1.</doc>
<shortdoc>Fails if objects are unequal after converting them to strings.</shortdoc>
</kw>
<kw name="Should Be True" lineno="532">
<arguments repr="condition, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given condition is not true.

If ``condition`` is a string (e.g. ``${rc} &lt; 10``), it is evaluated as
a Python expression as explained in `Evaluating expressions` and the
keyword status is decided based on the result. If a non-string item is
given, the status is got directly from its
[http://docs.python.org/library/stdtypes.html#truth|truth value].

The default error message (``&lt;condition&gt; should be true``) is not very
informative, but it can be overridden with the ``msg`` argument.

Examples:
| Should Be True | ${rc} &lt; 10            |
| Should Be True | '${status}' == 'PASS' | # Strings must be quoted |
| Should Be True | ${number}   | # Passes if ${number} is not zero |
| Should Be True | ${list}     | # Passes if ${list} is not empty  |

Variables used like ``${variable}``, as in the examples above, are
replaced in the expression before evaluation. Variables are also
available in the evaluation namespace, and can be accessed using
special ``$variable`` syntax as explained in the `Evaluating
expressions` section.

Examples:
| Should Be True | $rc &lt; 10          |
| Should Be True | $status == 'PASS' | # Expected string must be quoted |</doc>
<shortdoc>Fails if the given condition is not true.</shortdoc>
</kw>
<kw name="Should Contain" lineno="1020">
<arguments repr="container, item, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``container`` does not contain ``item`` one or more times.

Works with strings, lists, and anything that supports Python's ``in``
operator.

See `Should Be Equal` for an explanation on how to override the default
error message with arguments ``msg`` and ``values``.

If ``ignore_case`` is given a true value (see `Boolean arguments`) and
compared items are strings, it indicates that comparison should be
case-insensitive. If the ``container`` is a list-like object, string
items in it are compared case-insensitively.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

Examples:
| Should Contain | ${output}    | PASS  |
| Should Contain | ${some list} | value | msg=Failure! | values=False |
| Should Contain | ${some list} | value | ignore_case=True |

``strip_spaces`` is new in Robot Framework 4.0 and ``collapse_spaces`` is new
in Robot Framework 4.1.</doc>
<shortdoc>Fails if ``container`` does not contain ``item`` one or more times.</shortdoc>
</kw>
<kw name="Should Contain Any" lineno="1076">
<arguments repr="container, *items, **configuration">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**configuration">
<name>configuration</name>
</arg>
</arguments>
<doc>Fails if ``container`` does not contain any of the ``*items``.

Works with strings, lists, and anything that supports Python's ``in``
operator.

Supports additional configuration parameters ``msg``, ``values``,
``ignore_case`` and ``strip_spaces``, and ``collapse_spaces``
which have exactly the same semantics as arguments with same
names have with `Should Contain`. These arguments must always
be given using ``name=value`` syntax after all ``items``.

Note that possible equal signs in ``items`` must be escaped with
a backslash (e.g. ``foo\=bar``) to avoid them to be passed in
as ``**configuration``.

Examples:
| Should Contain Any | ${string} | substring 1 | substring 2 |
| Should Contain Any | ${list}   | item 1 | item 2 | item 3 |
| Should Contain Any | ${list}   | item 1 | item 2 | item 3 | ignore_case=True |
| Should Contain Any | ${list}   | @{items} | msg=Custom message | values=False |</doc>
<shortdoc>Fails if ``container`` does not contain any of the ``*items``.</shortdoc>
</kw>
<kw name="Should Contain X Times" lineno="1193">
<arguments repr="container, item, count, msg=None, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="count">
<name>count</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``container`` does not contain ``item`` ``count`` times.

Works with strings, lists and all objects that `Get Count` works
with. The default error message can be overridden with ``msg`` and
the actual count is always logged.

If ``ignore_case`` is given a true value (see `Boolean arguments`) and
compared items are strings, it indicates that comparison should be
case-insensitive. If the ``container`` is a list-like object, string
items in it are compared case-insensitively.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

Examples:
| Should Contain X Times | ${output}    | hello | 2 |
| Should Contain X Times | ${some list} | value | 3 | ignore_case=True |

``strip_spaces`` is new in Robot Framework 4.0 and ``collapse_spaces`` is new
in Robot Framework 4.1.</doc>
<shortdoc>Fails if ``container`` does not contain ``item`` ``count`` times.</shortdoc>
</kw>
<kw name="Should End With" lineno="942">
<arguments repr="str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str1">
<name>str1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str2">
<name>str2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the string ``str1`` does not end with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``, as well as for semantics
of the ``ignore_case``, ``strip_spaces``, and ``collapse_spaces`` options.</doc>
<shortdoc>Fails if the string ``str1`` does not end with the string ``str2``.</shortdoc>
</kw>
<kw name="Should Match" lineno="1289">
<arguments repr="string, pattern, msg=None, values=True, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the given ``string`` does not match the given ``pattern``.

Pattern matching is similar as matching files in a shell with
``*``, ``?`` and ``[chars]`` acting as wildcards. See the
`Glob patterns` section for more information.

If ``ignore_case`` is given a true value (see `Boolean arguments`) and
compared items are strings, it indicates that comparison should be
case-insensitive.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.</doc>
<shortdoc>Fails if the given ``string`` does not match the given ``pattern``.</shortdoc>
</kw>
<kw name="Should Match Regexp" lineno="1308">
<arguments repr="string, pattern, msg=None, values=True, flags=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="flags=None">
<name>flags</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if ``string`` does not match ``pattern`` as a regular expression.

See the `Regular expressions` section for more information about
regular expressions and how to use then in Robot Framework test data.

Notice that the given pattern does not need to match the whole string.
For example, the pattern ``ello`` matches the string ``Hello world!``.
If a full match is needed, the ``^`` and ``$`` characters can be used
to denote the beginning and end of the string, respectively.
For example, ``^ello$`` only matches the exact string ``ello``.

Possible flags altering how the expression is parsed (e.g. ``re.IGNORECASE``,
``re.MULTILINE``) can be given using the ``flags`` argument (e.g.
``flags=IGNORECASE | MULTILINE``) or embedded to the pattern (e.g.
``(?im)pattern``).

If this keyword passes, it returns the portion of the string that
matched the pattern. Additionally, the possible captured groups are
returned.

See the `Should Be Equal` keyword for an explanation on how to override
the default error message with the ``msg`` and ``values`` arguments.

Examples:
| Should Match Regexp | ${output} | \\d{6}   | # Output contains six numbers  |
| Should Match Regexp | ${output} | ^\\d{6}$ | # Six numbers and nothing more |
| ${ret} = | Should Match Regexp | Foo: 42 | foo: \\d+ | flags=IGNORECASE |
| ${ret} = | Should Match Regexp | Foo: 42 | (?i)foo: \\d+ |
| ${match} | ${group1} | ${group2} = |
| ...      | Should Match Regexp | Bar: 43 | (Foo|Bar): (\\d+) |
=&gt;
| ${ret} = 'Foo: 42'
| ${match} = 'Bar: 43'
| ${group1} = 'Bar'
| ${group2} = '43'

The ``flags`` argument is new in Robot Framework 6.0.</doc>
<shortdoc>Fails if ``string`` does not match ``pattern`` as a regular expression.</shortdoc>
</kw>
<kw name="Should Not Be Empty" lineno="1435">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Verifies that the given item is not empty.

The length of the item is got using the `Get Length` keyword. The
default error message can be overridden with the ``msg`` argument.</doc>
<shortdoc>Verifies that the given item is not empty.</shortdoc>
</kw>
<kw name="Should Not Be Equal" lineno="663">
<arguments repr="first, second, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the given objects are equal.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

If ``ignore_case`` is given a true value (see `Boolean arguments`) and
both arguments are strings, comparison is done case-insensitively.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

``strip_spaces`` is new in Robot Framework 4.0 and ``collapse_spaces`` is new
in Robot Framework 4.1.</doc>
<shortdoc>Fails if the given objects are equal.</shortdoc>
</kw>
<kw name="Should Not Be Equal As Integers" lineno="703">
<arguments repr="first, second, msg=None, values=True, base=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if objects are equal after converting them to integers.

See `Convert To Integer` for information how to convert integers from
other bases than 10 using ``base`` argument or ``0b/0o/0x`` prefixes.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

See `Should Be Equal As Integers` for some usage examples.</doc>
<shortdoc>Fails if objects are equal after converting them to integers.</shortdoc>
</kw>
<kw name="Should Not Be Equal As Numbers" lineno="740">
<arguments repr="first, second, msg=None, values=True, precision=6">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="precision=6">
<name>precision</name>
<default>6</default>
</arg>
</arguments>
<doc>Fails if objects are equal after converting them to real numbers.

The conversion is done with `Convert To Number` keyword using the
given ``precision``.

See `Should Be Equal As Numbers` for examples on how to use
``precision`` and why it does not always work as expected. See also
`Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.</doc>
<shortdoc>Fails if objects are equal after converting them to real numbers.</shortdoc>
</kw>
<kw name="Should Not Be Equal As Strings" lineno="795">
<arguments repr="first, second, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="first">
<name>first</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="second">
<name>second</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if objects are equal after converting them to strings.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

If ``ignore_case`` is given a true value (see `Boolean arguments`),
comparison is done case-insensitively.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

Strings are always [http://www.macchiato.com/unicode/nfc-faq|
NFC normalized].

``strip_spaces`` is new in Robot Framework 4.0 and ``collapse_spaces`` is new
in Robot Framework 4.1.</doc>
<shortdoc>Fails if objects are equal after converting them to strings.</shortdoc>
</kw>
<kw name="Should Not Be True" lineno="523">
<arguments repr="condition, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given condition is true.

See `Should Be True` for details about how ``condition`` is evaluated
and how ``msg`` can be used to override the default error message.</doc>
<shortdoc>Fails if the given condition is true.</shortdoc>
</kw>
<kw name="Should Not Contain" lineno="963">
<arguments repr="container, item, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``container`` contains ``item`` one or more times.

Works with strings, lists, and anything that supports Python's ``in``
operator.

See `Should Be Equal` for an explanation on how to override the default
error message with arguments ``msg`` and ``values``. ``ignore_case``
has exactly the same semantics as with `Should Contain`.

If ``strip_spaces`` is given a true value (see `Boolean arguments`)
and both arguments are strings, the comparison is done without leading
and trailing spaces. If ``strip_spaces`` is given a string value
``LEADING`` or ``TRAILING`` (case-insensitive), the comparison is done
without leading or trailing spaces, respectively.

If ``collapse_spaces`` is given a true value (see `Boolean arguments`) and both
arguments are strings, the comparison is done with all white spaces replaced by
a single space character.

Examples:
| Should Not Contain | ${some list} | value  |
| Should Not Contain | ${output}    | FAILED | ignore_case=True |

``strip_spaces`` is new in Robot Framework 4.0 and ``collapse_spaces`` is new
in Robot Framework 4.1.</doc>
<shortdoc>Fails if ``container`` contains ``item`` one or more times.</shortdoc>
</kw>
<kw name="Should Not Contain Any" lineno="1135">
<arguments repr="container, *items, **configuration">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**configuration">
<name>configuration</name>
</arg>
</arguments>
<doc>Fails if ``container`` contains one or more of the ``*items``.

Works with strings, lists, and anything that supports Python's ``in``
operator.

Supports additional configuration parameters ``msg``, ``values``,
``ignore_case`` and ``strip_spaces``, and ``collapse_spaces`` which have exactly
the same semantics as arguments with same names have with `Should Contain`.
These arguments must always be given using ``name=value`` syntax after all ``items``.

Note that possible equal signs in ``items`` must be escaped with
a backslash (e.g. ``foo\=bar``) to avoid them to be passed in
as ``**configuration``.

Examples:
| Should Not Contain Any | ${string} | substring 1 | substring 2 |
| Should Not Contain Any | ${list}   | item 1 | item 2 | item 3 |
| Should Not Contain Any | ${list}   | item 1 | item 2 | item 3 | ignore_case=True |
| Should Not Contain Any | ${list}   | @{items} | msg=Custom message | values=False |</doc>
<shortdoc>Fails if ``container`` contains one or more of the ``*items``.</shortdoc>
</kw>
<kw name="Should Not End With" lineno="920">
<arguments repr="str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str1">
<name>str1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str2">
<name>str2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the string ``str1`` ends with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``, as well as for semantics
of the ``ignore_case``, ``strip_spaces``, and ``collapse_spaces`` options.</doc>
<shortdoc>Fails if the string ``str1`` ends with the string ``str2``.</shortdoc>
</kw>
<kw name="Should Not Match" lineno="1271">
<arguments repr="string, pattern, msg=None, values=True, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the given ``string`` matches the given ``pattern``.

Pattern matching is similar as matching files in a shell with
``*``, ``?`` and ``[chars]`` acting as wildcards. See the
`Glob patterns` section for more information.

If ``ignore_case`` is given a true value (see `Boolean arguments`),
the comparison is case-insensitive.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values`.</doc>
<shortdoc>Fails if the given ``string`` matches the given ``pattern``.</shortdoc>
</kw>
<kw name="Should Not Match Regexp" lineno="1357">
<arguments repr="string, pattern, msg=None, values=True, flags=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="flags=None">
<name>flags</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if ``string`` matches ``pattern`` as a regular expression.

See `Should Match Regexp` for more information about arguments.</doc>
<shortdoc>Fails if ``string`` matches ``pattern`` as a regular expression.</shortdoc>
</kw>
<kw name="Should Not Start With" lineno="877">
<arguments repr="str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str1">
<name>str1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str2">
<name>str2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the string ``str1`` starts with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``, as well as for semantics
of the ``ignore_case``, ``strip_spaces``, and ``collapse_spaces`` options.</doc>
<shortdoc>Fails if the string ``str1`` starts with the string ``str2``.</shortdoc>
</kw>
<kw name="Should Start With" lineno="899">
<arguments repr="str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str1">
<name>str1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="str2">
<name>str2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_spaces=False">
<name>strip_spaces</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="collapse_spaces=False">
<name>collapse_spaces</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the string ``str1`` does not start with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``, as well as for semantics
of the ``ignore_case``, ``strip_spaces``, and ``collapse_spaces`` options.</doc>
<shortdoc>Fails if the string ``str1`` does not start with the string ``str2``.</shortdoc>
</kw>
<kw name="Skip" lineno="2508">
<arguments repr="msg=Skipped with Skip keyword.">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=Skipped with Skip keyword.">
<name>msg</name>
<default>Skipped with Skip keyword.</default>
</arg>
</arguments>
<doc>Skips the rest of the current test.

Skips the remaining keywords in the current test and sets the given
message to the test. If the test has teardown, it will be executed.</doc>
<shortdoc>Skips the rest of the current test.</shortdoc>
</kw>
<kw name="Skip If" lineno="2516">
<arguments repr="condition, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Skips the rest of the current test if the ``condition`` is True.

Skips the remaining keywords in the current test and sets the given
message to the test. If ``msg`` is not given, the ``condition`` will
be used as the message. If the test has teardown, it will be executed.

If the ``condition`` evaluates to False, does nothing.</doc>
<shortdoc>Skips the rest of the current test if the ``condition`` is True.</shortdoc>
</kw>
<kw name="Sleep" lineno="2888">
<arguments repr="time_, reason=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time_">
<name>time_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="reason=None">
<name>reason</name>
<default>None</default>
</arg>
</arguments>
<doc>Pauses the test executed for the given time.

``time`` may be either a number or a time string. Time strings are in
a format such as ``1 day 2 hours 3 minutes 4 seconds 5milliseconds`` or
``1d 2h 3m 4s 5ms``, and they are fully explained in an appendix of
Robot Framework User Guide. Providing a value without specifying minutes
or seconds, defaults to seconds.
Optional `reason` can be used to explain why
sleeping is necessary. Both the time slept and the reason are logged.

Examples:
| Sleep | 42                   |
| Sleep | 1.5                  |
| Sleep | 2 minutes 10 seconds |
| Sleep | 10s                  | Wait for a reply |</doc>
<shortdoc>Pauses the test executed for the given time.</shortdoc>
</kw>
<kw name="Variable Should Exist" lineno="1533">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails unless the given variable exists within the current scope.

The name of the variable can be given either as a normal variable name
like ``${name}`` or in escaped format like ``$name`` or ``\${name}``.
For the reasons explained in the `Using variables with keywords creating
or accessing variables` section, using the escaped format is recommended.

The default error message can be overridden with the ``msg`` argument.

See also `Variable Should Not Exist` and `Keyword Should Exist`.</doc>
<shortdoc>Fails unless the given variable exists within the current scope.</shortdoc>
</kw>
<kw name="Variable Should Not Exist" lineno="1553">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>Fails if the given variable exists within the current scope.

The name of the variable can be given either as a normal variable name
like ``${name}`` or in escaped format like ``$name`` or ``\${name}``.
For the reasons explained in the `Using variables with keywords creating
or accessing variables` section, using the escaped format is recommended.

The default error message can be overridden with the ``msg`` argument.

See also `Variable Should Exist` and `Keyword Should Exist`.</doc>
<shortdoc>Fails if the given variable exists within the current scope.</shortdoc>
</kw>
<kw name="Wait Until Keyword Succeeds" lineno="2284">
<arguments repr="retry, retry_interval, name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="retry">
<name>retry</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="retry_interval">
<name>retry_interval</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>Runs the specified keyword and retries if it fails.

``name`` and ``args`` define the keyword that is executed similarly
as with `Run Keyword`. How long to retry running the keyword is
defined using ``retry`` argument either as timeout or count.
``retry_interval`` is the time to wait between execution attempts.

If ``retry`` is given as timeout, it must be in Robot Framework's
time format (e.g. ``1 minute``, ``2 min 3 s``, ``4.5``) that is
explained in an appendix of Robot Framework User Guide. If it is
given as count, it must have ``times`` or ``x`` postfix (e.g.
``5 times``, ``10 x``). ``retry_interval`` must always be given in
Robot Framework's time format.

By default ``retry_interval`` is the time to wait _after_ a keyword has
failed. For example, if the first run takes 2 seconds and the retry
interval is 3 seconds, the second run starts 5 seconds after the first
run started. If ``retry_interval`` start with prefix ``strict:``, the
execution time of the previous keyword is subtracted from the retry time.
With the earlier example the second run would thus start 3 seconds after
the first run started. A warning is logged if keyword execution time is
longer than a strict interval.

If the keyword does not succeed regardless of retries, this keyword
fails. If the executed keyword passes, its return value is returned.

Examples:
| Wait Until Keyword Succeeds | 2 min | 5 sec | My keyword | argument |
| ${result} = | Wait Until Keyword Succeeds | 3x | 200ms | My keyword |
| ${result} = | Wait Until Keyword Succeeds | 3x | strict: 200ms | My keyword |

All normal failures are caught by this keyword. Errors caused by
invalid syntax, test or keyword timeouts, or fatal exceptions (caused
e.g. by `Fatal Error`) are not caught.

Running the same keyword multiple times inside this keyword can create
lots of output and considerably increase the size of the generated
output files. It is possible to remove unnecessary keywords from
the outputs using ``--RemoveKeywords WUKS`` command line option.

Support for "strict" retry interval is new in Robot Framework 4.1.</doc>
<shortdoc>Runs the specified keyword and retries if it fails.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
<typedocs>
</typedocs>
</keywordspec>
