<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="Collections" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2021-08-20T15:17:13Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/Collections.py" lineno="826">
<version>4.1</version>
<doc>&lt;p&gt;A test library providing keywords for handling lists and dictionaries.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;Collections&lt;/code&gt; is Robot Framework's standard library that provides a set of keywords for handling Python lists and dictionaries. This library has keywords, for example, for modifying and getting values from lists and dictionaries (e.g. &lt;a href="#Append%20To%20List" class="name"&gt;Append To List&lt;/a&gt;, &lt;a href="#Get%20From%20Dictionary" class="name"&gt;Get From Dictionary&lt;/a&gt;) and for verifying their contents (e.g. &lt;a href="#Lists%20Should%20Be%20Equal" class="name"&gt;Lists Should Be Equal&lt;/a&gt;, &lt;a href="#Dictionary%20Should%20Contain%20Value" class="name"&gt;Dictionary Should Contain Value&lt;/a&gt;).&lt;/p&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#Related%20keywords%20in%20BuiltIn" class="name"&gt;Related keywords in BuiltIn&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Using%20with%20list-like%20and%20dictionary-like%20objects" class="name"&gt;Using with list-like and dictionary-like objects&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Data%20in%20examples" class="name"&gt;Data in examples&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Related keywords in BuiltIn"&gt;Related keywords in BuiltIn&lt;/h2&gt;
&lt;p&gt;Following keywords in the BuiltIn library can also be used with lists and dictionaries:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Keyword Name&lt;/th&gt;
&lt;th&gt;Applicable With&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Create List&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;lists&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Create Dictionary&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;dicts&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Get Length&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;both&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Length Should Be&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;both&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Empty&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;both&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Not Be Empty&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;both&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Contain&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;both&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Not Contain&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;both&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Contain X Times&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;lists&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Not Contain X Times&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;lists&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Get Count&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;lists&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Using with list-like and dictionary-like objects"&gt;Using with list-like and dictionary-like objects&lt;/h2&gt;
&lt;p&gt;List keywords that do not alter the given list can also be used with tuples, and to some extend also with other iterables. &lt;a href="#Convert%20To%20List" class="name"&gt;Convert To List&lt;/a&gt; can be used to convert tuples and other iterables to Python &lt;code&gt;list&lt;/code&gt; objects.&lt;/p&gt;
&lt;p&gt;Similarly dictionary keywords can, for most parts, be used with other mappings. &lt;a href="#Convert%20To%20Dictionary" class="name"&gt;Convert To Dictionary&lt;/a&gt; can be used if real Python &lt;code&gt;dict&lt;/code&gt; objects are needed.&lt;/p&gt;
&lt;h2 id="Boolean arguments"&gt;Boolean arguments&lt;/h2&gt;
&lt;p&gt;Some keywords accept arguments that are handled as Boolean values true or false. If such an argument is given as a string, it is considered false if it is an empty string or equal to &lt;code&gt;FALSE&lt;/code&gt;, &lt;code&gt;NONE&lt;/code&gt;, &lt;code&gt;NO&lt;/code&gt;, &lt;code&gt;OFF&lt;/code&gt; or &lt;code&gt;0&lt;/code&gt;, case-insensitively. Keywords verifying something that allow dropping actual and expected values from the possible error message also consider string &lt;code&gt;no values&lt;/code&gt; to be false. Other strings are considered true regardless their value, and other argument types are tested using the same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;True examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=True&lt;/td&gt;
&lt;td&gt;# Strings are generally true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=yes&lt;/td&gt;
&lt;td&gt;# Same as the above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=${TRUE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;True&lt;/code&gt; is true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=${42}&lt;/td&gt;
&lt;td&gt;# Numbers other than 0 are true.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;False examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=False&lt;/td&gt;
&lt;td&gt;# String &lt;code&gt;false&lt;/code&gt; is false.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=no&lt;/td&gt;
&lt;td&gt;# Also string &lt;code&gt;no&lt;/code&gt; is false.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=${EMPTY}&lt;/td&gt;
&lt;td&gt;# Empty string is false.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;${pattern}&lt;/td&gt;
&lt;td&gt;case_insensitive=${FALSE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;False&lt;/code&gt; is false.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Lists%20Should%20Be%20Equal" class="name"&gt;Lists Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=no values&lt;/td&gt;
&lt;td&gt;# &lt;code&gt;no values&lt;/code&gt; works with &lt;code&gt;values&lt;/code&gt; argument&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Considering &lt;code&gt;OFF&lt;/code&gt; and &lt;code&gt;0&lt;/code&gt; false is new in Robot Framework 3.1.&lt;/p&gt;
&lt;h2 id="Data in examples"&gt;Data in examples&lt;/h2&gt;
&lt;p&gt;List related keywords use variables in format &lt;code&gt;${Lx}&lt;/code&gt; in their examples. They mean lists with as many alphabetic characters as specified by &lt;code&gt;x&lt;/code&gt;. For example, &lt;code&gt;${L1}&lt;/code&gt; means &lt;code&gt;['a']&lt;/code&gt; and &lt;code&gt;${L3}&lt;/code&gt; means &lt;code&gt;['a', 'b', 'c']&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Dictionary keywords use similar &lt;code&gt;${Dx}&lt;/code&gt; variables. For example, &lt;code&gt;${D1}&lt;/code&gt; means &lt;code&gt;{'a': 1}&lt;/code&gt; and &lt;code&gt;${D3}&lt;/code&gt; means &lt;code&gt;{'a': 1, 'b': 2, 'c': 3}&lt;/code&gt;.&lt;/p&gt;</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Append To List" lineno="41">
<arguments repr="list_, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Adds &lt;code&gt;values&lt;/code&gt; to the end of &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Append To List&lt;/td&gt;
&lt;td&gt;${L1}&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Append To List&lt;/td&gt;
&lt;td&gt;${L2}&lt;/td&gt;
&lt;td&gt;x&lt;/td&gt;
&lt;td&gt;y&lt;/td&gt;
&lt;td&gt;z&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${L1} = ['a', 'xxx']
${L2} = ['a', 'b', 'x', 'y', 'z']
&lt;/pre&gt;</doc>
<shortdoc>Adds ``values`` to the end of ``list``.</shortdoc>
</kw>
<kw name="Combine Lists" lineno="79">
<arguments repr="*lists">
<arg kind="VAR_POSITIONAL" required="false" repr="*lists">
<name>lists</name>
</arg>
</arguments>
<doc>&lt;p&gt;Combines the given &lt;code&gt;lists&lt;/code&gt; together and returns the result.&lt;/p&gt;
&lt;p&gt;The given lists are not altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Combine Lists&lt;/td&gt;
&lt;td&gt;${L1}&lt;/td&gt;
&lt;td&gt;${L2}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${y} =&lt;/td&gt;
&lt;td&gt;Combine Lists&lt;/td&gt;
&lt;td&gt;${L1}&lt;/td&gt;
&lt;td&gt;${L2}&lt;/td&gt;
&lt;td&gt;${L1}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} = ['a', 'a', 'b']
${y} = ['a', 'a', 'b', 'a']
${L1} and ${L2} are not changed.
&lt;/pre&gt;</doc>
<shortdoc>Combines the given ``lists`` together and returns the result.</shortdoc>
</kw>
<kw name="Convert To Dictionary" lineno="480">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given &lt;code&gt;item&lt;/code&gt; to a Python &lt;code&gt;dict&lt;/code&gt; type.&lt;/p&gt;
&lt;p&gt;Mainly useful for converting other mappings to normal dictionaries. This includes converting Robot Framework's own &lt;code&gt;DotDict&lt;/code&gt; instances that it uses if variables are created using the &lt;code&gt;&amp;amp;{var}&lt;/code&gt; syntax.&lt;/p&gt;
&lt;p&gt;Use &lt;span class="name"&gt;Create Dictionary&lt;/span&gt; from the BuiltIn library for constructing new dictionaries.&lt;/p&gt;</doc>
<shortdoc>Converts the given ``item`` to a Python ``dict`` type.</shortdoc>
</kw>
<kw name="Convert To List" lineno="33">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given &lt;code&gt;item&lt;/code&gt; to a Python &lt;code&gt;list&lt;/code&gt; type.&lt;/p&gt;
&lt;p&gt;Mainly useful for converting tuples and other iterable to lists. Use &lt;span class="name"&gt;Create List&lt;/span&gt; from the BuiltIn library for constructing new lists.&lt;/p&gt;</doc>
<shortdoc>Converts the given ``item`` to a Python ``list`` type.</shortdoc>
</kw>
<kw name="Copy Dictionary" lineno="571">
<arguments repr="dictionary, deepcopy=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="deepcopy=False">
<name>deepcopy</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a copy of the given dictionary.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;deepcopy&lt;/code&gt; argument controls should the returned dictionary be a &lt;a href="https://docs.python.org/library/copy.html"&gt;shallow or deep copy&lt;/a&gt;. By default returns a shallow copy, but that can be changed by giving &lt;code&gt;deepcopy&lt;/code&gt; a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). This is a new option in Robot Framework 3.1.2. Earlier versions always returned shallow copies.&lt;/p&gt;
&lt;p&gt;The given dictionary is never altered by this keyword.&lt;/p&gt;</doc>
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
<doc>&lt;p&gt;Returns a copy of the given list.&lt;/p&gt;
&lt;p&gt;If the optional &lt;code&gt;deepcopy&lt;/code&gt; is given a true value, the returned list is a deep copy. New option in Robot Framework 3.1.2.&lt;/p&gt;
&lt;p&gt;The given list is never altered by this keyword.&lt;/p&gt;</doc>
<shortdoc>Returns a copy of the given list.</shortdoc>
</kw>
<kw name="Count Values In List" lineno="227">
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
<doc>&lt;p&gt;Returns the number of occurrences of the given &lt;code&gt;value&lt;/code&gt; in &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The search can be narrowed to the selected sublist by the &lt;code&gt;start&lt;/code&gt; and &lt;code&gt;end&lt;/code&gt; indexes having the same semantics as with &lt;a href="#Get%20Slice%20From%20List" class="name"&gt;Get Slice From List&lt;/a&gt; keyword. The given list is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Count Values In List&lt;/td&gt;
&lt;td&gt;${L3}&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} = 1
${L3} is not changed
&lt;/pre&gt;</doc>
<shortdoc>Returns the number of occurrences of the given ``value`` in ``list``.</shortdoc>
</kw>
<kw name="Dictionaries Should Be Equal" lineno="740">
<arguments repr="dict1, dict2, msg=None, values=True">
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
</arguments>
<doc>&lt;p&gt;Fails if the given dictionaries are not equal.&lt;/p&gt;
&lt;p&gt;First the equality of dictionaries' keys is checked and after that all the key value pairs. If there are differences between the values, those are listed in the error message. The types of the dictionaries do not need to be same.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Lists%20Should%20Be%20Equal" class="name"&gt;Lists Should Be Equal&lt;/a&gt; for more information about configuring the error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt; arguments.&lt;/p&gt;</doc>
<shortdoc>Fails if the given dictionaries are not equal.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Item" lineno="709">
<arguments repr="dictionary, key, value, msg=None">
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
</arguments>
<doc>&lt;p&gt;An item of &lt;code&gt;key&lt;/code&gt; / &lt;code&gt;value&lt;/code&gt; must be found in a &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Value is converted to unicode for comparison.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>An item of ``key`` / ``value`` must be found in a ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Key" lineno="691">
<arguments repr="dictionary, key, msg=None">
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
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;key&lt;/code&gt; is not found from &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if ``key`` is not found from ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Sub Dictionary" lineno="756">
<arguments repr="dict1, dict2, msg=None, values=True">
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
</arguments>
<doc>&lt;p&gt;Fails unless all items in &lt;code&gt;dict2&lt;/code&gt; are found from &lt;code&gt;dict1&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Lists%20Should%20Be%20Equal" class="name"&gt;Lists Should Be Equal&lt;/a&gt; for more information about configuring the error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt; arguments.&lt;/p&gt;</doc>
<shortdoc>Fails unless all items in ``dict2`` are found from ``dict1``.</shortdoc>
</kw>
<kw name="Dictionary Should Contain Value" lineno="722">
<arguments repr="dictionary, value, msg=None">
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
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;value&lt;/code&gt; is not found from &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if ``value`` is not found from ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Not Contain Key" lineno="700">
<arguments repr="dictionary, key, msg=None">
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
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;key&lt;/code&gt; is found from &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if ``key`` is found from ``dictionary``.</shortdoc>
</kw>
<kw name="Dictionary Should Not Contain Value" lineno="731">
<arguments repr="dictionary, value, msg=None">
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
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;value&lt;/code&gt; is found from &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if ``value`` is found from ``dictionary``.</shortdoc>
</kw>
<kw name="Get Dictionary Items" lineno="643">
<arguments repr="dictionary, sort_keys=True">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="sort_keys=True">
<name>sort_keys</name>
<default>True</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns items of the given &lt;code&gt;dictionary&lt;/code&gt; as a list.&lt;/p&gt;
&lt;p&gt;Uses &lt;a href="#Get%20Dictionary%20Keys" class="name"&gt;Get Dictionary Keys&lt;/a&gt; to get keys and then returns corresponding items. By default keys are sorted and items returned in that order, but this can be changed by giving &lt;code&gt;sort_keys&lt;/code&gt; a false value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). Notice that with Python 3.5 and earlier dictionary order is undefined unless using ordered dictionaries.&lt;/p&gt;
&lt;p&gt;Items are returned as a flat list so that first item is a key, second item is a corresponding value, third item is the second key, and so on.&lt;/p&gt;
&lt;p&gt;The given &lt;code&gt;dictionary&lt;/code&gt; is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${sorted} =&lt;/td&gt;
&lt;td&gt;Get Dictionary Items&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${unsorted} =&lt;/td&gt;
&lt;td&gt;Get Dictionary Items&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;sort_keys=False&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${sorted} = ['a', 1, 'b', 2, 'c', 3]
${unsorted} = ['b', 2, 'a', 1, 'c', 3]    # Order depends on Python version.
&lt;/pre&gt;
&lt;p&gt;&lt;code&gt;sort_keys&lt;/code&gt; is a new option in Robot Framework 3.1.2. Earlier items were always sorted based on keys.&lt;/p&gt;</doc>
<shortdoc>Returns items of the given ``dictionary`` as a list.</shortdoc>
</kw>
<kw name="Get Dictionary Keys" lineno="588">
<arguments repr="dictionary, sort_keys=True">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="sort_keys=True">
<name>sort_keys</name>
<default>True</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns keys of the given &lt;code&gt;dictionary&lt;/code&gt; as a list.&lt;/p&gt;
&lt;p&gt;By default keys are returned in sorted order (assuming they are sortable), but they can be returned in the original order by giving &lt;code&gt;sort_keys&lt;/code&gt;  a false value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). Notice that with Python 3.5 and earlier dictionary order is undefined unless using ordered dictionaries.&lt;/p&gt;
&lt;p&gt;The given &lt;code&gt;dictionary&lt;/code&gt; is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${sorted} =&lt;/td&gt;
&lt;td&gt;Get Dictionary Keys&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${unsorted} =&lt;/td&gt;
&lt;td&gt;Get Dictionary Keys&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;sort_keys=False&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${sorted} = ['a', 'b', 'c']
${unsorted} = ['b', 'a', 'c']   # Order depends on Python version.
&lt;/pre&gt;
&lt;p&gt;&lt;code&gt;sort_keys&lt;/code&gt; is a new option in Robot Framework 3.1.2. Earlier keys were always sorted.&lt;/p&gt;</doc>
<shortdoc>Returns keys of the given ``dictionary`` as a list.</shortdoc>
</kw>
<kw name="Get Dictionary Values" lineno="618">
<arguments repr="dictionary, sort_keys=True">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="sort_keys=True">
<name>sort_keys</name>
<default>True</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns values of the given &lt;code&gt;dictionary&lt;/code&gt; as a list.&lt;/p&gt;
&lt;p&gt;Uses &lt;a href="#Get%20Dictionary%20Keys" class="name"&gt;Get Dictionary Keys&lt;/a&gt; to get keys and then returns corresponding values. By default keys are sorted and values returned in that order, but this can be changed by giving &lt;code&gt;sort_keys&lt;/code&gt; a false value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). Notice that with Python 3.5 and earlier dictionary order is undefined unless using ordered dictionaries.&lt;/p&gt;
&lt;p&gt;The given &lt;code&gt;dictionary&lt;/code&gt; is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${sorted} =&lt;/td&gt;
&lt;td&gt;Get Dictionary Values&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${unsorted} =&lt;/td&gt;
&lt;td&gt;Get Dictionary Values&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;sort_keys=False&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${sorted} = [1, 2, 3]
${unsorted} = [2, 1, 3]    # Order depends on Python version.
&lt;/pre&gt;
&lt;p&gt;&lt;code&gt;sort_keys&lt;/code&gt; is a new option in Robot Framework 3.1.2. Earlier values were always sorted based on keys.&lt;/p&gt;</doc>
<shortdoc>Returns values of the given ``dictionary`` as a list.</shortdoc>
</kw>
<kw name="Get From Dictionary" lineno="672">
<arguments repr="dictionary, key">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="key">
<name>key</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a value from the given &lt;code&gt;dictionary&lt;/code&gt; based on the given &lt;code&gt;key&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If the given &lt;code&gt;key&lt;/code&gt; cannot be found from the &lt;code&gt;dictionary&lt;/code&gt;, this keyword fails.&lt;/p&gt;
&lt;p&gt;The given dictionary is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${value} =&lt;/td&gt;
&lt;td&gt;Get From Dictionary&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${value} = 2
&lt;/pre&gt;</doc>
<shortdoc>Returns a value from the given ``dictionary`` based on the given ``key``.</shortdoc>
</kw>
<kw name="Get From List" lineno="172">
<arguments repr="list_, index">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index">
<name>index</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the value specified with an &lt;code&gt;index&lt;/code&gt; from &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The given list is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Index &lt;code&gt;0&lt;/code&gt; means the first position, &lt;code&gt;1&lt;/code&gt; the second, and so on. Similarly, &lt;code&gt;-1&lt;/code&gt; is the last position, &lt;code&gt;-2&lt;/code&gt; the second last, and so on. Using an index that does not exist on the list causes an error. The index can be either an integer or a string that can be converted to an integer.&lt;/p&gt;
&lt;p&gt;Examples (including Python equivalents in comments):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Get From List&lt;/td&gt;
&lt;td&gt;${L5}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;td&gt;# L5[0]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${y} =&lt;/td&gt;
&lt;td&gt;Get From List&lt;/td&gt;
&lt;td&gt;${L5}&lt;/td&gt;
&lt;td&gt;-2&lt;/td&gt;
&lt;td&gt;# L5[-2]&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} = 'a'
${y} = 'd'
${L5} is not changed
&lt;/pre&gt;</doc>
<shortdoc>Returns the value specified with an ``index`` from ``list``.</shortdoc>
</kw>
<kw name="Get Index From List" lineno="243">
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
<doc>&lt;p&gt;Returns the index of the first occurrence of the &lt;code&gt;value&lt;/code&gt; on the list.&lt;/p&gt;
&lt;p&gt;The search can be narrowed to the selected sublist by the &lt;code&gt;start&lt;/code&gt; and &lt;code&gt;end&lt;/code&gt; indexes having the same semantics as with &lt;a href="#Get%20Slice%20From%20List" class="name"&gt;Get Slice From List&lt;/a&gt; keyword. In case the value is not found, -1 is returned. The given list is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Get Index From List&lt;/td&gt;
&lt;td&gt;${L5}&lt;/td&gt;
&lt;td&gt;d&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} = 3
${L5} is not changed
&lt;/pre&gt;</doc>
<shortdoc>Returns the index of the first occurrence of the ``value`` on the list.</shortdoc>
</kw>
<kw name="Get Match Count" lineno="984">
<arguments repr="list, pattern, case_insensitive=False, whitespace_insensitive=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list">
<name>list</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive=False">
<name>case_insensitive</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive=False">
<name>whitespace_insensitive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the count of matches to &lt;code&gt;pattern&lt;/code&gt; in &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;For more information on &lt;code&gt;pattern&lt;/code&gt;, &lt;code&gt;case_insensitive&lt;/code&gt;, and &lt;code&gt;whitespace_insensitive&lt;/code&gt;, see &lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${count}=&lt;/td&gt;
&lt;td&gt;Get Match Count&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;a*&lt;/td&gt;
&lt;td&gt;# ${count} will be the count of strings beginning with 'a'&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${count}=&lt;/td&gt;
&lt;td&gt;Get Match Count&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;regexp=a.*&lt;/td&gt;
&lt;td&gt;# ${matches} will be the count of strings beginning with 'a' (regexp version)&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${count}=&lt;/td&gt;
&lt;td&gt;Get Match Count&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;a*&lt;/td&gt;
&lt;td&gt;case_insensitive=${True}&lt;/td&gt;
&lt;td&gt;# ${matches} will be the count of strings beginning with 'a' or 'A'&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns the count of matches to ``pattern`` in ``list``.</shortdoc>
</kw>
<kw name="Get Matches" lineno="968">
<arguments repr="list, pattern, case_insensitive=False, whitespace_insensitive=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list">
<name>list</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive=False">
<name>case_insensitive</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive=False">
<name>whitespace_insensitive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a list of matches to &lt;code&gt;pattern&lt;/code&gt; in &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;For more information on &lt;code&gt;pattern&lt;/code&gt;, &lt;code&gt;case_insensitive&lt;/code&gt;, and &lt;code&gt;whitespace_insensitive&lt;/code&gt;, see &lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${matches}=&lt;/td&gt;
&lt;td&gt;Get Matches&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;a*&lt;/td&gt;
&lt;td&gt;# ${matches} will contain any string beginning with 'a'&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${matches}=&lt;/td&gt;
&lt;td&gt;Get Matches&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;regexp=a.*&lt;/td&gt;
&lt;td&gt;# ${matches} will contain any string beginning with 'a' (regexp version)&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${matches}=&lt;/td&gt;
&lt;td&gt;Get Matches&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;a*&lt;/td&gt;
&lt;td&gt;case_insensitive=${True}&lt;/td&gt;
&lt;td&gt;# ${matches} will contain any string beginning with 'a' or 'A'&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns a list of matches to ``pattern`` in ``list``.</shortdoc>
</kw>
<kw name="Get Slice From List" lineno="197">
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
<doc>&lt;p&gt;Returns a slice of the given list between &lt;code&gt;start&lt;/code&gt; and &lt;code&gt;end&lt;/code&gt; indexes.&lt;/p&gt;
&lt;p&gt;The given list is never altered by this keyword.&lt;/p&gt;
&lt;p&gt;If both &lt;code&gt;start&lt;/code&gt; and &lt;code&gt;end&lt;/code&gt; are given, a sublist containing values from &lt;code&gt;start&lt;/code&gt; to &lt;code&gt;end&lt;/code&gt; is returned. This is the same as &lt;code&gt;list[start:end]&lt;/code&gt; in Python. To get all items from the beginning, use 0 as the start value, and to get all items until and including the end, use &lt;code&gt;None&lt;/code&gt; (default) as the end value.&lt;/p&gt;
&lt;p&gt;Using &lt;code&gt;start&lt;/code&gt; or &lt;code&gt;end&lt;/code&gt; not found on the list is the same as using the largest (or smallest) available index.&lt;/p&gt;
&lt;p&gt;Examples (incl. Python equivalents in comments):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Get Slice From List&lt;/td&gt;
&lt;td&gt;${L5}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;4&lt;/td&gt;
&lt;td&gt;# L5[2:4]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${y} =&lt;/td&gt;
&lt;td&gt;Get Slice From List&lt;/td&gt;
&lt;td&gt;${L5}&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# L5[1:None]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${z} =&lt;/td&gt;
&lt;td&gt;Get Slice From List&lt;/td&gt;
&lt;td&gt;${L5}&lt;/td&gt;
&lt;td&gt;end=-2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# L5[0:-2]&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} = ['c', 'd']
${y} = ['b', 'c', 'd', 'e']
${z} = ['a', 'b', 'c']
${L5} is not changed
&lt;/pre&gt;</doc>
<shortdoc>Returns a slice of the given list between ``start`` and ``end`` indexes.</shortdoc>
</kw>
<kw name="Insert Into List" lineno="55">
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
<doc>&lt;p&gt;Inserts &lt;code&gt;value&lt;/code&gt; into &lt;code&gt;list&lt;/code&gt; to the position specified with &lt;code&gt;index&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Index &lt;code&gt;0&lt;/code&gt; adds the value into the first position, &lt;code&gt;1&lt;/code&gt; to the second, and so on. Inserting from right works with negative indices so that &lt;code&gt;-1&lt;/code&gt; is the second last position, &lt;code&gt;-2&lt;/code&gt; third last, and so on. Use &lt;a href="#Append%20To%20List" class="name"&gt;Append To List&lt;/a&gt; to add items to the end of the list.&lt;/p&gt;
&lt;p&gt;If the absolute value of the index is greater than the length of the list, the value is added at the end (positive index) or the beginning (negative index). An index can be given either as an integer or a string that can be converted to an integer.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Insert Into List&lt;/td&gt;
&lt;td&gt;${L1}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Insert Into List&lt;/td&gt;
&lt;td&gt;${L2}&lt;/td&gt;
&lt;td&gt;${-1}&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${L1} = ['xxx', 'a']
${L2} = ['a', 'xxx', 'b']
&lt;/pre&gt;</doc>
<shortdoc>Inserts ``value`` into ``list`` to the position specified with ``index``.</shortdoc>
</kw>
<kw name="Keep In Dictionary" lineno="556">
<arguments repr="dictionary, *keys">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*keys">
<name>keys</name>
</arg>
</arguments>
<doc>&lt;p&gt;Keeps the given &lt;code&gt;keys&lt;/code&gt; in the &lt;code&gt;dictionary&lt;/code&gt; and removes all other.&lt;/p&gt;
&lt;p&gt;If the given &lt;code&gt;key&lt;/code&gt; cannot be found from the &lt;code&gt;dictionary&lt;/code&gt;, it is ignored.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Keep In Dictionary&lt;/td&gt;
&lt;td&gt;${D5}&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;td&gt;x&lt;/td&gt;
&lt;td&gt;d&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${D5} = {'b': 2, 'd': 4}
&lt;/pre&gt;</doc>
<shortdoc>Keeps the given ``keys`` in the ``dictionary`` and removes all other.</shortdoc>
</kw>
<kw name="List Should Contain Sub List" lineno="421">
<arguments repr="list1, list2, msg=None, values=True">
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
</arguments>
<doc>&lt;p&gt;Fails if not all of the elements in &lt;code&gt;list2&lt;/code&gt; are found in &lt;code&gt;list1&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The order of values and the number of values are not taken into account.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Lists%20Should%20Be%20Equal" class="name"&gt;Lists Should Be Equal&lt;/a&gt; for more information about configuring the error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt; arguments.&lt;/p&gt;</doc>
<shortdoc>Fails if not all of the elements in ``list2`` are found in ``list1``.</shortdoc>
</kw>
<kw name="List Should Contain Value" lineno="305">
<arguments repr="list_, value, msg=None">
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
</arguments>
<doc>&lt;p&gt;Fails if the &lt;code&gt;value&lt;/code&gt; is not found from &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if the ``value`` is not found from ``list``.</shortdoc>
</kw>
<kw name="List Should Not Contain Duplicates" lineno="323">
<arguments repr="list_, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if any element in the &lt;code&gt;list&lt;/code&gt; is found from it more than once.&lt;/p&gt;
&lt;p&gt;The default error message lists all the elements that were found from the &lt;code&gt;list&lt;/code&gt; multiple times, but it can be overridden by giving a custom &lt;code&gt;msg&lt;/code&gt;. All multiple times found items and their counts are also logged.&lt;/p&gt;
&lt;p&gt;This keyword works with all iterables that can be converted to a list. The original iterable is never altered.&lt;/p&gt;</doc>
<shortdoc>Fails if any element in the ``list`` is found from it more than once.</shortdoc>
</kw>
<kw name="List Should Not Contain Value" lineno="314">
<arguments repr="list_, value, msg=None">
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
</arguments>
<doc>&lt;p&gt;Fails if the &lt;code&gt;value&lt;/code&gt; is found from &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if the ``value`` is found from ``list``.</shortdoc>
</kw>
<kw name="Lists Should Be Equal" lineno="348">
<arguments repr="list1, list2, msg=None, values=True, names=None, ignore_order=False">
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
</arguments>
<doc>&lt;p&gt;Fails if given lists are unequal.&lt;/p&gt;
&lt;p&gt;The keyword first verifies that the lists have equal lengths, and then it checks are all their values equal. Possible differences between the values are listed in the default error message like &lt;code&gt;Index 4: ABC != Abc&lt;/code&gt;. The types of the lists do not need to be the same. For example, Python tuple and list with same content are considered equal.&lt;/p&gt;
&lt;p&gt;The error message can be configured using &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt; arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;If &lt;code&gt;msg&lt;/code&gt; is not given, the default error message is used.&lt;/li&gt;
&lt;li&gt;If &lt;code&gt;msg&lt;/code&gt; is given and &lt;code&gt;values&lt;/code&gt; gets a value considered true (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the error message starts with the given &lt;code&gt;msg&lt;/code&gt; followed by a newline and the default message.&lt;/li&gt;
&lt;li&gt;If &lt;code&gt;msg&lt;/code&gt; is given and &lt;code&gt;values&lt;/code&gt;  is not given a true value, the error message is just the given &lt;code&gt;msg&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;The optional &lt;code&gt;names&lt;/code&gt; argument can be used for naming the indices shown in the default error message. It can either be a list of names matching the indices in the lists or a dictionary where keys are indices that need to be named. It is not necessary to name all of the indices.  When using a dictionary, keys can be either integers or strings that can be converted to integers.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${names} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;First Name&lt;/td&gt;
&lt;td&gt;Family Name&lt;/td&gt;
&lt;td&gt;Email&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Lists Should Be Equal&lt;/td&gt;
&lt;td&gt;${people1}&lt;/td&gt;
&lt;td&gt;${people2}&lt;/td&gt;
&lt;td&gt;names=${names}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${names} =&lt;/td&gt;
&lt;td&gt;Create Dictionary&lt;/td&gt;
&lt;td&gt;0=First Name&lt;/td&gt;
&lt;td&gt;2=Email&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Lists Should Be Equal&lt;/td&gt;
&lt;td&gt;${people1}&lt;/td&gt;
&lt;td&gt;${people2}&lt;/td&gt;
&lt;td&gt;names=${names}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;If the items in index 2 would differ in the above examples, the error message would contain a row like &lt;code&gt;Index 2 (email): name@foo.com != name@bar.com&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The optional &lt;code&gt;ignore_order&lt;/code&gt; argument can be used to ignore the order of the elements in the lists. Using it requires items to be sortable. This is new in Robot Framework 3.2.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${list1} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;apple&lt;/td&gt;
&lt;td&gt;cherry&lt;/td&gt;
&lt;td&gt;banana&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${list2} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;cherry&lt;/td&gt;
&lt;td&gt;banana&lt;/td&gt;
&lt;td&gt;apple&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Lists Should Be Equal&lt;/td&gt;
&lt;td&gt;${list1}&lt;/td&gt;
&lt;td&gt;${list2}&lt;/td&gt;
&lt;td&gt;ignore_order=True&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Fails if given lists are unequal.</shortdoc>
</kw>
<kw name="Log Dictionary" lineno="772">
<arguments repr="dictionary, level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs the size and contents of the &lt;code&gt;dictionary&lt;/code&gt; using given &lt;code&gt;level&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Valid levels are TRACE, DEBUG, INFO (default), and WARN.&lt;/p&gt;
&lt;p&gt;If you only want to log the size, use keyword &lt;span class="name"&gt;Get Length&lt;/span&gt; from the BuiltIn library.&lt;/p&gt;</doc>
<shortdoc>Logs the size and contents of the ``dictionary`` using given ``level``.</shortdoc>
</kw>
<kw name="Log List" lineno="435">
<arguments repr="list_, level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs the length and contents of the &lt;code&gt;list&lt;/code&gt; using given &lt;code&gt;level&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Valid levels are TRACE, DEBUG, INFO (default), and WARN.&lt;/p&gt;
&lt;p&gt;If you only want to the length, use keyword &lt;span class="name"&gt;Get Length&lt;/span&gt; from the BuiltIn library.&lt;/p&gt;</doc>
<shortdoc>Logs the length and contents of the ``list`` using given ``level``.</shortdoc>
</kw>
<kw name="Pop From Dictionary" lineno="537">
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
<doc>&lt;p&gt;Pops the given &lt;code&gt;key&lt;/code&gt; from the &lt;code&gt;dictionary&lt;/code&gt; and returns its value.&lt;/p&gt;
&lt;p&gt;By default the keyword fails if the given &lt;code&gt;key&lt;/code&gt; cannot be found from the &lt;code&gt;dictionary&lt;/code&gt;. If optional &lt;code&gt;default&lt;/code&gt; value is given, it will be returned instead of failing.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${val}=&lt;/td&gt;
&lt;td&gt;Pop From Dictionary&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${val} = 2
${D3} = {'a': 1, 'c': 3}
&lt;/pre&gt;</doc>
<shortdoc>Pops the given ``key`` from the ``dictionary`` and returns its value.</shortdoc>
</kw>
<kw name="Remove Duplicates" lineno="155">
<arguments repr="list_">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a list without duplicates based on the given &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Creates and returns a new list that contains all items in the given list so that one item can appear only once. Order of the items in the new list is the same as in the original except for missing duplicates. Number of the removed duplicates is logged.&lt;/p&gt;</doc>
<shortdoc>Returns a list without duplicates based on the given ``list``.</shortdoc>
</kw>
<kw name="Remove From Dictionary" lineno="518">
<arguments repr="dictionary, *keys">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="dictionary">
<name>dictionary</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*keys">
<name>keys</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes the given &lt;code&gt;keys&lt;/code&gt; from the &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If the given &lt;code&gt;key&lt;/code&gt; cannot be found from the &lt;code&gt;dictionary&lt;/code&gt;, it is ignored.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove From Dictionary&lt;/td&gt;
&lt;td&gt;${D3}&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;td&gt;x&lt;/td&gt;
&lt;td&gt;y&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${D3} = {'a': 1, 'c': 3}
&lt;/pre&gt;</doc>
<shortdoc>Removes the given ``keys`` from the ``dictionary``.</shortdoc>
</kw>
<kw name="Remove From List" lineno="134">
<arguments repr="list_, index">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index">
<name>index</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes and returns the value specified with an &lt;code&gt;index&lt;/code&gt; from &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Index &lt;code&gt;0&lt;/code&gt; means the first position, &lt;code&gt;1&lt;/code&gt; the second and so on. Similarly, &lt;code&gt;-1&lt;/code&gt; is the last position, &lt;code&gt;-2&lt;/code&gt; the second last, and so on. Using an index that does not exist on the list causes an error. The index can be either an integer or a string that can be converted to an integer.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Remove From List&lt;/td&gt;
&lt;td&gt;${L2}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} = 'a'
${L2} = ['b']
&lt;/pre&gt;</doc>
<shortdoc>Removes and returns the value specified with an ``index`` from ``list``.</shortdoc>
</kw>
<kw name="Remove Values From List" lineno="119">
<arguments repr="list_, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes all occurrences of given &lt;code&gt;values&lt;/code&gt; from &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;It is not an error if a value does not exist in the list at all.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Values From List&lt;/td&gt;
&lt;td&gt;${L4}&lt;/td&gt;
&lt;td&gt;a&lt;/td&gt;
&lt;td&gt;c&lt;/td&gt;
&lt;td&gt;e&lt;/td&gt;
&lt;td&gt;f&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${L4} = ['b', 'd']
&lt;/pre&gt;</doc>
<shortdoc>Removes all occurrences of given ``values`` from ``list``.</shortdoc>
</kw>
<kw name="Reverse List" lineno="279">
<arguments repr="list_">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
</arguments>
<doc>&lt;p&gt;Reverses the given list in place.&lt;/p&gt;
&lt;p&gt;Note that the given list is changed and nothing is returned. Use &lt;a href="#Copy%20List" class="name"&gt;Copy List&lt;/a&gt; first, if you need to keep also the original order.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Reverse List&lt;/td&gt;
&lt;td&gt;${L3}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${L3} = ['c', 'b', 'a']
&lt;/pre&gt;</doc>
<shortdoc>Reverses the given list in place.</shortdoc>
</kw>
<kw name="Set List Value" lineno="98">
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
<doc>&lt;p&gt;Sets the value of &lt;code&gt;list&lt;/code&gt; specified by &lt;code&gt;index&lt;/code&gt; to the given &lt;code&gt;value&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Index &lt;code&gt;0&lt;/code&gt; means the first position, &lt;code&gt;1&lt;/code&gt; the second and so on. Similarly, &lt;code&gt;-1&lt;/code&gt; is the last position, &lt;code&gt;-2&lt;/code&gt; second last, and so on. Using an index that does not exist on the list causes an error. The index can be either an integer or a string that can be converted to an integer.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set List Value&lt;/td&gt;
&lt;td&gt;${L3}&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set List Value&lt;/td&gt;
&lt;td&gt;${L3}&lt;/td&gt;
&lt;td&gt;-1&lt;/td&gt;
&lt;td&gt;yyy&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${L3} = ['a', 'xxx', 'yyy']
&lt;/pre&gt;</doc>
<shortdoc>Sets the value of ``list`` specified by ``index`` to the given ``value``.</shortdoc>
</kw>
<kw name="Set To Dictionary" lineno="492">
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
<doc>&lt;p&gt;Adds the given &lt;code&gt;key_value_pairs&lt;/code&gt; and &lt;code&gt;items&lt;/code&gt; to the &lt;code&gt;dictionary&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Giving items as &lt;code&gt;key_value_pairs&lt;/code&gt; means giving keys and values as separate arguments:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set To Dictionary&lt;/td&gt;
&lt;td&gt;${D1}&lt;/td&gt;
&lt;td&gt;key&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;second&lt;/td&gt;
&lt;td&gt;${2}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${D1} = {'a': 1, 'key': 'value', 'second': 2}
&lt;/pre&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set To Dictionary&lt;/td&gt;
&lt;td&gt;${D1}&lt;/td&gt;
&lt;td&gt;key=value&lt;/td&gt;
&lt;td&gt;second=${2}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The latter syntax is typically more convenient to use, but it has a limitation that keys must be strings.&lt;/p&gt;
&lt;p&gt;If given keys already exist in the dictionary, their values are updated.&lt;/p&gt;</doc>
<shortdoc>Adds the given ``key_value_pairs`` and ``items`` to the ``dictionary``.</shortdoc>
</kw>
<kw name="Should Contain Match" lineno="908">
<arguments repr="list, pattern, msg=None, case_insensitive=False, whitespace_insensitive=False">
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive=False">
<name>case_insensitive</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive=False">
<name>whitespace_insensitive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;pattern&lt;/code&gt; is not found in &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;By default, pattern matching is similar to matching files in a shell and is case-sensitive and whitespace-sensitive. In the pattern syntax, &lt;code&gt;*&lt;/code&gt; matches to anything and &lt;code&gt;?&lt;/code&gt; matches to any single character. You can also prepend &lt;code&gt;glob=&lt;/code&gt; to your pattern to explicitly use this pattern matching behavior.&lt;/p&gt;
&lt;p&gt;If you prepend &lt;code&gt;regexp=&lt;/code&gt; to your pattern, your pattern will be used according to the Python &lt;a href="http://docs.python.org/library/re.html"&gt;re module&lt;/a&gt; regular expression syntax. Important note: Backslashes are an escape character, and must be escaped with another backslash (e.g. &lt;code&gt;regexp=\\d{6}&lt;/code&gt; to search for &lt;code&gt;\d{6}&lt;/code&gt;). See &lt;span class="name"&gt;BuiltIn.Should Match Regexp&lt;/span&gt; for more details.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;case_insensitive&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the pattern matching will ignore case.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;whitespace_insensitive&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the pattern matching will ignore whitespace.&lt;/p&gt;
&lt;p&gt;Non-string values in lists are ignored when matching patterns.&lt;/p&gt;
&lt;p&gt;Use the &lt;code&gt;msg&lt;/code&gt; argument to override the default error message.&lt;/p&gt;
&lt;p&gt;See also &lt;code&gt;Should Not Contain Match&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Match&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;a*&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Match strings beginning with 'a'.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Match&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;regexp=a.*&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Same as the above but with regexp.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Match&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;regexp=\\d{6}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Match strings containing six digits.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Match&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;a*&lt;/td&gt;
&lt;td&gt;case_insensitive=True&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Match strings beginning with 'a' or 'A'.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Match&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;ab*&lt;/td&gt;
&lt;td&gt;whitespace_insensitive=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Match strings beginning with 'ab' with possible whitespace ignored.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Match&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;ab*&lt;/td&gt;
&lt;td&gt;whitespace_insensitive=true&lt;/td&gt;
&lt;td&gt;case_insensitive=true&lt;/td&gt;
&lt;td&gt;# Same as the above but also ignore case.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Fails if ``pattern`` is not found in ``list``.</shortdoc>
</kw>
<kw name="Should Not Contain Match" lineno="953">
<arguments repr="list, pattern, msg=None, case_insensitive=False, whitespace_insensitive=False">
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive=False">
<name>case_insensitive</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="whitespace_insensitive=False">
<name>whitespace_insensitive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;pattern&lt;/code&gt; is found in &lt;code&gt;list&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Exact opposite of &lt;a href="#Should%20Contain%20Match" class="name"&gt;Should Contain Match&lt;/a&gt; keyword. See that keyword for information about arguments and usage in general.&lt;/p&gt;</doc>
<shortdoc>Fails if ``pattern`` is found in ``list``.</shortdoc>
</kw>
<kw name="Sort List" lineno="292">
<arguments repr="list_">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="list_">
<name>list_</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sorts the given list in place.&lt;/p&gt;
&lt;p&gt;Sorting fails if items in the list are not comparable with each others. On Python 2 most objects are comparable, but on Python 3 comparing, for example, strings with numbers is not possible.&lt;/p&gt;
&lt;p&gt;Note that the given list is changed and nothing is returned. Use &lt;a href="#Copy%20List" class="name"&gt;Copy List&lt;/a&gt; first, if you need to keep also the original order.&lt;/p&gt;</doc>
<shortdoc>Sorts the given list in place.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
