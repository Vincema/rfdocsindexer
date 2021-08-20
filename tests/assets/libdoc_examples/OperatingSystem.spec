<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="OperatingSystem" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2021-08-20T15:17:13Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/OperatingSystem.py" lineno="39">
<version>4.1</version>
<doc>&lt;p&gt;A test library providing keywords for OS related tasks.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;OperatingSystem&lt;/code&gt; is Robot Framework's standard library that enables various operating system related tasks to be performed in the system where Robot Framework is running. It can, among other things, execute commands (e.g. &lt;a href="#Run" class="name"&gt;Run&lt;/a&gt;), create and remove files and directories (e.g. &lt;a href="#Create%20File" class="name"&gt;Create File&lt;/a&gt;, &lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;), check whether files or directories exists or contain something (e.g. &lt;a href="#File%20Should%20Exist" class="name"&gt;File Should Exist&lt;/a&gt;, &lt;a href="#Directory%20Should%20Be%20Empty" class="name"&gt;Directory Should Be Empty&lt;/a&gt;) and manipulate environment variables (e.g. &lt;a href="#Set%20Environment%20Variable" class="name"&gt;Set Environment Variable&lt;/a&gt;).&lt;/p&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#Path%20separators" class="name"&gt;Path separators&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Tilde%20expansion" class="name"&gt;Tilde expansion&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Path separators"&gt;Path separators&lt;/h2&gt;
&lt;p&gt;Because Robot Framework uses the backslash (&lt;code&gt;\&lt;/code&gt;) as an escape character in the test data, using a literal backslash requires duplicating it like in &lt;code&gt;c:\\path\\file.txt&lt;/code&gt;. That can be inconvenient especially with longer Windows paths, and thus all keywords expecting paths as arguments convert forward slashes to backslashes automatically on Windows. This also means that paths like &lt;code&gt;${CURDIR}/path/file.txt&lt;/code&gt; are operating system independent.&lt;/p&gt;
&lt;p&gt;Notice that the automatic path separator conversion does not work if the path is only a part of an argument like with &lt;a href="#Run" class="name"&gt;Run&lt;/a&gt; and &lt;span class="name"&gt;Start Process&lt;/span&gt; keywords. In these cases the built-in variable &lt;code&gt;${/}&lt;/code&gt; that contains &lt;code&gt;\&lt;/code&gt; or &lt;code&gt;/&lt;/code&gt;, depending on the operating system, can be used instead.&lt;/p&gt;
&lt;h2 id="Pattern matching"&gt;Pattern matching&lt;/h2&gt;
&lt;p&gt;Some keywords allow their arguments to be specified as &lt;a href="http://en.wikipedia.org/wiki/Glob_(programming)"&gt;glob patterns&lt;/a&gt; where:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;*&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches any string, even an empty string&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;?&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches any single character&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[chars]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches one character in the bracket&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[!chars]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches one character not in the bracket&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[a-z]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches one character from the range in the bracket&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;[!a-z]&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;matches one character not from the range in the bracket&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Unless otherwise noted, matching is case-insensitive on case-insensitive operating systems such as Windows.&lt;/p&gt;
&lt;h2 id="Tilde expansion"&gt;Tilde expansion&lt;/h2&gt;
&lt;p&gt;Paths beginning with &lt;code&gt;~&lt;/code&gt; or &lt;code&gt;~username&lt;/code&gt; are expanded to the current or specified user's home directory, respectively. The resulting path is operating system dependent, but typically e.g. &lt;code&gt;~/robot&lt;/code&gt; is expanded to &lt;code&gt;C:\Users\&amp;lt;user&amp;gt;\robot&lt;/code&gt; on Windows and &lt;code&gt;/home/&amp;lt;user&amp;gt;/robot&lt;/code&gt; on Unixes.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;~username&lt;/code&gt; form does not work on Jython.&lt;/p&gt;
&lt;h2 id="Boolean arguments"&gt;Boolean arguments&lt;/h2&gt;
&lt;p&gt;Some keywords accept arguments that are handled as Boolean values true or false. If such an argument is given as a string, it is considered false if it is an empty string or equal to &lt;code&gt;FALSE&lt;/code&gt;, &lt;code&gt;NONE&lt;/code&gt;, &lt;code&gt;NO&lt;/code&gt;, &lt;code&gt;OFF&lt;/code&gt; or &lt;code&gt;0&lt;/code&gt;, case-insensitively. Other strings are considered true regardless their value, and other argument types are tested using the same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;True examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=True&lt;/td&gt;
&lt;td&gt;# Strings are generally true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=yes&lt;/td&gt;
&lt;td&gt;# Same as the above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=${TRUE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;True&lt;/code&gt; is true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=${42}&lt;/td&gt;
&lt;td&gt;# Numbers other than 0 are true.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;False examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=False&lt;/td&gt;
&lt;td&gt;# String &lt;code&gt;false&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=no&lt;/td&gt;
&lt;td&gt;# Also string &lt;code&gt;no&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=${EMPTY}&lt;/td&gt;
&lt;td&gt;# Empty string is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;recursive=${FALSE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;False&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Considering &lt;span class="name"&gt;OFF&lt;/span&gt;` and &lt;code&gt;0&lt;/code&gt; false is new in Robot Framework 3.1.&lt;/p&gt;
&lt;h2 id="Example"&gt;Example&lt;/h2&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Setting&lt;/th&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;OperatingSystem&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Variable&lt;/th&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${PATH}&lt;/td&gt;
&lt;td&gt;${CURDIR}/example.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Test Case&lt;/th&gt;
&lt;th&gt;Action&lt;/th&gt;
&lt;th&gt;Argument&lt;/th&gt;
&lt;th&gt;Argument&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Example&lt;/td&gt;
&lt;td&gt;Create File&lt;/td&gt;
&lt;td&gt;${PATH}&lt;/td&gt;
&lt;td&gt;Some text&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;File Should Exist&lt;/td&gt;
&lt;td&gt;${PATH}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Copy File&lt;/td&gt;
&lt;td&gt;${PATH}&lt;/td&gt;
&lt;td&gt;~/file.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;${output} =&lt;/td&gt;
&lt;td&gt;Run&lt;/td&gt;
&lt;td&gt;${TEMPDIR}${/}script.py arg&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Append To Environment Variable" lineno="962">
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
<doc>&lt;p&gt;Appends given &lt;code&gt;values&lt;/code&gt; to environment variable &lt;code&gt;name&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If the environment variable already exists, values are added after it, and otherwise a new environment variable is created.&lt;/p&gt;
&lt;p&gt;Values are, by default, joined together using the operating system path separator (&lt;code&gt;;&lt;/code&gt; on Windows, &lt;code&gt;:&lt;/code&gt; elsewhere). This can be changed by giving a separator after the values like &lt;code&gt;separator=value&lt;/code&gt;. No other configuration parameters are accepted.&lt;/p&gt;
&lt;p&gt;Examples (assuming &lt;code&gt;NAME&lt;/code&gt; and &lt;code&gt;NAME2&lt;/code&gt; do not exist initially):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Append To Environment Variable&lt;/td&gt;
&lt;td&gt;NAME&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;%{NAME}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Append To Environment Variable&lt;/td&gt;
&lt;td&gt;NAME&lt;/td&gt;
&lt;td&gt;second&lt;/td&gt;
&lt;td&gt;third&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;%{NAME}&lt;/td&gt;
&lt;td&gt;first${:}second${:}third&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Append To Environment Variable&lt;/td&gt;
&lt;td&gt;NAME2&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;td&gt;separator=-&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;%{NAME2}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Append To Environment Variable&lt;/td&gt;
&lt;td&gt;NAME2&lt;/td&gt;
&lt;td&gt;second&lt;/td&gt;
&lt;td&gt;separator=-&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;%{NAME2}&lt;/td&gt;
&lt;td&gt;first-second&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Appends given ``values`` to environment variable ``name``.</shortdoc>
</kw>
<kw name="Append To File" lineno="612">
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
<doc>&lt;p&gt;Appends the given content to the specified file.&lt;/p&gt;
&lt;p&gt;If the file exists, the given text is written to its end. If the file does not exist, it is created.&lt;/p&gt;
&lt;p&gt;Other than not overwriting possible existing files, this keyword works exactly like &lt;a href="#Create%20File" class="name"&gt;Create File&lt;/a&gt;. See its documentation for more details about the usage.&lt;/p&gt;
&lt;p&gt;Note that special encodings &lt;code&gt;SYSTEM&lt;/code&gt; and &lt;code&gt;CONSOLE&lt;/code&gt; only work with this keyword starting from Robot Framework 3.1.2.&lt;/p&gt;</doc>
<shortdoc>Appends the given content to the specified file.</shortdoc>
</kw>
<kw name="Copy Directory" lineno="885">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>&lt;p&gt;Copies the source directory into the destination.&lt;/p&gt;
&lt;p&gt;If the destination exists, the source is copied under it. Otherwise the destination directory and the possible missing intermediate directories are created.&lt;/p&gt;</doc>
<shortdoc>Copies the source directory into the destination.</shortdoc>
</kw>
<kw name="Copy File" lineno="714">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>&lt;p&gt;Copies the source file into the destination.&lt;/p&gt;
&lt;p&gt;Source must be a path to an existing file or a glob pattern (see &lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt;) that matches exactly one file. How the destination is interpreted is explained below.&lt;/p&gt;
&lt;p&gt;1) If the destination is an existing file, the source file is copied over it.&lt;/p&gt;
&lt;p&gt;2) If the destination is an existing directory, the source file is copied into it. A possible file with the same name as the source is overwritten.&lt;/p&gt;
&lt;p&gt;3) If the destination does not exist and it ends with a path separator (&lt;code&gt;/&lt;/code&gt; or &lt;code&gt;\&lt;/code&gt;), it is considered a directory. That directory is created and a source file copied into it. Possible missing intermediate directories are also created.&lt;/p&gt;
&lt;p&gt;4) If the destination does not exist and it does not end with a path separator, it is considered a file. If the path to the file does not exist, it is created.&lt;/p&gt;
&lt;p&gt;The resulting destination path is returned.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Copy%20Files" class="name"&gt;Copy Files&lt;/a&gt;, &lt;a href="#Move%20File" class="name"&gt;Move File&lt;/a&gt;, and &lt;a href="#Move%20Files" class="name"&gt;Move Files&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Copies the source file into the destination.</shortdoc>
</kw>
<kw name="Copy Files" lineno="838">
<arguments repr="*sources_and_destination">
<arg kind="VAR_POSITIONAL" required="false" repr="*sources_and_destination">
<name>sources_and_destination</name>
</arg>
</arguments>
<doc>&lt;p&gt;Copies specified files to the target directory.&lt;/p&gt;
&lt;p&gt;Source files can be given as exact paths and as glob patterns (see &lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt;). At least one source must be given, but it is not an error if it is a pattern that does not match anything.&lt;/p&gt;
&lt;p&gt;Last argument must be the destination directory. If the destination does not exist, it will be created.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Copy Files&lt;/td&gt;
&lt;td&gt;${dir}/file1.txt&lt;/td&gt;
&lt;td&gt;${dir}/file2.txt&lt;/td&gt;
&lt;td&gt;${dir2}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Copy Files&lt;/td&gt;
&lt;td&gt;${dir}/file-*.txt&lt;/td&gt;
&lt;td&gt;${dir2}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Copy%20File" class="name"&gt;Copy File&lt;/a&gt;, &lt;a href="#Move%20File" class="name"&gt;Move File&lt;/a&gt;, and &lt;a href="#Move%20Files" class="name"&gt;Move Files&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Copies specified files to the target directory.</shortdoc>
</kw>
<kw name="Count Directories In Directory" lineno="1350">
<arguments repr="path, pattern=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Wrapper for &lt;a href="#Count%20Items%20In%20Directory" class="name"&gt;Count Items In Directory&lt;/a&gt; returning only directory count.&lt;/p&gt;</doc>
<shortdoc>Wrapper for `Count Items In Directory` returning only directory count.</shortdoc>
</kw>
<kw name="Count Files In Directory" lineno="1344">
<arguments repr="path, pattern=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Wrapper for &lt;a href="#Count%20Items%20In%20Directory" class="name"&gt;Count Items In Directory&lt;/a&gt; returning only file count.&lt;/p&gt;</doc>
<shortdoc>Wrapper for `Count Items In Directory` returning only file count.</shortdoc>
</kw>
<kw name="Count Items In Directory" lineno="1333">
<arguments repr="path, pattern=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="pattern=None">
<name>pattern</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns and logs the number of all items in the given directory.&lt;/p&gt;
&lt;p&gt;The argument &lt;code&gt;pattern&lt;/code&gt; has the same semantics as with &lt;a href="#List%20Directory" class="name"&gt;List Directory&lt;/a&gt; keyword. The count is returned as an integer, so it must be checked e.g. with the built-in keyword &lt;span class="name"&gt;Should Be Equal As Integers&lt;/span&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns and logs the number of all items in the given directory.</shortdoc>
</kw>
<kw name="Create Binary File" lineno="586">
<arguments repr="path, content">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="content">
<name>content</name>
</arg>
</arguments>
<doc>&lt;p&gt;Creates a binary file with the given content.&lt;/p&gt;
&lt;p&gt;If content is given as a Unicode string, it is first converted to bytes character by character. All characters with ordinal below 256 can be used and are converted to bytes with same values. Using characters with higher ordinal is an error.&lt;/p&gt;
&lt;p&gt;Byte strings, and possible other types, are written to the file as is.&lt;/p&gt;
&lt;p&gt;If the directory for the file does not exist, it is created, along with missing intermediate directories.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Create Binary File&lt;/td&gt;
&lt;td&gt;${dir}/example.png&lt;/td&gt;
&lt;td&gt;${image content}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Create Binary File&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;\x01\x00\xe4\x00&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Create%20File" class="name"&gt;Create File&lt;/a&gt; if you want to create a text file using a certain encoding. &lt;a href="#File%20Should%20Not%20Exist" class="name"&gt;File Should Not Exist&lt;/a&gt; can be used to avoid overwriting existing files.&lt;/p&gt;</doc>
<shortdoc>Creates a binary file with the given content.</shortdoc>
</kw>
<kw name="Create Directory" lineno="672">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Creates the specified directory.&lt;/p&gt;
&lt;p&gt;Also possible intermediate directories are created. Passes if the directory already exists, but fails if the path exists and is not a directory.&lt;/p&gt;</doc>
<shortdoc>Creates the specified directory.</shortdoc>
</kw>
<kw name="Create File" lineno="542">
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
<doc>&lt;p&gt;Creates a file with the given content and encoding.&lt;/p&gt;
&lt;p&gt;If the directory where the file is created does not exist, it is automatically created along with possible missing intermediate directories. Possible existing file is overwritten.&lt;/p&gt;
&lt;p&gt;On Windows newline characters (&lt;code&gt;\n&lt;/code&gt;) in content are automatically converted to Windows native newline sequence (&lt;code&gt;\r\n&lt;/code&gt;).&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt; for more information about possible &lt;code&gt;encoding&lt;/code&gt; values, including special values &lt;code&gt;SYSTEM&lt;/code&gt; and &lt;code&gt;CONSOLE&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Create File&lt;/td&gt;
&lt;td&gt;${dir}/example.txt&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Create File&lt;/td&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;Hyv\xe4 esimerkki&lt;/td&gt;
&lt;td&gt;Latin-1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Create File&lt;/td&gt;
&lt;td&gt;/tmp/foo.txt&lt;/td&gt;
&lt;td&gt;3\nlines\nhere\n&lt;/td&gt;
&lt;td&gt;SYSTEM&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Append%20To%20File" class="name"&gt;Append To File&lt;/a&gt; if you want to append to an existing file and &lt;a href="#Create%20Binary%20File" class="name"&gt;Create Binary File&lt;/a&gt; if you need to write bytes without encoding. &lt;a href="#File%20Should%20Not%20Exist" class="name"&gt;File Should Not Exist&lt;/a&gt; can be used to avoid overwriting existing files.&lt;/p&gt;
&lt;p&gt;Automatically converting &lt;code&gt;\n&lt;/code&gt; to &lt;code&gt;\r\n&lt;/code&gt; on Windows is new in Robot Framework 3.1.&lt;/p&gt;</doc>
<shortdoc>Creates a file with the given content and encoding.</shortdoc>
</kw>
<kw name="Directory Should Be Empty" lineno="489">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the specified directory is empty.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails unless the specified directory is empty.</shortdoc>
</kw>
<kw name="Directory Should Exist" lineno="407">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the given path points to an existing directory.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails unless the given path points to an existing directory.</shortdoc>
</kw>
<kw name="Directory Should Not Be Empty" lineno="501">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the specified directory is empty.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the specified directory is empty.</shortdoc>
</kw>
<kw name="Directory Should Not Exist" lineno="420">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given path points to an existing file.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given path points to an existing file.</shortdoc>
</kw>
<kw name="Empty Directory" lineno="657">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Deletes all the content from the given directory.&lt;/p&gt;
&lt;p&gt;Deletes both files and sub-directories, but the specified directory itself if not removed. Use &lt;a href="#Remove%20Directory" class="name"&gt;Remove Directory&lt;/a&gt; if you want to remove the whole directory.&lt;/p&gt;</doc>
<shortdoc>Deletes all the content from the given directory.</shortdoc>
</kw>
<kw name="Environment Variable Should Be Set" lineno="1009">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the specified environment variable is not set.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the specified environment variable is not set.</shortdoc>
</kw>
<kw name="Environment Variable Should Not Be Set" lineno="1019">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the specified environment variable is set.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the specified environment variable is set.</shortdoc>
</kw>
<kw name="File Should Be Empty" lineno="513">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the specified file is empty.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails unless the specified file is empty.</shortdoc>
</kw>
<kw name="File Should Exist" lineno="381">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the given &lt;code&gt;path&lt;/code&gt; points to an existing file.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails unless the given ``path`` points to an existing file.</shortdoc>
</kw>
<kw name="File Should Not Be Empty" lineno="527">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the specified directory is empty.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the specified directory is empty.</shortdoc>
</kw>
<kw name="File Should Not Exist" lineno="394">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given path points to an existing file.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given path points to an existing file.</shortdoc>
</kw>
<kw name="Get Binary File" lineno="275">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the contents of a specified file.&lt;/p&gt;
&lt;p&gt;This keyword reads the specified file and returns the contents as is. See also &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns the contents of a specified file.</shortdoc>
</kw>
<kw name="Get Environment Variable" lineno="935">
<arguments repr="name, default=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=None">
<name>default</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the value of an environment variable with the given name.&lt;/p&gt;
&lt;p&gt;If no such environment variable is set, returns the default value, if given. Otherwise fails the test case.&lt;/p&gt;
&lt;p&gt;Returned variables are automatically decoded to Unicode using the system encoding.&lt;/p&gt;
&lt;p&gt;Note that you can also access environment variables directly using the variable syntax &lt;code&gt;%{ENV_VAR_NAME}&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns the value of an environment variable with the given name.</shortdoc>
</kw>
<kw name="Get Environment Variables" lineno="1030">
<arguments repr="">
</arguments>
<doc>&lt;p&gt;Returns currently available environment variables as a dictionary.&lt;/p&gt;
&lt;p&gt;Both keys and values are decoded to Unicode using the system encoding. Altering the returned dictionary has no effect on the actual environment variables.&lt;/p&gt;</doc>
<shortdoc>Returns currently available environment variables as a dictionary.</shortdoc>
</kw>
<kw name="Get File" lineno="229">
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
<doc>&lt;p&gt;Returns the contents of a specified file.&lt;/p&gt;
&lt;p&gt;This keyword reads the specified file and returns the contents. Line breaks in content are converted to platform independent form. See also &lt;a href="#Get%20Binary%20File" class="name"&gt;Get Binary File&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;encoding&lt;/code&gt; defines the encoding of the file. The default value is &lt;code&gt;UTF-8&lt;/code&gt;, which means that UTF-8 and ASCII encoded files are read correctly. In addition to the encodings supported by the underlying Python implementation, the following special encoding values can be used:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;SYSTEM&lt;/code&gt;: Use the default system encoding.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;CONSOLE&lt;/code&gt;: Use the console encoding. Outside Windows this is same as the system encoding.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;&lt;code&gt;encoding_errors&lt;/code&gt; argument controls what to do if decoding some bytes fails. All values accepted by &lt;code&gt;decode&lt;/code&gt; method in Python are valid, but in practice the following values are most useful:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;strict&lt;/code&gt;: Fail if characters cannot be decoded (default).&lt;/li&gt;
&lt;li&gt;&lt;code&gt;ignore&lt;/code&gt;: Ignore characters that cannot be decoded.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;replace&lt;/code&gt;: Replace characters that cannot be decoded with a replacement character.&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Returns the contents of a specified file.</shortdoc>
</kw>
<kw name="Get File Size" lineno="1281">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns and logs file size as an integer in bytes.&lt;/p&gt;</doc>
<shortdoc>Returns and logs file size as an integer in bytes.</shortdoc>
</kw>
<kw name="Get Modified Time" lineno="1192">
<arguments repr="path, format=timestamp">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="format=timestamp">
<name>format</name>
<default>timestamp</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the last modification time of a file or directory.&lt;/p&gt;
&lt;p&gt;How time is returned is determined based on the given &lt;code&gt;format&lt;/code&gt; string as follows. Note that all checks are case-insensitive. Returned time is also automatically logged.&lt;/p&gt;
&lt;p&gt;1) If &lt;code&gt;format&lt;/code&gt; contains the word &lt;code&gt;epoch&lt;/code&gt;, the time is returned in seconds after the UNIX epoch. The return value is always an integer.&lt;/p&gt;
&lt;p&gt;2) If &lt;code&gt;format&lt;/code&gt; contains any of the words &lt;code&gt;year&lt;/code&gt;, &lt;code&gt;month&lt;/code&gt;, &lt;code&gt;day&lt;/code&gt;, &lt;code&gt;hour&lt;/code&gt;, &lt;code&gt;min&lt;/code&gt; or &lt;code&gt;sec&lt;/code&gt;, only the selected parts are returned. The order of the returned parts is always the one in the previous sentence and the order of the words in &lt;code&gt;format&lt;/code&gt; is not significant. The parts are returned as zero-padded strings (e.g. May -&amp;gt; &lt;code&gt;05&lt;/code&gt;).&lt;/p&gt;
&lt;p&gt;3) Otherwise, and by default, the time is returned as a timestamp string in the format &lt;code&gt;2006-02-24 15:08:31&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples (when the modified time of &lt;code&gt;${CURDIR}&lt;/code&gt; is 2006-03-29 15:06:21):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Get Modified Time&lt;/td&gt;
&lt;td&gt;${CURDIR}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${secs} =&lt;/td&gt;
&lt;td&gt;Get Modified Time&lt;/td&gt;
&lt;td&gt;${CURDIR}&lt;/td&gt;
&lt;td&gt;epoch&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${year} =&lt;/td&gt;
&lt;td&gt;Get Modified Time&lt;/td&gt;
&lt;td&gt;${CURDIR}&lt;/td&gt;
&lt;td&gt;return year&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;${d} =&lt;/td&gt;
&lt;td&gt;Get Modified Time&lt;/td&gt;
&lt;td&gt;${CURDIR}&lt;/td&gt;
&lt;td&gt;year,day&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{time} =&lt;/td&gt;
&lt;td&gt;Get Modified Time&lt;/td&gt;
&lt;td&gt;${CURDIR}&lt;/td&gt;
&lt;td&gt;year,month,day,hour,min,sec&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;${time} = '2006-03-29 15:06:21'&lt;/li&gt;
&lt;li&gt;${secs} = 1143637581&lt;/li&gt;
&lt;li&gt;${year} = '2006'&lt;/li&gt;
&lt;li&gt;${y} = '2006' &amp;amp; ${d} = '29'&lt;/li&gt;
&lt;li&gt;@{time} = ['2006', '03', '29', '15', '06', '21']&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Returns the last modification time of a file or directory.</shortdoc>
</kw>
<kw name="Grep File" lineno="286">
<arguments repr="path, pattern, encoding=UTF-8, encoding_errors=strict">
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
</arguments>
<doc>&lt;p&gt;Returns the lines of the specified file that match the &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword reads a file from the file system using the defined &lt;code&gt;path&lt;/code&gt;, &lt;code&gt;encoding&lt;/code&gt; and &lt;code&gt;encoding_errors&lt;/code&gt; similarly as &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt;. A difference is that only the lines that match the given &lt;code&gt;pattern&lt;/code&gt; are returned. Lines are returned as a single string catenated back together with newlines and the number of matched lines is automatically logged. Possible trailing newline is never returned.&lt;/p&gt;
&lt;p&gt;A line matches if it contains the &lt;code&gt;pattern&lt;/code&gt; anywhere in it and it &lt;b&gt;does not need to match the pattern fully&lt;/b&gt;. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;, and in this case matching is case-sensitive.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${errors} =&lt;/td&gt;
&lt;td&gt;Grep File&lt;/td&gt;
&lt;td&gt;/var/log/myapp.log&lt;/td&gt;
&lt;td&gt;ERROR&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ret} =&lt;/td&gt;
&lt;td&gt;Grep File&lt;/td&gt;
&lt;td&gt;${CURDIR}/file.txt&lt;/td&gt;
&lt;td&gt;[Ww]ildc??d ex*ple&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;If more complex pattern matching is needed, it is possible to use &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt; in combination with String library keywords like &lt;span class="name"&gt;Get Lines Matching Regexp&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;This keyword supports special &lt;code&gt;SYSTEM&lt;/code&gt; and &lt;code&gt;CONSOLE&lt;/code&gt; encodings that &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt; supports only with Robot Framework 4.0 and newer. When using Python 3, it is possible to use &lt;code&gt;${NONE}&lt;/code&gt; instead of &lt;code&gt;SYSTEM&lt;/code&gt; with earlier versions.&lt;/p&gt;</doc>
<shortdoc>Returns the lines of the specified file that match the ``pattern``.</shortdoc>
</kw>
<kw name="Join Path" lineno="1052">
<arguments repr="base, *parts">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="base">
<name>base</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*parts">
<name>parts</name>
</arg>
</arguments>
<doc>&lt;p&gt;Joins the given path part(s) to the given base path.&lt;/p&gt;
&lt;p&gt;The path separator (&lt;code&gt;/&lt;/code&gt; or &lt;code&gt;\&lt;/code&gt;) is inserted when needed and the possible absolute paths handled as expected. The resulted path is also normalized.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${path} =&lt;/td&gt;
&lt;td&gt;Join Path&lt;/td&gt;
&lt;td&gt;my&lt;/td&gt;
&lt;td&gt;path&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p2} =&lt;/td&gt;
&lt;td&gt;Join Path&lt;/td&gt;
&lt;td&gt;my/&lt;/td&gt;
&lt;td&gt;path/&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p3} =&lt;/td&gt;
&lt;td&gt;Join Path&lt;/td&gt;
&lt;td&gt;my&lt;/td&gt;
&lt;td&gt;path&lt;/td&gt;
&lt;td&gt;my&lt;/td&gt;
&lt;td&gt;file.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p4} =&lt;/td&gt;
&lt;td&gt;Join Path&lt;/td&gt;
&lt;td&gt;my&lt;/td&gt;
&lt;td&gt;/path&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p5} =&lt;/td&gt;
&lt;td&gt;Join Path&lt;/td&gt;
&lt;td&gt;/my/path/&lt;/td&gt;
&lt;td&gt;..&lt;/td&gt;
&lt;td&gt;path2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;${path} = 'my/path'&lt;/li&gt;
&lt;li&gt;${p2} = 'my/path'&lt;/li&gt;
&lt;li&gt;${p3} = 'my/path/my/file.txt'&lt;/li&gt;
&lt;li&gt;${p4} = '/path'&lt;/li&gt;
&lt;li&gt;${p5} = '/my/path2'&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Joins the given path part(s) to the given base path.</shortdoc>
</kw>
<kw name="Join Paths" lineno="1076">
<arguments repr="base, *paths">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="base">
<name>base</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*paths">
<name>paths</name>
</arg>
</arguments>
<doc>&lt;p&gt;Joins given paths with base and returns resulted paths.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Join%20Path" class="name"&gt;Join Path&lt;/a&gt; for more information.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{p1} =&lt;/td&gt;
&lt;td&gt;Join Paths&lt;/td&gt;
&lt;td&gt;base&lt;/td&gt;
&lt;td&gt;example&lt;/td&gt;
&lt;td&gt;other&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{p2} =&lt;/td&gt;
&lt;td&gt;Join Paths&lt;/td&gt;
&lt;td&gt;/my/base&lt;/td&gt;
&lt;td&gt;/example&lt;/td&gt;
&lt;td&gt;other&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{p3} =&lt;/td&gt;
&lt;td&gt;Join Paths&lt;/td&gt;
&lt;td&gt;my/base&lt;/td&gt;
&lt;td&gt;example/path/&lt;/td&gt;
&lt;td&gt;other&lt;/td&gt;
&lt;td&gt;one/more&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;@{p1} = ['base/example', 'base/other']&lt;/li&gt;
&lt;li&gt;@{p2} = ['/example', '/my/base/other']&lt;/li&gt;
&lt;li&gt;@{p3} = ['my/base/example/path', 'my/base/other', 'my/base/one/more']&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Joins given paths with base and returns resulted paths.</shortdoc>
</kw>
<kw name="List Directories In Directory" lineno="1325">
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
<doc>&lt;p&gt;Wrapper for &lt;a href="#List%20Directory" class="name"&gt;List Directory&lt;/a&gt; that returns only directories.&lt;/p&gt;</doc>
<shortdoc>Wrapper for `List Directory` that returns only directories.</shortdoc>
</kw>
<kw name="List Directory" lineno="1291">
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
<doc>&lt;p&gt;Returns and logs items in a directory, optionally filtered with &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;File and directory names are returned in case-sensitive alphabetical order, e.g. &lt;code&gt;['A Name', 'Second', 'a lower case name', 'one more']&lt;/code&gt;. Implicit directories &lt;code&gt;.&lt;/code&gt; and &lt;code&gt;..&lt;/code&gt; are not returned. The returned items are automatically logged.&lt;/p&gt;
&lt;p&gt;File and directory names are returned relative to the given path (e.g. &lt;code&gt;'file.txt'&lt;/code&gt;) by default. If you want them be returned in absolute format (e.g. &lt;code&gt;'/home/robot/file.txt'&lt;/code&gt;), give the &lt;code&gt;absolute&lt;/code&gt; argument a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;).&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;pattern&lt;/code&gt; is given, only items matching it are returned. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;, and in this case matching is case-sensitive.&lt;/p&gt;
&lt;p&gt;Examples (using also other &lt;a href="#List%20Directory" class="name"&gt;List Directory&lt;/a&gt; variants):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{items} =&lt;/td&gt;
&lt;td&gt;List Directory&lt;/td&gt;
&lt;td&gt;${TEMPDIR}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{files} =&lt;/td&gt;
&lt;td&gt;List Files In Directory&lt;/td&gt;
&lt;td&gt;/tmp&lt;/td&gt;
&lt;td&gt;*.txt&lt;/td&gt;
&lt;td&gt;absolute&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${count} =&lt;/td&gt;
&lt;td&gt;Count Files In Directory&lt;/td&gt;
&lt;td&gt;${CURDIR}&lt;/td&gt;
&lt;td&gt;???&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns and logs items in a directory, optionally filtered with ``pattern``.</shortdoc>
</kw>
<kw name="List Files In Directory" lineno="1318">
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
<doc>&lt;p&gt;Wrapper for &lt;a href="#List%20Directory" class="name"&gt;List Directory&lt;/a&gt; that returns only files.&lt;/p&gt;</doc>
<shortdoc>Wrapper for `List Directory` that returns only files.</shortdoc>
</kw>
<kw name="Log Environment Variables" lineno="1039">
<arguments repr="level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs all environment variables using the given log level.&lt;/p&gt;
&lt;p&gt;Environment variables are also returned the same way as with &lt;a href="#Get%20Environment%20Variables" class="name"&gt;Get Environment Variables&lt;/a&gt; keyword.&lt;/p&gt;</doc>
<shortdoc>Logs all environment variables using the given log level.</shortdoc>
</kw>
<kw name="Log File" lineno="329">
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
<doc>&lt;p&gt;Wrapper for &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt; that also logs the returned file.&lt;/p&gt;
&lt;p&gt;The file is logged with the INFO level. If you want something else, just use &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt; and the built-in keyword &lt;span class="name"&gt;Log&lt;/span&gt; with the desired level.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Get%20File" class="name"&gt;Get File&lt;/a&gt; for more information about &lt;code&gt;encoding&lt;/code&gt; and &lt;code&gt;encoding_errors&lt;/code&gt; arguments.&lt;/p&gt;</doc>
<shortdoc>Wrapper for `Get File` that also logs the returned file.</shortdoc>
</kw>
<kw name="Move Directory" lineno="920">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>&lt;p&gt;Moves the source directory into a destination.&lt;/p&gt;
&lt;p&gt;Uses &lt;a href="#Copy%20Directory" class="name"&gt;Copy Directory&lt;/a&gt; keyword internally, and &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;destination&lt;/code&gt; arguments have exactly same semantics as with that keyword.&lt;/p&gt;</doc>
<shortdoc>Moves the source directory into a destination.</shortdoc>
</kw>
<kw name="Move File" lineno="819">
<arguments repr="source, destination">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="destination">
<name>destination</name>
</arg>
</arguments>
<doc>&lt;p&gt;Moves the source file into the destination.&lt;/p&gt;
&lt;p&gt;Arguments have exactly same semantics as with &lt;a href="#Copy%20File" class="name"&gt;Copy File&lt;/a&gt; keyword. Destination file path is returned.&lt;/p&gt;
&lt;p&gt;If the source and destination are on the same filesystem, rename operation is used. Otherwise file is copied to the destination filesystem and then removed from the original filesystem.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Move%20Files" class="name"&gt;Move Files&lt;/a&gt;, &lt;a href="#Copy%20File" class="name"&gt;Copy File&lt;/a&gt;, and &lt;a href="#Copy%20Files" class="name"&gt;Copy Files&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Moves the source file into the destination.</shortdoc>
</kw>
<kw name="Move Files" lineno="873">
<arguments repr="*sources_and_destination">
<arg kind="VAR_POSITIONAL" required="false" repr="*sources_and_destination">
<name>sources_and_destination</name>
</arg>
</arguments>
<doc>&lt;p&gt;Moves specified files to the target directory.&lt;/p&gt;
&lt;p&gt;Arguments have exactly same semantics as with &lt;a href="#Copy%20Files" class="name"&gt;Copy Files&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Move%20File" class="name"&gt;Move File&lt;/a&gt;, &lt;a href="#Copy%20File" class="name"&gt;Copy File&lt;/a&gt;, and &lt;a href="#Copy%20Files" class="name"&gt;Copy Files&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Moves specified files to the target directory.</shortdoc>
</kw>
<kw name="Normalize Path" lineno="1092">
<arguments repr="path, case_normalize=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="case_normalize=False">
<name>case_normalize</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Normalizes the given path.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Collapses redundant separators and up-level references.&lt;/li&gt;
&lt;li&gt;Converts &lt;code&gt;/&lt;/code&gt; to &lt;code&gt;\&lt;/code&gt; on Windows.&lt;/li&gt;
&lt;li&gt;Replaces initial &lt;code&gt;~&lt;/code&gt; or &lt;code&gt;~user&lt;/code&gt; by that user's home directory. The latter is not supported on Jython.&lt;/li&gt;
&lt;li&gt;If &lt;code&gt;case_normalize&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) on Windows, converts the path to all lowercase. New in Robot Framework 3.1.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${path1} =&lt;/td&gt;
&lt;td&gt;Normalize Path&lt;/td&gt;
&lt;td&gt;abc/&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${path2} =&lt;/td&gt;
&lt;td&gt;Normalize Path&lt;/td&gt;
&lt;td&gt;abc/../def&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${path3} =&lt;/td&gt;
&lt;td&gt;Normalize Path&lt;/td&gt;
&lt;td&gt;abc/./def//ghi&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${path4} =&lt;/td&gt;
&lt;td&gt;Normalize Path&lt;/td&gt;
&lt;td&gt;~robot/stuff&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;${path1} = 'abc'&lt;/li&gt;
&lt;li&gt;${path2} = 'def'&lt;/li&gt;
&lt;li&gt;${path3} = 'abc/def/ghi'&lt;/li&gt;
&lt;li&gt;${path4} = '/home/robot/stuff'&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;On Windows result would use &lt;code&gt;\&lt;/code&gt; instead of &lt;code&gt;/&lt;/code&gt; and home directory would be different.&lt;/p&gt;</doc>
<shortdoc>Normalizes the given path.</shortdoc>
</kw>
<kw name="Remove Directory" lineno="688">
<arguments repr="path, recursive=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="recursive=False">
<name>recursive</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes the directory pointed to by the given &lt;code&gt;path&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If the second argument &lt;code&gt;recursive&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the directory is removed recursively. Otherwise removing fails if the directory is not empty.&lt;/p&gt;
&lt;p&gt;If the directory pointed to by the &lt;code&gt;path&lt;/code&gt; does not exist, the keyword passes, but it fails, if the &lt;code&gt;path&lt;/code&gt; points to a file.&lt;/p&gt;</doc>
<shortdoc>Removes the directory pointed to by the given ``path``.</shortdoc>
</kw>
<kw name="Remove Environment Variable" lineno="994">
<arguments repr="*names">
<arg kind="VAR_POSITIONAL" required="false" repr="*names">
<name>names</name>
</arg>
</arguments>
<doc>&lt;p&gt;Deletes the specified environment variable.&lt;/p&gt;
&lt;p&gt;Does nothing if the environment variable is not set.&lt;/p&gt;
&lt;p&gt;It is possible to remove multiple variables by passing them to this keyword as separate arguments.&lt;/p&gt;</doc>
<shortdoc>Deletes the specified environment variable.</shortdoc>
</kw>
<kw name="Remove File" lineno="628">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes a file with the given path.&lt;/p&gt;
&lt;p&gt;Passes if the file does not exist, but fails if the path does not point to a regular file (e.g. it points to a directory).&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. If the path is a pattern, all files matching it are removed.&lt;/p&gt;</doc>
<shortdoc>Removes a file with the given path.</shortdoc>
</kw>
<kw name="Remove Files" lineno="648">
<arguments repr="*paths">
<arg kind="VAR_POSITIONAL" required="false" repr="*paths">
<name>paths</name>
</arg>
</arguments>
<doc>&lt;p&gt;Uses &lt;a href="#Remove%20File" class="name"&gt;Remove File&lt;/a&gt; to remove multiple files one-by-one.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Files&lt;/td&gt;
&lt;td&gt;${TEMPDIR}${/}foo.txt&lt;/td&gt;
&lt;td&gt;${TEMPDIR}${/}bar.txt&lt;/td&gt;
&lt;td&gt;${TEMPDIR}${/}zap.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Uses `Remove File` to remove multiple files one-by-one.</shortdoc>
</kw>
<kw name="Run" lineno="135">
<arguments repr="command">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given command in the system and returns the output.&lt;/p&gt;
&lt;p&gt;The execution status of the command &lt;b&gt;is not checked&lt;/b&gt; by this keyword, and it must be done separately based on the returned output. If the execution return code is needed, either &lt;a href="#Run%20And%20Return%20Rc" class="name"&gt;Run And Return RC&lt;/a&gt; or &lt;a href="#Run%20And%20Return%20Rc%20And%20Output" class="name"&gt;Run And Return RC And Output&lt;/a&gt; can be used.&lt;/p&gt;
&lt;p&gt;The standard error stream is automatically redirected to the standard output stream by adding &lt;code&gt;2&amp;gt;&amp;amp;1&lt;/code&gt; after the executed command. This automatic redirection is done only when the executed command does not contain additional output redirections. You can thus freely forward the standard error somewhere else, for example, like &lt;code&gt;my_command 2&amp;gt;stderr.txt&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The returned output contains everything written into the standard output or error streams by the command (unless either of them is redirected explicitly). Many commands add an extra newline (&lt;code&gt;\n&lt;/code&gt;) after the output to make it easier to read in the console. To ease processing the returned output, this possible trailing newline is stripped by this keyword.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${output} =&lt;/td&gt;
&lt;td&gt;Run&lt;/td&gt;
&lt;td&gt;ls -lhF /tmp&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Run&lt;/td&gt;
&lt;td&gt;${CURDIR}${/}tester.py arg1 arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;FAIL&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${stdout} =&lt;/td&gt;
&lt;td&gt;Run&lt;/td&gt;
&lt;td&gt;/opt/script.sh 2&amp;gt;/tmp/stderr.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stdout}&lt;/td&gt;
&lt;td&gt;TEST PASSED&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;File Should Be Empty&lt;/td&gt;
&lt;td&gt;/tmp/stderr.txt&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;b&gt;TIP:&lt;/b&gt; &lt;span class="name"&gt;Run Process&lt;/span&gt; keyword provided by the &lt;a href="http://robotframework.org/robotframework/latest/libraries/Process.html"&gt;Process library&lt;/a&gt; supports better process configuration and is generally recommended as a replacement for this keyword.&lt;/p&gt;</doc>
<shortdoc>Runs the given command in the system and returns the output.</shortdoc>
</kw>
<kw name="Run And Return Rc" lineno="173">
<arguments repr="command">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given command in the system and returns the return code.&lt;/p&gt;
&lt;p&gt;The return code (RC) is returned as a positive integer in range from 0 to 255 as returned by the executed command. On some operating systems (notable Windows) original return codes can be something else, but this keyword always maps them to the 0-255 range. Since the RC is an integer, it must be checked e.g. with the keyword &lt;span class="name"&gt;Should Be Equal As Integers&lt;/span&gt; instead of &lt;span class="name"&gt;Should Be Equal&lt;/span&gt; (both are built-in keywords).&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${rc} =&lt;/td&gt;
&lt;td&gt;Run and Return RC&lt;/td&gt;
&lt;td&gt;${CURDIR}${/}script.py arg&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${rc}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${rc} =&lt;/td&gt;
&lt;td&gt;Run and Return RC&lt;/td&gt;
&lt;td&gt;/path/to/example.rb arg1 arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;0 &amp;lt; ${rc} &amp;lt; 42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Run" class="name"&gt;Run&lt;/a&gt; and &lt;a href="#Run%20And%20Return%20Rc%20And%20Output" class="name"&gt;Run And Return RC And Output&lt;/a&gt; if you need to get the output of the executed command.&lt;/p&gt;
&lt;p&gt;&lt;b&gt;TIP:&lt;/b&gt; &lt;span class="name"&gt;Run Process&lt;/span&gt; keyword provided by the &lt;a href="http://robotframework.org/robotframework/latest/libraries/Process.html"&gt;Process library&lt;/a&gt; supports better process configuration and is generally recommended as a replacement for this keyword.&lt;/p&gt;</doc>
<shortdoc>Runs the given command in the system and returns the return code.</shortdoc>
</kw>
<kw name="Run And Return Rc And Output" lineno="200">
<arguments repr="command">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given command in the system and returns the RC and output.&lt;/p&gt;
&lt;p&gt;The return code (RC) is returned similarly as with &lt;a href="#Run%20And%20Return%20Rc" class="name"&gt;Run And Return RC&lt;/a&gt; and the output similarly as with &lt;a href="#Run" class="name"&gt;Run&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${rc}&lt;/td&gt;
&lt;td&gt;${output} =&lt;/td&gt;
&lt;td&gt;Run and Return RC and Output&lt;/td&gt;
&lt;td&gt;${CURDIR}${/}mytool&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${rc}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;FAIL&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${rc}&lt;/td&gt;
&lt;td&gt;${stdout} =&lt;/td&gt;
&lt;td&gt;Run and Return RC and Output&lt;/td&gt;
&lt;td&gt;/opt/script.sh 2&amp;gt;/tmp/stderr.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stdout}&lt;/td&gt;
&lt;td&gt;TEST PASSED&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;File Should Be Empty&lt;/td&gt;
&lt;td&gt;/tmp/stderr.txt&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;b&gt;TIP:&lt;/b&gt; &lt;span class="name"&gt;Run Process&lt;/span&gt; keyword provided by the &lt;a href="http://robotframework.org/robotframework/latest/libraries/Process.html"&gt;Process library&lt;/a&gt; supports better process configuration and is generally recommended as a replacement for this keyword.&lt;/p&gt;</doc>
<shortdoc>Runs the given command in the system and returns the RC and output.</shortdoc>
</kw>
<kw name="Set Environment Variable" lineno="952">
<arguments repr="name, value">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets an environment variable to a specified value.&lt;/p&gt;
&lt;p&gt;Values are converted to strings automatically. Set variables are automatically encoded using the system encoding.&lt;/p&gt;</doc>
<shortdoc>Sets an environment variable to a specified value.</shortdoc>
</kw>
<kw name="Set Modified Time" lineno="1234">
<arguments repr="path, mtime">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="mtime">
<name>mtime</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the file modification and access times.&lt;/p&gt;
&lt;p&gt;Changes the modification and access times of the given file to the value determined by &lt;code&gt;mtime&lt;/code&gt;. The time can be given in different formats described below. Note that all checks involving strings are case-insensitive. Modified time can only be set to regular files.&lt;/p&gt;
&lt;p&gt;1) If &lt;code&gt;mtime&lt;/code&gt; is a number, or a string that can be converted to a number, it is interpreted as seconds since the UNIX epoch (1970-01-01 00:00:00 UTC). This documentation was originally written about 1177654467 seconds after the epoch.&lt;/p&gt;
&lt;p&gt;2) If &lt;code&gt;mtime&lt;/code&gt; is a timestamp, that time will be used. Valid timestamp formats are &lt;code&gt;YYYY-MM-DD hh:mm:ss&lt;/code&gt; and &lt;code&gt;YYYYMMDD hhmmss&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;3) If &lt;code&gt;mtime&lt;/code&gt; is equal to &lt;code&gt;NOW&lt;/code&gt;, the current local time is used.&lt;/p&gt;
&lt;p&gt;4) If &lt;code&gt;mtime&lt;/code&gt; is equal to &lt;code&gt;UTC&lt;/code&gt;, the current time in &lt;a href="http://en.wikipedia.org/wiki/Coordinated_Universal_Time"&gt;UTC&lt;/a&gt; is used.&lt;/p&gt;
&lt;p&gt;5) If &lt;code&gt;mtime&lt;/code&gt; is in the format like &lt;code&gt;NOW - 1 day&lt;/code&gt; or &lt;code&gt;UTC + 1 hour 30 min&lt;/code&gt;, the current local/UTC time plus/minus the time specified with the time string is used. The time string format is described in an appendix of Robot Framework User Guide.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Modified Time&lt;/td&gt;
&lt;td&gt;/path/file&lt;/td&gt;
&lt;td&gt;1177654467&lt;/td&gt;
&lt;td&gt;# Time given as epoch seconds&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Modified Time&lt;/td&gt;
&lt;td&gt;/path/file&lt;/td&gt;
&lt;td&gt;2007-04-27 9:14:27&lt;/td&gt;
&lt;td&gt;# Time given as a timestamp&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Modified Time&lt;/td&gt;
&lt;td&gt;/path/file&lt;/td&gt;
&lt;td&gt;NOW&lt;/td&gt;
&lt;td&gt;# The local time of execution&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Modified Time&lt;/td&gt;
&lt;td&gt;/path/file&lt;/td&gt;
&lt;td&gt;NOW - 1 day&lt;/td&gt;
&lt;td&gt;# 1 day subtracted from the local time&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Modified Time&lt;/td&gt;
&lt;td&gt;/path/file&lt;/td&gt;
&lt;td&gt;UTC + 1h 2min 3s&lt;/td&gt;
&lt;td&gt;# 1h 2min 3s added to the UTC time&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Sets the file modification and access times.</shortdoc>
</kw>
<kw name="Should Exist" lineno="345">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the given path (file or directory) exists.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails unless the given path (file or directory) exists.</shortdoc>
</kw>
<kw name="Should Not Exist" lineno="357">
<arguments repr="path, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given path (file or directory) exists.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Fails if the given path (file or directory) exists.</shortdoc>
</kw>
<kw name="Split Extension" lineno="1145">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Splits the extension from the given path.&lt;/p&gt;
&lt;p&gt;The given path is first normalized (e.g. possible trailing path separators removed, special directories &lt;code&gt;..&lt;/code&gt; and &lt;code&gt;.&lt;/code&gt; removed). The base path and extension are returned as separate components so that the dot used as an extension separator is removed. If the path contains no extension, an empty string is returned for it. Possible leading and trailing dots in the file name are never considered to be extension separators.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${path}&lt;/td&gt;
&lt;td&gt;${ext} =&lt;/td&gt;
&lt;td&gt;Split Extension&lt;/td&gt;
&lt;td&gt;file.extension&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p2}&lt;/td&gt;
&lt;td&gt;${e2} =&lt;/td&gt;
&lt;td&gt;Split Extension&lt;/td&gt;
&lt;td&gt;path/file.ext&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p3}&lt;/td&gt;
&lt;td&gt;${e3} =&lt;/td&gt;
&lt;td&gt;Split Extension&lt;/td&gt;
&lt;td&gt;path/file&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p4}&lt;/td&gt;
&lt;td&gt;${e4} =&lt;/td&gt;
&lt;td&gt;Split Extension&lt;/td&gt;
&lt;td&gt;p1/../p2/file.ext&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p5}&lt;/td&gt;
&lt;td&gt;${e5} =&lt;/td&gt;
&lt;td&gt;Split Extension&lt;/td&gt;
&lt;td&gt;path/.file.ext&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p6}&lt;/td&gt;
&lt;td&gt;${e6} =&lt;/td&gt;
&lt;td&gt;Split Extension&lt;/td&gt;
&lt;td&gt;path/.file&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;${path} = 'file' &amp;amp; ${ext} = 'extension'&lt;/li&gt;
&lt;li&gt;${p2} = 'path/file' &amp;amp; ${e2} = 'ext'&lt;/li&gt;
&lt;li&gt;${p3} = 'path/file' &amp;amp; ${e3} = ''&lt;/li&gt;
&lt;li&gt;${p4} = 'p2/file' &amp;amp; ${e4} = 'ext'&lt;/li&gt;
&lt;li&gt;${p5} = 'path/.file' &amp;amp; ${e5} = 'ext'&lt;/li&gt;
&lt;li&gt;${p6} = 'path/.file' &amp;amp; ${e6} = ''&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Splits the extension from the given path.</shortdoc>
</kw>
<kw name="Split Path" lineno="1126">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Splits the given path from the last path separator (&lt;code&gt;/&lt;/code&gt; or &lt;code&gt;\&lt;/code&gt;).&lt;/p&gt;
&lt;p&gt;The given path is first normalized (e.g. a possible trailing path separator is removed, special directories &lt;code&gt;..&lt;/code&gt; and &lt;code&gt;.&lt;/code&gt; removed). The parts that are split are returned as separate components.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${path1}&lt;/td&gt;
&lt;td&gt;${dir} =&lt;/td&gt;
&lt;td&gt;Split Path&lt;/td&gt;
&lt;td&gt;abc/def&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${path2}&lt;/td&gt;
&lt;td&gt;${file} =&lt;/td&gt;
&lt;td&gt;Split Path&lt;/td&gt;
&lt;td&gt;abc/def/ghi.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${path3}&lt;/td&gt;
&lt;td&gt;${d2}  =&lt;/td&gt;
&lt;td&gt;Split Path&lt;/td&gt;
&lt;td&gt;abc/../def/ghi/&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;${path1} = 'abc' &amp;amp; ${dir} = 'def'&lt;/li&gt;
&lt;li&gt;${path2} = 'abc/def' &amp;amp; ${file} = 'ghi.txt'&lt;/li&gt;
&lt;li&gt;${path3} = 'def' &amp;amp; ${d2} = 'ghi'&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Splits the given path from the last path separator (``/`` or ``\``).</shortdoc>
</kw>
<kw name="Touch" lineno="1378">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Emulates the UNIX touch command.&lt;/p&gt;
&lt;p&gt;Creates a file, if it does not exist. Otherwise changes its access and modification times to the current time.&lt;/p&gt;
&lt;p&gt;Fails if used with the directories or the parent directory of the given file does not exist.&lt;/p&gt;</doc>
<shortdoc>Emulates the UNIX touch command.</shortdoc>
</kw>
<kw name="Wait Until Created" lineno="461">
<arguments repr="path, timeout=1 minute">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=1 minute">
<name>timeout</name>
<default>1 minute</default>
</arg>
</arguments>
<doc>&lt;p&gt;Waits until the given file or directory is created.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. If the path is a pattern, the keyword returns when an item matching it is created.&lt;/p&gt;
&lt;p&gt;The optional &lt;code&gt;timeout&lt;/code&gt; can be used to control the maximum time of waiting. The timeout is given as a timeout string, e.g. in a format &lt;code&gt;15 seconds&lt;/code&gt;, &lt;code&gt;1min 10s&lt;/code&gt; or just &lt;code&gt;10&lt;/code&gt;. The time string format is described in an appendix of Robot Framework User Guide.&lt;/p&gt;
&lt;p&gt;If the timeout is negative, the keyword is never timed-out. The keyword returns immediately, if the path already exists.&lt;/p&gt;</doc>
<shortdoc>Waits until the given file or directory is created.</shortdoc>
</kw>
<kw name="Wait Until Removed" lineno="435">
<arguments repr="path, timeout=1 minute">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=1 minute">
<name>timeout</name>
<default>1 minute</default>
</arg>
</arguments>
<doc>&lt;p&gt;Waits until the given file or directory is removed.&lt;/p&gt;
&lt;p&gt;The path can be given as an exact path or as a glob pattern. The pattern matching syntax is explained in &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;. If the path is a pattern, the keyword waits until all matching items are removed.&lt;/p&gt;
&lt;p&gt;The optional &lt;code&gt;timeout&lt;/code&gt; can be used to control the maximum time of waiting. The timeout is given as a timeout string, e.g. in a format &lt;code&gt;15 seconds&lt;/code&gt;, &lt;code&gt;1min 10s&lt;/code&gt; or just &lt;code&gt;10&lt;/code&gt;. The time string format is described in an appendix of Robot Framework User Guide.&lt;/p&gt;
&lt;p&gt;If the timeout is negative, the keyword is never timed-out. The keyword returns immediately, if the path does not exist in the first place.&lt;/p&gt;</doc>
<shortdoc>Waits until the given file or directory is removed.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
