<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="Process" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2021-08-20T15:17:13Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/Process.py" lineno="30">
<version>4.1</version>
<doc>&lt;p&gt;Robot Framework test library for running processes.&lt;/p&gt;
&lt;p&gt;This library utilizes Python's &lt;a href="http://docs.python.org/library/subprocess.html"&gt;subprocess&lt;/a&gt; module and its &lt;a href="http://docs.python.org/library/subprocess.html#popen-constructor"&gt;Popen&lt;/a&gt; class.&lt;/p&gt;
&lt;p&gt;The library has following main usages:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Running processes in system and waiting for their completion using &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; keyword.&lt;/li&gt;
&lt;li&gt;Starting processes on background using &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;Waiting started process to complete using &lt;a href="#Wait%20For%20Process" class="name"&gt;Wait For Process&lt;/a&gt; or stopping them with &lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt; or &lt;a href="#Terminate%20All%20Processes" class="name"&gt;Terminate All Processes&lt;/a&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#Specifying%20command%20and%20arguments" class="name"&gt;Specifying command and arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Process%20configuration" class="name"&gt;Process configuration&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Active%20process" class="name"&gt;Active process&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Result%20object" class="name"&gt;Result object&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Specifying command and arguments"&gt;Specifying command and arguments&lt;/h2&gt;
&lt;p&gt;Both &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; and &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; accept the command to execute and all arguments passed to the command as separate arguments. This makes usage convenient and also allows these keywords to automatically escape possible spaces and other special characters in commands and arguments. Notice that if a command accepts options that themselves accept values, these options and their values must be given as separate arguments.&lt;/p&gt;
&lt;p&gt;When &lt;a href="#Running%20processes%20in%20shell" class="name"&gt;running processes in shell&lt;/a&gt;, it is also possible to give the whole command to execute as a single string. The command can then contain multiple commands to be run together. When using this approach, the caller is responsible on escaping.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${tools}${/}prog.py&lt;/td&gt;
&lt;td&gt;argument&lt;/td&gt;
&lt;td&gt;second arg with spaces&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;java&lt;/td&gt;
&lt;td&gt;-jar&lt;/td&gt;
&lt;td&gt;${jars}${/}example.jar&lt;/td&gt;
&lt;td&gt;--option&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;prog.py "one arg" &amp;amp;&amp;amp; tool.sh&lt;/td&gt;
&lt;td&gt;shell=yes&lt;/td&gt;
&lt;td&gt;cwd=${tools}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Possible non-string arguments are converted to strings automatically.&lt;/p&gt;
&lt;h2 id="Process configuration"&gt;Process configuration&lt;/h2&gt;
&lt;p&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; and &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; keywords can be configured using optional &lt;code&gt;**configuration&lt;/code&gt; keyword arguments. Configuration arguments must be given after other arguments passed to these keywords and must use syntax like &lt;code&gt;name=value&lt;/code&gt;. Available configuration arguments are listed below and discussed further in sections afterwards.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Name&lt;/th&gt;
&lt;th&gt;Explanation&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;shell&lt;/td&gt;
&lt;td&gt;Specifies whether to run the command in shell or not.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;cwd&lt;/td&gt;
&lt;td&gt;Specifies the working directory.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;env&lt;/td&gt;
&lt;td&gt;Specifies environment variables given to the process.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;env:&amp;lt;name&amp;gt;&lt;/td&gt;
&lt;td&gt;Overrides the named environment variable(s) only.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;stdout&lt;/td&gt;
&lt;td&gt;Path of a file where to write standard output.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;stderr&lt;/td&gt;
&lt;td&gt;Path of a file where to write standard error.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;output_encoding&lt;/td&gt;
&lt;td&gt;Encoding to use when reading command outputs.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;alias&lt;/td&gt;
&lt;td&gt;Alias given to the process.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Note that because &lt;code&gt;**configuration&lt;/code&gt; is passed using &lt;code&gt;name=value&lt;/code&gt; syntax, possible equal signs in other arguments passed to &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; and &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; must be escaped with a backslash like &lt;code&gt;name\=value&lt;/code&gt;. See &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; for an example.&lt;/p&gt;
&lt;h3 id="Running processes in shell"&gt;Running processes in shell&lt;/h3&gt;
&lt;p&gt;The &lt;code&gt;shell&lt;/code&gt; argument specifies whether to run the process in a shell or not. By default shell is not used, which means that shell specific commands, like &lt;code&gt;copy&lt;/code&gt; and &lt;code&gt;dir&lt;/code&gt; on Windows, are not available. You can, however, run shell scripts and batch files without using a shell.&lt;/p&gt;
&lt;p&gt;Giving the &lt;code&gt;shell&lt;/code&gt; argument any non-false value, such as &lt;code&gt;shell=True&lt;/code&gt;, changes the program to be executed in a shell. It allows using the shell capabilities, but can also make the process invocation operating system dependent. Having a shell between the actually started process and this library can also interfere communication with the process such as stopping it and reading its outputs. Because of these problems, it is recommended to use the shell only when absolutely necessary.&lt;/p&gt;
&lt;p&gt;When using a shell it is possible to give the whole command to execute as a single string. See &lt;a href="#Specifying%20command%20and%20arguments" class="name"&gt;Specifying command and arguments&lt;/a&gt; section for examples and more details in general.&lt;/p&gt;
&lt;h3 id="Current working directory"&gt;Current working directory&lt;/h3&gt;
&lt;p&gt;By default the child process will be executed in the same directory as the parent process, the process running tests, is executed. This can be changed by giving an alternative location using the &lt;code&gt;cwd&lt;/code&gt; argument. Forward slashes in the given path are automatically converted to backslashes on Windows.&lt;/p&gt;
&lt;p&gt;&lt;a href="#Standard%20output%20and%20error%20streams" class="name"&gt;Standard output and error streams&lt;/a&gt;, when redirected to files, are also relative to the current working directory possibly set using the &lt;code&gt;cwd&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;prog.exe&lt;/td&gt;
&lt;td&gt;cwd=${ROOT}/directory&lt;/td&gt;
&lt;td&gt;stdout=stdout.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Environment variables"&gt;Environment variables&lt;/h3&gt;
&lt;p&gt;By default the child process will get a copy of the parent process's environment variables. The &lt;code&gt;env&lt;/code&gt; argument can be used to give the child a custom environment as a Python dictionary. If there is a need to specify only certain environment variable, it is possible to use the &lt;code&gt;env:&amp;lt;name&amp;gt;=&amp;lt;value&amp;gt;&lt;/code&gt; format to set or override only that named variables. It is also possible to use these two approaches together.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;env=${environ}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;env:http_proxy=10.144.1.10:8080&lt;/td&gt;
&lt;td&gt;env:PATH=%{PATH}${:}${PROGDIR}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;env=${environ}&lt;/td&gt;
&lt;td&gt;env:EXTRA=value&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Standard output and error streams"&gt;Standard output and error streams&lt;/h3&gt;
&lt;p&gt;By default processes are run so that their standard output and standard error streams are kept in the memory. This works fine normally, but if there is a lot of output, the output buffers may get full and the program can hang. Additionally on Jython, everything written to these in-memory buffers can be lost if the process is terminated.&lt;/p&gt;
&lt;p&gt;To avoid the above mentioned problems, it is possible to use &lt;code&gt;stdout&lt;/code&gt; and &lt;code&gt;stderr&lt;/code&gt; arguments to specify files on the file system where to redirect the outputs. This can also be useful if other processes or other keywords need to read or manipulate the outputs somehow.&lt;/p&gt;
&lt;p&gt;Given &lt;code&gt;stdout&lt;/code&gt; and &lt;code&gt;stderr&lt;/code&gt; paths are relative to the &lt;a href="#Current%20working%20directory" class="name"&gt;current working directory&lt;/a&gt;. Forward slashes in the given paths are automatically converted to backslashes on Windows.&lt;/p&gt;
&lt;p&gt;As a special feature, it is possible to redirect the standard error to the standard output by using &lt;code&gt;stderr=STDOUT&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Regardless are outputs redirected to files or not, they are accessible through the &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; returned when the process ends. Commands are expected to write outputs using the console encoding, but &lt;a href="#Output%20encoding" class="name"&gt;output encoding&lt;/a&gt; can be configured using the &lt;code&gt;output_encoding&lt;/code&gt; argument if needed.&lt;/p&gt;
&lt;p&gt;If you are not interested in outputs at all, you can explicitly ignore them by using a special value &lt;code&gt;DEVNULL&lt;/code&gt; both with &lt;code&gt;stdout&lt;/code&gt; and &lt;code&gt;stderr&lt;/code&gt;. For example, &lt;code&gt;stdout=DEVNULL&lt;/code&gt; is the same as redirecting output on console with &lt;code&gt;&amp;gt; /dev/null&lt;/code&gt; on UNIX-like operating systems or &lt;code&gt;&amp;gt; NUL&lt;/code&gt; on Windows. This way the process will not hang even if there would be a lot of output, but naturally output is not available after execution either.&lt;/p&gt;
&lt;p&gt;Support for the special value &lt;code&gt;DEVNULL&lt;/code&gt; is new in Robot Framework 3.2.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;stdout=${TEMPDIR}/stdout.txt&lt;/td&gt;
&lt;td&gt;stderr=${TEMPDIR}/stderr.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Log Many&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;stdout: ${result.stdout}&lt;/td&gt;
&lt;td&gt;stderr: ${result.stderr}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;stderr=STDOUT&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Log&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;all output: ${result.stdout}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;stdout=DEVNULL&lt;/td&gt;
&lt;td&gt;stderr=DEVNULL&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Note that the created output files are not automatically removed after the test run. The user is responsible to remove them if needed.&lt;/p&gt;
&lt;h3 id="Output encoding"&gt;Output encoding&lt;/h3&gt;
&lt;p&gt;Executed commands are, by default, expected to write outputs to the &lt;a href="#Standard%20output%20and%20error%20streams" class="name"&gt;standard output and error streams&lt;/a&gt; using the encoding used by the system console. If the command uses some other encoding, that can be configured using the &lt;code&gt;output_encoding&lt;/code&gt; argument. This is especially useful on Windows where the console uses a different encoding than rest of the system, and many commands use the general system encoding instead of the console encoding.&lt;/p&gt;
&lt;p&gt;The value used with the &lt;code&gt;output_encoding&lt;/code&gt; argument must be a valid encoding and must match the encoding actually used by the command. As a convenience, it is possible to use strings &lt;code&gt;CONSOLE&lt;/code&gt; and &lt;code&gt;SYSTEM&lt;/code&gt; to specify that the console or system encoding is used, respectively. If produced outputs use different encoding then configured, values got through the &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; will be invalid.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;output_encoding=UTF-8&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;stdout=${path}&lt;/td&gt;
&lt;td&gt;output_encoding=SYSTEM&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Alias"&gt;Alias&lt;/h3&gt;
&lt;p&gt;A custom name given to the process that can be used when selecting the &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;td&gt;alias=example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;python&lt;/td&gt;
&lt;td&gt;-c&lt;/td&gt;
&lt;td&gt;print('hello')&lt;/td&gt;
&lt;td&gt;alias=hello&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Active process"&gt;Active process&lt;/h2&gt;
&lt;p&gt;The test library keeps record which of the started processes is currently active. By default it is latest process started with &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;, but &lt;a href="#Switch%20Process" class="name"&gt;Switch Process&lt;/a&gt; can be used to select a different one. Using &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; does not affect the active process.&lt;/p&gt;
&lt;p&gt;The keywords that operate on started processes will use the active process by default, but it is possible to explicitly select a different process using the &lt;code&gt;handle&lt;/code&gt; argument. The handle can be the identifier returned by &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; or an &lt;code&gt;alias&lt;/code&gt; explicitly given to &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; or &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;.&lt;/p&gt;
&lt;h2 id="Result object"&gt;Result object&lt;/h2&gt;
&lt;p&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;, &lt;a href="#Wait%20For%20Process" class="name"&gt;Wait For Process&lt;/a&gt; and &lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt; keywords return a result object that contains information about the process execution as its attributes. The same result object, or some of its attributes, can also be get using &lt;a href="#Get%20Process%20Result" class="name"&gt;Get Process Result&lt;/a&gt; keyword. Attributes available in the object are documented in the table below.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Attribute&lt;/th&gt;
&lt;th&gt;Explanation&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;rc&lt;/td&gt;
&lt;td&gt;Return code of the process as an integer.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;stdout&lt;/td&gt;
&lt;td&gt;Contents of the standard output stream.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;stderr&lt;/td&gt;
&lt;td&gt;Contents of the standard error stream.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;stdout_path&lt;/td&gt;
&lt;td&gt;Path where stdout was redirected or &lt;code&gt;None&lt;/code&gt; if not redirected.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;stderr_path&lt;/td&gt;
&lt;td&gt;Path where stderr was redirected or &lt;code&gt;None&lt;/code&gt; if not redirected.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;program&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal As Integers&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${result.rc}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Match&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${result.stdout}&lt;/td&gt;
&lt;td&gt;Some t?xt*&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Empty&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${result.stderr}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${stdout} =&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Get File&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${result.stdout_path}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${stdout}&lt;/td&gt;
&lt;td&gt;${result.stdout}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;File Should Be Empty&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${result.stderr_path}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Boolean arguments"&gt;Boolean arguments&lt;/h2&gt;
&lt;p&gt;Some keywords accept arguments that are handled as Boolean values true or false. If such an argument is given as a string, it is considered false if it is an empty string or equal to &lt;code&gt;FALSE&lt;/code&gt;, &lt;code&gt;NONE&lt;/code&gt;, &lt;code&gt;NO&lt;/code&gt;, &lt;code&gt;OFF&lt;/code&gt; or &lt;code&gt;0&lt;/code&gt;, case-insensitively. Other strings are considered true regardless their value, and other argument types are tested using the same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;True examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=True&lt;/td&gt;
&lt;td&gt;# Strings are generally true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=yes&lt;/td&gt;
&lt;td&gt;# Same as the above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=${TRUE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;True&lt;/code&gt; is true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=${42}&lt;/td&gt;
&lt;td&gt;# Numbers other than 0 are true.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;False examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=False&lt;/td&gt;
&lt;td&gt;# String &lt;code&gt;false&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=no&lt;/td&gt;
&lt;td&gt;# Also string &lt;code&gt;no&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=${EMPTY}&lt;/td&gt;
&lt;td&gt;# Empty string is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;kill=${FALSE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;False&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Considering &lt;code&gt;OFF&lt;/code&gt; and &lt;code&gt;0&lt;/code&gt; false is new in Robot Framework 3.1.&lt;/p&gt;
&lt;h2 id="Example"&gt;Example&lt;/h2&gt;
&lt;pre&gt;
&lt;b&gt;***&lt;/b&gt; Settings &lt;b&gt;***&lt;/b&gt;
Library           Process
Suite Teardown    &lt;a href="#Terminate%20All%20Processes" class="name"&gt;Terminate All Processes&lt;/a&gt;    kill=True

