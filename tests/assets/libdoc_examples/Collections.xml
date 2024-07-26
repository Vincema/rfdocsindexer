<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="Collections" type="LIBRARY" format="ROBOT" scope="GLOBAL" generated="2024-07-26T11:05:33+00:00" specversion="6" source="C:\Users\maire\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\robot\libraries\Collections.py" lineno="888">
<version>7.0.1</version>
<doc>A library providing keywords for handling lists and dictionaries.

``Collections`` is Robot Framework's standard library that provides a
set of keywords for handling Python lists and dictionaries. This
library has keywords, for example, for modifying and getting
values from lists and dictionaries (e.g. `Append To List`, `Get
From Dictionary`) and for verifying their contents (e.g. `Lists
Should Be Equal`, `Dictionary Should Contain Value`).

== Table of contents ==

- `Related keywords in BuiltIn`
- `Using with list-like and dictionary-like objects`
- `Ignore case`
- `Boolean arguments`
- `Data in examples`
- `Keywords`

= Related keywords in BuiltIn =

Following keywords in the BuiltIn library can also be used with
lists and dictionaries:

| = Keyword Name =             | = Applicable With = |
| `Create List`                | lists |
| `Create Dictionary`          | dicts |
| `Get Length`                 | both  |
| `Length Should Be`           | both  |
| `Should Be Empty`            | both  |
| `Should Not Be Empty`        | both  |
| `Should Contain`             | both  |
| `Should Not Contain`         | both  |
| `Should Contain X Times`     | lists |
| `Should Not Contain X Times` | lists |
| `Get Count`                  | lists |

= Using with list-like and dictionary-like objects =

List keywords that do not alter the given list can also be used
with tuples, and to some extent also with other iterables.
`Convert To List` can be used to convert tuples and other iterables
to Python ``list`` objects.

Similarly, dictionary keywords can, for most parts, be used with other
mappings. `Convert To Dictionary` can be used if real Python ``dict``
objects are needed.

= Ignore case =

Various keywords support ignoring case in comparisons by using the optional
``ignore_case`` argument. Case-insensitivity can be enabled by using
``ignore_case=True`` (see `Boolean arguments`) and it works recursively.
With dictionaries, it is also possible to use special values ``keys`` and
``values`` to normalize only keys or values, respectively. These options
themselves are case-insensitive and also singular forms ``key`` and
``value`` are supported.

If a dictionary contains keys that normalize to the same value, e.g.
``{'a': 1, 'A': 2}``, normalizing keys causes an error.

Examples:
| `Lists Should Be Equal`        | ${list1} | ${list2} | ignore_case=True   |
| `Dictionaries Should Be Equal` | ${dict1} | ${dict2} | ignore_case=values |

Notice that some keywords accept also an older ``case_insensitive`` argument
in addition to ``ignore_case``. The latter is new in Robot Framework 7.0 and
should be used unless there is a need to support older versions. The old
argument is considered deprecated and will eventually be removed.

= Boolean arguments =

