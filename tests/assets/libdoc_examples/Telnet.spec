<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="Telnet" type="LIBRARY" format="HTML" scope="SUITE" generated="2021-08-20T15:17:14Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/Telnet.py" lineno="36">
<version>4.1</version>
<doc>&lt;p&gt;A test library providing communication over Telnet connections.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;Telnet&lt;/code&gt; is Robot Framework's standard library that makes it possible to connect to Telnet servers and execute commands on the opened connections.&lt;/p&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#Connections" class="name"&gt;Connections&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Writing%20and%20reading" class="name"&gt;Writing and reading&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Terminal%20emulation" class="name"&gt;Terminal emulation&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Time%20string%20format" class="name"&gt;Time string format&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Importing" class="name"&gt;Importing&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Connections"&gt;Connections&lt;/h2&gt;
&lt;p&gt;The first step of using &lt;code&gt;Telnet&lt;/code&gt; is opening a connection with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; keyword. Typically the next step is logging in with &lt;a href="#Login" class="name"&gt;Login&lt;/a&gt; keyword, and in the end the opened connection can be closed with &lt;a href="#Close%20Connection" class="name"&gt;Close Connection&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;It is possible to open multiple connections and switch the active one using &lt;a href="#Switch%20Connection" class="name"&gt;Switch Connection&lt;/a&gt;. &lt;a href="#Close%20All%20Connections" class="name"&gt;Close All Connections&lt;/a&gt; can be used to close all the connections, which is especially useful in suite teardowns to guarantee that all connections are always closed.&lt;/p&gt;
&lt;h2 id="Writing and reading"&gt;Writing and reading&lt;/h2&gt;
&lt;p&gt;After opening a connection and possibly logging in, commands can be executed or text written to the connection for other reasons using &lt;a href="#Write" class="name"&gt;Write&lt;/a&gt; and &lt;a href="#Write%20Bare" class="name"&gt;Write Bare&lt;/a&gt; keywords. The main difference between these two is that the former adds a &lt;a href="#Configuration"&gt;configurable newline&lt;/a&gt; after the text automatically.&lt;/p&gt;
&lt;p&gt;After writing something to the connection, the resulting output can be read using &lt;a href="#Read" class="name"&gt;Read&lt;/a&gt;, &lt;a href="#Read%20Until" class="name"&gt;Read Until&lt;/a&gt;, &lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt;, and &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt; keywords. Which one to use depends on the context, but the latest one is often the most convenient.&lt;/p&gt;
&lt;p&gt;As a convenience when running a command, it is possible to use &lt;a href="#Execute%20Command" class="name"&gt;Execute Command&lt;/a&gt; that simply uses &lt;a href="#Write" class="name"&gt;Write&lt;/a&gt; and &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt; internally. &lt;a href="#Write%20Until%20Expected%20Output" class="name"&gt;Write Until Expected Output&lt;/a&gt; is useful if you need to wait until writing something produces a desired output.&lt;/p&gt;
&lt;p&gt;Written and read text is automatically encoded/decoded using a &lt;a href="#Configuration"&gt;configured encoding&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The ANSI escape codes, like cursor movement and color codes, are normally returned as part of the read operation. If an escape code occurs in middle of a search pattern it may also prevent finding the searched string. &lt;a href="#Terminal%20emulation" class="name"&gt;Terminal emulation&lt;/a&gt; can be used to process these escape codes as they would be if a real terminal would be in use.&lt;/p&gt;
&lt;h2 id="Configuration"&gt;Configuration&lt;/h2&gt;
&lt;p&gt;Many aspects related the connections can be easily configured either globally or per connection basis. Global configuration is done when &lt;a href="#Importing"&gt;library is imported&lt;/a&gt;, and these values can be overridden per connection by &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; or with setting specific keywords &lt;a href="#Set%20Timeout" class="name"&gt;Set Timeout&lt;/a&gt;, &lt;a href="#Set%20Newline" class="name"&gt;Set Newline&lt;/a&gt;, &lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt;, &lt;a href="#Set%20Encoding" class="name"&gt;Set Encoding&lt;/a&gt;, &lt;a href="#Set%20Default%20Log%20Level" class="name"&gt;Set Default Log Level&lt;/a&gt; and &lt;a href="#Set%20Telnetlib%20Log%20Level" class="name"&gt;Set Telnetlib Log Level&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Values of &lt;code&gt;environ_user&lt;/code&gt;, &lt;code&gt;window_size&lt;/code&gt;, &lt;code&gt;terminal_emulation&lt;/code&gt;, and &lt;code&gt;terminal_type&lt;/code&gt; can not be changed after opening the connection.&lt;/p&gt;
&lt;h3 id="Timeout"&gt;Timeout&lt;/h3&gt;
&lt;p&gt;Timeout defines how long is the maximum time to wait when reading output. It is used internally by &lt;a href="#Read%20Until" class="name"&gt;Read Until&lt;/a&gt;, &lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt;, &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt;, and &lt;a href="#Login" class="name"&gt;Login&lt;/a&gt; keywords. The default value is 3 seconds.&lt;/p&gt;
&lt;h3 id="Connection Timeout"&gt;Connection Timeout&lt;/h3&gt;
&lt;p&gt;Connection Timeout defines how long is the maximum time to wait when opening the telnet connection. It is used internally by &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;. The default value is the system global default timeout.&lt;/p&gt;
&lt;h3 id="Newline"&gt;Newline&lt;/h3&gt;
&lt;p&gt;Newline defines which line separator &lt;a href="#Write" class="name"&gt;Write&lt;/a&gt; keyword should use. The default value is &lt;code&gt;CRLF&lt;/code&gt; that is typically used by Telnet connections.&lt;/p&gt;
&lt;p&gt;Newline can be given either in escaped format using &lt;code&gt;\n&lt;/code&gt; and &lt;code&gt;\r&lt;/code&gt; or with special &lt;code&gt;LF&lt;/code&gt; and &lt;code&gt;CR&lt;/code&gt; syntax.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Newline" class="name"&gt;Set Newline&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;\n&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Newline" class="name"&gt;Set Newline&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;CRLF&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Prompt"&gt;Prompt&lt;/h3&gt;
&lt;p&gt;Often the easiest way to read the output of a command is reading all the output until the next prompt with &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt;. It also makes it easier, and faster, to verify did &lt;a href="#Login" class="name"&gt;Login&lt;/a&gt; succeed.&lt;/p&gt;
&lt;p&gt;Prompt can be specified either as a normal string or a regular expression. The latter is especially useful if the prompt changes as a result of the executed commands. Prompt can be set to be a regular expression by giving &lt;code&gt;prompt_is_regexp&lt;/code&gt; argument a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;).&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;prompt=$&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;(&amp;gt; |# )&lt;/td&gt;
&lt;td&gt;prompt_is_regexp=true&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Encoding"&gt;Encoding&lt;/h3&gt;
&lt;p&gt;To ease handling text containing non-ASCII characters, all written text is encoded and read text decoded by default. The default encoding is UTF-8 that works also with ASCII. Encoding can be disabled by using a special encoding value &lt;code&gt;NONE&lt;/code&gt;. This is mainly useful if you need to get the bytes received from the connection as-is.&lt;/p&gt;
&lt;p&gt;Notice that when writing to the connection, only Unicode strings are encoded using the defined encoding. Byte strings are expected to be already encoded correctly. Notice also that normal text in test data is passed to the library as Unicode and you need to use variables to use bytes.&lt;/p&gt;
&lt;p&gt;It is also possible to configure the error handler to use if encoding or decoding characters fails. Accepted values are the same that encode/decode functions in Python strings accept. In practice the following values are the most useful:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;ignore&lt;/code&gt;: ignore characters that cannot be encoded (default)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;strict&lt;/code&gt;: fail if characters cannot be encoded&lt;/li&gt;
&lt;li&gt;&lt;code&gt;replace&lt;/code&gt;: replace characters that cannot be encoded with a replacement character&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;encoding=Latin1&lt;/td&gt;
&lt;td&gt;encoding_errors=strict&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Encoding" class="name"&gt;Set Encoding&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;ISO-8859-15&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Encoding" class="name"&gt;Set Encoding&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;errors=ignore&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Default log level"&gt;Default log level&lt;/h3&gt;
&lt;p&gt;Default log level specifies the log level keywords use for &lt;a href="#Logging" class="name"&gt;logging&lt;/a&gt; unless they are given an explicit log level. The default value is &lt;code&gt;INFO&lt;/code&gt;, and changing it, for example, to &lt;code&gt;DEBUG&lt;/code&gt; can be a good idea if there is lot of unnecessary output that makes log files big.&lt;/p&gt;
&lt;h3 id="Terminal type"&gt;Terminal type&lt;/h3&gt;
&lt;p&gt;By default the Telnet library does not negotiate any specific terminal type with the server. If a specific terminal type, for example &lt;code&gt;vt100&lt;/code&gt;, is desired, the terminal type can be configured in &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; and with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;.&lt;/p&gt;
&lt;h3 id="Window size"&gt;Window size&lt;/h3&gt;
&lt;p&gt;Window size for negotiation with the server can be configured when &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; the library and with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;.&lt;/p&gt;
&lt;h3 id="USER environment variable"&gt;USER environment variable&lt;/h3&gt;
&lt;p&gt;Telnet protocol allows the &lt;code&gt;USER&lt;/code&gt; environment variable to be sent when connecting to the server. On some servers it may happen that there is no login prompt, and on those cases this configuration option will allow still to define the desired username. The option &lt;code&gt;environ_user&lt;/code&gt; can be used in &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; and with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;.&lt;/p&gt;
&lt;h2 id="Terminal emulation"&gt;Terminal emulation&lt;/h2&gt;
&lt;p&gt;Telnet library supports terminal emulation with &lt;a href="http://pyte.readthedocs.io"&gt;Pyte&lt;/a&gt;. Terminal emulation will process the output in a virtual screen. This means that ANSI escape codes, like cursor movements, and also control characters, like carriage returns and backspaces, have the same effect on the result as they would have on a normal terminal screen. For example the sequence &lt;code&gt;acdc\x1b[3Dbba&lt;/code&gt; will result in output &lt;code&gt;abba&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Terminal emulation is taken into use by giving &lt;code&gt;terminal_emulation&lt;/code&gt; argument a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) either in the library initialization or with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;As Pyte approximates vt-style terminal, you may also want to set the terminal type as &lt;code&gt;vt100&lt;/code&gt;. We also recommend that you increase the window size, as the terminal emulation will break all lines that are longer than the window row length.&lt;/p&gt;
&lt;p&gt;When terminal emulation is used, the &lt;a href="#Newline" class="name"&gt;newline&lt;/a&gt; and &lt;a href="#Encoding" class="name"&gt;encoding&lt;/a&gt; can not be changed anymore after opening the connection.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=True&lt;/td&gt;
&lt;td&gt;terminal_type=vt100&lt;/td&gt;
&lt;td&gt;window_size=400x100&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;As a prerequisite for using terminal emulation, you need to have Pyte installed. Due to backwards incompatible changes in Pyte, different Robot Framework versions support different Pyte versions:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Pyte 0.6 and newer are supported by Robot Framework 3.0.3. Latest Pyte version can be installed (or upgraded) with &lt;code&gt;pip install --upgrade pyte&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;Pyte 0.5.2 and older are supported by Robot Framework 3.0.2 and earlier. Pyte 0.5.2 can be installed with &lt;code&gt;pip install pyte==0.5.2&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Logging"&gt;Logging&lt;/h2&gt;
&lt;p&gt;All keywords that read something log the output. These keywords take the log level to use as an optional argument, and if no log level is specified they use the &lt;a href="#Configuration"&gt;configured&lt;/a&gt; default value.&lt;/p&gt;
&lt;p&gt;The valid log levels to use are &lt;code&gt;TRACE&lt;/code&gt;, &lt;code&gt;DEBUG&lt;/code&gt;, &lt;code&gt;INFO&lt;/code&gt; (default), and &lt;code&gt;WARN&lt;/code&gt;. Levels below &lt;code&gt;INFO&lt;/code&gt; are not shown in log files by default whereas warnings are shown more prominently.&lt;/p&gt;
&lt;p&gt;The &lt;a href="http://docs.python.org/library/telnetlib.html"&gt;telnetlib module&lt;/a&gt; used by this library has a custom logging system for logging content it sends and receives. By default these messages are written using &lt;code&gt;TRACE&lt;/code&gt; level, but the level is configurable with the &lt;code&gt;telnetlib_log_level&lt;/code&gt; option either in the library initialization, to the &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; or by using the &lt;a href="#Set%20Telnetlib%20Log%20Level" class="name"&gt;Set Telnetlib Log Level&lt;/a&gt; keyword to the active connection. Special level &lt;code&gt;NONE&lt;/code&gt; con be used to disable the logging altogether.&lt;/p&gt;
&lt;h2 id="Time string format"&gt;Time string format&lt;/h2&gt;
&lt;p&gt;Timeouts and other times used must be given as a time string using format like &lt;code&gt;15 seconds&lt;/code&gt; or &lt;code&gt;1min 10s&lt;/code&gt;. If the timeout is given as just a number, for example, &lt;code&gt;10&lt;/code&gt; or &lt;code&gt;1.5&lt;/code&gt;, it is considered to be seconds. The time string format is described in more detail in an appendix of &lt;a href="http://robotframework.org/robotframework/#user-guide"&gt;Robot Framework User Guide&lt;/a&gt;.&lt;/p&gt;
&lt;h2 id="Boolean arguments"&gt;Boolean arguments&lt;/h2&gt;
&lt;p&gt;Some keywords accept arguments that are handled as Boolean values true or false. If such an argument is given as a string, it is considered false if it is an empty string or equal to &lt;code&gt;FALSE&lt;/code&gt;, &lt;code&gt;NONE&lt;/code&gt;, &lt;code&gt;NO&lt;/code&gt;, &lt;code&gt;OFF&lt;/code&gt; or &lt;code&gt;0&lt;/code&gt;, case-insensitively. Other strings are considered true regardless their value, and other argument types are tested using the same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;True examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=True&lt;/td&gt;
&lt;td&gt;# Strings are generally true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=yes&lt;/td&gt;
&lt;td&gt;# Same as the above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=${TRUE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;True&lt;/code&gt; is true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=${42}&lt;/td&gt;
&lt;td&gt;# Numbers other than 0 are true.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;False examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=False&lt;/td&gt;
&lt;td&gt;# String &lt;code&gt;false&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=no&lt;/td&gt;
&lt;td&gt;# Also string &lt;code&gt;no&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=${EMPTY}&lt;/td&gt;
&lt;td&gt;# Empty string is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;lolcathost&lt;/td&gt;
&lt;td&gt;terminal_emulation=${FALSE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;False&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Considering string &lt;code&gt;NONE&lt;/code&gt; false is new in Robot Framework 3.0.3 and considering also &lt;code&gt;OFF&lt;/code&gt; and &lt;code&gt;0&lt;/code&gt; false is new in Robot Framework 3.1.&lt;/p&gt;</doc>
<tags>
</tags>
<inits>
<init name="Init" lineno="281">
<arguments repr="timeout=3 seconds, newline=CRLF, prompt=None, prompt_is_regexp=False, encoding=UTF-8, encoding_errors=ignore, default_log_level=INFO, window_size=None, environ_user=None, terminal_emulation=False, terminal_type=None, telnetlib_log_level=TRACE, connection_timeout=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=3 seconds">
<name>timeout</name>
<default>3 seconds</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="newline=CRLF">
<name>newline</name>
<default>CRLF</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prompt=None">
<name>prompt</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prompt_is_regexp=False">
<name>prompt_is_regexp</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding_errors=ignore">
<name>encoding_errors</name>
<default>ignore</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default_log_level=INFO">
<name>default_log_level</name>
<default>INFO</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="window_size=None">
<name>window_size</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="environ_user=None">
<name>environ_user</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="terminal_emulation=False">
<name>terminal_emulation</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="terminal_type=None">
<name>terminal_type</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="telnetlib_log_level=TRACE">
<name>telnetlib_log_level</name>
<default>TRACE</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="connection_timeout=None">
<name>connection_timeout</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Telnet library can be imported with optional configuration parameters.&lt;/p&gt;
&lt;p&gt;Configuration parameters are used as default values when new connections are opened with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; keyword. They can also be overridden after opening the connection using the &lt;span class="name"&gt;Set ...&lt;/span&gt; &lt;a href="#Keywords" class="name"&gt;keywords&lt;/a&gt;. See these keywords as well as &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt;, &lt;a href="#Terminal%20emulation" class="name"&gt;Terminal emulation&lt;/a&gt; and &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; sections above for more information about these parameters and their possible values.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Time%20string%20format" class="name"&gt;Time string format&lt;/a&gt; and &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt; sections for information about using arguments accepting times and Boolean values, respectively.&lt;/p&gt;
&lt;p&gt;Examples (use only one of these):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Setting&lt;/th&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;th&gt;Comment&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# default values&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;5 seconds&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# set only timeout&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;newline=LF&lt;/td&gt;
&lt;td&gt;encoding=ISO-8859-1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# set newline and encoding using named arguments&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;prompt=$&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# set prompt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;prompt=(&amp;gt; |# )&lt;/td&gt;
&lt;td&gt;prompt_is_regexp=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# set prompt as a regular expression&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;terminal_emulation=True&lt;/td&gt;
&lt;td&gt;terminal_type=vt100&lt;/td&gt;
&lt;td&gt;window_size=400x100&lt;/td&gt;
&lt;td&gt;# use terminal emulation with defined window size and terminal type&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Library&lt;/td&gt;
&lt;td&gt;Telnet&lt;/td&gt;
&lt;td&gt;telnetlib_log_level=NONE&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# disable logging messages from the underlying telnetlib&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Telnet library can be imported with optional configuration parameters.</shortdoc>
</init>
</inits>
<keywords>
<kw name="Close All Connections" lineno="470">
<arguments repr="">
</arguments>
<doc>&lt;p&gt;Closes all open connections and empties the connection cache.&lt;/p&gt;
&lt;p&gt;If multiple connections are opened, this keyword should be used in a test or suite teardown to make sure that all connections are closed. It is not an error is some of the connections have already been closed by &lt;a href="#Close%20Connection" class="name"&gt;Close Connection&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;After this keyword, new indexes returned by &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; keyword are reset to 1.&lt;/p&gt;</doc>
<shortdoc>Closes all open connections and empties the connection cache.</shortdoc>
</kw>
<kw name="Close Connection" lineno="687">
<arguments repr="loglevel=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Closes the current Telnet connection.&lt;/p&gt;
&lt;p&gt;Remaining output in the connection is read, logged, and returned. It is not an error to close an already closed connection.&lt;/p&gt;
&lt;p&gt;Use &lt;a href="#Close%20All%20Connections" class="name"&gt;Close All Connections&lt;/a&gt; if you want to make sure all opened connections are closed.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels.&lt;/p&gt;</doc>
<shortdoc>Closes the current Telnet connection.</shortdoc>
</kw>
<kw name="Execute Command" lineno="1056">
<arguments repr="command, loglevel=None, strip_prompt=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_prompt=False">
<name>strip_prompt</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Executes the given &lt;code&gt;command&lt;/code&gt; and reads, logs, and returns everything until the prompt.&lt;/p&gt;
&lt;p&gt;This keyword requires the prompt to be &lt;a href="#Configuration"&gt;configured&lt;/a&gt; either in &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; or with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; or &lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;This is a convenience keyword that uses &lt;a href="#Write" class="name"&gt;Write&lt;/a&gt; and &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt; internally. Following two examples are thus functionally identical:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${out} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Execute%20Command" class="name"&gt;Execute Command&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;pwd&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Write" class="name"&gt;Write&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;pwd&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${out} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels and &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt; for more information about the &lt;code&gt;strip_prompt&lt;/code&gt; parameter.&lt;/p&gt;</doc>
<shortdoc>Executes the given ``command`` and reads, logs, and returns everything until the prompt.</shortdoc>
</kw>
<kw name="Login" lineno="705">
<arguments repr="username, password, login_prompt=login: \, password_prompt=Password: \, login_timeout=1 second, login_incorrect=Login incorrect">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="username">
<name>username</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="password">
<name>password</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="login_prompt=login: \">
<name>login_prompt</name>
<default>login: \</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="password_prompt=Password: \">
<name>password_prompt</name>
<default>Password: \</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="login_timeout=1 second">
<name>login_timeout</name>
<default>1 second</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="login_incorrect=Login incorrect">
<name>login_incorrect</name>
<default>Login incorrect</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs in to the Telnet server with the given user information.&lt;/p&gt;
&lt;p&gt;This keyword reads from the connection until the &lt;code&gt;login_prompt&lt;/code&gt; is encountered and then types the given &lt;code&gt;username&lt;/code&gt;. Then it reads until the &lt;code&gt;password_prompt&lt;/code&gt; and types the given &lt;code&gt;password&lt;/code&gt;. In both cases a newline is appended automatically and the connection specific timeout used when waiting for outputs.&lt;/p&gt;
&lt;p&gt;How logging status is verified depends on whether a prompt is set for this connection or not:&lt;/p&gt;
&lt;p&gt;1) If the prompt is set, this keyword reads the output until the prompt is found using the normal timeout. If no prompt is found, login is considered failed and also this keyword fails. Note that in this case both &lt;code&gt;login_timeout&lt;/code&gt; and &lt;code&gt;login_incorrect&lt;/code&gt; arguments are ignored.&lt;/p&gt;
&lt;p&gt;2) If the prompt is not set, this keywords sleeps until &lt;code&gt;login_timeout&lt;/code&gt; and then reads all the output available on the connection. If the output contains &lt;code&gt;login_incorrect&lt;/code&gt; text, login is considered failed and also this keyword fails.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt; section for more information about setting newline, timeout, and prompt.&lt;/p&gt;</doc>
<shortdoc>Logs in to the Telnet server with the given user information.</shortdoc>
</kw>
<kw name="Open Connection" lineno="362">
<arguments repr="host, alias=None, port=23, timeout=None, newline=None, prompt=None, prompt_is_regexp=False, encoding=None, encoding_errors=None, default_log_level=None, window_size=None, environ_user=None, terminal_emulation=None, terminal_type=None, telnetlib_log_level=None, connection_timeout=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="host">
<name>host</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="alias=None">
<name>alias</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="port=23">
<name>port</name>
<default>23</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=None">
<name>timeout</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="newline=None">
<name>newline</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prompt=None">
<name>prompt</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prompt_is_regexp=False">
<name>prompt_is_regexp</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=None">
<name>encoding</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding_errors=None">
<name>encoding_errors</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default_log_level=None">
<name>default_log_level</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="window_size=None">
<name>window_size</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="environ_user=None">
<name>environ_user</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="terminal_emulation=None">
<name>terminal_emulation</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="terminal_type=None">
<name>terminal_type</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="telnetlib_log_level=None">
<name>telnetlib_log_level</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="connection_timeout=None">
<name>connection_timeout</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Opens a new Telnet connection to the given host and port.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;timeout&lt;/code&gt;, &lt;code&gt;newline&lt;/code&gt;, &lt;code&gt;prompt&lt;/code&gt;, &lt;code&gt;prompt_is_regexp&lt;/code&gt;, &lt;code&gt;encoding&lt;/code&gt;, &lt;code&gt;default_log_level&lt;/code&gt;, &lt;code&gt;window_size&lt;/code&gt;, &lt;code&gt;environ_user&lt;/code&gt;, &lt;code&gt;terminal_emulation&lt;/code&gt;, &lt;code&gt;terminal_type&lt;/code&gt; and &lt;code&gt;telnetlib_log_level&lt;/code&gt; arguments get default values when the library is &lt;a href="#Importing"&gt;imported&lt;/a&gt;. Setting them here overrides those values for the opened connection. See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt;, &lt;a href="#Terminal%20emulation" class="name"&gt;Terminal emulation&lt;/a&gt; and &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; sections for more information about these parameters and their possible values.&lt;/p&gt;
&lt;p&gt;Possible already opened connections are cached and it is possible to switch back to them using &lt;a href="#Switch%20Connection" class="name"&gt;Switch Connection&lt;/a&gt; keyword. It is possible to switch either using explicitly given &lt;code&gt;alias&lt;/code&gt; or using index returned by this keyword. Indexing starts from 1 and is reset back to it by &lt;a href="#Close%20All%20Connections" class="name"&gt;Close All Connections&lt;/a&gt; keyword.&lt;/p&gt;</doc>
<shortdoc>Opens a new Telnet connection to the given host and port.</shortdoc>
</kw>
<kw name="Read" lineno="875">
<arguments repr="loglevel=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Reads everything that is currently available in the output.&lt;/p&gt;
&lt;p&gt;Read output is both returned and logged. See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels.&lt;/p&gt;</doc>
<shortdoc>Reads everything that is currently available in the output.</shortdoc>
</kw>
<kw name="Read Until" lineno="889">
<arguments repr="expected, loglevel=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected">
<name>expected</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Reads output until &lt;code&gt;expected&lt;/code&gt; text is encountered.&lt;/p&gt;
&lt;p&gt;Text up to and including the match is returned and logged. If no match is found, this keyword fails. How much to wait for the output depends on the &lt;a href="#Configuration"&gt;configured timeout&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels. Use &lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt; if more complex matching is needed.&lt;/p&gt;</doc>
<shortdoc>Reads output until ``expected`` text is encountered.</shortdoc>
</kw>
<kw name="Read Until Prompt" lineno="1011">
<arguments repr="loglevel=None, strip_prompt=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_prompt=False">
<name>strip_prompt</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Reads output until the prompt is encountered.&lt;/p&gt;
&lt;p&gt;This keyword requires the prompt to be &lt;a href="#Configuration"&gt;configured&lt;/a&gt; either in &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; or with &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; or &lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;By default, text up to and including the prompt is returned and logged. If no prompt is found, this keyword fails. How much to wait for the output depends on the &lt;a href="#Configuration"&gt;configured timeout&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If you want to exclude the prompt from the returned output, set &lt;code&gt;strip_prompt&lt;/code&gt; to a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). If your prompt is a regular expression, make sure that the expression spans the whole prompt, because only the part of the output that matches the regular expression is stripped away.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels.&lt;/p&gt;</doc>
<shortdoc>Reads output until the prompt is encountered.</shortdoc>
</kw>
<kw name="Read Until Regexp" lineno="973">
<arguments repr="*expected">
<arg kind="VAR_POSITIONAL" required="false" repr="*expected">
<name>expected</name>
</arg>
</arguments>
<doc>&lt;p&gt;Reads output until any of the &lt;code&gt;expected&lt;/code&gt; regular expressions match.&lt;/p&gt;
&lt;p&gt;This keyword accepts any number of regular expressions patterns or compiled Python regular expression objects as arguments. Text up to and including the first match to any of the regular expressions is returned and logged. If no match is found, this keyword fails. How much to wait for the output depends on the &lt;a href="#Configuration"&gt;configured timeout&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If the last given argument is a &lt;a href="#Logging"&gt;valid log level&lt;/a&gt;, it is used as &lt;code&gt;loglevel&lt;/code&gt; similarly as with &lt;a href="#Read%20Until" class="name"&gt;Read Until&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;See the documentation of &lt;a href="http://docs.python.org/library/re.html"&gt;Python re module&lt;/a&gt; for more information about the supported regular expression syntax. Notice that possible backslashes need to be escaped in Robot Framework test data.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;(#|$)&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;first_regexp&lt;/td&gt;
&lt;td&gt;second_regexp&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;\\d{4}-\\d{2}-\\d{2}&lt;/td&gt;
&lt;td&gt;DEBUG&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Reads output until any of the ``expected`` regular expressions match.</shortdoc>
</kw>
<kw name="Set Default Log Level" lineno="661">
<arguments repr="level">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="level">
<name>level</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the default log level used for &lt;a href="#Logging" class="name"&gt;logging&lt;/a&gt; in the current connection.&lt;/p&gt;
&lt;p&gt;The old default log level is returned and can be used to restore the log level later.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt; section for more information about global and connection specific configuration.&lt;/p&gt;</doc>
<shortdoc>Sets the default log level used for `logging` in the current connection.</shortdoc>
</kw>
<kw name="Set Encoding" lineno="602">
<arguments repr="encoding=None, errors=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=None">
<name>encoding</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="errors=None">
<name>errors</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the encoding to use for &lt;a href="#Writing%20and%20reading" class="name"&gt;writing and reading&lt;/a&gt; in the current connection.&lt;/p&gt;
&lt;p&gt;The given &lt;code&gt;encoding&lt;/code&gt; specifies the encoding to use when written/read text is encoded/decoded, and &lt;code&gt;errors&lt;/code&gt; specifies the error handler to use if encoding/decoding fails. Either of these can be omitted and in that case the old value is not affected. Use string &lt;code&gt;NONE&lt;/code&gt; to disable encoding altogether.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt; section for more information about encoding and error handlers, as well as global and connection specific configuration in general.&lt;/p&gt;
&lt;p&gt;The old values are returned and can be used to restore the encoding and the error handler later. See &lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt; for a similar example.&lt;/p&gt;
&lt;p&gt;If terminal emulation is used, the encoding can not be changed on an open connection.&lt;/p&gt;</doc>
<shortdoc>Sets the encoding to use for `writing and reading` in the current connection.</shortdoc>
</kw>
<kw name="Set Newline" lineno="540">
<arguments repr="newline">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="newline">
<name>newline</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the newline used by &lt;a href="#Write" class="name"&gt;Write&lt;/a&gt; keyword in the current connection.&lt;/p&gt;
&lt;p&gt;The old newline is returned and can be used to restore the newline later. See &lt;a href="#Set%20Timeout" class="name"&gt;Set Timeout&lt;/a&gt; for a similar example.&lt;/p&gt;
&lt;p&gt;If terminal emulation is used, the newline can not be changed on an open connection.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt; section for more information about global and connection specific configuration.&lt;/p&gt;</doc>
<shortdoc>Sets the newline used by `Write` keyword in the current connection.</shortdoc>
</kw>
<kw name="Set Prompt" lineno="563">
<arguments repr="prompt, prompt_is_regexp=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="prompt">
<name>prompt</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="prompt_is_regexp=False">
<name>prompt_is_regexp</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the prompt used by &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt; and &lt;a href="#Login" class="name"&gt;Login&lt;/a&gt; in the current connection.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;prompt_is_regexp&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the given &lt;code&gt;prompt&lt;/code&gt; is considered to be a regular expression.&lt;/p&gt;
&lt;p&gt;The old prompt is returned and can be used to restore the prompt later.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${prompt}&lt;/td&gt;
&lt;td&gt;${regexp} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;$&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Do Something&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Prompt" class="name"&gt;Set Prompt&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${prompt}&lt;/td&gt;
&lt;td&gt;${regexp}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See the documentation of &lt;a href="http://docs.python.org/library/re.html"&gt;Python re module&lt;/a&gt; for more information about the supported regular expression syntax. Notice that possible backslashes need to be escaped in Robot Framework test data.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt; section for more information about global and connection specific configuration.&lt;/p&gt;</doc>
<shortdoc>Sets the prompt used by `Read Until Prompt` and `Login` in the current connection.</shortdoc>
</kw>
<kw name="Set Telnetlib Log Level" lineno="643">
<arguments repr="level">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="level">
<name>level</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the log level used for &lt;a href="#Logging" class="name"&gt;logging&lt;/a&gt; in the underlying &lt;code&gt;telnetlib&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Note that &lt;code&gt;telnetlib&lt;/code&gt; can be very noisy thus using the level &lt;code&gt;NONE&lt;/code&gt; can shutdown the messages generated by this library.&lt;/p&gt;</doc>
<shortdoc>Sets the log level used for `logging` in the underlying ``telnetlib``.</shortdoc>
</kw>
<kw name="Set Timeout" lineno="514">
<arguments repr="timeout">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="timeout">
<name>timeout</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the timeout used for waiting output in the current connection.&lt;/p&gt;
&lt;p&gt;Read operations that expect some output to appear (&lt;a href="#Read%20Until" class="name"&gt;Read Until&lt;/a&gt;, &lt;a href="#Read%20Until%20Regexp" class="name"&gt;Read Until Regexp&lt;/a&gt;, &lt;a href="#Read%20Until%20Prompt" class="name"&gt;Read Until Prompt&lt;/a&gt;, &lt;a href="#Login" class="name"&gt;Login&lt;/a&gt;) use this timeout and fail if the expected output does not appear before this timeout expires.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;timeout&lt;/code&gt; must be given in &lt;a href="#Time%20string%20format" class="name"&gt;time string format&lt;/a&gt;. The old timeout is returned and can be used to restore the timeout later.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${old} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Set%20Timeout" class="name"&gt;Set Timeout&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;2 minute 30 seconds&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Do Something&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Set%20Timeout" class="name"&gt;Set Timeout&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${old}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Configuration" class="name"&gt;Configuration&lt;/a&gt; section for more information about global and connection specific configuration.&lt;/p&gt;</doc>
<shortdoc>Sets the timeout used for waiting output in the current connection.</shortdoc>
</kw>
<kw name="Switch Connection" lineno="434">
<arguments repr="index_or_alias">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="index_or_alias">
<name>index_or_alias</name>
</arg>
</arguments>
<doc>&lt;p&gt;Switches between active connections using an index or an alias.&lt;/p&gt;
&lt;p&gt;Aliases can be given to &lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt; keyword which also always returns the connection index.&lt;/p&gt;
&lt;p&gt;This keyword returns the index of previous active connection.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;myhost.net&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Login" class="name"&gt;Login&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;john&lt;/td&gt;
&lt;td&gt;secret&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Write" class="name"&gt;Write&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;some command&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;yourhost.com&lt;/td&gt;
&lt;td&gt;2nd conn&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Login" class="name"&gt;Login&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;root&lt;/td&gt;
&lt;td&gt;password&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Write" class="name"&gt;Write&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;another cmd&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${old index}=&lt;/td&gt;
&lt;td&gt;&lt;a href="#Switch%20Connection" class="name"&gt;Switch Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;# index&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Write" class="name"&gt;Write&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;something&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Switch%20Connection" class="name"&gt;Switch Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;2nd conn&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# alias&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Write" class="name"&gt;Write&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;whatever&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Switch%20Connection" class="name"&gt;Switch Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${old index}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# back to original&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;[Teardown]&lt;/td&gt;
&lt;td&gt;&lt;a href="#Close%20All%20Connections" class="name"&gt;Close All Connections&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The example above expects that there were no other open connections when opening the first one, because it used index &lt;code&gt;1&lt;/code&gt; when switching to the connection later. If you are not sure about that, you can store the index into a variable as shown below.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${index} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Open%20Connection" class="name"&gt;Open Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;myhost.net&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Do Something&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Switch%20Connection" class="name"&gt;Switch Connection&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${index}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Switches between active connections using an index or an alias.</shortdoc>
</kw>
<kw name="Write" lineno="760">
<arguments repr="text, loglevel=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="text">
<name>text</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Writes the given text plus a newline into the connection.&lt;/p&gt;
&lt;p&gt;The newline character sequence to use can be &lt;a href="#Configuration"&gt;configured&lt;/a&gt; both globally and per connection basis. The default value is &lt;code&gt;CRLF&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword consumes the written text, until the added newline, from the output and logs and returns it. The given text itself must not contain newlines. Use &lt;a href="#Write%20Bare" class="name"&gt;Write Bare&lt;/a&gt; instead if either of these features causes a problem.&lt;/p&gt;
&lt;p&gt;&lt;b&gt;Note:&lt;/b&gt; This keyword does not return the possible output of the executed command. To get the output, one of the &lt;span class="name"&gt;Read ...&lt;/span&gt; &lt;a href="#Keywords" class="name"&gt;keywords&lt;/a&gt; must be used. See &lt;a href="#Writing%20and%20reading" class="name"&gt;Writing and reading&lt;/a&gt; section for more details.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels.&lt;/p&gt;</doc>
<shortdoc>Writes the given text plus a newline into the connection.</shortdoc>
</kw>
<kw name="Write Bare" lineno="790">
<arguments repr="text">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="text">
<name>text</name>
</arg>
</arguments>
<doc>&lt;p&gt;Writes the given text, and nothing else, into the connection.&lt;/p&gt;
&lt;p&gt;This keyword does not append a newline nor consume the written text. Use &lt;a href="#Write" class="name"&gt;Write&lt;/a&gt; if these features are needed.&lt;/p&gt;</doc>
<shortdoc>Writes the given text, and nothing else, into the connection.</shortdoc>
</kw>
<kw name="Write Control Character" lineno="836">
<arguments repr="character">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="character">
<name>character</name>
</arg>
</arguments>
<doc>&lt;p&gt;Writes the given control character into the connection.&lt;/p&gt;
&lt;p&gt;The control character is prepended with an IAC (interpret as command) character.&lt;/p&gt;
&lt;p&gt;The following control character names are supported: BRK, IP, AO, AYT, EC, EL, NOP. Additionally, you can use arbitrary numbers to send any control character.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Write Control Character&lt;/td&gt;
&lt;td&gt;BRK&lt;/td&gt;
&lt;td&gt;# Send Break command&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Write Control Character&lt;/td&gt;
&lt;td&gt;241&lt;/td&gt;
&lt;td&gt;# Send No operation command&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Writes the given control character into the connection.</shortdoc>
</kw>
<kw name="Write Until Expected Output" lineno="799">
<arguments repr="text, expected, timeout, retry_interval, loglevel=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="text">
<name>text</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected">
<name>expected</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="timeout">
<name>timeout</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="retry_interval">
<name>retry_interval</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="loglevel=None">
<name>loglevel</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Writes the given &lt;code&gt;text&lt;/code&gt; repeatedly, until &lt;code&gt;expected&lt;/code&gt; appears in the output.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;text&lt;/code&gt; is written without appending a newline and it is consumed from the output before trying to find &lt;code&gt;expected&lt;/code&gt;. If &lt;code&gt;expected&lt;/code&gt; does not appear in the output within &lt;code&gt;timeout&lt;/code&gt;, this keyword fails.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;retry_interval&lt;/code&gt; defines the time to wait &lt;code&gt;expected&lt;/code&gt; to appear before writing the &lt;code&gt;text&lt;/code&gt; again. Consuming the written &lt;code&gt;text&lt;/code&gt; is subject to the normal &lt;a href="#Configuration"&gt;configured timeout&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Both &lt;code&gt;timeout&lt;/code&gt; and &lt;code&gt;retry_interval&lt;/code&gt; must be given in &lt;a href="#Time%20string%20format" class="name"&gt;time string format&lt;/a&gt;. See &lt;a href="#Logging" class="name"&gt;Logging&lt;/a&gt; section for more information about log levels.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Write Until Expected Output&lt;/td&gt;
&lt;td&gt;ps -ef| grep myprocess\r\n&lt;/td&gt;
&lt;td&gt;myprocess&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;5 s&lt;/td&gt;
&lt;td&gt;0.5 s&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The above example writes command &lt;code&gt;ps -ef | grep myprocess\r\n&lt;/code&gt; until &lt;code&gt;myprocess&lt;/code&gt; appears in the output. The command is written every 0.5 seconds and the keyword fails if &lt;code&gt;myprocess&lt;/code&gt; does not appear in the output in 5 seconds.&lt;/p&gt;</doc>
<shortdoc>Writes the given ``text`` repeatedly, until ``expected`` appears in the output.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
