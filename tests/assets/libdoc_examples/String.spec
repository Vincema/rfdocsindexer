<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="String" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2021-08-18T02:53:35Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/String.py" lineno="32">
<version>4.1</version>
<doc>&lt;p&gt;A test library for string manipulation and verification.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;String&lt;/code&gt; is Robot Framework's standard library for manipulating strings (e.g. &lt;a href="#Replace%20String%20Using%20Regexp" class="name"&gt;Replace String Using Regexp&lt;/a&gt;, &lt;a href="#Split%20To%20Lines" class="name"&gt;Split To Lines&lt;/a&gt;) and verifying their contents (e.g. &lt;a href="#Should%20Be%20String" class="name"&gt;Should Be String&lt;/a&gt;).&lt;/p&gt;
&lt;p&gt;Following keywords from &lt;code&gt;BuiltIn&lt;/code&gt; library can also be used with strings:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;span class="name"&gt;Catenate&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Get Length&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Length Should Be&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Should (Not) Be Empty&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Should (Not) Be Equal (As Strings/Integers/Numbers)&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Should (Not) Match (Regexp)&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Should (Not) Contain&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Should (Not) Start With&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Should (Not) End With&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Convert To String&lt;/span&gt;&lt;/li&gt;
&lt;li&gt;&lt;span class="name"&gt;Convert To Bytes&lt;/span&gt;&lt;/li&gt;
&lt;/ul&gt;</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Convert To Lower Case" lineno="56">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>&lt;p&gt;Converts string to lower case.&lt;/p&gt;
&lt;p&gt;Uses Python's standard &lt;a href="https://docs.python.org/library/stdtypes.html#str.lower"&gt;lower()&lt;/a&gt; method.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str1} =&lt;/td&gt;
&lt;td&gt;Convert To Lower Case&lt;/td&gt;
&lt;td&gt;ABC&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str2} =&lt;/td&gt;
&lt;td&gt;Convert To Lower Case&lt;/td&gt;
&lt;td&gt;1A2c3D&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str1}&lt;/td&gt;
&lt;td&gt;abc&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str2}&lt;/td&gt;
&lt;td&gt;1a2c3d&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Converts string to lower case.</shortdoc>
</kw>
<kw name="Convert To Title Case" lineno="89">
<arguments repr="string, exclude=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude=None">
<name>exclude</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Converts string to title case.&lt;/p&gt;
&lt;p&gt;Uses the following algorithm:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Split the string to words from whitespace characters (spaces, newlines, etc.).&lt;/li&gt;
&lt;li&gt;Exclude words that are not all lower case. This preserves, for example, "OK" and "iPhone".&lt;/li&gt;
&lt;li&gt;Exclude also words listed in the optional &lt;code&gt;exclude&lt;/code&gt; argument.&lt;/li&gt;
&lt;li&gt;Title case the first alphabetical character of each word that has not been excluded.&lt;/li&gt;
&lt;li&gt;Join all words together so that original whitespace is preserved.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Explicitly excluded words can be given as a list or as a string with words separated by a comma and an optional space. Excluded words are actually considered to be regular expression patterns, so it is possible to use something like "example[.!?]?" to match the word "example" on it own and also if followed by ".", "!" or "?". See &lt;span class="name"&gt;BuiltIn.Should Match Regexp&lt;/span&gt; for more information about Python regular expression syntax in general and how to use it in Robot Framework test data in particular.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str1} =&lt;/td&gt;
&lt;td&gt;Convert To Title Case&lt;/td&gt;
&lt;td&gt;hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str2} =&lt;/td&gt;
&lt;td&gt;Convert To Title Case&lt;/td&gt;
&lt;td&gt;it's an OK iPhone&lt;/td&gt;
&lt;td&gt;exclude=a, an, the&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str3} =&lt;/td&gt;
&lt;td&gt;Convert To Title Case&lt;/td&gt;
&lt;td&gt;distance is 1 km.&lt;/td&gt;
&lt;td&gt;exclude=is, km.?&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str1}&lt;/td&gt;
&lt;td&gt;Hello, World!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str2}&lt;/td&gt;
&lt;td&gt;It's an OK iPhone&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str3}&lt;/td&gt;
&lt;td&gt;Distance is 1 km.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The reason this keyword does not use Python's standard &lt;a href="https://docs.python.org/library/stdtypes.html#str.title"&gt;title()&lt;/a&gt; method is that it can yield undesired results, for example, if strings contain upper case letters or special characters like apostrophes. It would, for example, convert "it's an OK iPhone" to "It'S An Ok Iphone".&lt;/p&gt;
&lt;p&gt;New in Robot Framework 3.2.&lt;/p&gt;</doc>
<shortdoc>Converts string to title case.</shortdoc>
</kw>
<kw name="Convert To Upper Case" lineno="73">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>&lt;p&gt;Converts string to upper case.&lt;/p&gt;
&lt;p&gt;Uses Python's standard &lt;a href="https://docs.python.org/library/stdtypes.html#str.upper"&gt;upper()&lt;/a&gt; method.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str1} =&lt;/td&gt;
&lt;td&gt;Convert To Upper Case&lt;/td&gt;
&lt;td&gt;abc&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str2} =&lt;/td&gt;
&lt;td&gt;Convert To Upper Case&lt;/td&gt;
&lt;td&gt;1a2C3d&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str1}&lt;/td&gt;
&lt;td&gt;ABC&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str2}&lt;/td&gt;
&lt;td&gt;1A2C3D&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Converts string to upper case.</shortdoc>
</kw>
<kw name="Decode Bytes To String" lineno="171">
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
<doc>&lt;p&gt;Decodes the given &lt;code&gt;bytes&lt;/code&gt; to a Unicode string using the given &lt;code&gt;encoding&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;errors&lt;/code&gt; argument controls what to do if decoding some bytes fails. All values accepted by &lt;code&gt;decode&lt;/code&gt; method in Python are valid, but in practice the following values are most useful:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;strict&lt;/code&gt;: fail if characters cannot be decoded (default)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;ignore&lt;/code&gt;: ignore characters that cannot be decoded&lt;/li&gt;
&lt;li&gt;&lt;code&gt;replace&lt;/code&gt;: replace characters that cannot be decoded with a replacement character&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${string} =&lt;/td&gt;
&lt;td&gt;Decode Bytes To String&lt;/td&gt;
&lt;td&gt;${bytes}&lt;/td&gt;
&lt;td&gt;UTF-8&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${string} =&lt;/td&gt;
&lt;td&gt;Decode Bytes To String&lt;/td&gt;
&lt;td&gt;${bytes}&lt;/td&gt;
&lt;td&gt;ASCII&lt;/td&gt;
&lt;td&gt;errors=ignore&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Encode%20String%20To%20Bytes" class="name"&gt;Encode String To Bytes&lt;/a&gt; if you need to convert Unicode strings to byte strings, and &lt;span class="name"&gt;Convert To String&lt;/span&gt; in &lt;code&gt;BuiltIn&lt;/code&gt; if you need to convert arbitrary objects to Unicode strings.&lt;/p&gt;</doc>
<shortdoc>Decodes the given ``bytes`` to a Unicode string using the given ``encoding``.</shortdoc>
</kw>
<kw name="Encode String To Bytes" lineno="148">
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
<doc>&lt;p&gt;Encodes the given Unicode &lt;code&gt;string&lt;/code&gt; to bytes using the given &lt;code&gt;encoding&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;errors&lt;/code&gt; argument controls what to do if encoding some characters fails. All values accepted by &lt;code&gt;encode&lt;/code&gt; method in Python are valid, but in practice the following values are most useful:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;strict&lt;/code&gt;: fail if characters cannot be encoded (default)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;ignore&lt;/code&gt;: ignore characters that cannot be encoded&lt;/li&gt;
&lt;li&gt;&lt;code&gt;replace&lt;/code&gt;: replace characters that cannot be encoded with a replacement character&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Encode String To Bytes&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;UTF-8&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Encode String To Bytes&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;ASCII&lt;/td&gt;
&lt;td&gt;errors=ignore&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;span class="name"&gt;Convert To Bytes&lt;/span&gt; in &lt;code&gt;BuiltIn&lt;/code&gt; if you want to create bytes based on character or integer sequences. Use &lt;a href="#Decode%20Bytes%20To%20String" class="name"&gt;Decode Bytes To String&lt;/a&gt; if you need to convert byte strings to Unicode strings and &lt;span class="name"&gt;Convert To String&lt;/span&gt; in &lt;code&gt;BuiltIn&lt;/code&gt; if you need to convert arbitrary objects to Unicode.&lt;/p&gt;</doc>
<shortdoc>Encodes the given Unicode ``string`` to bytes using the given ``encoding``.</shortdoc>
</kw>
<kw name="Fetch From Left" lineno="556">
<arguments repr="string, marker">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="marker">
<name>marker</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns contents of the &lt;code&gt;string&lt;/code&gt; before the first occurrence of &lt;code&gt;marker&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If the &lt;code&gt;marker&lt;/code&gt; is not found, whole string is returned.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Fetch%20From%20Right" class="name"&gt;Fetch From Right&lt;/a&gt;, &lt;a href="#Split%20String" class="name"&gt;Split String&lt;/a&gt; and &lt;a href="#Split%20String%20From%20Right" class="name"&gt;Split String From Right&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns contents of the ``string`` before the first occurrence of ``marker``.</shortdoc>
</kw>
<kw name="Fetch From Right" lineno="566">
<arguments repr="string, marker">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="marker">
<name>marker</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns contents of the &lt;code&gt;string&lt;/code&gt; after the last occurrence of &lt;code&gt;marker&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If the &lt;code&gt;marker&lt;/code&gt; is not found, whole string is returned.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Fetch%20From%20Left" class="name"&gt;Fetch From Left&lt;/a&gt;, &lt;a href="#Split%20String" class="name"&gt;Split String&lt;/a&gt; and &lt;a href="#Split%20String%20From%20Right" class="name"&gt;Split String From Right&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns contents of the ``string`` after the last occurrence of ``marker``.</shortdoc>
</kw>
<kw name="Format String" lineno="195">
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
<doc>&lt;p&gt;Formats a &lt;code&gt;template&lt;/code&gt; using the given &lt;code&gt;positional&lt;/code&gt; and &lt;code&gt;named&lt;/code&gt; arguments.&lt;/p&gt;
&lt;p&gt;The template can be either be a string or an absolute path to an existing file. In the latter case the file is read and its contents are used as the template. If the template file contains non-ASCII characters, it must be encoded using UTF-8.&lt;/p&gt;
&lt;p&gt;The template is formatted using Python's &lt;a href="https://docs.python.org/library/string.html#format-string-syntax"&gt;format string syntax&lt;/a&gt;. Placeholders are marked using &lt;code&gt;{}&lt;/code&gt; with possible field name and format specification inside. Literal curly braces can be inserted by doubling them like &lt;span class="name"&gt;{{&lt;/span&gt; and &lt;span class="name"&gt;}}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${to} =&lt;/td&gt;
&lt;td&gt;Format String&lt;/td&gt;
&lt;td&gt;To: {} &amp;lt;{}&amp;gt;&lt;/td&gt;
&lt;td&gt;${user}&lt;/td&gt;
&lt;td&gt;${email}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${to} =&lt;/td&gt;
&lt;td&gt;Format String&lt;/td&gt;
&lt;td&gt;To: {name} &amp;lt;{email}&amp;gt;&lt;/td&gt;
&lt;td&gt;name=${name}&lt;/td&gt;
&lt;td&gt;email=${email}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${to} =&lt;/td&gt;
&lt;td&gt;Format String&lt;/td&gt;
&lt;td&gt;To: {user.name} &amp;lt;{user.email}&amp;gt;&lt;/td&gt;
&lt;td&gt;user=${user}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${xx} =&lt;/td&gt;
&lt;td&gt;Format String&lt;/td&gt;
&lt;td&gt;{:*^30}&lt;/td&gt;
&lt;td&gt;centered&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${yy} =&lt;/td&gt;
&lt;td&gt;Format String&lt;/td&gt;
&lt;td&gt;{0:{width}{base}}&lt;/td&gt;
&lt;td&gt;${42}&lt;/td&gt;
&lt;td&gt;base=X&lt;/td&gt;
&lt;td&gt;width=10&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${zz} =&lt;/td&gt;
&lt;td&gt;Format String&lt;/td&gt;
&lt;td&gt;${CURDIR}/template.txt&lt;/td&gt;
&lt;td&gt;positional&lt;/td&gt;
&lt;td&gt;named=value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;New in Robot Framework 3.1.&lt;/p&gt;</doc>
<shortdoc>Formats a ``template`` using the given ``positional`` and ``named`` arguments.</shortdoc>
</kw>
<kw name="Generate Random String" lineno="576">
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
<doc>&lt;p&gt;Generates a string with a desired &lt;code&gt;length&lt;/code&gt; from the given &lt;code&gt;chars&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The population sequence &lt;code&gt;chars&lt;/code&gt; contains the characters to use when generating the random string. It can contain any characters, and it is possible to use special markers explained in the table below:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Marker&lt;/th&gt;
&lt;th&gt;Explanation&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[LOWER]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Lowercase ASCII characters from &lt;code&gt;a&lt;/code&gt; to &lt;code&gt;z&lt;/code&gt;.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[UPPER]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Uppercase ASCII characters from &lt;code&gt;A&lt;/code&gt; to &lt;code&gt;Z&lt;/code&gt;.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[LETTERS]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Lowercase and uppercase ASCII characters.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[NUMBERS]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Numbers from 0 to 9.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${ret} =&lt;/td&gt;
&lt;td&gt;Generate Random String&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${low} =&lt;/td&gt;
&lt;td&gt;Generate Random String&lt;/td&gt;
&lt;td&gt;12&lt;/td&gt;
&lt;td&gt;[LOWER]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bin} =&lt;/td&gt;
&lt;td&gt;Generate Random String&lt;/td&gt;
&lt;td&gt;8&lt;/td&gt;
&lt;td&gt;01&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${hex} =&lt;/td&gt;
&lt;td&gt;Generate Random String&lt;/td&gt;
&lt;td&gt;4&lt;/td&gt;
&lt;td&gt;[NUMBERS]abcdef&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Generates a string with a desired ``length`` from the given ``chars``.</shortdoc>
</kw>
<kw name="Get Line" lineno="260">
<arguments repr="string, line_number">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="line_number">
<name>line_number</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the specified line from the given &lt;code&gt;string&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Line numbering starts from 0 and it is possible to use negative indices to refer to lines from the end. The line is returned without the newline character.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${first} =&lt;/td&gt;
&lt;td&gt;Get Line&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${2nd last} =&lt;/td&gt;
&lt;td&gt;Get Line&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;-2&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Split%20To%20Lines" class="name"&gt;Split To Lines&lt;/a&gt; if all lines are needed.&lt;/p&gt;</doc>
<shortdoc>Returns the specified line from the given ``string``.</shortdoc>
</kw>
<kw name="Get Line Count" lineno="227">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns and logs the number of lines in the given string.&lt;/p&gt;</doc>
<shortdoc>Returns and logs the number of lines in the given string.</shortdoc>
</kw>
<kw name="Get Lines Containing String" lineno="276">
<arguments repr="string, pattern, case_insensitive=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive=False">
<name>case_insensitive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns lines of the given &lt;code&gt;string&lt;/code&gt; that contain the &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;pattern&lt;/code&gt; is always considered to be a normal string, not a glob or regexp pattern. A line matches if the &lt;code&gt;pattern&lt;/code&gt; is found anywhere on it.&lt;/p&gt;
&lt;p&gt;The match is case-sensitive by default, but giving &lt;code&gt;case_insensitive&lt;/code&gt; a true value makes it case-insensitive. The value is considered true if it is a non-empty string that is not equal to &lt;code&gt;false&lt;/code&gt;, &lt;code&gt;none&lt;/code&gt; or &lt;code&gt;no&lt;/code&gt;. If the value is not a string, its truth value is got directly in Python.&lt;/p&gt;
&lt;p&gt;Lines are returned as one string catenated back together with newlines. Possible trailing newline is never returned. The number of matching lines is automatically logged.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${lines} =&lt;/td&gt;
&lt;td&gt;Get Lines Containing String&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;An example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ret} =&lt;/td&gt;
&lt;td&gt;Get Lines Containing String&lt;/td&gt;
&lt;td&gt;${ret}&lt;/td&gt;
&lt;td&gt;FAIL&lt;/td&gt;
&lt;td&gt;case-insensitive&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Get%20Lines%20Matching%20Pattern" class="name"&gt;Get Lines Matching Pattern&lt;/a&gt; and &lt;a href="#Get%20Lines%20Matching%20Regexp" class="name"&gt;Get Lines Matching Regexp&lt;/a&gt; if you need more complex pattern matching.&lt;/p&gt;</doc>
<shortdoc>Returns lines of the given ``string`` that contain the ``pattern``.</shortdoc>
</kw>
<kw name="Get Lines Matching Pattern" lineno="307">
<arguments repr="string, pattern, case_insensitive=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_insensitive=False">
<name>case_insensitive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns lines of the given &lt;code&gt;string&lt;/code&gt; that match the &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;pattern&lt;/code&gt; is a &lt;i&gt;glob pattern&lt;/i&gt; where:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;*&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches everything&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;?&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches any single character&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[chars]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches any character inside square brackets (e.g. &lt;code&gt;[abc]&lt;/code&gt; matches either &lt;code&gt;a&lt;/code&gt;, &lt;code&gt;b&lt;/code&gt; or &lt;code&gt;c&lt;/code&gt;)&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[!chars]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches any character not inside square brackets&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;A line matches only if it matches the &lt;code&gt;pattern&lt;/code&gt; fully.&lt;/p&gt;
&lt;p&gt;The match is case-sensitive by default, but giving &lt;code&gt;case_insensitive&lt;/code&gt; a true value makes it case-insensitive. The value is considered true if it is a non-empty string that is not equal to &lt;code&gt;false&lt;/code&gt;, &lt;code&gt;none&lt;/code&gt; or &lt;code&gt;no&lt;/code&gt;. If the value is not a string, its truth value is got directly in Python.&lt;/p&gt;
&lt;p&gt;Lines are returned as one string catenated back together with newlines. Possible trailing newline is never returned. The number of matching lines is automatically logged.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${lines} =&lt;/td&gt;
&lt;td&gt;Get Lines Matching Pattern&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;Wild???? example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ret} =&lt;/td&gt;
&lt;td&gt;Get Lines Matching Pattern&lt;/td&gt;
&lt;td&gt;${ret}&lt;/td&gt;
&lt;td&gt;FAIL: *&lt;/td&gt;
&lt;td&gt;case_insensitive=true&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Get%20Lines%20Matching%20Regexp" class="name"&gt;Get Lines Matching Regexp&lt;/a&gt; if you need more complex patterns and &lt;a href="#Get%20Lines%20Containing%20String" class="name"&gt;Get Lines Containing String&lt;/a&gt; if searching literal strings is enough.&lt;/p&gt;</doc>
<shortdoc>Returns lines of the given ``string`` that match the ``pattern``.</shortdoc>
</kw>
<kw name="Get Lines Matching Regexp" lineno="343">
<arguments repr="string, pattern, partial_match=False">
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
</arguments>
<doc>&lt;p&gt;Returns lines of the given &lt;code&gt;string&lt;/code&gt; that match the regexp &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;span class="name"&gt;BuiltIn.Should Match Regexp&lt;/span&gt; for more information about Python regular expression syntax in general and how to use it in Robot Framework test data in particular.&lt;/p&gt;
&lt;p&gt;By default lines match only if they match the pattern fully, but partial matching can be enabled by giving the &lt;code&gt;partial_match&lt;/code&gt; argument a true value. The value is considered true if it is a non-empty string that is not equal to &lt;code&gt;false&lt;/code&gt;, &lt;code&gt;none&lt;/code&gt; or &lt;code&gt;no&lt;/code&gt;. If the value is not a string, its truth value is got directly in Python.&lt;/p&gt;
&lt;p&gt;If the pattern is empty, it matches only empty lines by default. When partial matching is enabled, empty pattern matches all lines.&lt;/p&gt;
&lt;p&gt;Notice that to make the match case-insensitive, you need to prefix the pattern with case-insensitive flag &lt;code&gt;(?i)&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Lines are returned as one string concatenated back together with newlines. Possible trailing newline is never returned. The number of matching lines is automatically logged.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${lines} =&lt;/td&gt;
&lt;td&gt;Get Lines Matching Regexp&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;Reg\\w{3} example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${lines} =&lt;/td&gt;
&lt;td&gt;Get Lines Matching Regexp&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;Reg\\w{3} example&lt;/td&gt;
&lt;td&gt;partial_match=true&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ret} =&lt;/td&gt;
&lt;td&gt;Get Lines Matching Regexp&lt;/td&gt;
&lt;td&gt;${ret}&lt;/td&gt;
&lt;td&gt;(?i)FAIL: .*&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Get%20Lines%20Matching%20Pattern" class="name"&gt;Get Lines Matching Pattern&lt;/a&gt; and &lt;a href="#Get%20Lines%20Containing%20String" class="name"&gt;Get Lines Containing String&lt;/a&gt; if you do not need full regular expression powers (and complexity).&lt;/p&gt;</doc>
<shortdoc>Returns lines of the given ``string`` that match the regexp ``pattern``.</shortdoc>
</kw>
<kw name="Get Regexp Matches" lineno="386">
<arguments repr="string, pattern, *groups">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*groups">
<name>groups</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a list of all non-overlapping matches in the given string.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;string&lt;/code&gt; is the string to find matches from and &lt;code&gt;pattern&lt;/code&gt; is the regular expression. See &lt;span class="name"&gt;BuiltIn.Should Match Regexp&lt;/span&gt; for more information about Python regular expression syntax in general and how to use it in Robot Framework test data in particular.&lt;/p&gt;
&lt;p&gt;If no groups are used, the returned list contains full matches. If one group is used, the list contains only contents of that group. If multiple groups are used, the list contains tuples that contain individual group contents. All groups can be given as indexes (starting from 1) and named groups also as names.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${no match} =&lt;/td&gt;
&lt;td&gt;Get Regexp Matches&lt;/td&gt;
&lt;td&gt;the string&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${matches} =&lt;/td&gt;
&lt;td&gt;Get Regexp Matches&lt;/td&gt;
&lt;td&gt;the string&lt;/td&gt;
&lt;td&gt;t..&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${one group} =&lt;/td&gt;
&lt;td&gt;Get Regexp Matches&lt;/td&gt;
&lt;td&gt;the string&lt;/td&gt;
&lt;td&gt;t(..)&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${named group} =&lt;/td&gt;
&lt;td&gt;Get Regexp Matches&lt;/td&gt;
&lt;td&gt;the string&lt;/td&gt;
&lt;td&gt;t(?P&amp;lt;name&amp;gt;..)&lt;/td&gt;
&lt;td&gt;name&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${two groups} =&lt;/td&gt;
&lt;td&gt;Get Regexp Matches&lt;/td&gt;
&lt;td&gt;the string&lt;/td&gt;
&lt;td&gt;t(.)(.)&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${no match} = []
${matches} = ['the', 'tri']
${one group} = ['he', 'ri']
${named group} = ['he', 'ri']
${two groups} = [('h', 'e'), ('r', 'i')]
&lt;/pre&gt;</doc>
<shortdoc>Returns a list of all non-overlapping matches in the given string.</shortdoc>
</kw>
<kw name="Get Substring" lineno="607">
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
<doc>&lt;p&gt;Returns a substring from &lt;code&gt;start&lt;/code&gt; index to &lt;code&gt;end&lt;/code&gt; index.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;start&lt;/code&gt; index is inclusive and &lt;code&gt;end&lt;/code&gt; is exclusive. Indexing starts from 0, and it is possible to use negative indices to refer to characters from the end.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${ignore first} =&lt;/td&gt;
&lt;td&gt;Get Substring&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ignore last} =&lt;/td&gt;
&lt;td&gt;Get Substring&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;-1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${5th to 10th} =&lt;/td&gt;
&lt;td&gt;Get Substring&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;4&lt;/td&gt;
&lt;td&gt;10&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${first two} =&lt;/td&gt;
&lt;td&gt;Get Substring&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${last two} =&lt;/td&gt;
&lt;td&gt;Get Substring&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;-2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns a substring from ``start`` index to ``end`` index.</shortdoc>
</kw>
<kw name="Remove String" lineno="468">
<arguments repr="string, *removables">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*removables">
<name>removables</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes all &lt;code&gt;removables&lt;/code&gt; from the given &lt;code&gt;string&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;removables&lt;/code&gt; are used as literal strings. Each removable will be matched to a temporary string from which preceding removables have been already removed. See second example below.&lt;/p&gt;
&lt;p&gt;Use &lt;a href="#Remove%20String%20Using%20Regexp" class="name"&gt;Remove String Using Regexp&lt;/a&gt; if more powerful pattern matching is needed. If only a certain number of matches should be removed, &lt;a href="#Replace%20String" class="name"&gt;Replace String&lt;/a&gt; or &lt;a href="#Replace%20String%20Using%20Regexp" class="name"&gt;Replace String Using Regexp&lt;/a&gt; can be used.&lt;/p&gt;
&lt;p&gt;A modified version of the string is returned and the original string is not altered.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str} =&lt;/td&gt;
&lt;td&gt;Remove String&lt;/td&gt;
&lt;td&gt;Robot Framework&lt;/td&gt;
&lt;td&gt;work&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str}&lt;/td&gt;
&lt;td&gt;Robot Frame&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str} =&lt;/td&gt;
&lt;td&gt;Remove String&lt;/td&gt;
&lt;td&gt;Robot Framework&lt;/td&gt;
&lt;td&gt;o&lt;/td&gt;
&lt;td&gt;bt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str}&lt;/td&gt;
&lt;td&gt;R Framewrk&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Removes all ``removables`` from the given ``string``.</shortdoc>
</kw>
<kw name="Remove String Using Regexp" lineno="492">
<arguments repr="string, *patterns">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*patterns">
<name>patterns</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes &lt;code&gt;patterns&lt;/code&gt; from the given &lt;code&gt;string&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword is otherwise identical to &lt;a href="#Remove%20String" class="name"&gt;Remove String&lt;/a&gt;, but the &lt;code&gt;patterns&lt;/code&gt; to search for are considered to be a regular expression. See &lt;a href="#Replace%20String%20Using%20Regexp" class="name"&gt;Replace String Using Regexp&lt;/a&gt; for more information about the regular expression syntax. That keyword can also be used if there is a need to remove only a certain number of occurrences.&lt;/p&gt;</doc>
<shortdoc>Removes ``patterns`` from the given ``string``.</shortdoc>
</kw>
<kw name="Replace String" lineno="423">
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
<doc>&lt;p&gt;Replaces &lt;code&gt;search_for&lt;/code&gt; in the given &lt;code&gt;string&lt;/code&gt; with &lt;code&gt;replace_with&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;search_for&lt;/code&gt; is used as a literal string. See &lt;a href="#Replace%20String%20Using%20Regexp" class="name"&gt;Replace String Using Regexp&lt;/a&gt; if more powerful pattern matching is needed. If you need to just remove a string see &lt;a href="#Remove%20String" class="name"&gt;Remove String&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If the optional argument &lt;code&gt;count&lt;/code&gt; is given, only that many occurrences from left are replaced. Negative &lt;code&gt;count&lt;/code&gt; means that all occurrences are replaced (default behaviour) and zero means that nothing is done.&lt;/p&gt;
&lt;p&gt;A modified version of the string is returned and the original string is not altered.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str} =&lt;/td&gt;
&lt;td&gt;Replace String&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;world&lt;/td&gt;
&lt;td&gt;tellus&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str}&lt;/td&gt;
&lt;td&gt;Hello, tellus!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str} =&lt;/td&gt;
&lt;td&gt;Replace String&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;l&lt;/td&gt;
&lt;td&gt;${EMPTY}&lt;/td&gt;
&lt;td&gt;count=1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${str}&lt;/td&gt;
&lt;td&gt;Helo, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Replaces ``search_for`` in the given ``string`` with ``replace_with``.</shortdoc>
</kw>
<kw name="Replace String Using Regexp" lineno="447">
<arguments repr="string, pattern, replace_with, count=-1">
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
</arguments>
<doc>&lt;p&gt;Replaces &lt;code&gt;pattern&lt;/code&gt; in the given &lt;code&gt;string&lt;/code&gt; with &lt;code&gt;replace_with&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword is otherwise identical to &lt;a href="#Replace%20String" class="name"&gt;Replace String&lt;/a&gt;, but the &lt;code&gt;pattern&lt;/code&gt; to search for is considered to be a regular expression.  See &lt;span class="name"&gt;BuiltIn.Should Match Regexp&lt;/span&gt; for more information about Python regular expression syntax in general and how to use it in Robot Framework test data in particular.&lt;/p&gt;
&lt;p&gt;If you need to just remove a string see &lt;a href="#Remove%20String%20Using%20Regexp" class="name"&gt;Remove String Using Regexp&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str} =&lt;/td&gt;
&lt;td&gt;Replace String Using Regexp&lt;/td&gt;
&lt;td&gt;${str}&lt;/td&gt;
&lt;td&gt;20\\d\\d-\\d\\d-\\d\\d&lt;/td&gt;
&lt;td&gt;&amp;lt;DATE&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str} =&lt;/td&gt;
&lt;td&gt;Replace String Using Regexp&lt;/td&gt;
&lt;td&gt;${str}&lt;/td&gt;
&lt;td&gt;(Hello|Hi)&lt;/td&gt;
&lt;td&gt;${EMPTY}&lt;/td&gt;
&lt;td&gt;count=1&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Replaces ``pattern`` in the given ``string`` with ``replace_with``.</shortdoc>
</kw>
<kw name="Should Be Byte String" lineno="703">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given &lt;code&gt;item&lt;/code&gt; is not a byte string.&lt;/p&gt;
&lt;p&gt;Use &lt;a href="#Should%20Be%20Unicode%20String" class="name"&gt;Should Be Unicode String&lt;/a&gt; if you want to verify the &lt;code&gt;item&lt;/code&gt; is a Unicode string, or &lt;a href="#Should%20Be%20String" class="name"&gt;Should Be String&lt;/a&gt; if both Unicode and byte strings are fine. See &lt;a href="#Should%20Be%20String" class="name"&gt;Should Be String&lt;/a&gt; for more details about Unicode strings and byte strings.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``item`` is not a byte string.</shortdoc>
</kw>
<kw name="Should Be Lower Case" lineno="717">
<arguments repr="string, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given &lt;code&gt;string&lt;/code&gt; is not in lower case.&lt;/p&gt;
&lt;p&gt;For example, &lt;code&gt;'string'&lt;/code&gt; and &lt;code&gt;'with specials!'&lt;/code&gt; would pass, and &lt;code&gt;'String'&lt;/code&gt;, &lt;code&gt;''&lt;/code&gt; and &lt;code&gt;' '&lt;/code&gt; would fail.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Should%20Be%20Upper%20Case" class="name"&gt;Should Be Upper Case&lt;/a&gt; and &lt;a href="#Should%20Be%20Title%20Case" class="name"&gt;Should Be Title Case&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``string`` is not in lower case.</shortdoc>
</kw>
<kw name="Should Be String" lineno="656">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given &lt;code&gt;item&lt;/code&gt; is not a string.&lt;/p&gt;
&lt;p&gt;With Python 2, except with IronPython, this keyword passes regardless is the &lt;code&gt;item&lt;/code&gt; a Unicode string or a byte string. Use &lt;a href="#Should%20Be%20Unicode%20String" class="name"&gt;Should Be Unicode String&lt;/a&gt; or &lt;a href="#Should%20Be%20Byte%20String" class="name"&gt;Should Be Byte String&lt;/a&gt; if you want to restrict the string type. Notice that with Python 2, except with IronPython, &lt;code&gt;'string'&lt;/code&gt; creates a byte string and &lt;code&gt;u'unicode'&lt;/code&gt; must be used to create a Unicode string.&lt;/p&gt;
&lt;p&gt;With Python 3 and IronPython, this keyword passes if the string is a Unicode string but fails if it is bytes. Notice that with both Python 3 and IronPython, &lt;code&gt;'string'&lt;/code&gt; creates a Unicode string, and &lt;code&gt;b'bytes'&lt;/code&gt; must be used to create a byte string.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``item`` is not a string.</shortdoc>
</kw>
<kw name="Should Be Title Case" lineno="746">
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
<doc>&lt;p&gt;Fails if given &lt;code&gt;string&lt;/code&gt; is not title.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;string&lt;/code&gt; is a title cased string if there is at least one upper case letter in each word.&lt;/p&gt;
&lt;p&gt;For example, &lt;code&gt;'This Is Title'&lt;/code&gt; and &lt;code&gt;'OK, Give Me My iPhone'&lt;/code&gt; would pass. &lt;code&gt;'all words lower'&lt;/code&gt; and &lt;code&gt;'Word In lower'&lt;/code&gt; would fail.&lt;/p&gt;
&lt;p&gt;This logic changed in Robot Framework 4.0 to be compatible with &lt;a href="#Convert%20To%20Title%20Case" class="name"&gt;Convert to Title Case&lt;/a&gt;. See &lt;a href="#Convert%20To%20Title%20Case" class="name"&gt;Convert to Title Case&lt;/a&gt; for title case algorithm and reasoning.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Words can be explicitly excluded with the optional &lt;code&gt;exclude&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Explicitly excluded words can be given as a list or as a string with words separated by a comma and an optional space. Excluded words are actually considered to be regular expression patterns, so it is possible to use something like "example[.!?]?" to match the word "example" on it own and also if followed by ".", "!" or "?". See &lt;span class="name"&gt;BuiltIn.Should Match Regexp&lt;/span&gt; for more information about Python regular expression syntax in general and how to use it in Robot Framework test data in particular.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Should%20Be%20Upper%20Case" class="name"&gt;Should Be Upper Case&lt;/a&gt; and &lt;a href="#Should%20Be%20Lower%20Case" class="name"&gt;Should Be Lower Case&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if given ``string`` is not title.</shortdoc>
</kw>
<kw name="Should Be Unicode String" lineno="689">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given &lt;code&gt;item&lt;/code&gt; is not a Unicode string.&lt;/p&gt;
&lt;p&gt;Use &lt;a href="#Should%20Be%20Byte%20String" class="name"&gt;Should Be Byte String&lt;/a&gt; if you want to verify the &lt;code&gt;item&lt;/code&gt; is a byte string, or &lt;a href="#Should%20Be%20String" class="name"&gt;Should Be String&lt;/a&gt; if both Unicode and byte strings are fine. See &lt;a href="#Should%20Be%20String" class="name"&gt;Should Be String&lt;/a&gt; for more details about Unicode strings and byte strings.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``item`` is not a Unicode string.</shortdoc>
</kw>
<kw name="Should Be Upper Case" lineno="731">
<arguments repr="string, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given &lt;code&gt;string&lt;/code&gt; is not in upper case.&lt;/p&gt;
&lt;p&gt;For example, &lt;code&gt;'STRING'&lt;/code&gt; and &lt;code&gt;'WITH SPECIALS!'&lt;/code&gt; would pass, and &lt;code&gt;'String'&lt;/code&gt;, &lt;code&gt;''&lt;/code&gt; and &lt;code&gt;' '&lt;/code&gt; would fail.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Should%20Be%20Title%20Case" class="name"&gt;Should Be Title Case&lt;/a&gt; and &lt;a href="#Should%20Be%20Lower%20Case" class="name"&gt;Should Be Lower Case&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``string`` is not in upper case.</shortdoc>
</kw>
<kw name="Should Not Be String" lineno="677">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given &lt;code&gt;item&lt;/code&gt; is a string.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20String" class="name"&gt;Should Be String&lt;/a&gt; for more details about Unicode strings and byte strings.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the optional &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``item`` is a string.</shortdoc>
</kw>
<kw name="Split String" lineno="507">
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
<doc>&lt;p&gt;Splits the &lt;code&gt;string&lt;/code&gt; using &lt;code&gt;separator&lt;/code&gt; as a delimiter string.&lt;/p&gt;
&lt;p&gt;If a &lt;code&gt;separator&lt;/code&gt; is not given, any whitespace string is a separator. In that case also possible consecutive whitespace as well as leading and trailing whitespace is ignored.&lt;/p&gt;
&lt;p&gt;Split words are returned as a list. If the optional &lt;code&gt;max_split&lt;/code&gt; is given, at most &lt;code&gt;max_split&lt;/code&gt; splits are done, and the returned list will have maximum &lt;code&gt;max_split + 1&lt;/code&gt; elements.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{words} =&lt;/td&gt;
&lt;td&gt;Split String&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{words} =&lt;/td&gt;
&lt;td&gt;Split String&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;,${SPACE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${pre}&lt;/td&gt;
&lt;td&gt;${post} =&lt;/td&gt;
&lt;td&gt;Split String&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;::&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Split%20String%20From%20Right" class="name"&gt;Split String From Right&lt;/a&gt; if you want to start splitting from right, and &lt;a href="#Fetch%20From%20Left" class="name"&gt;Fetch From Left&lt;/a&gt; and &lt;a href="#Fetch%20From%20Right" class="name"&gt;Fetch From Right&lt;/a&gt; if you only want to get first/last part of the string.&lt;/p&gt;</doc>
<shortdoc>Splits the ``string`` using ``separator`` as a delimiter string.</shortdoc>
</kw>
<kw name="Split String From Right" lineno="533">
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
<doc>&lt;p&gt;Splits the &lt;code&gt;string&lt;/code&gt; using &lt;code&gt;separator&lt;/code&gt; starting from right.&lt;/p&gt;
&lt;p&gt;Same as &lt;a href="#Split%20String" class="name"&gt;Split String&lt;/a&gt;, but splitting is started from right. This has an effect only when &lt;code&gt;max_split&lt;/code&gt; is given.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;${rest} =&lt;/td&gt;
&lt;td&gt;Split String&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;-&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${rest}&lt;/td&gt;
&lt;td&gt;${last} =&lt;/td&gt;
&lt;td&gt;Split String From Right&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;-&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Splits the ``string`` using ``separator`` starting from right.</shortdoc>
</kw>
<kw name="Split String To Characters" lineno="548">
<arguments repr="string">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="string">
<name>string</name>
</arg>
</arguments>
<doc>&lt;p&gt;Splits the given &lt;code&gt;string&lt;/code&gt; to characters.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{characters} =&lt;/td&gt;
&lt;td&gt;Split String To Characters&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Splits the given ``string`` to characters.</shortdoc>
</kw>
<kw name="Split To Lines" lineno="233">
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
<doc>&lt;p&gt;Splits the given string to lines.&lt;/p&gt;
&lt;p&gt;It is possible to get only a selection of lines from &lt;code&gt;start&lt;/code&gt; to &lt;code&gt;end&lt;/code&gt; so that &lt;code&gt;start&lt;/code&gt; index is inclusive and &lt;code&gt;end&lt;/code&gt; is exclusive. Line numbering starts from 0, and it is possible to use negative indices to refer to lines from the end.&lt;/p&gt;
&lt;p&gt;Lines are returned without the newlines. The number of returned lines is automatically logged.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{lines} =&lt;/td&gt;
&lt;td&gt;Split To Lines&lt;/td&gt;
&lt;td&gt;${manylines}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{ignore first} =&lt;/td&gt;
&lt;td&gt;Split To Lines&lt;/td&gt;
&lt;td&gt;${manylines}&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{ignore last} =&lt;/td&gt;
&lt;td&gt;Split To Lines&lt;/td&gt;
&lt;td&gt;${manylines}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;-1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{5th to 10th} =&lt;/td&gt;
&lt;td&gt;Split To Lines&lt;/td&gt;
&lt;td&gt;${manylines}&lt;/td&gt;
&lt;td&gt;4&lt;/td&gt;
&lt;td&gt;10&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{first two} =&lt;/td&gt;
&lt;td&gt;Split To Lines&lt;/td&gt;
&lt;td&gt;${manylines}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{last two} =&lt;/td&gt;
&lt;td&gt;Split To Lines&lt;/td&gt;
&lt;td&gt;${manylines}&lt;/td&gt;
&lt;td&gt;-2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Get%20Line" class="name"&gt;Get Line&lt;/a&gt; if you only need to get a single line.&lt;/p&gt;</doc>
<shortdoc>Splits the given string to lines.</shortdoc>
</kw>
<kw name="Strip String" lineno="626">
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
<doc>&lt;p&gt;Remove leading and/or trailing whitespaces from the given string.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;mode&lt;/code&gt; is either &lt;code&gt;left&lt;/code&gt; to remove leading characters, &lt;code&gt;right&lt;/code&gt; to remove trailing characters, &lt;code&gt;both&lt;/code&gt; (default) to remove the characters from both sides of the string or &lt;code&gt;none&lt;/code&gt; to return the unmodified string.&lt;/p&gt;
&lt;p&gt;If the optional &lt;code&gt;characters&lt;/code&gt; is given, it must be a string and the characters in the string will be stripped in the string. Please note, that this is not a substring to be removed but a list of characters, see the example below.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${stripped}=&lt;/td&gt;
&lt;td&gt;Strip String&lt;/td&gt;
&lt;td&gt;${SPACE}Hello${SPACE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stripped}&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${stripped}=&lt;/td&gt;
&lt;td&gt;Strip String&lt;/td&gt;
&lt;td&gt;${SPACE}Hello${SPACE}&lt;/td&gt;
&lt;td&gt;mode=left&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stripped}&lt;/td&gt;
&lt;td&gt;Hello${SPACE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${stripped}=&lt;/td&gt;
&lt;td&gt;Strip String&lt;/td&gt;
&lt;td&gt;aabaHelloeee&lt;/td&gt;
&lt;td&gt;characters=abe&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stripped}&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Remove leading and/or trailing whitespaces from the given string.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