Some keywords accept arguments that are handled as Boolean values true or
false. If such an argument is given as a string, it is considered false if
it is an empty string or equal to ``FALSE``, ``NONE``, ``NO``, ``OFF`` or
``0``, case-insensitively. Keywords verifying something that allow dropping
actual and expected values from the possible error message also consider
string ``no values`` to be false. Other strings are considered true
regardless their value, and other argument types are tested using the same
[http://docs.python.org/library/stdtypes.html#truth|rules as in Python].

| `Should Contain Match` | ${list} | ${pattern} | ignore_case=True  |
| `Should Contain Match` | ${list} | ${pattern} | ignore_case=False |
| `Lists Should Be Equal` | ${list1} | ${list2} | Custom error | no values |

= Data in examples =

List related keywords use variables in format ``${Lx}`` in their examples.
They mean lists with as many alphabetic characters as specified by ``x``.
For example, ``${L1}`` means ``['a']`` and ``${L3}`` means
``['a', 'b', 'c']``.

Dictionary keywords use similar ``${Dx}`` variables. For example, ``${D1}``
means ``{'a': 1}`` and ``${D3}`` means ``{'a': 1, 'b': 2, 'c': 3}``.</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Append To List" lineno="40">
<arguments repr="list_, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Adds ``values`` to the end of ``list``.

Example:
| Append To List | ${L1} | xxx |   |   |
| Append To List | ${L2} | x   | y | z |
=&gt;
| ${L1} = ['a', 'xxx']
| ${L2} = ['a', 'b', 'x', 'y', 'z']</doc>
<shortdoc>Adds ``values`` to the end of ``list``.</shortdoc>
</kw>
<kw name="Combine Lists" lineno="78">
<arguments repr="*lists">
<arg kind="VAR_POSITIONAL" required="false" repr="*lists">
<name>lists</name>
</arg>
</arguments>
<doc>Combines the given ``lists`` together and returns the result.

The given lists are not altered by this keyword.

Example:
| ${x} = | Combine Lists | ${L1} | ${L2} |       |
| ${y} = | Combine Lists | ${L1} | ${L2} | ${L1} |
=&gt;
| ${x} = ['a', 'a', 'b']
| ${y} = ['a', 'a', 'b', 'a']
| ${L1} and ${L2} are not changed.</doc>
<shortdoc>Combines the given ``lists`` together and returns the result.</shortdoc>
</kw>
<kw name="Convert To Dictionary" lineno="507">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>Converts the given ``item`` to a Python ``dict`` type.

Mainly useful for converting other mappings to normal dictionaries.
This includes converting Robot Framework's own ``DotDict`` instances
that it uses if variables are created using the ``&amp;{var}`` syntax.

Use `Create Dictionary` from the BuiltIn library for constructing new
dictionaries.</doc>
<shortdoc>Converts the given ``item`` to a Python ``dict`` type.</shortdoc>
</kw>
<kw name="Convert To List" lineno="32">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>Converts the given ``item`` to a Python ``list`` type.

Mainly useful for converting tuples and other iterable to lists.
Use `Create List` from the BuiltIn library for constructing new lists.</doc>
<shortdoc>Converts the given ``item`` to a Python ``list`` type.</shortdoc>
</kw>
<kw name="Copy Dictionary" lineno="602">
<arguments repr="dictionary, deepcopy=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="deepcopy=False">
<name>deepcopy</name>
<default>False</default>
</arg>
</arguments>
<doc>Returns a copy of the given dictionary.

By default, returns a new dictionary with same items as in the original.
Set the ``deepcopy`` argument to a true value if also items should
be copied.

The given dictionary is never altered by this keyword.</doc>
<shortdoc>Returns a copy of the given dictionary.</shortdoc>
</kw>
<kw name="Copy List" lineno="266">
<arguments repr="list_, deepcopy=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="deepcopy=False">
<name>deepcopy</name>
<default>False</default>
</arg>
</arguments>
<doc>Returns a copy of the given list.

By default, returns a new list with same items as in the original.
Set the ``deepcopy`` argument to a true value if also items should
be copied.

The given list is never altered by this keyword.</doc>
<shortdoc>Returns a copy of the given list.</shortdoc>
</kw>
<kw name="Count Values In List" lineno="228">
<arguments repr="list_, value, start=0, end=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
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
<doc>Returns the number of occurrences of the given ``value`` in ``list``.

The search can be narrowed to the selected sublist by the ``start`` and
``end`` indexes having the same semantics as with `Get Slice From List`
keyword. The given list is never altered by this keyword.

Example:
| ${x} = | Count Values In List | ${L3} | b |
=&gt;
| ${x} = 1
| ${L3} is not changed</doc>
<shortdoc>Returns the number of occurrences of the given ``value`` in ``list``.</shortdoc>
</kw>
<kw name="Dictionaries Should Be Equal" lineno="786">
<arguments repr="dict1, dict2, msg=None, values=True, ignore_keys=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dict1">
<name>dict1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dict2">
<name>dict2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_keys=None">
<name>ignore_keys</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the given dictionaries are not equal.

First the equality of dictionaries' keys is checked and after that all
the key value pairs. If there are differences between the values, those
are listed in the error message. The types of the dictionaries do not
need to be same.

``ignore_keys`` can be used to provide a list of keys to ignore in the
comparison. It can be an actual list or a Python list literal. This
option is new in Robot Framework 6.1. It works recursively with nested
dictionaries starting from Robot Framework 7.0.

Examples:
| Dictionaries Should Be Equal | ${dict} | ${expected} |
| Dictionaries Should Be Equal | ${dict} | ${expected} | ignore_keys=${ignored} |
| Dictionaries Should Be Equal | ${dict} | ${expected} | ignore_keys=['key1', 'key2'] |

See `Lists Should Be Equal` for more information about configuring
the error message with ``msg`` and ``values`` arguments.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if the given dictionaries are not equal.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Item" lineno="733">
<arguments repr="dictionary, key, value, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="key">
<name>key</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>An item of ``key`` / ``value`` must be found in a ``dictionary``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>An item of ``key`` / ``value`` must be found in a ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Key" lineno="699">
<arguments repr="dictionary, key, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="key">
<name>key</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``key`` is not found from ``dictionary``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if ``key`` is not found from ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Sub Dictionary" lineno="842">
<arguments repr="dict1, dict2, msg=None, values=True, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dict1">
<name>dict1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dict2">
<name>dict2</name>
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
<doc>Fails unless all items in ``dict2`` are found from ``dict1``.

See `Lists Should Be Equal` for more information about configuring
the error message with ``msg`` and ``values`` arguments.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails unless all items in ``dict2`` are found from ``dict1``.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Value" lineno="752">
<arguments repr="dictionary, value, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``value`` is not found from ``dictionary``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if ``value`` is not found from ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Not Contain Key" lineno="716">
<arguments repr="dictionary, key, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="key">
<name>key</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``key`` is found from ``dictionary``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if ``key`` is found from ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Not Contain Value" lineno="769">
<arguments repr="dictionary, value, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``value`` is found from ``dictionary``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if ``value`` is found from ``dictionary``.</shortdoc>
</kw>
<kw name="Get Dictionary Items" lineno="654">
<arguments repr="dictionary, sort_keys=True">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="sort_keys=True">
<name>sort_keys</name>
<default>True</default>
</arg>
</arguments>
<doc>Returns items of the given ``dictionary`` as a list.

Uses `Get Dictionary Keys` to get keys and then returns corresponding
items. By default, keys are sorted and items returned in that order,
but this can be changed by giving ``sort_keys`` a false value.

Items are returned as a flat list so that first item is a key,
second item is a corresponding value, third item is the second key,
and so on.

The given ``dictionary`` is never altered by this keyword.

Example:
| ${sorted} =   | Get Dictionary Items | ${D3} |
| ${unsorted} = | Get Dictionary Items | ${D3} | sort_keys=False |</doc>
<shortdoc>Returns items of the given ``dictionary`` as a list.</shortdoc>
</kw>
<kw name="Get Dictionary Keys" lineno="616">
<arguments repr="dictionary, sort_keys=True">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="sort_keys=True">
<name>sort_keys</name>
<default>True</default>
</arg>
</arguments>
<doc>Returns keys of the given ``dictionary`` as a list.

By default, keys are returned in sorted order (assuming they are
sortable), but they can be returned in the original order by giving
``sort_keys`` a false value.

The given ``dictionary`` is never altered by this keyword.

Example:
| ${sorted} =   | Get Dictionary Keys | ${D3} |
| ${unsorted} = | Get Dictionary Keys | ${D3} | sort_keys=False |</doc>
<shortdoc>Returns keys of the given ``dictionary`` as a list.</shortdoc>
</kw>
<kw name="Get Dictionary Values" lineno="637">
<arguments repr="dictionary, sort_keys=True">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="sort_keys=True">
<name>sort_keys</name>
<default>True</default>
</arg>
</arguments>
<doc>Returns values of the given ``dictionary`` as a list.

Uses `Get Dictionary Keys` to get keys and then returns corresponding
values. By default, keys are sorted and values returned in that order,
but this can be changed by giving ``sort_keys`` a false value.

The given ``dictionary`` is never altered by this keyword.

Example:
| ${sorted} =   | Get Dictionary Values | ${D3} |
| ${unsorted} = | Get Dictionary Values | ${D3} | sort_keys=False |</doc>
<shortdoc>Returns values of the given ``dictionary`` as a list.</shortdoc>
</kw>
<kw name="Get From Dictionary" lineno="675">
<arguments repr="dictionary, key, default=">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="key">
<name>key</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=">
<name>default</name>
<default/>
</arg>
</arguments>
<doc>Returns a value from the given ``dictionary`` based on the given ``key``.

If the given ``key`` cannot be found from the ``dictionary``, this
keyword fails. If optional ``default`` value is given, it will be
returned instead of failing.

The given dictionary is never altered by this keyword.

Example:
| ${value} = | Get From Dictionary | ${D3} | b |
=&gt;
| ${value} = 2

Support for ``default`` is new in Robot Framework 6.0.</doc>
<shortdoc>Returns a value from the given ``dictionary`` based on the given ``key``.</shortdoc>
</kw>
<kw name="Get From List" lineno="173">
<arguments repr="list_, index">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index">
<name>index</name>
</arg>
</arguments>
<doc>Returns the value specified with an ``index`` from ``list``.

The given list is never altered by this keyword.

Index ``0`` means the first position, ``1`` the second, and so on.
Similarly, ``-1`` is the last position, ``-2`` the second last, and so on.
Using an index that does not exist on the list causes an error.
The index can be either an integer or a string that can be converted
to an integer.

Examples (including Python equivalents in comments):
| ${x} = | Get From List | ${L5} | 0  | # L5[0]  |
| ${y} = | Get From List | ${L5} | -2 | # L5[-2] |
=&gt;
| ${x} = 'a'
| ${y} = 'd'
| ${L5} is not changed</doc>
<shortdoc>Returns the value specified with an ``index`` from ``list``.</shortdoc>
</kw>
<kw name="Get Index From List" lineno="244">
<arguments repr="list_, value, start=0, end=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
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
<doc>Returns the index of the first occurrence of the ``value`` on the list.

The search can be narrowed to the selected sublist by the ``start`` and
``end`` indexes having the same semantics as with `Get Slice From List`
keyword. In case the value is not found, -1 is returned. The given list
is never altered by this keyword.

Example:
| ${x} = | Get Index From List | ${L5} | d |
=&gt;
| ${x} = 3
| ${L5} is not changed</doc>
<shortdoc>Returns the index of the first occurrence of the ``value`` on the list.</shortdoc>
</kw>
<kw name="Get Match Count" lineno="1071">
<arguments repr="list, pattern, case_insensitive: bool | None = None, whitespace_insensitive: bool | None = None, ignore_case: bool = False, ignore_whitespace: bool = False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list">
<name>list</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive: bool | None = None">
<name>case_insensitive</name>
<type name="Union" union="true">
<type name="bool" typedoc="boolean"/>
<type name="None" typedoc="None"/>
</type>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive: bool | None = None">
<name>whitespace_insensitive</name>
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_whitespace: bool = False">
<name>ignore_whitespace</name>
<type name="bool" typedoc="boolean"/>
<default>False</default>
</arg>
</arguments>
<doc>Returns the count of matches to ``pattern`` in ``list``.

For more information on ``pattern``, ``case_insensitive/ignore_case``, and
``whitespace_insensitive/ignore_whitespace``, see `Should Contain Match`.

Examples:
| ${count}= | Get Match Count | ${list} | a* | # ${count} will be the count of strings beginning with 'a' |
| ${count}= | Get Match Count | ${list} | regexp=a.* | # ${matches} will be the count of strings beginning with 'a' (regexp version) |
| ${count}= | Get Match Count | ${list} | a* | case_insensitive=${True} | # ${matches} will be the count of strings beginning with 'a' or 'A' |</doc>
<shortdoc>Returns the count of matches to ``pattern`` in ``list``.</shortdoc>
</kw>
<kw name="Get Matches" lineno="1051">
<arguments repr="list, pattern, case_insensitive: bool | None = None, whitespace_insensitive: bool | None = None, ignore_case: bool = False, ignore_whitespace: bool = False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list">
<name>list</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive: bool | None = None">
<name>case_insensitive</name>
<type name="Union" union="true">
<type name="bool" typedoc="boolean"/>
<type name="None" typedoc="None"/>
</type>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive: bool | None = None">
<name>whitespace_insensitive</name>
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_whitespace: bool = False">
<name>ignore_whitespace</name>
<type name="bool" typedoc="boolean"/>
<default>False</default>
</arg>
</arguments>
<doc>Returns a list of matches to ``pattern`` in ``list``.

For more information on ``pattern``, ``case_insensitive/ignore_case``, and
``whitespace_insensitive/ignore_whitespace``, see `Should Contain Match`.

Examples:
| ${matches}= | Get Matches | ${list} | a* | # ${matches} will contain any string beginning with 'a' |
| ${matches}= | Get Matches | ${list} | regexp=a.* | # ${matches} will contain any string beginning with 'a' (regexp version) |
| ${matches}= | Get Matches | ${list} | a* | ignore_case=True | # ${matches} will contain any string beginning with 'a' or 'A' |</doc>
<shortdoc>Returns a list of matches to ``pattern`` in ``list``.</shortdoc>
</kw>
<kw name="Get Slice From List" lineno="198">
<arguments repr="list_, start=0, end=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
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
<doc>Returns a slice of the given list between ``start`` and ``end`` indexes.

The given list is never altered by this keyword.

If both ``start`` and ``end`` are given, a sublist containing values
from ``start`` to ``end`` is returned. This is the same as
``list[start:end]`` in Python. To get all items from the beginning,
use 0 as the start value, and to get all items until and including
the end, use ``None`` (default) as the end value.

Using ``start`` or ``end`` not found on the list is the same as using
the largest (or smallest) available index.

Examples (incl. Python equivalents in comments):
| ${x} = | Get Slice From List | ${L5} | 2      | 4 | # L5[2:4]    |
| ${y} = | Get Slice From List | ${L5} | 1      |   | # L5[1:None] |
| ${z} = | Get Slice From List | ${L5} | end=-2 |   | # L5[0:-2]   |
=&gt;
| ${x} = ['c', 'd']
| ${y} = ['b', 'c', 'd', 'e']
| ${z} = ['a', 'b', 'c']
| ${L5} is not changed</doc>
<shortdoc>Returns a slice of the given list between ``start`` and ``end`` indexes.</shortdoc>
</kw>
<kw name="Insert Into List" lineno="54">
<arguments repr="list_, index, value">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index">
<name>index</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
</arguments>
<doc>Inserts ``value`` into ``list`` to the position specified with ``index``.

Index ``0`` adds the value into the first position, ``1`` to the second,
and so on. Inserting from right works with negative indices so that
``-1`` is the second last position, ``-2`` third last, and so on. Use
`Append To List` to add items to the end of the list.

If the absolute value of the index is greater than
the length of the list, the value is added at the end
(positive index) or the beginning (negative index). An index
can be given either as an integer or a string that can be
converted to an integer.

Example:
| Insert Into List | ${L1} | 0     | xxx |
| Insert Into List | ${L2} | ${-1} | xxx |
=&gt;
| ${L1} = ['xxx', 'a']
| ${L2} = ['a', 'xxx', 'b']</doc>
<shortdoc>Inserts ``value`` into ``list`` to the position specified with ``index``.</shortdoc>
</kw>
<kw name="Keep In Dictionary" lineno="587">
<arguments repr="dictionary, *keys">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*keys">
<name>keys</name>
</arg>
</arguments>
<doc>Keeps the given ``keys`` in the ``dictionary`` and removes all other.

If the given ``key`` cannot be found from the ``dictionary``, it
is ignored.

Example:
| Keep In Dictionary | ${D5} | b | x | d |
=&gt;
| ${D5} = {'b': 2, 'd': 4}</doc>
<shortdoc>Keeps the given ``keys`` in the ``dictionary`` and removes all other.</shortdoc>
</kw>
<kw name="List Should Contain Sub List" lineno="440">
<arguments repr="list1, list2, msg=None, values=True, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list1">
<name>list1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list2">
<name>list2</name>
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
<doc>Fails if not all elements in ``list2`` are found in ``list1``.

The order of values and the number of values are not taken into
account.

See `Lists Should Be Equal` for more information about configuring
the error message with ``msg`` and ``values`` arguments.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if not all elements in ``list2`` are found in ``list1``.</shortdoc>
</kw>
<kw name="List Should Contain Value" lineno="306">
<arguments repr="list_, value, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the ``value`` is not found from ``list``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if the ``value`` is not found from ``list``.</shortdoc>
</kw>
<kw name="List Should Not Contain Duplicates" lineno="334">
<arguments repr="list_, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if any element in the ``list`` is found from it more than once.

The default error message lists all the elements that were found
from the ``list`` multiple times, but it can be overridden by giving
a custom ``msg``. All multiple times found items and their counts are
also logged.

This keyword works with all iterables that can be converted to a list.
The original iterable is never altered.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if any element in the ``list`` is found from it more than once.</shortdoc>
</kw>
<kw name="List Should Not Contain Value" lineno="320">
<arguments repr="list_, value, msg=None, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if the ``value`` is found from ``list``.

Use the ``msg`` argument to override the default error message.

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if the ``value`` is found from ``list``.</shortdoc>
</kw>
<kw name="Lists Should Be Equal" lineno="361">
<arguments repr="list1, list2, msg=None, values=True, names=None, ignore_order=False, ignore_case=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list1">
<name>list1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list2">
<name>list2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="values=True">
<name>values</name>
<default>True</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="names=None">
<name>names</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_order=False">
<name>ignore_order</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_case=False">
<name>ignore_case</name>
<default>False</default>
</arg>
</arguments>
<doc>Fails if given lists are unequal.

The keyword first verifies that the lists have equal lengths, and then
it checks are all their values equal. Possible differences between the
values are listed in the default error message like ``Index 4: ABC !=
Abc``. The types of the lists do not need to be the same. For example,
Python tuple and list with same content are considered equal.

The error message can be configured using ``msg`` and ``values``
arguments:
- If ``msg`` is not given, the default error message is used.
- If ``msg`` is given and ``values`` gets a value considered true
  (see `Boolean arguments`), the error message starts with the given
  ``msg`` followed by a newline and the default message.
- If ``msg`` is given and ``values``  is not given a true value,
  the error message is just the given ``msg``.

The optional ``names`` argument can be used for naming the indices
shown in the default error message. It can either be a list of names
matching the indices in the lists or a dictionary where keys are
indices that need to be named. It is not necessary to name all indices.
When using a dictionary, keys can be either integers
or strings that can be converted to integers.

Examples:
| ${names} = | Create List | First Name | Family Name | Email |
| Lists Should Be Equal | ${people1} | ${people2} | names=${names} |
| ${names} = | Create Dictionary | 0=First Name | 2=Email |
| Lists Should Be Equal | ${people1} | ${people2} | names=${names} |

If the items in index 2 would differ in the above examples, the error
message would contain a row like ``Index 2 (email): name@foo.com !=
name@bar.com``.

The optional ``ignore_order`` argument can be used to ignore the order
of the elements in the lists. Using it requires items to be sortable.
This option works recursively with nested lists starting from Robot
Framework 7.0.

Example:
| ${list1} = | Create List | apple | cherry | banana |
| ${list2} = | Create List | cherry | banana | apple |
| Lists Should Be Equal | ${list1} | ${list2} | ignore_order=True |

The ``ignore_case`` argument can be used to make comparison case-insensitive.
See the `Ignore case` section for more details. This option is new in
Robot Framework 7.0.</doc>
<shortdoc>Fails if given lists are unequal.</shortdoc>
</kw>
<kw name="Log Dictionary" lineno="860">
<arguments repr="dictionary, level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>Logs the size and contents of the ``dictionary`` using given ``level``.

Valid levels are TRACE, DEBUG, INFO (default), and WARN.

If you only want to log the size, use keyword `Get Length` from
the BuiltIn library.</doc>
<shortdoc>Logs the size and contents of the ``dictionary`` using given ``level``.</shortdoc>
</kw>
<kw name="Log List" lineno="463">
<arguments repr="list_, level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>Logs the length and contents of the ``list`` using given ``level``.

Valid levels are TRACE, DEBUG, INFO (default), and WARN.

If you only want to the length, use keyword `Get Length` from
the BuiltIn library.</doc>
<shortdoc>Logs the length and contents of the ``list`` using given ``level``.</shortdoc>
</kw>
<kw name="Pop From Dictionary" lineno="568">
<arguments repr="dictionary, key, default=">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="key">
<name>key</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=">
<name>default</name>
<default/>
</arg>
</arguments>
<doc>Pops the given ``key`` from the ``dictionary`` and returns its value.

By default the keyword fails if the given ``key`` cannot be found from
the ``dictionary``. If optional ``default`` value is given, it will be
returned instead of failing.

Example:
| ${val}= | Pop From Dictionary | ${D3} | b |
=&gt;
| ${val} = 2
| ${D3} = {'a': 1, 'c': 3}</doc>
<shortdoc>Pops the given ``key`` from the ``dictionary`` and returns its value.</shortdoc>
</kw>
<kw name="Remove Duplicates" lineno="156">
<arguments repr="list_">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
</arguments>
<doc>Returns a list without duplicates based on the given ``list``.

Creates and returns a new list that contains all items in the given
list so that one item can appear only once. Order of the items in
the new list is the same as in the original except for missing
duplicates. Number of the removed duplicates is logged.</doc>
<shortdoc>Returns a list without duplicates based on the given ``list``.</shortdoc>
</kw>
<kw name="Remove From Dictionary" lineno="549">
<arguments repr="dictionary, *keys">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*keys">
<name>keys</name>
</arg>
</arguments>
<doc>Removes the given ``keys`` from the ``dictionary``.

If the given ``key`` cannot be found from the ``dictionary``, it
is ignored.

Example:
| Remove From Dictionary | ${D3} | b | x | y |
=&gt;
| ${D3} = {'a': 1, 'c': 3}</doc>
<shortdoc>Removes the given ``keys`` from the ``dictionary``.</shortdoc>
</kw>
<kw name="Remove From List" lineno="135">
<arguments repr="list_, index">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index">
<name>index</name>
</arg>
</arguments>
<doc>Removes and returns the value specified with an ``index`` from ``list``.

Index ``0`` means the first position, ``1`` the second and so on.
Similarly, ``-1`` is the last position, ``-2`` the second last, and so on.
Using an index that does not exist on the list causes an error.
The index can be either an integer or a string that can be converted
to an integer.

Example:
| ${x} = | Remove From List | ${L2} | 0 |
=&gt;
| ${x} = 'a'
| ${L2} = ['b']</doc>
<shortdoc>Removes and returns the value specified with an ``index`` from ``list``.</shortdoc>
</kw>
<kw name="Remove Values From List" lineno="120">
<arguments repr="list_, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>Removes all occurrences of given ``values`` from ``list``.

It is not an error if a value does not exist in the list at all.

Example:
| Remove Values From List | ${L4} | a | c | e | f |
=&gt;
| ${L4} = ['b', 'd']</doc>
<shortdoc>Removes all occurrences of given ``values`` from ``list``.</shortdoc>
</kw>
<kw name="Reverse List" lineno="280">
<arguments repr="list_">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
</arguments>
<doc>Reverses the given list in place.

Note that the given list is changed and nothing is returned. Use
`Copy List` first, if you need to keep also the original order.

| Reverse List | ${L3} |
=&gt;
| ${L3} = ['c', 'b', 'a']</doc>
<shortdoc>Reverses the given list in place.</shortdoc>
</kw>
<kw name="Set List Value" lineno="94">
<arguments repr="list_, index, value">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index">
<name>index</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
</arguments>
<doc>Sets the value of ``list`` specified by ``index`` to the given ``value``.

Index ``0`` means the first position, ``1`` the second and so on.
Similarly, ``-1`` is the last position, ``-2`` second last, and so on.
Using an index that does not exist on the list causes an error.
The index can be either an integer or a string that can be converted to
an integer.

Example:
| Set List Value | ${L3} | 1  | xxx |
| Set List Value | ${L3} | -1 | yyy |
=&gt;
| ${L3} = ['a', 'xxx', 'yyy']

Starting from Robot Framework 6.1, it is also possible to use the native
item assignment syntax. This is equivalent to the above:
| ${L3}[1] =  | Set Variable | xxx |
| ${L3}[-1] = | Set Variable | yyy |</doc>
<shortdoc>Sets the value of ``list`` specified by ``index`` to the given ``value``.</shortdoc>
</kw>
<kw name="Set To Dictionary" lineno="519">
<arguments repr="dictionary, *key_value_pairs, **items">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*key_value_pairs">
<name>key_value_pairs</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**items">
<name>items</name>
</arg>
</arguments>
<doc>Adds the given ``key_value_pairs`` and/or ``items`` to the ``dictionary``.

If given items already exist in the dictionary, their values are updated.

It is easiest to specify items using the ``name=value`` syntax:
| Set To Dictionary | ${D1} | key=value | second=${2} |
=&gt;
| ${D1} = {'a': 1, 'key': 'value', 'second': 2}

A limitation of the above syntax is that keys must be strings.
That can be avoided by passing keys and values as separate arguments:
| Set To Dictionary | ${D1} | key | value | ${2} | value 2 |
=&gt;
| ${D1} = {'a': 1, 'key': 'value', 2: 'value 2'}

Starting from Robot Framework 6.1, it is also possible to use the native
item assignment syntax. This is equivalent to the above:
| ${D1}[key] =  | Set Variable | value |
| ${D1}[${2}] = | Set Variable | value 2 |</doc>
<shortdoc>Adds the given ``key_value_pairs`` and/or ``items`` to the ``dictionary``.</shortdoc>
</kw>
<kw name="Should Contain Match" lineno="982">
<arguments repr="list, pattern, msg=None, case_insensitive: bool | None = None, whitespace_insensitive: bool | None = None, ignore_case: bool = False, ignore_whitespace: bool = False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list">
<name>list</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive: bool | None = None">
<name>case_insensitive</name>
<type name="Union" union="true">
<type name="bool" typedoc="boolean"/>
<type name="None" typedoc="None"/>
</type>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive: bool | None = None">
<name>whitespace_insensitive</name>
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_whitespace: bool = False">
<name>ignore_whitespace</name>
<type name="bool" typedoc="boolean"/>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``pattern`` is not found in ``list``.

By default, pattern matching is similar to matching files in a shell
and is case-sensitive and whitespace-sensitive. In the pattern syntax,
``*`` matches to anything and ``?`` matches to any single character. You
can also prepend ``glob=`` to your pattern to explicitly use this pattern
matching behavior.

If you prepend ``regexp=`` to your pattern, your pattern will be used
according to the Python
[http://docs.python.org/library/re.html|re module] regular expression
syntax. Notice that the backslash character often used with regular
expressions is an escape character in Robot Framework data and needs
to be escaped with another backslash like ``regexp=\\d{6}``. See
`BuiltIn.Should Match Regexp` for more details.

Matching is case-sensitive by default, but that can be changed by giving
the ``ignore_case`` argument a true value (see `Boolean arguments`).
This argument is new in Robot Framework 7.0, but with earlier versions
it is possible to use ``case_insensitive`` for the same purpose.

It is possible to ignore all whitespace by giving the ``ignore_whitespace``
argument a true value. This argument is new in Robot Framework 7.0 as well,
and with earlier versions it is possible to use ``whitespace_insensitive``.

Notice that both ``case_insensitive`` and ``whitespace_insensitive``
are considered deprecated. They will eventually be removed.

Non-string values in lists are ignored when matching patterns.

Use the ``msg`` argument to override the default error message.

Examples:
| Should Contain Match | ${list} | a*              | | | # Match strings beginning with 'a'. |
| Should Contain Match | ${list} | regexp=a.*      | | | # Same as the above but with regexp. |
| Should Contain Match | ${list} | regexp=\\d{6} | | | # Match strings containing six digits. |
| Should Contain Match | ${list} | a*  | ignore_case=True       | | # Match strings beginning with 'a' or 'A'. |
| Should Contain Match | ${list} | ab* | ignore_whitespace=yes  | | # Match strings beginning with 'ab' with possible whitespace ignored. |
| Should Contain Match | ${list} | ab* | ignore_whitespace=true | ignore_case=true | # Same as the above but also ignore case. |</doc>
<shortdoc>Fails if ``pattern`` is not found in ``list``.</shortdoc>
</kw>
<kw name="Should Not Contain Match" lineno="1034">
<arguments repr="list, pattern, msg=None, case_insensitive: bool | None = None, whitespace_insensitive: bool | None = None, ignore_case: bool = False, ignore_whitespace: bool = False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list">
<name>list</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive: bool | None = None">
<name>case_insensitive</name>
<type name="Union" union="true">
<type name="bool" typedoc="boolean"/>
<type name="None" typedoc="None"/>
</type>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive: bool | None = None">
<name>whitespace_insensitive</name>
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="ignore_whitespace: bool = False">
<name>ignore_whitespace</name>
<type name="bool" typedoc="boolean"/>
<default>False</default>
</arg>
</arguments>
<doc>Fails if ``pattern`` is found in ``list``.

Exact opposite of `Should Contain Match` keyword. See that keyword
for information about arguments and usage in general.</doc>
<shortdoc>Fails if ``pattern`` is found in ``list``.</shortdoc>
</kw>
<kw name="Sort List" lineno="293">
<arguments repr="list_">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
</arguments>
<doc>Sorts the given list in place.

Sorting fails if items in the list are not comparable with each others.
For example, sorting a list containing strings and numbers is not possible.

Note that the given list is changed and nothing is returned. Use
`Copy List` first, if you need to preserve the list also in the original
order.</doc>
<shortdoc>Sorts the given list in place.</shortdoc>
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
<usage>Get Match Count</usage>
<usage>Get Matches</usage>
<usage>Should Contain Match</usage>
<usage>Should Not Contain Match</usage>
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
<usage>Get Match Count</usage>
<usage>Get Matches</usage>
<usage>Should Contain Match</usage>
<usage>Should Not Contain Match</usage>
</usages>
</type>
</typedocs>
</keywordspec>