&lt;b&gt;***&lt;/b&gt; Test Cases &lt;b&gt;***&lt;/b&gt;
Example
    &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;    program    arg1    arg2    alias=First
    ${handle} =    &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;    command.sh arg | command2.sh    shell=True    cwd=/path
    ${result} =    &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt;    ${CURDIR}/script.py
    &lt;span class="name"&gt;Should Not Contain&lt;/span&gt;    ${result.stdout}    FAIL
    &lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt;    ${handle}
    ${result} =    &lt;a href="#Wait%20For%20Process" class="name"&gt;Wait For Process&lt;/a&gt;    First
    &lt;span class="name"&gt;Should Be Equal As Integers&lt;/span&gt;    ${result.rc}    0
&lt;/pre&gt;</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Get Process Id" lineno="623">
<arguments repr="handle=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the process ID (pid) of the process as an integer.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Notice that the pid is not the same as the handle returned by &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; that is used internally by this library.&lt;/p&gt;</doc>
<shortdoc>Returns the process ID (pid) of the process as an integer.</shortdoc>
</kw>
<kw name="Get Process Object" lineno="633">
<arguments repr="handle=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Return the underlying &lt;code&gt;subprocess.Popen&lt;/code&gt; object.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Return the underlying ``subprocess.Popen`` object.</shortdoc>
</kw>
<kw name="Get Process Result" lineno="640">
<arguments repr="handle=None, rc=False, stdout=False, stderr=False, stdout_path=False, stderr_path=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="rc=False">
<name>rc</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="stdout=False">
<name>stdout</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="stderr=False">
<name>stderr</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="stdout_path=False">
<name>stdout_path</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="stderr_path=False">
<name>stderr_path</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the specified &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; or some of its attributes.&lt;/p&gt;
&lt;p&gt;The given &lt;code&gt;handle&lt;/code&gt; specifies the process whose results should be returned. If no &lt;code&gt;handle&lt;/code&gt; is given, results of the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt; are returned. In either case, the process must have been finishes before this keyword can be used. In practice this means that processes started with &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; must be finished either with &lt;a href="#Wait%20For%20Process" class="name"&gt;Wait For Process&lt;/a&gt; or &lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt; before using this keyword.&lt;/p&gt;
&lt;p&gt;If no other arguments than the optional &lt;code&gt;handle&lt;/code&gt; are given, a whole &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; is returned. If one or more of the other arguments are given any true value, only the specified attributes of the &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; are returned. These attributes are always returned in the same order as arguments are specified in the keyword signature. See &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt; section for more details about true and false values.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Run Process&lt;/td&gt;
&lt;td&gt;python&lt;/td&gt;
&lt;td&gt;-c&lt;/td&gt;
&lt;td&gt;print('Hello, world!')&lt;/td&gt;
&lt;td&gt;alias=myproc&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Get result object&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Get Process Result&lt;/td&gt;
&lt;td&gt;myproc&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${result.rc}&lt;/td&gt;
&lt;td&gt;${0}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${result.stdout}&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Empty&lt;/td&gt;
&lt;td&gt;${result.stderr}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Get one attribute&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${stdout} =&lt;/td&gt;
&lt;td&gt;Get Process Result&lt;/td&gt;
&lt;td&gt;myproc&lt;/td&gt;
&lt;td&gt;stdout=true&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stdout}&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Multiple attributes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${stdout}&lt;/td&gt;
&lt;td&gt;${stderr} =&lt;/td&gt;
&lt;td&gt;Get Process Result&lt;/td&gt;
&lt;td&gt;myproc&lt;/td&gt;
&lt;td&gt;stdout=yes&lt;/td&gt;
&lt;td&gt;stderr=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${stdout}&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Empty&lt;/td&gt;
&lt;td&gt;${stderr}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Although getting results of a previously executed process can be handy in general, the main use case for this keyword is returning results over the remote library interface. The remote interface does not support returning the whole result object, but individual attributes can be returned without problems.&lt;/p&gt;</doc>
<shortdoc>Returns the specified `result object` or some of its attributes.</shortdoc>
</kw>
<kw name="Is Process Running" lineno="368">
<arguments repr="handle=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Checks is the process running or not.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Returns &lt;code&gt;True&lt;/code&gt; if the process is still running and &lt;code&gt;False&lt;/code&gt; otherwise.&lt;/p&gt;</doc>
<shortdoc>Checks is the process running or not.</shortdoc>
</kw>
<kw name="Join Command Line" lineno="736">
<arguments repr="*args">
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Joins arguments into one command line string.&lt;/p&gt;
&lt;p&gt;In resulting command line string arguments are delimited with a space, arguments containing spaces are surrounded with quotes, and possible quotes are escaped with a backslash.&lt;/p&gt;
&lt;p&gt;If this keyword is given only one argument and that is a list like object, then the values of that list are joined instead.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${cmd} =&lt;/td&gt;
&lt;td&gt;Join Command Line&lt;/td&gt;
&lt;td&gt;--option&lt;/td&gt;
&lt;td&gt;value with spaces&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${cmd}&lt;/td&gt;
&lt;td&gt;--option "value with spaces"&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Joins arguments into one command line string.</shortdoc>
</kw>
<kw name="Process Should Be Running" lineno="377">
<arguments repr="handle=None, error_message=Process is not running.">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="error_message=Process is not running.">
<name>error_message</name>
<default>Process is not running.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the process is running.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Fails if the process has stopped.&lt;/p&gt;</doc>
<shortdoc>Verifies that the process is running.</shortdoc>
</kw>
<kw name="Process Should Be Stopped" lineno="388">
<arguments repr="handle=None, error_message=Process is running.">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="error_message=Process is running.">
<name>error_message</name>
<default>Process is running.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the process is not running.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Fails if the process is still running.&lt;/p&gt;</doc>
<shortdoc>Verifies that the process is not running.</shortdoc>
</kw>
<kw name="Run Process" lineno="302">
<arguments repr="command, *arguments, **configuration">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*arguments">
<name>arguments</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**configuration">
<name>configuration</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs a process and waits for it to complete.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;command&lt;/code&gt; and &lt;code&gt;*arguments&lt;/code&gt; specify the command to execute and arguments passed to it. See &lt;a href="#Specifying%20command%20and%20arguments" class="name"&gt;Specifying command and arguments&lt;/a&gt; for more details.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;**configuration&lt;/code&gt; contains additional configuration related to starting processes and waiting for them to finish. See &lt;a href="#Process%20configuration" class="name"&gt;Process configuration&lt;/a&gt; for more details about configuration related to starting processes. Configuration related to waiting for processes consists of &lt;code&gt;timeout&lt;/code&gt; and &lt;code&gt;on_timeout&lt;/code&gt; arguments that have same semantics as with &lt;a href="#Wait%20For%20Process" class="name"&gt;Wait For Process&lt;/a&gt; keyword. By default there is no timeout, and if timeout is defined the default action on timeout is &lt;code&gt;terminate&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Returns a &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; containing information about the execution.&lt;/p&gt;
&lt;p&gt;Note that possible equal signs in &lt;code&gt;*arguments&lt;/code&gt; must be escaped with a backslash (e.g. &lt;code&gt;name\=value&lt;/code&gt;) to avoid them to be passed in as &lt;code&gt;**configuration&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Run Process&lt;/td&gt;
&lt;td&gt;python&lt;/td&gt;
&lt;td&gt;-c&lt;/td&gt;
&lt;td&gt;print('Hello, world!')&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${result.stdout}&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Run Process&lt;/td&gt;
&lt;td&gt;${command}&lt;/td&gt;
&lt;td&gt;stderr=STDOUT&lt;/td&gt;
&lt;td&gt;timeout=10s&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Run Process&lt;/td&gt;
&lt;td&gt;${command}&lt;/td&gt;
&lt;td&gt;timeout=1min&lt;/td&gt;
&lt;td&gt;on_timeout=continue&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Run Process&lt;/td&gt;
&lt;td&gt;java -Dname\=value Example&lt;/td&gt;
&lt;td&gt;shell=True&lt;/td&gt;
&lt;td&gt;cwd=${EXAMPLE}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword does not change the &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Runs a process and waits for it to complete.</shortdoc>
</kw>
<kw name="Send Signal To Process" lineno="569">
<arguments repr="signal, handle=None, group=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="signal">
<name>signal</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="group=False">
<name>group</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sends the given &lt;code&gt;signal&lt;/code&gt; to the specified process.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Signal can be specified either as an integer as a signal name. In the latter case it is possible to give the name both with or without &lt;code&gt;SIG&lt;/code&gt; prefix, but names are case-sensitive. For example, all the examples below send signal &lt;code&gt;INT (2)&lt;/code&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Send Signal To Process&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Send to active process&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Send Signal To Process&lt;/td&gt;
&lt;td&gt;INT&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Send Signal To Process&lt;/td&gt;
&lt;td&gt;SIGINT&lt;/td&gt;
&lt;td&gt;myproc&lt;/td&gt;
&lt;td&gt;# Send to named process&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword is only supported on Unix-like machines, not on Windows. What signals are supported depends on the system. For a list of existing signals on your system, see the Unix man pages related to signal handling (typically &lt;code&gt;man signal&lt;/code&gt; or &lt;code&gt;man 7 signal&lt;/code&gt;).&lt;/p&gt;
&lt;p&gt;By default sends the signal only to the parent process, not to possible child processes started by it. Notice that when &lt;a href="#Running%20processes%20in%20shell" class="name"&gt;running processes in shell&lt;/a&gt;, the shell is the parent process and it depends on the system does the shell propagate the signal to the actual started process.&lt;/p&gt;
&lt;p&gt;To send the signal to the whole process group, &lt;code&gt;group&lt;/code&gt; argument can be set to any true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). This is not supported by Jython, however.&lt;/p&gt;</doc>
<shortdoc>Sends the given ``signal`` to the specified process.</shortdoc>
</kw>
<kw name="Split Command Line" lineno="721">
<arguments repr="args, escaping=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="args">
<name>args</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="escaping=False">
<name>escaping</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Splits command line string into a list of arguments.&lt;/p&gt;
&lt;p&gt;String is split from spaces, but argument surrounded in quotes may contain spaces in them. If &lt;code&gt;escaping&lt;/code&gt; is given a true value, then backslash is treated as an escape character. It can escape unquoted spaces, quotes inside quotes, and so on, but it also requires using double backslashes when using Windows paths.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{cmd} =&lt;/td&gt;
&lt;td&gt;Split Command Line&lt;/td&gt;
&lt;td&gt;--option "value with spaces"&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;$cmd == ['--option', 'value with spaces']&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Splits command line string into a list of arguments.</shortdoc>
</kw>
<kw name="Start Process" lineno="341">
<arguments repr="command, *arguments, **configuration">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="command">
<name>command</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*arguments">
<name>arguments</name>
</arg>
<arg kind="VAR_NAMED" required="false" repr="**configuration">
<name>configuration</name>
</arg>
</arguments>
<doc>&lt;p&gt;Starts a new process on background.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Specifying%20command%20and%20arguments" class="name"&gt;Specifying command and arguments&lt;/a&gt; and &lt;a href="#Process%20configuration" class="name"&gt;Process configuration&lt;/a&gt; for more information about the arguments, and &lt;a href="#Run%20Process" class="name"&gt;Run Process&lt;/a&gt; keyword for related examples.&lt;/p&gt;
&lt;p&gt;Makes the started process new &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;. Returns an identifier that can be used as a handle to activate the started process if needed.&lt;/p&gt;
&lt;p&gt;Processes are started so that they create a new process group. This allows sending signals to and terminating also possible child processes. This is not supported on Jython.&lt;/p&gt;</doc>
<shortdoc>Starts a new process on background.</shortdoc>
</kw>
<kw name="Switch Process" lineno="699">
<arguments repr="handle">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="handle">
<name>handle</name>
</arg>
</arguments>
<doc>&lt;p&gt;Makes the specified process the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The handle can be an identifier returned by &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt; or the &lt;code&gt;alias&lt;/code&gt; given to it explicitly.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Start Process&lt;/td&gt;
&lt;td&gt;prog1&lt;/td&gt;
&lt;td&gt;alias=process1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Start Process&lt;/td&gt;
&lt;td&gt;prog2&lt;/td&gt;
&lt;td&gt;alias=process2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# currently active process is process2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Switch Process&lt;/td&gt;
&lt;td&gt;process1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# now active process is process1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Makes the specified process the current `active process`.</shortdoc>
</kw>
<kw name="Terminate All Processes" lineno="554">
<arguments repr="kill=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="kill=False">
<name>kill</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Terminates all still running processes started by this library.&lt;/p&gt;
&lt;p&gt;This keyword can be used in suite teardown or elsewhere to make sure that all processes are stopped,&lt;/p&gt;
&lt;p&gt;By default tries to terminate processes gracefully, but can be configured to forcefully kill them immediately. See &lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt; that this keyword uses internally for more details.&lt;/p&gt;</doc>
<shortdoc>Terminates all still running processes started by this library.</shortdoc>
</kw>
<kw name="Terminate Process" lineno="479">
<arguments repr="handle=None, kill=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="kill=False">
<name>kill</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Stops the process gracefully or forcefully.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;By default first tries to stop the process gracefully. If the process does not stop in 30 seconds, or &lt;code&gt;kill&lt;/code&gt; argument is given a true value, (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) kills the process forcefully. Stops also all the child processes of the originally started process.&lt;/p&gt;
&lt;p&gt;Waits for the process to stop after terminating it. Returns a &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; containing information about the execution similarly as &lt;a href="#Wait%20For%20Process" class="name"&gt;Wait For Process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;On Unix-like machines graceful termination is done using &lt;code&gt;TERM (15)&lt;/code&gt; signal and killing using &lt;code&gt;KILL (9)&lt;/code&gt;. Use &lt;a href="#Send%20Signal%20To%20Process" class="name"&gt;Send Signal To Process&lt;/a&gt; instead if you just want to send either of these signals without waiting for the process to stop.&lt;/p&gt;
&lt;p&gt;On Windows graceful termination is done using &lt;code&gt;CTRL_BREAK_EVENT&lt;/code&gt; event and killing using Win32 API function &lt;code&gt;TerminateProcess()&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Terminate Process&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${result.rc}&lt;/td&gt;
&lt;td&gt;-15&lt;/td&gt;
&lt;td&gt;# On Unixes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Terminate Process&lt;/td&gt;
&lt;td&gt;myproc&lt;/td&gt;
&lt;td&gt;kill=true&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Limitations:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Graceful termination is not supported on Windows when using Jython. Process is killed instead.&lt;/li&gt;
&lt;li&gt;Stopping the whole process group is not supported when using Jython.&lt;/li&gt;
&lt;li&gt;On Windows forceful kill only stops the main process, not possible child processes.&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Stops the process gracefully or forcefully.</shortdoc>
</kw>
<kw name="Wait For Process" lineno="399">
<arguments repr="handle=None, timeout=None, on_timeout=continue">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="handle=None">
<name>handle</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="timeout=None">
<name>timeout</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="on_timeout=continue">
<name>on_timeout</name>
<default>continue</default>
</arg>
</arguments>
<doc>&lt;p&gt;Waits for the process to complete or to reach the given timeout.&lt;/p&gt;
&lt;p&gt;The process to wait for must have been started earlier with &lt;a href="#Start%20Process" class="name"&gt;Start Process&lt;/a&gt;. If &lt;code&gt;handle&lt;/code&gt; is not given, uses the current &lt;a href="#Active%20process" class="name"&gt;active process&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;timeout&lt;/code&gt; defines the maximum time to wait for the process. It can be given in &lt;a href="http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format"&gt;various time formats&lt;/a&gt; supported by Robot Framework, for example, &lt;code&gt;42&lt;/code&gt;, &lt;code&gt;42 s&lt;/code&gt;, or &lt;code&gt;1 minute 30 seconds&lt;/code&gt;. The timeout is ignored if it is Python &lt;code&gt;None&lt;/code&gt; (default), string &lt;code&gt;NONE&lt;/code&gt; (case-insensitively), zero, or negative.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;on_timeout&lt;/code&gt; defines what to do if the timeout occurs. Possible values and corresponding actions are explained in the table below. Notice that reaching the timeout never fails the test.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Value&lt;/th&gt;
&lt;th&gt;Action&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;continue&lt;/td&gt;
&lt;td&gt;The process is left running (default).&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;terminate&lt;/td&gt;
&lt;td&gt;The process is gracefully terminated.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;kill&lt;/td&gt;
&lt;td&gt;The process is forcefully stopped.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Terminate%20Process" class="name"&gt;Terminate Process&lt;/a&gt; keyword for more details how processes are terminated and killed.&lt;/p&gt;
&lt;p&gt;If the process ends before the timeout or it is terminated or killed, this keyword returns a &lt;a href="#Result%20object" class="name"&gt;result object&lt;/a&gt; containing information about the execution. If the process is left running, Python &lt;code&gt;None&lt;/code&gt; is returned instead.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;# Process ends cleanly&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Wait For Process&lt;/td&gt;
&lt;td&gt;example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Process Should Be Stopped&lt;/td&gt;
&lt;td&gt;example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${result.rc}&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Process does not end&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Wait For Process&lt;/td&gt;
&lt;td&gt;timeout=42 secs&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Process Should Be Running&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;${NONE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Kill non-ending process&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Wait For Process&lt;/td&gt;
&lt;td&gt;timeout=1min 30s&lt;/td&gt;
&lt;td&gt;on_timeout=kill&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Process Should Be Stopped&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${result.rc}&lt;/td&gt;
&lt;td&gt;-9&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Ignoring timeout if it is string &lt;code&gt;NONE&lt;/code&gt;, zero, or negative is new in Robot Framework 3.2.&lt;/p&gt;</doc>
<shortdoc>Waits for the process to complete or to reach the given timeout.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
