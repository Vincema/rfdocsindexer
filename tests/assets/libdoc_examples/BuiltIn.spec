<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="BuiltIn" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2021-08-18T02:53:35Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/BuiltIn.py" lineno="3560">
<version>4.1</version>
<doc>&lt;p&gt;An always available standard library with often needed keywords.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;BuiltIn&lt;/code&gt; is Robot Framework's standard library that provides a set of generic keywords needed often. It is imported automatically and thus always available. The provided keywords can be used, for example, for verifications (e.g. &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;, &lt;a href="#Should%20Contain" class="name"&gt;Should Contain&lt;/a&gt;), conversions (e.g. &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt;) and for various other purposes (e.g. &lt;a href="#Log" class="name"&gt;Log&lt;/a&gt;, &lt;a href="#Sleep" class="name"&gt;Sleep&lt;/a&gt;, &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;, &lt;a href="#Set%20Global%20Variable" class="name"&gt;Set Global Variable&lt;/a&gt;).&lt;/p&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#HTML%20error%20messages" class="name"&gt;HTML error messages&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Multiline%20string%20comparison" class="name"&gt;Multiline string comparison&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#String%20representations" class="name"&gt;String representations&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="HTML error messages"&gt;HTML error messages&lt;/h2&gt;
&lt;p&gt;Many of the keywords accept an optional error message to use if the keyword fails, and it is possible to use HTML in these messages by prefixing them with &lt;code&gt;*HTML*&lt;/code&gt;. See &lt;a href="#Fail" class="name"&gt;Fail&lt;/a&gt; keyword for a usage example. Notice that using HTML in messages is not limited to BuiltIn library but works with any error message.&lt;/p&gt;
&lt;h2 id="Evaluating expressions"&gt;Evaluating expressions&lt;/h2&gt;
&lt;p&gt;Many keywords, such as &lt;a href="#Evaluate" class="name"&gt;Evaluate&lt;/a&gt;, &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; and &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt;, accept an expression that is evaluated in Python.&lt;/p&gt;
&lt;h3 id="Evaluation namespace"&gt;Evaluation namespace&lt;/h3&gt;
&lt;p&gt;Expressions are evaluated using Python's &lt;a href="http://docs.python.org/library/functions.html#eval"&gt;eval&lt;/a&gt; function so that all Python built-ins like &lt;code&gt;len()&lt;/code&gt; and &lt;code&gt;int()&lt;/code&gt; are available. In addition to that, all unrecognized variables are considered to be modules that are automatically imported. It is possible to use all available Python modules, including the standard modules and the installed third party modules.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;len('${result}') &amp;gt; 3&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;os.sep == '/'&lt;/td&gt;
&lt;td&gt;Non-Windows Keyword&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${robot version} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Evaluate" class="name"&gt;Evaluate&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;robot.__version__&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;a href="#Evaluate" class="name"&gt;Evaluate&lt;/a&gt; also allows configuring the execution namespace with a custom namespace and with custom modules to be imported. The latter functionality is useful in special cases where the automatic module import does not work such as when using nested modules like &lt;code&gt;rootmod.submod&lt;/code&gt; or list comprehensions. See the documentation of the &lt;a href="#Evaluate" class="name"&gt;Evaluate&lt;/a&gt; keyword for mode details.&lt;/p&gt;
&lt;p&gt;&lt;b&gt;NOTE:&lt;/b&gt; Automatic module import is a new feature in Robot Framework 3.2. Earlier modules needed to be explicitly taken into use when using the &lt;a href="#Evaluate" class="name"&gt;Evaluate&lt;/a&gt; keyword and other keywords only had access to &lt;code&gt;sys&lt;/code&gt; and &lt;code&gt;os&lt;/code&gt; modules.&lt;/p&gt;
&lt;h3 id="Using variables"&gt;Using variables&lt;/h3&gt;
&lt;p&gt;When a variable is used in the expressing using the normal &lt;code&gt;${variable}&lt;/code&gt; syntax, its value is replaced before the expression is evaluated. This means that the value used in the expression will be the string representation of the variable value, not the variable value itself. This is not a problem with numbers and other objects that have a string representation that can be evaluated directly, but with other objects the behavior depends on the string representation. Most importantly, strings must always be quoted, and if they can contain newlines, they must be triple quoted.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 10&lt;/td&gt;
&lt;td&gt;Return code greater than 10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;'${status}' == 'PASS'&lt;/td&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;Passed&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;'FAIL' in '''${output}'''&lt;/td&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;Output contains FAIL&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Actual variables values are also available in the evaluation namespace. They can be accessed using special variable syntax without the curly braces like &lt;code&gt;$variable&lt;/code&gt;. These variables should never be quoted.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;$rc &amp;lt; 10&lt;/td&gt;
&lt;td&gt;Return code greater than 10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;$status == 'PASS'&lt;/td&gt;
&lt;td&gt;&lt;a href="#Log" class="name"&gt;Log&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;Passed&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;'FAIL' in $output&lt;/td&gt;
&lt;td&gt;&lt;a href="#Log" class="name"&gt;Log&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;Output contains FAIL&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;len($result) &amp;gt; 1 and $result[1] == 'OK'&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;$result is not None&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Using the &lt;code&gt;$variable&lt;/code&gt; syntax slows down expression evaluation a little. This should not typically matter, but should be taken into account if complex expressions are evaluated often and there are strict time constrains.&lt;/p&gt;
&lt;p&gt;Notice that instead of creating complicated expressions, it is often better to move the logic into a test library. That eases maintenance and can also enhance execution speed.&lt;/p&gt;
&lt;h2 id="Boolean arguments"&gt;Boolean arguments&lt;/h2&gt;
&lt;p&gt;Some keywords accept arguments that are handled as Boolean values true or false. If such an argument is given as a string, it is considered false if it is an empty string or equal to &lt;code&gt;FALSE&lt;/code&gt;, &lt;code&gt;NONE&lt;/code&gt;, &lt;code&gt;NO&lt;/code&gt;, &lt;code&gt;OFF&lt;/code&gt; or &lt;code&gt;0&lt;/code&gt;, case-insensitively. Keywords verifying something that allow dropping actual and expected values from the possible error message also consider string &lt;code&gt;no values&lt;/code&gt; to be false. Other strings are considered true unless the keyword documentation explicitly states otherwise, and other argument types are tested using the same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;True examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=True&lt;/td&gt;
&lt;td&gt;# Strings are generally true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=yes&lt;/td&gt;
&lt;td&gt;# Same as the above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=${TRUE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;True&lt;/code&gt; is true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=${42}&lt;/td&gt;
&lt;td&gt;# Numbers other than 0 are true.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;False examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=False&lt;/td&gt;
&lt;td&gt;# String &lt;code&gt;false&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=no&lt;/td&gt;
&lt;td&gt;# Also string &lt;code&gt;no&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=${EMPTY}&lt;/td&gt;
&lt;td&gt;# Empty string is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=${FALSE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;False&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;Custom error&lt;/td&gt;
&lt;td&gt;values=no values&lt;/td&gt;
&lt;td&gt;# &lt;code&gt;no values&lt;/code&gt; works with &lt;code&gt;values&lt;/code&gt; argument&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Pattern matching"&gt;Pattern matching&lt;/h2&gt;
&lt;p&gt;Many keywords accepts arguments as either glob or regular expression patterns.&lt;/p&gt;
&lt;h3 id="Glob patterns"&gt;Glob patterns&lt;/h3&gt;
&lt;p&gt;Some keywords, for example &lt;a href="#Should%20Match" class="name"&gt;Should Match&lt;/a&gt;, support so called &lt;a href="http://en.wikipedia.org/wiki/Glob_(programming)"&gt;glob patterns&lt;/a&gt; where:&lt;/p&gt;
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
&lt;p&gt;Unlike with glob patterns normally, path separator characters &lt;code&gt;/&lt;/code&gt; and &lt;code&gt;\&lt;/code&gt; and the newline character &lt;code&gt;\n&lt;/code&gt; are matches by the above wildcards.&lt;/p&gt;
&lt;h3 id="Regular expressions"&gt;Regular expressions&lt;/h3&gt;
&lt;p&gt;Some keywords, for example &lt;a href="#Should%20Match%20Regexp" class="name"&gt;Should Match Regexp&lt;/a&gt;, support &lt;a href="http://en.wikipedia.org/wiki/Regular_expression"&gt;regular expressions&lt;/a&gt; that are more powerful but also more complicated that glob patterns. The regular expression support is implemented using Python's &lt;a href="http://docs.python.org/library/re.html"&gt;re module&lt;/a&gt; and its documentation should be consulted for more information about the syntax.&lt;/p&gt;
&lt;p&gt;Because the backslash character (&lt;code&gt;\&lt;/code&gt;) is an escape character in Robot Framework test data, possible backslash characters in regular expressions need to be escaped with another backslash like &lt;code&gt;\\d\\w+&lt;/code&gt;. Strings that may contain special characters but should be handled as literal strings, can be escaped with the &lt;a href="#Regexp%20Escape" class="name"&gt;Regexp Escape&lt;/a&gt; keyword.&lt;/p&gt;
&lt;h2 id="Multiline string comparison"&gt;Multiline string comparison&lt;/h2&gt;
&lt;p&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; and &lt;a href="#Should%20Be%20Equal%20As%20Strings" class="name"&gt;Should Be Equal As Strings&lt;/a&gt; report the failures using &lt;a href="http://en.wikipedia.org/wiki/Diff_utility#Unified_format"&gt;unified diff format&lt;/a&gt; if both strings have more than two lines.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${first} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Catenate" class="name"&gt;Catenate&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;SEPARATOR=\n&lt;/td&gt;
&lt;td&gt;Not in second&lt;/td&gt;
&lt;td&gt;Same&lt;/td&gt;
&lt;td&gt;Differs&lt;/td&gt;
&lt;td&gt;Same&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${second} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Catenate" class="name"&gt;Catenate&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;SEPARATOR=\n&lt;/td&gt;
&lt;td&gt;Same&lt;/td&gt;
&lt;td&gt;Differs2&lt;/td&gt;
&lt;td&gt;Same&lt;/td&gt;
&lt;td&gt;Not in first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;${second}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Results in the following error message:&lt;/p&gt;
&lt;pre&gt;
Multiline strings are different:
--- first
+++ second
@@ -1,4 +1,4 @@
-Not in second
 Same
-Differs
+Differs2
 Same
+Not in first
&lt;/pre&gt;
&lt;h2 id="String representations"&gt;String representations&lt;/h2&gt;
&lt;p&gt;Several keywords log values explicitly (e.g. &lt;a href="#Log" class="name"&gt;Log&lt;/a&gt;) or implicitly (e.g. &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; when there are failures). By default keywords log values using "human readable" string representation, which means that strings like &lt;code&gt;Hello&lt;/code&gt; and numbers like &lt;code&gt;42&lt;/code&gt; are logged as-is. Most of the time this is the desired behavior, but there are some problems as well:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;It is not possible to see difference between different objects that have same string representation like string &lt;code&gt;42&lt;/code&gt; and integer &lt;code&gt;42&lt;/code&gt;. &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; and some other keywords add the type information to the error message in these cases, though.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;Non-printable characters such as the null byte are not visible.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;Trailing whitespace is not visible.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;Different newlines (&lt;code&gt;\r\n&lt;/code&gt; on Windows, &lt;code&gt;\n&lt;/code&gt; elsewhere) cannot be separated from each others.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;There are several Unicode characters that are different but look the same. One example is the Latin &lt;code&gt;a&lt;/code&gt; (&lt;code&gt;\u0061&lt;/code&gt;) and the Cyrillic &lt;code&gt;а&lt;/code&gt; (&lt;code&gt;\u0430&lt;/code&gt;). Error messages like &lt;code&gt;a != а&lt;/code&gt; are not very helpful.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;Some Unicode characters can be represented using &lt;a href="https://en.wikipedia.org/wiki/Unicode_equivalence"&gt;different forms&lt;/a&gt;. For example, &lt;code&gt;ä&lt;/code&gt; can be represented either as a single code point &lt;code&gt;\u00e4&lt;/code&gt; or using two code points &lt;code&gt;\u0061&lt;/code&gt; and &lt;code&gt;\u0308&lt;/code&gt; combined together. Such forms are considered canonically equivalent, but strings containing them are not considered equal when compared in Python. Error messages like &lt;code&gt;ä != ä&lt;/code&gt; are not that helpful either.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;Containers such as lists and dictionaries are formatted into a single line making it hard to see individual items they contain.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;To overcome the above problems, some keywords such as &lt;a href="#Log" class="name"&gt;Log&lt;/a&gt; and &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; have an optional &lt;code&gt;formatter&lt;/code&gt; argument that can be used to configure the string representation. The supported values are &lt;code&gt;str&lt;/code&gt; (default), &lt;code&gt;repr&lt;/code&gt;, and &lt;code&gt;ascii&lt;/code&gt; that work similarly as &lt;a href="https://docs.python.org/library/functions.html"&gt;Python built-in functions&lt;/a&gt; with same names. More detailed semantics are explained below.&lt;/p&gt;
&lt;h3 id="str"&gt;str&lt;/h3&gt;
&lt;p&gt;Use the "human readable" string representation. Equivalent to using &lt;code&gt;str()&lt;/code&gt; in Python 3 and &lt;code&gt;unicode()&lt;/code&gt; in Python 2. This is the default.&lt;/p&gt;
&lt;h3 id="repr"&gt;repr&lt;/h3&gt;
&lt;p&gt;Use the "machine readable" string representation. Similar to using &lt;code&gt;repr()&lt;/code&gt; in Python, which means that strings like &lt;code&gt;Hello&lt;/code&gt; are logged like &lt;code&gt;'Hello'&lt;/code&gt;, newlines and non-printable characters are escaped like &lt;code&gt;\n&lt;/code&gt; and &lt;code&gt;\x00&lt;/code&gt;, and so on. Non-ASCII characters are shown as-is like &lt;code&gt;ä&lt;/code&gt; in Python 3 and in escaped format like &lt;code&gt;\xe4&lt;/code&gt; in Python 2. Use &lt;code&gt;ascii&lt;/code&gt; to always get the escaped format.&lt;/p&gt;
&lt;p&gt;There are also some enhancements compared to the standard &lt;code&gt;repr()&lt;/code&gt;:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Bigger lists, dictionaries and other containers are pretty-printed so that there is one item per row.&lt;/li&gt;
&lt;li&gt;On Python 2 the &lt;code&gt;u&lt;/code&gt; prefix is omitted with Unicode strings and the &lt;code&gt;b&lt;/code&gt; prefix is added to byte strings.&lt;/li&gt;
&lt;/ul&gt;
&lt;h3 id="ascii"&gt;ascii&lt;/h3&gt;
&lt;p&gt;Same as using &lt;code&gt;ascii()&lt;/code&gt; in Python 3 or &lt;code&gt;repr()&lt;/code&gt; in Python 2 where &lt;code&gt;ascii()&lt;/code&gt; does not exist. Similar to using &lt;code&gt;repr&lt;/code&gt; explained above but with the following differences:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;On Python 3 non-ASCII characters are escaped like &lt;code&gt;\xe4&lt;/code&gt; instead of showing them as-is like &lt;code&gt;ä&lt;/code&gt;. This makes it easier to see differences between Unicode characters that look the same but are not equal. This is how &lt;code&gt;repr()&lt;/code&gt; works in Python 2.&lt;/li&gt;
&lt;li&gt;On Python 2 just uses the standard &lt;code&gt;repr()&lt;/code&gt; meaning that Unicode strings get the &lt;code&gt;u&lt;/code&gt; prefix and no &lt;code&gt;b&lt;/code&gt; prefix is added to byte strings.&lt;/li&gt;
&lt;li&gt;Containers are not pretty-printed.&lt;/li&gt;
&lt;/ul&gt;</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Call Method" lineno="3308">
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
<doc>&lt;p&gt;Calls the named method of the given object with the provided arguments.&lt;/p&gt;
&lt;p&gt;The possible return value from the method is returned and can be assigned to a variable. Keyword fails both if the object does not have a method with the given name or if executing the method raises an exception.&lt;/p&gt;
&lt;p&gt;Possible equal signs in arguments must be escaped with a backslash like &lt;code&gt;\=&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Call Method&lt;/td&gt;
&lt;td&gt;${hashtable}&lt;/td&gt;
&lt;td&gt;put&lt;/td&gt;
&lt;td&gt;myname&lt;/td&gt;
&lt;td&gt;myvalue&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${isempty} =&lt;/td&gt;
&lt;td&gt;Call Method&lt;/td&gt;
&lt;td&gt;${hashtable}&lt;/td&gt;
&lt;td&gt;isEmpty&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Be True&lt;/td&gt;
&lt;td&gt;${isempty}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${value} =&lt;/td&gt;
&lt;td&gt;Call Method&lt;/td&gt;
&lt;td&gt;${hashtable}&lt;/td&gt;
&lt;td&gt;get&lt;/td&gt;
&lt;td&gt;myname&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${value}&lt;/td&gt;
&lt;td&gt;myvalue&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Call Method&lt;/td&gt;
&lt;td&gt;${object}&lt;/td&gt;
&lt;td&gt;kwargs&lt;/td&gt;
&lt;td&gt;name=value&lt;/td&gt;
&lt;td&gt;foo=bar&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Call Method&lt;/td&gt;
&lt;td&gt;${object}&lt;/td&gt;
&lt;td&gt;positional&lt;/td&gt;
&lt;td&gt;escaped\=equals&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Calls the named method of the given object with the provided arguments.</shortdoc>
</kw>
<kw name="Catenate" lineno="2833">
<arguments repr="*items">
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
</arguments>
<doc>&lt;p&gt;Catenates the given items together and returns the resulted string.&lt;/p&gt;
&lt;p&gt;By default, items are catenated with spaces, but if the first item contains the string &lt;code&gt;SEPARATOR=&amp;lt;sep&amp;gt;&lt;/code&gt;, the separator &lt;code&gt;&amp;lt;sep&amp;gt;&lt;/code&gt; is used instead. Items are converted into strings when necessary.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${str1} =&lt;/td&gt;
&lt;td&gt;Catenate&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;world&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str2} =&lt;/td&gt;
&lt;td&gt;Catenate&lt;/td&gt;
&lt;td&gt;SEPARATOR=---&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;world&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${str3} =&lt;/td&gt;
&lt;td&gt;Catenate&lt;/td&gt;
&lt;td&gt;SEPARATOR=&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;world&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${str1} = 'Hello world'
${str2} = 'Hello---world'
${str3} = 'Helloworld'
&lt;/pre&gt;</doc>
<shortdoc>Catenates the given items together and returns the resulted string.</shortdoc>
</kw>
<kw name="Comment" lineno="2982">
<arguments repr="*messages">
<arg kind="VAR_POSITIONAL" required="false" repr="*messages">
<name>messages</name>
</arg>
</arguments>
<doc>&lt;p&gt;Displays the given messages in the log file as keyword arguments.&lt;/p&gt;
&lt;p&gt;This keyword does nothing with the arguments it receives, but as they are visible in the log, this keyword can be used to display simple messages. Given arguments are ignored so thoroughly that they can even contain non-existing variables. If you are interested about variable values, you can use the &lt;a href="#Log" class="name"&gt;Log&lt;/a&gt; or &lt;a href="#Log%20Many" class="name"&gt;Log Many&lt;/a&gt; keywords.&lt;/p&gt;</doc>
<shortdoc>Displays the given messages in the log file as keyword arguments.</shortdoc>
</kw>
<kw name="Continue For Loop" lineno="2529">
<arguments repr="">
</arguments>
<doc>&lt;p&gt;Skips the current for loop iteration and continues from the next.&lt;/p&gt;
&lt;p&gt;Skips the remaining keywords in the current for loop iteration and continues from the next one. Can be used directly in a for loop or in a keyword that the loop uses.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;FOR&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;IN&lt;/td&gt;
&lt;td&gt;@{VALUES}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Run Keyword If&lt;/td&gt;
&lt;td&gt;'${var}' == 'CONTINUE'&lt;/td&gt;
&lt;td&gt;Continue For Loop&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Do Something&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;END&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Continue%20For%20Loop%20If" class="name"&gt;Continue For Loop If&lt;/a&gt; to conditionally continue a for loop without using &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; or other wrapper keywords.&lt;/p&gt;</doc>
<shortdoc>Skips the current for loop iteration and continues from the next.</shortdoc>
</kw>
<kw name="Continue For Loop If" lineno="2548">
<arguments repr="condition">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
</arguments>
<doc>&lt;p&gt;Skips the current for loop iteration if the &lt;code&gt;condition&lt;/code&gt; is true.&lt;/p&gt;
&lt;p&gt;A wrapper for &lt;a href="#Continue%20For%20Loop" class="name"&gt;Continue For Loop&lt;/a&gt; to continue a for loop based on the given condition. The condition is evaluated using the same semantics as with &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;FOR&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;IN&lt;/td&gt;
&lt;td&gt;@{VALUES}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Continue For Loop If&lt;/td&gt;
&lt;td&gt;'${var}' == 'CONTINUE'&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Do Something&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;END&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Skips the current for loop iteration if the ``condition`` is true.</shortdoc>
</kw>
<kw name="Convert To Binary" lineno="169">
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
<doc>&lt;p&gt;Converts the given item to a binary string.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;item&lt;/code&gt;, with an optional &lt;code&gt;base&lt;/code&gt;, is first converted to an integer using &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt; internally. After that it is converted to a binary number (base 2) represented as a string such as &lt;code&gt;1011&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The returned value can contain an optional &lt;code&gt;prefix&lt;/code&gt; and can be required to be of minimum &lt;code&gt;length&lt;/code&gt; (excluding the prefix and a possible minus sign). If the value is initially shorter than the required length, it is padded with zeros.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Binary&lt;/td&gt;
&lt;td&gt;10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is 1010&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Binary&lt;/td&gt;
&lt;td&gt;F&lt;/td&gt;
&lt;td&gt;base=16&lt;/td&gt;
&lt;td&gt;prefix=0b&lt;/td&gt;
&lt;td&gt;# Result is 0b1111&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Binary&lt;/td&gt;
&lt;td&gt;-2&lt;/td&gt;
&lt;td&gt;prefix=B&lt;/td&gt;
&lt;td&gt;length=4&lt;/td&gt;
&lt;td&gt;# Result is -B0010&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt;, &lt;a href="#Convert%20To%20Octal" class="name"&gt;Convert To Octal&lt;/a&gt; and &lt;a href="#Convert%20To%20Hex" class="name"&gt;Convert To Hex&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to a binary string.</shortdoc>
</kw>
<kw name="Convert To Boolean" lineno="322">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given item to Boolean true or false.&lt;/p&gt;
&lt;p&gt;Handles strings &lt;code&gt;True&lt;/code&gt; and &lt;code&gt;False&lt;/code&gt; (case-insensitive) as expected, otherwise returns item's &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;truth value&lt;/a&gt; using Python's &lt;code&gt;bool()&lt;/code&gt; method.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to Boolean true or false.</shortdoc>
</kw>
<kw name="Convert To Bytes" lineno="338">
<arguments repr="input, input_type=text">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="input">
<name>input</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="input_type=text">
<name>input_type</name>
<default>text</default>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given &lt;code&gt;input&lt;/code&gt; to bytes according to the &lt;code&gt;input_type&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Valid input types are listed below:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;text:&lt;/code&gt; Converts text to bytes character by character. All characters with ordinal below 256 can be used and are converted to bytes with same values. Many characters are easiest to represent using escapes like &lt;code&gt;\x00&lt;/code&gt; or &lt;code&gt;\xff&lt;/code&gt;. Supports both Unicode strings and bytes.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;int:&lt;/code&gt; Converts integers separated by spaces to bytes. Similarly as with &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt;, it is possible to use binary, octal, or hex values by prefixing the values with &lt;code&gt;0b&lt;/code&gt;, &lt;code&gt;0o&lt;/code&gt;, or &lt;code&gt;0x&lt;/code&gt;, respectively.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;hex:&lt;/code&gt; Converts hexadecimal values to bytes. Single byte is always two characters long (e.g. &lt;code&gt;01&lt;/code&gt; or &lt;code&gt;FF&lt;/code&gt;). Spaces are ignored and can be used freely as a visual separator.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;bin:&lt;/code&gt; Converts binary values to bytes. Single byte is always eight characters long (e.g. &lt;code&gt;00001010&lt;/code&gt;). Spaces are ignored and can be used freely as a visual separator.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;In addition to giving the input as a string, it is possible to use lists or other iterables containing individual characters or numbers. In that case numbers do not need to be padded to certain length and they cannot contain extra spaces.&lt;/p&gt;
&lt;p&gt;Examples (last column shows returned bytes):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;hyvä&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# hyv\xe4&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;\xff\x07&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# \xff\x07&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;82 70&lt;/td&gt;
&lt;td&gt;int&lt;/td&gt;
&lt;td&gt;# RF&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;0b10 0x10&lt;/td&gt;
&lt;td&gt;int&lt;/td&gt;
&lt;td&gt;# \x02\x10&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;ff 00 07&lt;/td&gt;
&lt;td&gt;hex&lt;/td&gt;
&lt;td&gt;# \xff\x00\x07&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;5246212121&lt;/td&gt;
&lt;td&gt;hex&lt;/td&gt;
&lt;td&gt;# RF!!!&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;0000 1000&lt;/td&gt;
&lt;td&gt;bin&lt;/td&gt;
&lt;td&gt;# \x08&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${input} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;12&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;${input}&lt;/td&gt;
&lt;td&gt;int&lt;/td&gt;
&lt;td&gt;# \x01\x02\x0c&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bytes} =&lt;/td&gt;
&lt;td&gt;Convert To Bytes&lt;/td&gt;
&lt;td&gt;${input}&lt;/td&gt;
&lt;td&gt;hex&lt;/td&gt;
&lt;td&gt;# \x01\x02\x12&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;span class="name"&gt;Encode String To Bytes&lt;/span&gt; in &lt;code&gt;String&lt;/code&gt; library if you need to convert text to bytes using a certain encoding.&lt;/p&gt;</doc>
<shortdoc>Converts the given ``input`` to bytes according to the ``input_type``.</shortdoc>
</kw>
<kw name="Convert To Hex" lineno="213">
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
<doc>&lt;p&gt;Converts the given item to a hexadecimal string.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;item&lt;/code&gt;, with an optional &lt;code&gt;base&lt;/code&gt;, is first converted to an integer using &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt; internally. After that it is converted to a hexadecimal number (base 16) represented as a string such as &lt;code&gt;FF0A&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The returned value can contain an optional &lt;code&gt;prefix&lt;/code&gt; and can be required to be of minimum &lt;code&gt;length&lt;/code&gt; (excluding the prefix and a possible minus sign). If the value is initially shorter than the required length, it is padded with zeros.&lt;/p&gt;
&lt;p&gt;By default the value is returned as an upper case string, but the &lt;code&gt;lowercase&lt;/code&gt; argument a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) turns the value (but not the given prefix) to lower case.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Hex&lt;/td&gt;
&lt;td&gt;255&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is FF&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Hex&lt;/td&gt;
&lt;td&gt;-10&lt;/td&gt;
&lt;td&gt;prefix=0x&lt;/td&gt;
&lt;td&gt;length=2&lt;/td&gt;
&lt;td&gt;# Result is -0x0A&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Hex&lt;/td&gt;
&lt;td&gt;255&lt;/td&gt;
&lt;td&gt;prefix=X&lt;/td&gt;
&lt;td&gt;lowercase=yes&lt;/td&gt;
&lt;td&gt;# Result is Xff&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt;, &lt;a href="#Convert%20To%20Binary" class="name"&gt;Convert To Binary&lt;/a&gt; and &lt;a href="#Convert%20To%20Octal" class="name"&gt;Convert To Octal&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to a hexadecimal string.</shortdoc>
</kw>
<kw name="Convert To Integer" lineno="106">
<arguments repr="item, base=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="base=None">
<name>base</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given item to an integer number.&lt;/p&gt;
&lt;p&gt;If the given item is a string, it is by default expected to be an integer in base 10. There are two ways to convert from other bases:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Give base explicitly to the keyword as &lt;code&gt;base&lt;/code&gt; argument.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;Prefix the given string with the base so that &lt;code&gt;0b&lt;/code&gt; means binary (base 2), &lt;code&gt;0o&lt;/code&gt; means octal (base 8), and &lt;code&gt;0x&lt;/code&gt; means hex (base 16). The prefix is considered only when &lt;code&gt;base&lt;/code&gt; argument is not given and may itself be prefixed with a plus or minus sign.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;The syntax is case-insensitive and possible spaces are ignored.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Integer&lt;/td&gt;
&lt;td&gt;100&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is 100&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Integer&lt;/td&gt;
&lt;td&gt;FF AA&lt;/td&gt;
&lt;td&gt;16&lt;/td&gt;
&lt;td&gt;# Result is 65450&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Integer&lt;/td&gt;
&lt;td&gt;100&lt;/td&gt;
&lt;td&gt;8&lt;/td&gt;
&lt;td&gt;# Result is 64&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Integer&lt;/td&gt;
&lt;td&gt;-100&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;# Result is -4&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Integer&lt;/td&gt;
&lt;td&gt;0b100&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is 4&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Integer&lt;/td&gt;
&lt;td&gt;-0x100&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is -256&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Convert%20To%20Number" class="name"&gt;Convert To Number&lt;/a&gt;, &lt;a href="#Convert%20To%20Binary" class="name"&gt;Convert To Binary&lt;/a&gt;, &lt;a href="#Convert%20To%20Octal" class="name"&gt;Convert To Octal&lt;/a&gt;, &lt;a href="#Convert%20To%20Hex" class="name"&gt;Convert To Hex&lt;/a&gt;, and &lt;a href="#Convert%20To%20Bytes" class="name"&gt;Convert To Bytes&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to an integer number.</shortdoc>
</kw>
<kw name="Convert To Number" lineno="252">
<arguments repr="item, precision=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="precision=None">
<name>precision</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given item to a floating point number.&lt;/p&gt;
&lt;p&gt;If the optional &lt;code&gt;precision&lt;/code&gt; is positive or zero, the returned number is rounded to that number of decimal digits. Negative precision means that the number is rounded to the closest multiple of 10 to the power of the absolute precision. If a number is equally close to a certain precision, it is always rounded away from zero.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Number&lt;/td&gt;
&lt;td&gt;42.512&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is 42.512&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Number&lt;/td&gt;
&lt;td&gt;42.512&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;# Result is 42.5&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Number&lt;/td&gt;
&lt;td&gt;42.512&lt;/td&gt;
&lt;td&gt;0&lt;/td&gt;
&lt;td&gt;# Result is 43.0&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Number&lt;/td&gt;
&lt;td&gt;42.512&lt;/td&gt;
&lt;td&gt;-1&lt;/td&gt;
&lt;td&gt;# Result is 40.0&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Notice that machines generally cannot store floating point numbers accurately. This may cause surprises with these numbers in general and also when they are rounded. For more information see, for example, these resources:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="http://docs.python.org/tutorial/floatingpoint.html"&gt;http://docs.python.org/tutorial/floatingpoint.html&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition"&gt;http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;If you want to avoid possible problems with floating point numbers, you can implement custom keywords using Python's &lt;a href="http://docs.python.org/library/decimal.html"&gt;decimal&lt;/a&gt; or &lt;a href="http://docs.python.org/library/fractions.html"&gt;fractions&lt;/a&gt; modules.&lt;/p&gt;
&lt;p&gt;If you need an integer number, use &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt; instead.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to a floating point number.</shortdoc>
</kw>
<kw name="Convert To Octal" lineno="191">
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
<doc>&lt;p&gt;Converts the given item to an octal string.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;item&lt;/code&gt;, with an optional &lt;code&gt;base&lt;/code&gt;, is first converted to an integer using &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt; internally. After that it is converted to an octal number (base 8) represented as a string such as &lt;code&gt;775&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The returned value can contain an optional &lt;code&gt;prefix&lt;/code&gt; and can be required to be of minimum &lt;code&gt;length&lt;/code&gt; (excluding the prefix and a possible minus sign). If the value is initially shorter than the required length, it is padded with zeros.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Octal&lt;/td&gt;
&lt;td&gt;10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Result is 12&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Octal&lt;/td&gt;
&lt;td&gt;-F&lt;/td&gt;
&lt;td&gt;base=16&lt;/td&gt;
&lt;td&gt;prefix=0&lt;/td&gt;
&lt;td&gt;# Result is -017&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Convert To Octal&lt;/td&gt;
&lt;td&gt;16&lt;/td&gt;
&lt;td&gt;prefix=oct&lt;/td&gt;
&lt;td&gt;length=4&lt;/td&gt;
&lt;td&gt;# Result is oct0020&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt;, &lt;a href="#Convert%20To%20Binary" class="name"&gt;Convert To Binary&lt;/a&gt; and &lt;a href="#Convert%20To%20Hex" class="name"&gt;Convert To Hex&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to an octal string.</shortdoc>
</kw>
<kw name="Convert To String" lineno="305">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>&lt;p&gt;Converts the given item to a Unicode string.&lt;/p&gt;
&lt;p&gt;Strings are also &lt;a href="http://www.macchiato.com/unicode/nfc-faq"&gt;NFC normalized&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Use &lt;span class="name"&gt;Encode String To Bytes&lt;/span&gt; and &lt;span class="name"&gt;Decode Bytes To String&lt;/span&gt; keywords in &lt;code&gt;String&lt;/code&gt; library if you need to convert between Unicode and byte strings using different encodings. Use &lt;a href="#Convert%20To%20Bytes" class="name"&gt;Convert To Bytes&lt;/a&gt; if you just want to create byte strings.&lt;/p&gt;</doc>
<shortdoc>Converts the given item to a Unicode string.</shortdoc>
</kw>
<kw name="Create Dictionary" lineno="446">
<arguments repr="*items">
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
</arguments>
<doc>&lt;p&gt;Creates and returns a dictionary based on the given &lt;code&gt;items&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Items are typically given using the &lt;code&gt;key=value&lt;/code&gt; syntax same way as &lt;code&gt;&amp;amp;{dictionary}&lt;/code&gt; variables are created in the Variable table. Both keys and values can contain variables, and possible equal sign in key can be escaped with a backslash like &lt;code&gt;escaped\=key=value&lt;/code&gt;. It is also possible to get items from existing dictionaries by simply using them like &lt;code&gt;&amp;amp;{dict}&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Alternatively items can be specified so that keys and values are given separately. This and the &lt;code&gt;key=value&lt;/code&gt; syntax can even be combined, but separately given items must be first. If same key is used multiple times, the last value has precedence.&lt;/p&gt;
&lt;p&gt;The returned dictionary is ordered, and values with strings as keys can also be accessed using a convenient dot-access syntax like &lt;code&gt;${dict.key}&lt;/code&gt;. Technically the returned dictionary is Robot Framework's own &lt;code&gt;DotDict&lt;/code&gt; instance. If there is a need, it can be converted into a regular Python &lt;code&gt;dict&lt;/code&gt; instance by using the &lt;span class="name"&gt;Convert To Dictionary&lt;/span&gt; keyword from the Collections library.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&amp;amp;{dict} =&lt;/td&gt;
&lt;td&gt;Create Dictionary&lt;/td&gt;
&lt;td&gt;key=value&lt;/td&gt;
&lt;td&gt;foo=bar&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# key=value syntax&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;${dict} == {'key': 'value', 'foo': 'bar'}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&amp;amp;{dict2} =&lt;/td&gt;
&lt;td&gt;Create Dictionary&lt;/td&gt;
&lt;td&gt;key&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;foo&lt;/td&gt;
&lt;td&gt;bar&lt;/td&gt;
&lt;td&gt;# separate key and value&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${dict}&lt;/td&gt;
&lt;td&gt;${dict2}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&amp;amp;{dict} =&lt;/td&gt;
&lt;td&gt;Create Dictionary&lt;/td&gt;
&lt;td&gt;${1}=${2}&lt;/td&gt;
&lt;td&gt;&amp;amp;{dict}&lt;/td&gt;
&lt;td&gt;foo=new&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# using variables&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;${dict} == {1: 2, 'key': 'value', 'foo': 'new'}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${dict.key}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# dot-access&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Creates and returns a dictionary based on the given ``items``.</shortdoc>
</kw>
<kw name="Create List" lineno="432">
<arguments repr="*items">
<arg kind="VAR_POSITIONAL" required="false" repr="*items">
<name>items</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a list containing given items.&lt;/p&gt;
&lt;p&gt;The returned list can be assigned both to &lt;code&gt;${scalar}&lt;/code&gt; and &lt;code&gt;@{list}&lt;/code&gt; variables.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{list} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;a&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;td&gt;c&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${scalar} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;a&lt;/td&gt;
&lt;td&gt;b&lt;/td&gt;
&lt;td&gt;c&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ints} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;${1}&lt;/td&gt;
&lt;td&gt;${2}&lt;/td&gt;
&lt;td&gt;${3}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns a list containing given items.</shortdoc>
</kw>
<kw name="Evaluate" lineno="3252">
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
<doc>&lt;p&gt;Evaluates the given expression in Python and returns the result.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;expression&lt;/code&gt; is evaluated in Python as explained in the &lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt; section.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;modules&lt;/code&gt; argument can be used to specify a comma separated list of Python modules to be imported and added to the evaluation namespace.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;namespace&lt;/code&gt; argument can be used to pass a custom evaluation namespace as a dictionary. Possible &lt;code&gt;modules&lt;/code&gt; are added to this namespace.&lt;/p&gt;
&lt;p&gt;Variables used like &lt;code&gt;${variable}&lt;/code&gt; are replaced in the expression before evaluation. Variables are also available in the evaluation namespace and can be accessed using the special &lt;code&gt;$variable&lt;/code&gt; syntax as explained in the &lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt; section.&lt;/p&gt;
&lt;p&gt;Starting from Robot Framework 3.2, modules used in the expression are imported automatically. There are, however, two cases where they need to be explicitly specified using the &lt;code&gt;modules&lt;/code&gt; argument:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;When nested modules like &lt;code&gt;rootmod.submod&lt;/code&gt; are implemented so that the root module does not automatically import sub modules. This is illustrated by the &lt;code&gt;selenium.webdriver&lt;/code&gt; example below.&lt;/li&gt;
&lt;/ul&gt;
&lt;ul&gt;
&lt;li&gt;When using a module in the expression part of a list comprehension. This is illustrated by the &lt;code&gt;json&lt;/code&gt; example below.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples (expecting &lt;code&gt;${result}&lt;/code&gt; is number 3.14):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${status} =&lt;/td&gt;
&lt;td&gt;Evaluate&lt;/td&gt;
&lt;td&gt;0 &amp;lt; ${result} &amp;lt; 10&lt;/td&gt;
&lt;td&gt;# Would also work with string '3.14'&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${status} =&lt;/td&gt;
&lt;td&gt;Evaluate&lt;/td&gt;
&lt;td&gt;0 &amp;lt; $result &amp;lt; 10&lt;/td&gt;
&lt;td&gt;# Using variable itself, not string representation&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${random} =&lt;/td&gt;
&lt;td&gt;Evaluate&lt;/td&gt;
&lt;td&gt;random.randint(0, sys.maxsize)&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${options} =&lt;/td&gt;
&lt;td&gt;Evaluate&lt;/td&gt;
&lt;td&gt;selenium.webdriver.ChromeOptions()&lt;/td&gt;
&lt;td&gt;modules=selenium.webdriver&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${items} =&lt;/td&gt;
&lt;td&gt;Evaluate&lt;/td&gt;
&lt;td&gt;[json.loads(item) for item in ('1', '"b"')]&lt;/td&gt;
&lt;td&gt;modules=json&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ns} =&lt;/td&gt;
&lt;td&gt;Create Dictionary&lt;/td&gt;
&lt;td&gt;x=${4}&lt;/td&gt;
&lt;td&gt;y=${2}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Evaluate&lt;/td&gt;
&lt;td&gt;x*10 + y&lt;/td&gt;
&lt;td&gt;namespace=${ns}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${status} = True
${random} = &amp;lt;random integer&amp;gt;
${options} = ChromeOptions instance
${items} = [1, 'b']
${result} = 42
&lt;/pre&gt;
&lt;p&gt;&lt;b&gt;NOTE&lt;/b&gt;: Prior to Robot Framework 3.2 using &lt;code&gt;modules=rootmod.submod&lt;/code&gt; was not enough to make the root module itself available in the evaluation namespace. It needed to be taken into use explicitly like &lt;code&gt;modules=rootmod, rootmod.submod&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Evaluates the given expression in Python and returns the result.</shortdoc>
</kw>
<kw name="Exit For Loop" lineno="2564">
<arguments repr="">
</arguments>
<doc>&lt;p&gt;Stops executing the enclosing for loop.&lt;/p&gt;
&lt;p&gt;Exits the enclosing for loop and continues execution after it. Can be used directly in a for loop or in a keyword that the loop uses.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;FOR&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;IN&lt;/td&gt;
&lt;td&gt;@{VALUES}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Run Keyword If&lt;/td&gt;
&lt;td&gt;'${var}' == 'EXIT'&lt;/td&gt;
&lt;td&gt;Exit For Loop&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Do Something&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;END&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Exit%20For%20Loop%20If" class="name"&gt;Exit For Loop If&lt;/a&gt; to conditionally exit a for loop without using &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; or other wrapper keywords.&lt;/p&gt;</doc>
<shortdoc>Stops executing the enclosing for loop.</shortdoc>
</kw>
<kw name="Exit For Loop If" lineno="2582">
<arguments repr="condition">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
</arguments>
<doc>&lt;p&gt;Stops executing the enclosing for loop if the &lt;code&gt;condition&lt;/code&gt; is true.&lt;/p&gt;
&lt;p&gt;A wrapper for &lt;a href="#Exit%20For%20Loop" class="name"&gt;Exit For Loop&lt;/a&gt; to exit a for loop based on the given condition. The condition is evaluated using the same semantics as with &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;FOR&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;IN&lt;/td&gt;
&lt;td&gt;@{VALUES}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Exit For Loop If&lt;/td&gt;
&lt;td&gt;'${var}' == 'EXIT'&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Do Something&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;END&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Stops executing the enclosing for loop if the ``condition`` is true.</shortdoc>
</kw>
<kw name="Fail" lineno="510">
<arguments repr="msg=None, *tags">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>&lt;p&gt;Fails the test with the given message and optionally alters its tags.&lt;/p&gt;
&lt;p&gt;The error message is specified using the &lt;code&gt;msg&lt;/code&gt; argument. It is possible to use HTML in the given error message, similarly as with any other keyword accepting an error message, by prefixing the error with &lt;code&gt;*HTML*&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;It is possible to modify tags of the current test case by passing tags after the message. Tags starting with a hyphen (e.g. &lt;code&gt;-regression&lt;/code&gt;) are removed and others added. Tags are modified using &lt;a href="#Set%20Tags" class="name"&gt;Set Tags&lt;/a&gt; and &lt;a href="#Remove%20Tags" class="name"&gt;Remove Tags&lt;/a&gt; internally, and the semantics setting and removing them are the same as with these keywords.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Fail&lt;/td&gt;
&lt;td&gt;Test not ready&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Fails with the given message.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Fail&lt;/td&gt;
&lt;td&gt;*HTML*&amp;lt;b&amp;gt;Test not ready&amp;lt;/b&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Fails using HTML in the message.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Fail&lt;/td&gt;
&lt;td&gt;Test not ready&lt;/td&gt;
&lt;td&gt;not-ready&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Fails and adds 'not-ready' tag.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Fail&lt;/td&gt;
&lt;td&gt;OS not supported&lt;/td&gt;
&lt;td&gt;-regression&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Removes tag 'regression'.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Fail&lt;/td&gt;
&lt;td&gt;My message&lt;/td&gt;
&lt;td&gt;tag&lt;/td&gt;
&lt;td&gt;-t*&lt;/td&gt;
&lt;td&gt;# Removes all tags starting with 't' except the newly added 'tag'.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Fatal%20Error" class="name"&gt;Fatal Error&lt;/a&gt; if you need to stop the whole test execution.&lt;/p&gt;</doc>
<shortdoc>Fails the test with the given message and optionally alters its tags.</shortdoc>
</kw>
<kw name="Fatal Error" lineno="536">
<arguments repr="msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Stops the whole test execution.&lt;/p&gt;
&lt;p&gt;The test or suite where this keyword is used fails with the provided message, and subsequent tests fail with a canned message. Possible teardowns will nevertheless be executed.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Fail" class="name"&gt;Fail&lt;/a&gt; if you only want to stop one test case unconditionally.&lt;/p&gt;</doc>
<shortdoc>Stops the whole test execution.</shortdoc>
</kw>
<kw name="Get Count" lineno="1286">
<arguments repr="container, item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="container">
<name>container</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns and logs how many times &lt;code&gt;item&lt;/code&gt; is found from &lt;code&gt;container&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword works with Python strings and lists and all objects that either have &lt;code&gt;count&lt;/code&gt; method or can be converted to Python lists.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${count} =&lt;/td&gt;
&lt;td&gt;Get Count&lt;/td&gt;
&lt;td&gt;${some item}&lt;/td&gt;
&lt;td&gt;interesting value&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;5 &amp;lt; ${count} &amp;lt; 10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns and logs how many times ``item`` is found from ``container``.</shortdoc>
</kw>
<kw name="Get Length" lineno="1399">
<arguments repr="item">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns and logs the length of the given item as an integer.&lt;/p&gt;
&lt;p&gt;The item can be anything that has a length, for example, a string, a list, or a mapping. The keyword first tries to get the length with the Python function &lt;code&gt;len&lt;/code&gt;, which calls the  item's &lt;code&gt;__len__&lt;/code&gt; method internally. If that fails, the keyword tries to call the item's possible &lt;code&gt;length&lt;/code&gt; and &lt;code&gt;size&lt;/code&gt; methods directly. The final attempt is trying to get the value of the item's &lt;code&gt;length&lt;/code&gt; attribute. If all these attempts are unsuccessful, the keyword fails.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${length} =&lt;/td&gt;
&lt;td&gt;Get Length&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${length}&lt;/td&gt;
&lt;td&gt;13&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{list} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;Hello,&lt;/td&gt;
&lt;td&gt;world!&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${length} =&lt;/td&gt;
&lt;td&gt;Get Length&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${length}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Length%20Should%20Be" class="name"&gt;Length Should Be&lt;/a&gt;, &lt;a href="#Should%20Be%20Empty" class="name"&gt;Should Be Empty&lt;/a&gt; and &lt;a href="#Should%20Not%20Be%20Empty" class="name"&gt;Should Not Be Empty&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns and logs the length of the given item as an integer.</shortdoc>
</kw>
<kw name="Get Library Instance" lineno="3525">
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
<doc>&lt;p&gt;Returns the currently active instance of the specified test library.&lt;/p&gt;
&lt;p&gt;This keyword makes it easy for test libraries to interact with other test libraries that have state. This is illustrated by the Python example below:&lt;/p&gt;
&lt;pre&gt;
from robot.libraries.BuiltIn import BuiltIn

def title_should_start_with(expected):
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    title = seleniumlib.get_title()
    if not title.startswith(expected):
        raise AssertionError("Title '%s' did not start with '%s'"
                             % (title, expected))
&lt;/pre&gt;
&lt;p&gt;It is also possible to use this keyword in the test data and pass the returned library instance to another keyword. If a library is imported with a custom name, the &lt;code&gt;name&lt;/code&gt; used to get the instance must be that name and not the original library name.&lt;/p&gt;
&lt;p&gt;If the optional argument &lt;code&gt;all&lt;/code&gt; is given a true value, then a dictionary mapping all library names to instances will be returned.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&amp;amp;{all libs} =&lt;/td&gt;
&lt;td&gt;Get library instance&lt;/td&gt;
&lt;td&gt;all=True&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns the currently active instance of the specified test library.</shortdoc>
</kw>
<kw name="Get Time" lineno="3169">
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
<doc>&lt;p&gt;Returns the given time in the requested format.&lt;/p&gt;
&lt;p&gt;&lt;b&gt;NOTE:&lt;/b&gt; DateTime library contains much more flexible keywords for getting the current date and time and for date and time handling in general.&lt;/p&gt;
&lt;p&gt;How time is returned is determined based on the given &lt;code&gt;format&lt;/code&gt; string as follows. Note that all checks are case-insensitive.&lt;/p&gt;
&lt;p&gt;1) If &lt;code&gt;format&lt;/code&gt; contains the word &lt;code&gt;epoch&lt;/code&gt;, the time is returned in seconds after the UNIX epoch (1970-01-01 00:00:00 UTC). The return value is always an integer.&lt;/p&gt;
&lt;p&gt;2) If &lt;code&gt;format&lt;/code&gt; contains any of the words &lt;code&gt;year&lt;/code&gt;, &lt;code&gt;month&lt;/code&gt;, &lt;code&gt;day&lt;/code&gt;, &lt;code&gt;hour&lt;/code&gt;, &lt;code&gt;min&lt;/code&gt;, or &lt;code&gt;sec&lt;/code&gt;, only the selected parts are returned. The order of the returned parts is always the one in the previous sentence and the order of words in &lt;code&gt;format&lt;/code&gt; is not significant. The parts are returned as zero-padded strings (e.g. May -&amp;gt; &lt;code&gt;05&lt;/code&gt;).&lt;/p&gt;
&lt;p&gt;3) Otherwise (and by default) the time is returned as a timestamp string in the format &lt;code&gt;2006-02-24 15:08:31&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;By default this keyword returns the current local time, but that can be altered using &lt;code&gt;time&lt;/code&gt; argument as explained below. Note that all checks involving strings are case-insensitive.&lt;/p&gt;
&lt;p&gt;1) If &lt;code&gt;time&lt;/code&gt; is a number, or a string that can be converted to a number, it is interpreted as seconds since the UNIX epoch. This documentation was originally written about 1177654467 seconds after the epoch.&lt;/p&gt;
&lt;p&gt;2) If &lt;code&gt;time&lt;/code&gt; is a timestamp, that time will be used. Valid timestamp formats are &lt;code&gt;YYYY-MM-DD hh:mm:ss&lt;/code&gt; and &lt;code&gt;YYYYMMDD hhmmss&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;3) If &lt;code&gt;time&lt;/code&gt; is equal to &lt;code&gt;NOW&lt;/code&gt; (default), the current local time is used.&lt;/p&gt;
&lt;p&gt;4) If &lt;code&gt;time&lt;/code&gt; is equal to &lt;code&gt;UTC&lt;/code&gt;, the current time in &lt;a href="http://en.wikipedia.org/wiki/Coordinated_Universal_Time"&gt;UTC&lt;/a&gt; is used.&lt;/p&gt;
&lt;p&gt;5) If &lt;code&gt;time&lt;/code&gt; is in the format like &lt;code&gt;NOW - 1 day&lt;/code&gt; or &lt;code&gt;UTC + 1 hour 30 min&lt;/code&gt;, the current local/UTC time plus/minus the time specified with the time string is used. The time string format is described in an appendix of Robot Framework User Guide.&lt;/p&gt;
&lt;p&gt;Examples (expecting the current local time is 2006-03-29 15:06:21):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${secs} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;epoch&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${year} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;return year&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${yyyy}&lt;/td&gt;
&lt;td&gt;${mm}&lt;/td&gt;
&lt;td&gt;${dd} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;year,month,day&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{time} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;year month day hour min sec&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${y}&lt;/td&gt;
&lt;td&gt;${s} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;seconds and year&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${time} = '2006-03-29 15:06:21'
${secs} = 1143637581
${year} = '2006'
${yyyy} = '2006', ${mm} = '03', ${dd} = '29'
@{time} = ['2006', '03', '29', '15', '06', '21']
${y} = '2006'
${s} = '21'
&lt;/pre&gt;
&lt;p&gt;Examples (expecting the current local time is 2006-03-29 15:06:21 and UTC time is 2006-03-29 12:06:21):&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;1177654467&lt;/td&gt;
&lt;td&gt;# Time given as epoch seconds&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${secs} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;sec&lt;/td&gt;
&lt;td&gt;2007-04-27 09:14:27&lt;/td&gt;
&lt;td&gt;# Time given as a timestamp&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${year} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;year&lt;/td&gt;
&lt;td&gt;NOW&lt;/td&gt;
&lt;td&gt;# The local time of execution&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{time} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;hour min sec&lt;/td&gt;
&lt;td&gt;NOW + 1h 2min 3s&lt;/td&gt;
&lt;td&gt;# 1h 2min 3s added to the local time&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{utc} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;hour min sec&lt;/td&gt;
&lt;td&gt;UTC&lt;/td&gt;
&lt;td&gt;# The UTC time of execution&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${hour} =&lt;/td&gt;
&lt;td&gt;Get Time&lt;/td&gt;
&lt;td&gt;hour&lt;/td&gt;
&lt;td&gt;UTC - 1 hour&lt;/td&gt;
&lt;td&gt;# 1h subtracted from the UTC  time&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${time} = '2007-04-27 09:14:27'
${secs} = 27
${year} = '2006'
@{time} = ['16', '08', '24']
@{utc} = ['12', '06', '21']
${hour} = '11'
&lt;/pre&gt;</doc>
<shortdoc>Returns the given time in the requested format.</shortdoc>
</kw>
<kw name="Get Variable Value" lineno="1521">
<arguments repr="name, default=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=None">
<name>default</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns variable value or &lt;code&gt;default&lt;/code&gt; if the variable does not exist.&lt;/p&gt;
&lt;p&gt;The name of the variable can be given either as a normal variable name (e.g. &lt;code&gt;${NAME}&lt;/code&gt;) or in escaped format (e.g. &lt;code&gt;\${NAME}&lt;/code&gt;). Notice that the former has some limitations explained in &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${x} =&lt;/td&gt;
&lt;td&gt;Get Variable Value&lt;/td&gt;
&lt;td&gt;${a}&lt;/td&gt;
&lt;td&gt;default&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${y} =&lt;/td&gt;
&lt;td&gt;Get Variable Value&lt;/td&gt;
&lt;td&gt;${a}&lt;/td&gt;
&lt;td&gt;${b}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${z} =&lt;/td&gt;
&lt;td&gt;Get Variable Value&lt;/td&gt;
&lt;td&gt;${z}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${x} gets value of ${a} if ${a} exists and string 'default' otherwise
${y} gets value of ${a} if ${a} exists and value of ${b} otherwise
${z} is set to Python None if it does not exist previously
&lt;/pre&gt;
&lt;p&gt;See &lt;a href="#Set%20Variable%20If" class="name"&gt;Set Variable If&lt;/a&gt; for another keyword to set variables dynamically.&lt;/p&gt;</doc>
<shortdoc>Returns variable value or ``default`` if the variable does not exist.</shortdoc>
</kw>
<kw name="Get Variables" lineno="1491">
<arguments repr="no_decoration=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="no_decoration=False">
<name>no_decoration</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a dictionary containing all variables in the current scope.&lt;/p&gt;
&lt;p&gt;Variables are returned as a special dictionary that allows accessing variables in space, case, and underscore insensitive manner similarly as accessing variables in the test data. This dictionary supports all same operations as normal Python dictionaries and, for example, Collections library can be used to access or modify it. Modifying the returned dictionary has no effect on the variables available in the current scope.&lt;/p&gt;
&lt;p&gt;By default variables are returned with &lt;code&gt;${}&lt;/code&gt;, &lt;code&gt;@{}&lt;/code&gt; or &lt;code&gt;&amp;amp;{}&lt;/code&gt; decoration based on variable types. Giving a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) to the optional argument &lt;code&gt;no_decoration&lt;/code&gt; will return the variables without the decoration.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${example_variable} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;example value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${variables} =&lt;/td&gt;
&lt;td&gt;Get Variables&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Dictionary Should Contain Key&lt;/td&gt;
&lt;td&gt;${variables}&lt;/td&gt;
&lt;td&gt;\${example_variable}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Dictionary Should Contain Key&lt;/td&gt;
&lt;td&gt;${variables}&lt;/td&gt;
&lt;td&gt;\${ExampleVariable}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set To Dictionary&lt;/td&gt;
&lt;td&gt;${variables}&lt;/td&gt;
&lt;td&gt;\${name}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Variable Should Not Exist&lt;/td&gt;
&lt;td&gt;\${name}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${no decoration} =&lt;/td&gt;
&lt;td&gt;Get Variables&lt;/td&gt;
&lt;td&gt;no_decoration=Yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Dictionary Should Contain Key&lt;/td&gt;
&lt;td&gt;${no decoration}&lt;/td&gt;
&lt;td&gt;example_variable&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns a dictionary containing all variables in the current scope.</shortdoc>
</kw>
<kw name="Import Library" lineno="3026">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Imports a library with the given name and optional arguments.&lt;/p&gt;
&lt;p&gt;This functionality allows dynamic importing of libraries while tests are running. That may be necessary, if the library itself is dynamic and not yet available when test data is processed. In a normal case, libraries should be imported using the Library setting in the Setting table.&lt;/p&gt;
&lt;p&gt;This keyword supports importing libraries both using library names and physical paths. When paths are used, they must be given in absolute format or found from &lt;a href="http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#pythonpath-jythonpath-and-ironpythonpath"&gt;search path&lt;/a&gt;. Forward slashes can be used as path separators in all operating systems.&lt;/p&gt;
&lt;p&gt;It is possible to pass arguments to the imported library and also named argument syntax works if the library supports it. &lt;code&gt;WITH NAME&lt;/code&gt; syntax can be used to give a custom name to the imported library.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Import Library&lt;/td&gt;
&lt;td&gt;MyLibrary&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Import Library&lt;/td&gt;
&lt;td&gt;${CURDIR}/../Library.py&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;named=arg2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Import Library&lt;/td&gt;
&lt;td&gt;${LIBRARIES}/Lib.java&lt;/td&gt;
&lt;td&gt;arg&lt;/td&gt;
&lt;td&gt;WITH NAME&lt;/td&gt;
&lt;td&gt;JavaLib&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Imports a library with the given name and optional arguments.</shortdoc>
</kw>
<kw name="Import Resource" lineno="3088">
<arguments repr="path">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
</arguments>
<doc>&lt;p&gt;Imports a resource file with the given path.&lt;/p&gt;
&lt;p&gt;Resources imported with this keyword are set into the test suite scope similarly when importing them in the Setting table using the Resource setting.&lt;/p&gt;
&lt;p&gt;The given path must be absolute or found from &lt;a href="http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#pythonpath-jythonpath-and-ironpythonpath"&gt;search path&lt;/a&gt;. Forward slashes can be used as path separator regardless the operating system.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Import Resource&lt;/td&gt;
&lt;td&gt;${CURDIR}/resource.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Import Resource&lt;/td&gt;
&lt;td&gt;${CURDIR}/../resources/resource.html&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Import Resource&lt;/td&gt;
&lt;td&gt;found_from_pythonpath.robot&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Imports a resource file with the given path.</shortdoc>
</kw>
<kw name="Import Variables" lineno="3063">
<arguments repr="path, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Imports a variable file with the given path and optional arguments.&lt;/p&gt;
&lt;p&gt;Variables imported with this keyword are set into the test suite scope similarly when importing them in the Setting table using the Variables setting. These variables override possible existing variables with the same names. This functionality can thus be used to import new variables, for example, for each test in a test suite.&lt;/p&gt;
&lt;p&gt;The given path must be absolute or found from &lt;a href="http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#pythonpath-jythonpath-and-ironpythonpath"&gt;search path&lt;/a&gt;. Forward slashes can be used as path separator regardless the operating system.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Import Variables&lt;/td&gt;
&lt;td&gt;${CURDIR}/variables.py&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Import Variables&lt;/td&gt;
&lt;td&gt;${CURDIR}/../vars/env.py&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Import Variables&lt;/td&gt;
&lt;td&gt;file_from_pythonpath.py&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Imports a variable file with the given path and optional arguments.</shortdoc>
</kw>
<kw name="Keyword Should Exist" lineno="3151">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the given keyword exists in the current scope.&lt;/p&gt;
&lt;p&gt;Fails also if there are more than one keywords with the same name. Works both with the short name (e.g. &lt;code&gt;Log&lt;/code&gt;) and the full name (e.g. &lt;code&gt;BuiltIn.Log&lt;/code&gt;).&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Variable%20Should%20Exist" class="name"&gt;Variable Should Exist&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails unless the given keyword exists in the current scope.</shortdoc>
</kw>
<kw name="Length Should Be" lineno="1447">
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
<doc>&lt;p&gt;Verifies that the length of the given item is correct.&lt;/p&gt;
&lt;p&gt;The length of the item is got using the &lt;a href="#Get%20Length" class="name"&gt;Get Length&lt;/a&gt; keyword. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Verifies that the length of the given item is correct.</shortdoc>
</kw>
<kw name="Log" lineno="2859">
<arguments repr="message, level=INFO, html=False, console=False, repr=False, formatter=str">
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
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="repr=False">
<name>repr</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="formatter=str">
<name>formatter</name>
<default>str</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs the given message with the given level.&lt;/p&gt;
&lt;p&gt;Valid levels are TRACE, DEBUG, INFO (default), HTML, WARN, and ERROR. Messages below the current active log level are ignored. See &lt;a href="#Set%20Log%20Level" class="name"&gt;Set Log Level&lt;/a&gt; keyword and &lt;code&gt;--loglevel&lt;/code&gt; command line option for more details about setting the level.&lt;/p&gt;
&lt;p&gt;Messages logged with the WARN or ERROR levels will be automatically visible also in the console and in the Test Execution Errors section in the log file.&lt;/p&gt;
&lt;p&gt;If the &lt;code&gt;html&lt;/code&gt; argument is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the message will be considered HTML and special characters such as &lt;code&gt;&amp;lt;&lt;/code&gt; are not escaped. For example, logging &lt;code&gt;&amp;lt;img src="image.png"&amp;gt;&lt;/code&gt; creates an image when &lt;code&gt;html&lt;/code&gt; is true, but otherwise the message is that exact string. An alternative to using the &lt;code&gt;html&lt;/code&gt; argument is using the HTML pseudo log level. It logs the message as HTML using the INFO level.&lt;/p&gt;
&lt;p&gt;If the &lt;code&gt;console&lt;/code&gt; argument is true, the message will be written to the console where test execution was started from in addition to the log file. This keyword always uses the standard output stream and adds a newline after the written message. Use &lt;a href="#Log%20To%20Console" class="name"&gt;Log To Console&lt;/a&gt; instead if either of these is undesirable,&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;formatter&lt;/code&gt; argument controls how to format the string representation of the message. Possible values are &lt;code&gt;str&lt;/code&gt; (default), &lt;code&gt;repr&lt;/code&gt; and &lt;code&gt;ascii&lt;/code&gt;, and they work similarly to Python built-in functions with same names. When using &lt;code&gt;repr&lt;/code&gt;, bigger lists, dictionaries and other containers are also pretty-printed so that there is one item per row. For more details see &lt;a href="#String%20representations" class="name"&gt;String representations&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The old way to control string representation was using the &lt;code&gt;repr&lt;/code&gt; argument, and &lt;code&gt;repr=True&lt;/code&gt; is still equivalent to using &lt;code&gt;formatter=repr&lt;/code&gt;. The &lt;code&gt;repr&lt;/code&gt; argument will be deprecated in the future, though, and using &lt;code&gt;formatter&lt;/code&gt; is thus recommended.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Normal INFO message.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;Warning, world!&lt;/td&gt;
&lt;td&gt;WARN&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Warning.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;&amp;lt;b&amp;gt;Hello&amp;lt;/b&amp;gt;, world!&lt;/td&gt;
&lt;td&gt;html=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# INFO message as HTML.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;&amp;lt;b&amp;gt;Hello&amp;lt;/b&amp;gt;, world!&lt;/td&gt;
&lt;td&gt;HTML&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Same as above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;&amp;lt;b&amp;gt;Hello&amp;lt;/b&amp;gt;, world!&lt;/td&gt;
&lt;td&gt;DEBUG&lt;/td&gt;
&lt;td&gt;html=true&lt;/td&gt;
&lt;td&gt;# DEBUG as HTML.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;Hello, console!&lt;/td&gt;
&lt;td&gt;console=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Log also to the console.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;Null is \x00&lt;/td&gt;
&lt;td&gt;formatter=repr&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Log &lt;code&gt;'Null is \x00'&lt;/code&gt;.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Log%20Many" class="name"&gt;Log Many&lt;/a&gt; if you want to log multiple messages in one go, and &lt;a href="#Log%20To%20Console" class="name"&gt;Log To Console&lt;/a&gt; if you only want to write to the console.&lt;/p&gt;</doc>
<shortdoc>Logs the given message with the given level.</shortdoc>
</kw>
<kw name="Log Many" lineno="2931">
<arguments repr="*messages">
<arg kind="VAR_POSITIONAL" required="false" repr="*messages">
<name>messages</name>
</arg>
</arguments>
<doc>&lt;p&gt;Logs the given messages as separate entries using the INFO level.&lt;/p&gt;
&lt;p&gt;Supports also logging list and dictionary variable items individually.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Log Many&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log Many&lt;/td&gt;
&lt;td&gt;@{list}&lt;/td&gt;
&lt;td&gt;&amp;amp;{dict}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Log" class="name"&gt;Log&lt;/a&gt; and &lt;a href="#Log%20To%20Console" class="name"&gt;Log To Console&lt;/a&gt; keywords if you want to use alternative log levels, use HTML, or log to the console.&lt;/p&gt;</doc>
<shortdoc>Logs the given messages as separate entries using the INFO level.</shortdoc>
</kw>
<kw name="Log To Console" lineno="2959">
<arguments repr="message, stream=STDOUT, no_newline=False">
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
</arguments>
<doc>&lt;p&gt;Logs the given message to the console.&lt;/p&gt;
&lt;p&gt;By default uses the standard output stream. Using the standard error stream is possibly by giving the &lt;code&gt;stream&lt;/code&gt; argument value &lt;code&gt;STDERR&lt;/code&gt; (case-insensitive).&lt;/p&gt;
&lt;p&gt;By default appends a newline to the logged message. This can be disabled by giving the &lt;code&gt;no_newline&lt;/code&gt; argument a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;).&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Log To Console&lt;/td&gt;
&lt;td&gt;Hello, console!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log To Console&lt;/td&gt;
&lt;td&gt;Hello, stderr!&lt;/td&gt;
&lt;td&gt;STDERR&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log To Console&lt;/td&gt;
&lt;td&gt;Message starts here and is&lt;/td&gt;
&lt;td&gt;no_newline=true&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log To Console&lt;/td&gt;
&lt;td&gt;continued without newline.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword does not log the message to the normal log file. Use &lt;a href="#Log" class="name"&gt;Log&lt;/a&gt; keyword, possibly with argument &lt;code&gt;console&lt;/code&gt;, if that is desired.&lt;/p&gt;</doc>
<shortdoc>Logs the given message to the console.</shortdoc>
</kw>
<kw name="Log Variables" lineno="1545">
<arguments repr="level=INFO">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs all variables in the current scope with given log level.&lt;/p&gt;</doc>
<shortdoc>Logs all variables in the current scope with given log level.</shortdoc>
</kw>
<kw name="No Operation" lineno="2795">
<arguments repr="">
</arguments>
<doc>&lt;p&gt;Does absolutely nothing.&lt;/p&gt;</doc>
<shortdoc>Does absolutely nothing.</shortdoc>
</kw>
<kw name="Pass Execution" lineno="2721">
<arguments repr="message, *tags">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>&lt;p&gt;Skips rest of the current test, setup, or teardown with PASS status.&lt;/p&gt;
&lt;p&gt;This keyword can be used anywhere in the test data, but the place where used affects the behavior:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;When used in any setup or teardown (suite, test or keyword), passes that setup or teardown. Possible keyword teardowns of the started keywords are executed. Does not affect execution or statuses otherwise.&lt;/li&gt;
&lt;li&gt;When used in a test outside setup or teardown, passes that particular test case. Possible test and keyword teardowns are executed.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Possible continuable failures before this keyword is used, as well as failures in executed teardowns, will fail the execution.&lt;/p&gt;
&lt;p&gt;It is mandatory to give a message explaining why execution was passed. By default the message is considered plain text, but starting it with &lt;code&gt;*HTML*&lt;/code&gt; allows using HTML formatting.&lt;/p&gt;
&lt;p&gt;It is also possible to modify test tags passing tags after the message similarly as with &lt;a href="#Fail" class="name"&gt;Fail&lt;/a&gt; keyword. Tags starting with a hyphen (e.g. &lt;code&gt;-regression&lt;/code&gt;) are removed and others added. Tags are modified using &lt;a href="#Set%20Tags" class="name"&gt;Set Tags&lt;/a&gt; and &lt;a href="#Remove%20Tags" class="name"&gt;Remove Tags&lt;/a&gt; internally, and the semantics setting and removing them are the same as with these keywords.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Pass Execution&lt;/td&gt;
&lt;td&gt;All features available in this version tested.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Pass Execution&lt;/td&gt;
&lt;td&gt;Deprecated test.&lt;/td&gt;
&lt;td&gt;deprecated&lt;/td&gt;
&lt;td&gt;-regression&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword is typically wrapped to some other keyword, such as &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;, to pass based on a condition. The most common case can be handled also with &lt;a href="#Pass%20Execution%20If" class="name"&gt;Pass Execution If&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword If&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 0&lt;/td&gt;
&lt;td&gt;Pass Execution&lt;/td&gt;
&lt;td&gt;Negative values are cool.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Pass Execution If&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 0&lt;/td&gt;
&lt;td&gt;Negative values are cool.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Passing execution in the middle of a test, setup or teardown should be used with care. In the worst case it leads to tests that skip all the parts that could actually uncover problems in the tested application. In cases where execution cannot continue do to external factors, it is often safer to fail the test case and make it non-critical.&lt;/p&gt;</doc>
<shortdoc>Skips rest of the current test, setup, or teardown with PASS status.</shortdoc>
</kw>
<kw name="Pass Execution If" lineno="2773">
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
<doc>&lt;p&gt;Conditionally skips rest of the current test, setup, or teardown with PASS status.&lt;/p&gt;
&lt;p&gt;A wrapper for &lt;a href="#Pass%20Execution" class="name"&gt;Pass Execution&lt;/a&gt; to skip rest of the current test, setup or teardown based the given &lt;code&gt;condition&lt;/code&gt;. The condition is evaluated similarly as with &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; keyword, and &lt;code&gt;message&lt;/code&gt; and &lt;code&gt;*tags&lt;/code&gt; have same semantics as with &lt;a href="#Pass%20Execution" class="name"&gt;Pass Execution&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;FOR&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;IN&lt;/td&gt;
&lt;td&gt;@{VALUES}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Pass Execution If&lt;/td&gt;
&lt;td&gt;'${var}' == 'EXPECTED'&lt;/td&gt;
&lt;td&gt;Correct value was found&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;Do Something&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;END&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Conditionally skips rest of the current test, setup, or teardown with PASS status.</shortdoc>
</kw>
<kw name="Regexp Escape" lineno="3339">
<arguments repr="*patterns">
<arg kind="VAR_POSITIONAL" required="false" repr="*patterns">
<name>patterns</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns each argument string escaped for use as a regular expression.&lt;/p&gt;
&lt;p&gt;This keyword can be used to escape strings to be used with &lt;a href="#Should%20Match%20Regexp" class="name"&gt;Should Match Regexp&lt;/a&gt; and &lt;a href="#Should%20Not%20Match%20Regexp" class="name"&gt;Should Not Match Regexp&lt;/a&gt; keywords.&lt;/p&gt;
&lt;p&gt;Escaping is done with Python's &lt;code&gt;re.escape()&lt;/code&gt; function.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${escaped} =&lt;/td&gt;
&lt;td&gt;Regexp Escape&lt;/td&gt;
&lt;td&gt;${original}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{strings} =&lt;/td&gt;
&lt;td&gt;Regexp Escape&lt;/td&gt;
&lt;td&gt;@{strings}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns each argument string escaped for use as a regular expression.</shortdoc>
</kw>
<kw name="Reload Library" lineno="3011">
<arguments repr="name_or_instance">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name_or_instance">
<name>name_or_instance</name>
</arg>
</arguments>
<doc>&lt;p&gt;Rechecks what keywords the specified library provides.&lt;/p&gt;
&lt;p&gt;Can be called explicitly in the test data or by a library itself when keywords it provides have changed.&lt;/p&gt;
&lt;p&gt;The library can be specified by its name or as the active instance of the library. The latter is especially useful if the library itself calls this keyword as a method.&lt;/p&gt;</doc>
<shortdoc>Rechecks what keywords the specified library provides.</shortdoc>
</kw>
<kw name="Remove Tags" lineno="3497">
<arguments repr="*tags">
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>&lt;p&gt;Removes given &lt;code&gt;tags&lt;/code&gt; from the current test or all tests in a suite.&lt;/p&gt;
&lt;p&gt;Tags can be given exactly or using a pattern with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; acting as wildcards. See the &lt;a href="#Glob%20patterns" class="name"&gt;Glob patterns&lt;/a&gt; section for more information.&lt;/p&gt;
&lt;p&gt;This keyword can affect either one test case or all test cases in a test suite similarly as &lt;a href="#Set%20Tags" class="name"&gt;Set Tags&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The current tags are available as a built-in variable &lt;code&gt;@{TEST TAGS}&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Tags&lt;/td&gt;
&lt;td&gt;mytag&lt;/td&gt;
&lt;td&gt;something-*&lt;/td&gt;
&lt;td&gt;?ython&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Set%20Tags" class="name"&gt;Set Tags&lt;/a&gt; if you want to add certain tags and &lt;a href="#Fail" class="name"&gt;Fail&lt;/a&gt; if you want to fail the test case after setting and/or removing tags.&lt;/p&gt;</doc>
<shortdoc>Removes given ``tags`` from the current test or all tests in a suite.</shortdoc>
</kw>
<kw name="Repeat Keyword" lineno="2195">
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
<doc>&lt;p&gt;Executes the specified keyword multiple times.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;name&lt;/code&gt; and &lt;code&gt;args&lt;/code&gt; define the keyword that is executed similarly as with &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;. &lt;code&gt;repeat&lt;/code&gt; specifies how many times (as a count) or how long time (as a timeout) the keyword should be executed.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;repeat&lt;/code&gt; is given as count, it specifies how many times the keyword should be executed. &lt;code&gt;repeat&lt;/code&gt; can be given as an integer or as a string that can be converted to an integer. If it is a string, it can have postfix &lt;code&gt;times&lt;/code&gt; or &lt;code&gt;x&lt;/code&gt; (case and space insensitive) to make the expression more explicit.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;repeat&lt;/code&gt; is given as timeout, it must be in Robot Framework's time format (e.g. &lt;code&gt;1 minute&lt;/code&gt;, &lt;code&gt;2 min 3 s&lt;/code&gt;). Using a number alone (e.g. &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;1.5&lt;/code&gt;) does not work in this context.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;repeat&lt;/code&gt; is zero or negative, the keyword is not executed at all. This keyword fails immediately if any of the execution rounds fails.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Repeat Keyword&lt;/td&gt;
&lt;td&gt;5 times&lt;/td&gt;
&lt;td&gt;Go to Previous Page&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Repeat Keyword&lt;/td&gt;
&lt;td&gt;${var}&lt;/td&gt;
&lt;td&gt;Some Keyword&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Repeat Keyword&lt;/td&gt;
&lt;td&gt;2 minutes&lt;/td&gt;
&lt;td&gt;Some Keyword&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Executes the specified keyword multiple times.</shortdoc>
</kw>
<kw name="Replace Variables" lineno="1606">
<arguments repr="text">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="text">
<name>text</name>
</arg>
</arguments>
<doc>&lt;p&gt;Replaces variables in the given text with their current values.&lt;/p&gt;
&lt;p&gt;If the text contains undefined variables, this keyword fails. If the given &lt;code&gt;text&lt;/code&gt; contains only a single variable, its value is returned as-is and it can be any object. Otherwise this keyword always returns a string.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;p&gt;The file &lt;code&gt;template.txt&lt;/code&gt; contains &lt;code&gt;Hello ${NAME}!&lt;/code&gt; and variable &lt;code&gt;${NAME}&lt;/code&gt; has the value &lt;code&gt;Robot&lt;/code&gt;.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${template} =&lt;/td&gt;
&lt;td&gt;Get File&lt;/td&gt;
&lt;td&gt;${CURDIR}/template.txt&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${message} =&lt;/td&gt;
&lt;td&gt;Replace Variables&lt;/td&gt;
&lt;td&gt;${template}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${message}&lt;/td&gt;
&lt;td&gt;Hello Robot!&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Replaces variables in the given text with their current values.</shortdoc>
</kw>
<kw name="Return From Keyword" lineno="2599">
<arguments repr="*return_values">
<arg kind="VAR_POSITIONAL" required="false" repr="*return_values">
<name>return_values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns from the enclosing user keyword.&lt;/p&gt;
&lt;p&gt;This keyword can be used to return from a user keyword with PASS status without executing it fully. It is also possible to return values similarly as with the &lt;code&gt;[Return]&lt;/code&gt; setting. For more detailed information about working with the return values, see the User Guide.&lt;/p&gt;
&lt;p&gt;This keyword is typically wrapped to some other keyword, such as &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; or &lt;a href="#Run%20Keyword%20If%20Test%20Passed" class="name"&gt;Run Keyword If Test Passed&lt;/a&gt;, to return based on a condition:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword If&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 0&lt;/td&gt;
&lt;td&gt;Return From Keyword&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword If Test Passed&lt;/td&gt;
&lt;td&gt;Return From Keyword&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;It is possible to use this keyword to return from a keyword also inside a for loop. That, as well as returning values, is demonstrated by the &lt;span class="name"&gt;Find Index&lt;/span&gt; keyword in the following somewhat advanced example. Notice that it is often a good idea to move this kind of complicated logic into a test library.&lt;/p&gt;
&lt;pre&gt;
&lt;b&gt;***&lt;/b&gt; Variables &lt;b&gt;***&lt;/b&gt;
@{LIST} =    foo    baz

&lt;b&gt;***&lt;/b&gt; Test Cases &lt;b&gt;***&lt;/b&gt;
Example
    ${index} =    Find Index    baz    @{LIST}
    Should Be Equal    ${index}    ${1}
    ${index} =    Find Index    non existing    @{LIST}
    Should Be Equal    ${index}    ${-1}

&lt;b&gt;***&lt;/b&gt; Keywords &lt;b&gt;***&lt;/b&gt;
Find Index
   [Arguments]    ${element}    @{items}
   ${index} =    Set Variable    ${0}
   FOR    ${item}    IN    @{items}
       Run Keyword If    '${item}' == '${element}'    Return From Keyword    ${index}
       ${index} =    Set Variable    ${index + 1}
   END
   Return From Keyword    ${-1}    # Also [Return] would work here.
&lt;/pre&gt;
&lt;p&gt;The most common use case, returning based on an expression, can be accomplished directly with &lt;a href="#Return%20From%20Keyword%20If" class="name"&gt;Return From Keyword If&lt;/a&gt;. See also &lt;a href="#Run%20Keyword%20And%20Return" class="name"&gt;Run Keyword And Return&lt;/a&gt; and &lt;a href="#Run%20Keyword%20And%20Return%20If" class="name"&gt;Run Keyword And Return If&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns from the enclosing user keyword.</shortdoc>
</kw>
<kw name="Return From Keyword If" lineno="2651">
<arguments repr="condition, *return_values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*return_values">
<name>return_values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns from the enclosing user keyword if &lt;code&gt;condition&lt;/code&gt; is true.&lt;/p&gt;
&lt;p&gt;A wrapper for &lt;a href="#Return%20From%20Keyword" class="name"&gt;Return From Keyword&lt;/a&gt; to return based on the given condition. The condition is evaluated using the same semantics as with &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;Given the same example as in &lt;a href="#Return%20From%20Keyword" class="name"&gt;Return From Keyword&lt;/a&gt;, we can rewrite the &lt;span class="name"&gt;Find Index&lt;/span&gt; keyword as follows:&lt;/p&gt;
&lt;pre&gt;
&lt;b&gt;***&lt;/b&gt; Keywords &lt;b&gt;***&lt;/b&gt;
Find Index
   [Arguments]    ${element}    @{items}
   ${index} =    Set Variable    ${0}
   FOR    ${item}    IN    @{items}
       Return From Keyword If    '${item}' == '${element}'    ${index}
       ${index} =    Set Variable    ${index + 1}
   END
   Return From Keyword    ${-1}    # Also [Return] would work here.
&lt;/pre&gt;
&lt;p&gt;See also &lt;a href="#Run%20Keyword%20And%20Return" class="name"&gt;Run Keyword And Return&lt;/a&gt; and &lt;a href="#Run%20Keyword%20And%20Return%20If" class="name"&gt;Run Keyword And Return If&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns from the enclosing user keyword if ``condition`` is true.</shortdoc>
</kw>
<kw name="Run Keyword" lineno="1857">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Executes the given keyword with the given arguments.&lt;/p&gt;
&lt;p&gt;Because the name of the keyword to execute is given as an argument, it can be a variable and thus set dynamically, e.g. from a return value of another keyword or from the command line.&lt;/p&gt;</doc>
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
<doc>&lt;p&gt;Runs the keyword and continues execution even if a failure occurs.&lt;/p&gt;
&lt;p&gt;The keyword name and arguments work as with &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword And Continue On Failure&lt;/td&gt;
&lt;td&gt;Fail&lt;/td&gt;
&lt;td&gt;This is a stupid example&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log&lt;/td&gt;
&lt;td&gt;This keyword is executed&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The execution is not continued if the failure is caused by invalid syntax, timeout, or fatal exception.&lt;/p&gt;</doc>
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
<doc>&lt;p&gt;Runs the keyword and checks that the expected error occurred.&lt;/p&gt;
&lt;p&gt;The keyword to execute and its arguments are specified using &lt;code&gt;name&lt;/code&gt; and &lt;code&gt;*args&lt;/code&gt; exactly like with &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The expected error must be given in the same format as in Robot Framework reports. By default it is interpreted as a glob pattern with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; as wildcards, but that can be changed by using various prefixes explained in the table below. Prefixes are case-sensitive and they must be separated from the actual message with a colon and an optional space like &lt;code&gt;PREFIX: Message&lt;/code&gt; or &lt;code&gt;PREFIX:Message&lt;/code&gt;.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Prefix&lt;/th&gt;
&lt;th&gt;Explanation&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;EQUALS&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Exact match. Especially useful if the error contains glob wildcards.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;STARTS&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Error must start with the specified error.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;REGEXP&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Regular expression match.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;code&gt;GLOB&lt;/code&gt;&lt;/td&gt;
&lt;td&gt;Same as the default behavior.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See the &lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt; section for more information about glob patterns and regular expressions.&lt;/p&gt;
&lt;p&gt;If the expected error occurs, the error message is returned and it can be further processed or tested if needed. If there is no error, or the error does not match the expected error, this keyword fails.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword And Expect Error&lt;/td&gt;
&lt;td&gt;My error&lt;/td&gt;
&lt;td&gt;Keyword&lt;/td&gt;
&lt;td&gt;arg&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword And Expect Error&lt;/td&gt;
&lt;td&gt;ValueError: *&lt;/td&gt;
&lt;td&gt;Some Keyword&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword And Expect Error&lt;/td&gt;
&lt;td&gt;STARTS: ValueError:&lt;/td&gt;
&lt;td&gt;Some Keyword&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Run Keyword And Expect Error&lt;/td&gt;
&lt;td&gt;EQUALS:No match for '//input[@type="text"]'&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;Find Element&lt;/td&gt;
&lt;td&gt;//input[@type="text"]&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${msg} =&lt;/td&gt;
&lt;td&gt;Run Keyword And Expect Error&lt;/td&gt;
&lt;td&gt;*&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;Keyword&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Log To Console&lt;/td&gt;
&lt;td&gt;${msg}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Errors caused by invalid syntax, timeouts, or fatal exceptions are not caught by this keyword.&lt;/p&gt;</doc>
<shortdoc>Runs the keyword and checks that the expected error occurred.</shortdoc>
</kw>
<kw name="Run Keyword And Ignore Error" lineno="2046">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given keyword with the given arguments and ignores possible error.&lt;/p&gt;
&lt;p&gt;This keyword returns two values, so that the first is either string &lt;code&gt;PASS&lt;/code&gt; or &lt;code&gt;FAIL&lt;/code&gt;, depending on the status of the executed keyword. The second value is either the return value of the keyword or the received error message. See &lt;a href="#Run%20Keyword%20And%20Return%20Status" class="name"&gt;Run Keyword And Return Status&lt;/a&gt; If you are only interested in the execution status.&lt;/p&gt;
&lt;p&gt;The keyword name and arguments work as in &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;. See &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; for a usage example.&lt;/p&gt;
&lt;p&gt;Errors caused by invalid syntax, timeouts, or fatal exceptions are not caught by this keyword. Otherwise this keyword itself never fails.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments and ignores possible error.</shortdoc>
</kw>
<kw name="Run Keyword And Return" lineno="2677">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the specified keyword and returns from the enclosing user keyword.&lt;/p&gt;
&lt;p&gt;The keyword to execute is defined with &lt;code&gt;name&lt;/code&gt; and &lt;code&gt;*args&lt;/code&gt; exactly like with &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;. After running the keyword, returns from the enclosing user keyword and passes possible return value from the executed keyword further. Returning from a keyword has exactly same semantics as with &lt;a href="#Return%20From%20Keyword" class="name"&gt;Return From Keyword&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20And%20Return" class="name"&gt;Run Keyword And Return&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;My Keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Above is equivalent to:&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;My Keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Return%20From%20Keyword" class="name"&gt;Return From Keyword&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${result}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Run%20Keyword%20And%20Return%20If" class="name"&gt;Run Keyword And Return If&lt;/a&gt; if you want to run keyword and return based on a condition.&lt;/p&gt;</doc>
<shortdoc>Runs the specified keyword and returns from the enclosing user keyword.</shortdoc>
</kw>
<kw name="Run Keyword And Return If" lineno="2703">
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
<doc>&lt;p&gt;Runs the specified keyword and returns from the enclosing user keyword.&lt;/p&gt;
&lt;p&gt;A wrapper for &lt;a href="#Run%20Keyword%20And%20Return" class="name"&gt;Run Keyword And Return&lt;/a&gt; to run and return based on the given &lt;code&gt;condition&lt;/code&gt;. The condition is evaluated using the same semantics as with &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20And%20Return%20If" class="name"&gt;Run Keyword And Return If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 0&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;My Keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;# Above is equivalent to:&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 0&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20And%20Return" class="name"&gt;Run Keyword And Return&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;My Keyword &lt;/span&gt;&lt;/td&gt;
&lt;td&gt;arg1&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Return%20From%20Keyword%20If" class="name"&gt;Return From Keyword If&lt;/a&gt; if you want to return a certain value based on a condition.&lt;/p&gt;</doc>
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
<doc>&lt;p&gt;Runs the given keyword with given arguments and returns the status as a Boolean value.&lt;/p&gt;
&lt;p&gt;This keyword returns Boolean &lt;code&gt;True&lt;/code&gt; if the keyword that is executed succeeds and &lt;code&gt;False&lt;/code&gt; if it fails. This is useful, for example, in combination with &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;. If you are interested in the error message or return value, use &lt;a href="#Run%20Keyword%20And%20Ignore%20Error" class="name"&gt;Run Keyword And Ignore Error&lt;/a&gt; instead.&lt;/p&gt;
&lt;p&gt;The keyword name and arguments work as in &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${passed} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20And%20Return%20Status" class="name"&gt;Run Keyword And Return Status&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;Keyword&lt;/td&gt;
&lt;td&gt;args&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${passed}&lt;/td&gt;
&lt;td&gt;Another keyword&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Errors caused by invalid syntax, timeouts, or fatal exceptions are not caught by this keyword. Otherwise this keyword itself never fails.&lt;/p&gt;</doc>
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
<doc>&lt;p&gt;Runs the specified keyword logs a warning if the keyword fails.&lt;/p&gt;
&lt;p&gt;This keyword is similar to &lt;a href="#Run%20Keyword%20And%20Ignore%20Error" class="name"&gt;Run Keyword And Ignore Error&lt;/a&gt; but if the executed keyword fails, the error message is logged as a warning to make it more visible. Returns status and possible return value or error message exactly like &lt;a href="#Run%20Keyword%20And%20Ignore%20Error" class="name"&gt;Run Keyword And Ignore Error&lt;/a&gt; does.&lt;/p&gt;
&lt;p&gt;Errors caused by invalid syntax, timeouts, or fatal exceptions are not caught by this keyword. Otherwise this keyword itself never fails.&lt;/p&gt;
&lt;p&gt;New in Robot Framework 4.0.&lt;/p&gt;</doc>
<shortdoc>Runs the specified keyword logs a warning if the keyword fails.</shortdoc>
</kw>
<kw name="Run Keyword If" lineno="1940">
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
<doc>&lt;p&gt;Runs the given keyword with the given arguments, if &lt;code&gt;condition&lt;/code&gt; is true.&lt;/p&gt;
&lt;p&gt;&lt;b&gt;NOTE:&lt;/b&gt; Robot Framework 4.0 introduced built-in IF/ELSE support and using that is generally recommended over using this keyword.&lt;/p&gt;
&lt;p&gt;The given &lt;code&gt;condition&lt;/code&gt; is evaluated in Python as explained in &lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt;, and &lt;code&gt;name&lt;/code&gt; and &lt;code&gt;*args&lt;/code&gt; have same semantics as with &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Example, a simple if/else construct:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${status}&lt;/td&gt;
&lt;td&gt;${value} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20And%20Ignore%20Error" class="name"&gt;Run Keyword And Ignore Error&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;My Keyword&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;'${status}' == 'PASS'&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Some Action&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;arg&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20Unless" class="name"&gt;Run Keyword Unless&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;'${status}' == 'PASS'&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Another Action&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;In this example, only either &lt;span class="name"&gt;Some Action&lt;/span&gt; or &lt;span class="name"&gt;Another Action&lt;/span&gt; is executed, based on the status of &lt;span class="name"&gt;My Keyword&lt;/span&gt;. Instead of &lt;a href="#Run%20Keyword%20And%20Ignore%20Error" class="name"&gt;Run Keyword And Ignore Error&lt;/a&gt; you can also use &lt;a href="#Run%20Keyword%20And%20Return%20Status" class="name"&gt;Run Keyword And Return Status&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Variables used like &lt;code&gt;${variable}&lt;/code&gt;, as in the examples above, are replaced in the expression before evaluation. Variables are also available in the evaluation namespace and can be accessed using special syntax &lt;code&gt;$variable&lt;/code&gt; as explained in the &lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt; section.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;$result is None or $result == 'FAIL'&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Keyword&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword supports also optional ELSE and ELSE IF branches. Both of them are defined in &lt;code&gt;*args&lt;/code&gt; and must use exactly format &lt;code&gt;ELSE&lt;/code&gt; or &lt;code&gt;ELSE IF&lt;/code&gt;, respectively. ELSE branches must contain first the name of the keyword to execute and then its possible arguments. ELSE IF branches must first contain a condition, like the first argument to this keyword, and then the keyword to execute and its possible arguments. It is possible to have ELSE branch after ELSE IF and to have multiple ELSE IF branches. Nested &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; usage is not supported when using ELSE and/or ELSE IF branches.&lt;/p&gt;
&lt;p&gt;Given previous example, if/else construct can also be created like this:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${status}&lt;/td&gt;
&lt;td&gt;${value} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20And%20Ignore%20Error" class="name"&gt;Run Keyword And Ignore Error&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;My Keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;'${status}' == 'PASS'&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Some Action&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;arg&lt;/td&gt;
&lt;td&gt;ELSE&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Another Action&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The return value of this keyword is the return value of the actually executed keyword or Python &lt;code&gt;None&lt;/code&gt; if no keyword was executed (i.e. if &lt;code&gt;condition&lt;/code&gt; was false). Hence, it is recommended to use ELSE and/or ELSE IF branches to conditionally assign return values from keyword to variables (see &lt;a href="#Set%20Variable%20If" class="name"&gt;Set Variable If&lt;/a&gt; if you need to set fixed values conditionally). This is illustrated by the example below:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${var1} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${rc} == 0&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Some keyword returning a value&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;ELSE IF&lt;/td&gt;
&lt;td&gt;0 &amp;lt; ${rc} &amp;lt; 42&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Another keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;ELSE IF&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 0&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Another keyword with args&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${rc}&lt;/td&gt;
&lt;td&gt;arg2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;ELSE&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Final keyword to handle abnormal cases&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${rc}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${var2} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${condition}&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Some keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;In this example, ${var2} will be set to &lt;code&gt;None&lt;/code&gt; if ${condition} is false.&lt;/p&gt;
&lt;p&gt;Notice that &lt;code&gt;ELSE&lt;/code&gt; and &lt;code&gt;ELSE IF&lt;/code&gt; control words must be used explicitly and thus cannot come from variables. If you need to use literal &lt;code&gt;ELSE&lt;/code&gt; and &lt;code&gt;ELSE IF&lt;/code&gt; strings as arguments, you can escape them with a backslash like &lt;code&gt;\ELSE&lt;/code&gt; and &lt;code&gt;\ELSE IF&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Python's &lt;a href="http://docs.python.org/library/os.html"&gt;os&lt;/a&gt; and &lt;a href="http://docs.python.org/library/sys.html"&gt;sys&lt;/a&gt; modules are automatically imported when evaluating the &lt;code&gt;condition&lt;/code&gt;. Attributes they contain can thus be used in the condition:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;os.sep == '/'&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Unix Keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;ELSE IF&lt;/td&gt;
&lt;td&gt;sys.platform.startswith('java')&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Jython Keyword&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;ELSE&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Windows Keyword&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments, if ``condition`` is true.</shortdoc>
</kw>
<kw name="Run Keyword If All Critical Tests Passed" lineno="2463">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;&lt;b&gt;DEPRECATED.&lt;/b&gt; Use &lt;span class="name"&gt;BuiltIn.Run Keyword If All Tests Passed&lt;/span&gt; instead.&lt;/p&gt;</doc>
<shortdoc>*DEPRECATED.* Use `BuiltIn.Run Keyword If All Tests Passed` instead.</shortdoc>
</kw>
<kw name="Run Keyword If All Tests Passed" lineno="2473">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given keyword with the given arguments, if all tests passed.&lt;/p&gt;
&lt;p&gt;This keyword can only be used in a suite teardown. Trying to use it anywhere else results in an error.&lt;/p&gt;
&lt;p&gt;Otherwise, this keyword works exactly like &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;, see its documentation for more details.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments, if all tests passed.</shortdoc>
</kw>
<kw name="Run Keyword If Any Critical Tests Failed" lineno="2468">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;&lt;b&gt;DEPRECATED.&lt;/b&gt; Use &lt;span class="name"&gt;BuiltIn.Run Keyword If Any Tests Failed&lt;/span&gt; instead.&lt;/p&gt;</doc>
<shortdoc>*DEPRECATED.* Use `BuiltIn.Run Keyword If Any Tests Failed` instead.</shortdoc>
</kw>
<kw name="Run Keyword If Any Tests Failed" lineno="2487">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given keyword with the given arguments, if one or more tests failed.&lt;/p&gt;
&lt;p&gt;This keyword can only be used in a suite teardown. Trying to use it anywhere else results in an error.&lt;/p&gt;
&lt;p&gt;Otherwise, this keyword works exactly like &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;, see its documentation for more details.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments, if one or more tests failed.</shortdoc>
</kw>
<kw name="Run Keyword If Test Failed" lineno="2414">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given keyword with the given arguments, if the test failed.&lt;/p&gt;
&lt;p&gt;This keyword can only be used in a test teardown. Trying to use it anywhere else results in an error.&lt;/p&gt;
&lt;p&gt;Otherwise, this keyword works exactly like &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;, see its documentation for more details.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments, if the test failed.</shortdoc>
</kw>
<kw name="Run Keyword If Test Passed" lineno="2428">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given keyword with the given arguments, if the test passed.&lt;/p&gt;
&lt;p&gt;This keyword can only be used in a test teardown. Trying to use it anywhere else results in an error.&lt;/p&gt;
&lt;p&gt;Otherwise, this keyword works exactly like &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;, see its documentation for more details.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments, if the test passed.</shortdoc>
</kw>
<kw name="Run Keyword If Timeout Occurred" lineno="2442">
<arguments repr="name, *args">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*args">
<name>args</name>
</arg>
</arguments>
<doc>&lt;p&gt;Runs the given keyword if either a test or a keyword timeout has occurred.&lt;/p&gt;
&lt;p&gt;This keyword can only be used in a test teardown. Trying to use it anywhere else results in an error.&lt;/p&gt;
&lt;p&gt;Otherwise, this keyword works exactly like &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;, see its documentation for more details.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword if either a test or a keyword timeout has occurred.</shortdoc>
</kw>
<kw name="Run Keyword Unless" lineno="2035">
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
<doc>&lt;p&gt;Runs the given keyword with the given arguments if &lt;code&gt;condition&lt;/code&gt; is false.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; for more information and an example. Notice that this keyword does not support &lt;code&gt;ELSE&lt;/code&gt; or &lt;code&gt;ELSE IF&lt;/code&gt; branches like &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt; does, though.&lt;/p&gt;</doc>
<shortdoc>Runs the given keyword with the given arguments if ``condition`` is false.</shortdoc>
</kw>
<kw name="Run Keywords" lineno="1870">
<arguments repr="*keywords">
<arg kind="VAR_POSITIONAL" required="false" repr="*keywords">
<name>keywords</name>
</arg>
</arguments>
<doc>&lt;p&gt;Executes all the given keywords in a sequence.&lt;/p&gt;
&lt;p&gt;This keyword is mainly useful in setups and teardowns when they need to take care of multiple actions and creating a new higher level user keyword would be an overkill.&lt;/p&gt;
&lt;p&gt;By default all arguments are expected to be keywords to be executed.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keywords" class="name"&gt;Run Keywords&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Initialize database&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Start servers&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Clear logs&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keywords" class="name"&gt;Run Keywords&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${KW 1}&lt;/td&gt;
&lt;td&gt;${KW 2}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keywords" class="name"&gt;Run Keywords&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;@{KEYWORDS}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Keywords can also be run with arguments using upper case &lt;code&gt;AND&lt;/code&gt; as a separator between keywords. The keywords are executed so that the first argument is the first keyword and proceeding arguments until the first &lt;code&gt;AND&lt;/code&gt; are arguments to it. First argument after the first &lt;code&gt;AND&lt;/code&gt; is the second keyword and proceeding arguments until the next &lt;code&gt;AND&lt;/code&gt; are its arguments. And so on.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keywords" class="name"&gt;Run Keywords&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Initialize database&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;db1&lt;/td&gt;
&lt;td&gt;AND&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Start servers&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;server1&lt;/td&gt;
&lt;td&gt;server2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keywords" class="name"&gt;Run Keywords&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Initialize database&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${DB NAME}&lt;/td&gt;
&lt;td&gt;AND&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Start servers&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;@{SERVERS}&lt;/td&gt;
&lt;td&gt;AND&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;Clear logs&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Run%20Keywords" class="name"&gt;Run Keywords&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${KW}&lt;/td&gt;
&lt;td&gt;AND&lt;/td&gt;
&lt;td&gt;@{KW WITH ARGS}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Notice that the &lt;code&gt;AND&lt;/code&gt; control argument must be used explicitly and cannot itself come from a variable. If you need to use literal &lt;code&gt;AND&lt;/code&gt; string as argument, you can either use variables or escape it with a backslash like &lt;code&gt;\AND&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Executes all the given keywords in a sequence.</shortdoc>
</kw>
<kw name="Set Global Variable" lineno="1777">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Makes a variable available globally in all tests and suites.&lt;/p&gt;
&lt;p&gt;Variables set with this keyword are globally available in all subsequent test suites, test cases and user keywords. Also variables in variable tables are overridden. Variables assigned locally based on keyword return values or by using &lt;a href="#Set%20Test%20Variable" class="name"&gt;Set Test Variable&lt;/a&gt; and &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt; override these variables in that scope, but the global value is not changed in those cases.&lt;/p&gt;
&lt;p&gt;In practice setting variables with this keyword has the same effect as using command line options &lt;code&gt;--variable&lt;/code&gt; and &lt;code&gt;--variablefile&lt;/code&gt;. Because this keyword can change variables everywhere, it should be used with care.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt; for more information and examples.&lt;/p&gt;</doc>
<shortdoc>Makes a variable available globally in all tests and suites.</shortdoc>
</kw>
<kw name="Set Library Search Order" lineno="3110">
<arguments repr="*search_order">
<arg kind="VAR_POSITIONAL" required="false" repr="*search_order">
<name>search_order</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the resolution order to use when a name matches multiple keywords.&lt;/p&gt;
&lt;p&gt;The library search order is used to resolve conflicts when a keyword name in the test data matches multiple keywords. The first library (or resource, see below) containing the keyword is selected and that keyword implementation used. If the keyword is not found from any library (or resource), test executing fails the same way as when the search order is not set.&lt;/p&gt;
&lt;p&gt;When this keyword is used, there is no need to use the long &lt;code&gt;LibraryName.Keyword Name&lt;/code&gt; notation.  For example, instead of having&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;MyLibrary.Keyword&lt;/td&gt;
&lt;td&gt;arg&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;MyLibrary.Another Keyword&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;MyLibrary.Keyword&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;you can have&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Library Search Order&lt;/td&gt;
&lt;td&gt;MyLibrary&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Keyword&lt;/td&gt;
&lt;td&gt;arg&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Another Keyword&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Keyword&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword can be used also to set the order of keywords in different resource files. In this case resource names must be given without paths or extensions like:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Library Search Order&lt;/td&gt;
&lt;td&gt;resource&lt;/td&gt;
&lt;td&gt;another_resource&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;b&gt;NOTE:&lt;/b&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;The search order is valid only in the suite where this keywords is used.&lt;/li&gt;
&lt;li&gt;Keywords in resources always have higher priority than keywords in libraries regardless the search order.&lt;/li&gt;
&lt;li&gt;The old order is returned and can be used to reset the search order later.&lt;/li&gt;
&lt;li&gt;Library and resource names in the search order are both case and space insensitive.&lt;/li&gt;
&lt;/ul&gt;</doc>
<shortdoc>Sets the resolution order to use when a name matches multiple keywords.</shortdoc>
</kw>
<kw name="Set Local Variable" lineno="1653">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Makes a variable available everywhere within the local scope.&lt;/p&gt;
&lt;p&gt;Variables set with this keyword are available within the local scope of the currently executed test case or in the local scope of the keyword in which they are defined. For example, if you set a variable in a user keyword, it is available only in that keyword. Other test cases or keywords will not see variables set with this keyword.&lt;/p&gt;
&lt;p&gt;This keyword is equivalent to a normal variable assignment based on a keyword return value.&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{list} =&lt;/td&gt;
&lt;td&gt;Create List&lt;/td&gt;
&lt;td&gt;item1&lt;/td&gt;
&lt;td&gt;item2&lt;/td&gt;
&lt;td&gt;item3&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;is equivalent with&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Local Variable&lt;/td&gt;
&lt;td&gt;@{list}&lt;/td&gt;
&lt;td&gt;item1&lt;/td&gt;
&lt;td&gt;item2&lt;/td&gt;
&lt;td&gt;item3&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword will provide the option of setting local variables inside keywords like &lt;a href="#Run%20Keyword%20If" class="name"&gt;Run Keyword If&lt;/a&gt;, &lt;a href="#Run%20Keyword%20And%20Return%20If" class="name"&gt;Run Keyword And Return If&lt;/a&gt;, &lt;a href="#Run%20Keyword%20Unless" class="name"&gt;Run Keyword Unless&lt;/a&gt; which until now was not possible by using &lt;a href="#Set%20Variable" class="name"&gt;Set Variable&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;It will also be possible to use this keyword from external libraries that want to set local variables.&lt;/p&gt;
&lt;p&gt;New in Robot Framework 3.2.&lt;/p&gt;</doc>
<shortdoc>Makes a variable available everywhere within the local scope.</shortdoc>
</kw>
<kw name="Set Log Level" lineno="2993">
<arguments repr="level">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="level">
<name>level</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the log threshold to the specified level and returns the old level.&lt;/p&gt;
&lt;p&gt;Messages below the level will not logged. The default logging level is INFO, but it can be overridden with the command line option &lt;code&gt;--loglevel&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The available levels: TRACE, DEBUG, INFO (default), WARN, ERROR and NONE (no logging).&lt;/p&gt;</doc>
<shortdoc>Sets the log threshold to the specified level and returns the old level.</shortdoc>
</kw>
<kw name="Set Suite Documentation" lineno="3429">
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
<doc>&lt;p&gt;Sets documentation for the current test suite.&lt;/p&gt;
&lt;p&gt;By default the possible existing documentation is overwritten, but this can be changed using the optional &lt;code&gt;append&lt;/code&gt; argument similarly as with &lt;a href="#Set%20Test%20Message" class="name"&gt;Set Test Message&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;This keyword sets the documentation of the current suite by default. If the optional &lt;code&gt;top&lt;/code&gt; argument is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the documentation of the top level suite is altered instead.&lt;/p&gt;
&lt;p&gt;The documentation of the current suite is available as a built-in variable &lt;code&gt;${SUITE DOCUMENTATION}&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Sets documentation for the current test suite.</shortdoc>
</kw>
<kw name="Set Suite Metadata" lineno="3449">
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
<doc>&lt;p&gt;Sets metadata for the current test suite.&lt;/p&gt;
&lt;p&gt;By default possible existing metadata values are overwritten, but this can be changed using the optional &lt;code&gt;append&lt;/code&gt; argument similarly as with &lt;a href="#Set%20Test%20Message" class="name"&gt;Set Test Message&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;This keyword sets the metadata of the current suite by default. If the optional &lt;code&gt;top&lt;/code&gt; argument is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the metadata of the top level suite is altered instead.&lt;/p&gt;
&lt;p&gt;The metadata of the current suite is available as a built-in variable &lt;code&gt;${SUITE METADATA}&lt;/code&gt; in a Python dictionary. Notice that modifying this variable directly has no effect on the actual metadata the suite has.&lt;/p&gt;</doc>
<shortdoc>Sets metadata for the current test suite.</shortdoc>
</kw>
<kw name="Set Suite Variable" lineno="1713">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Makes a variable available everywhere within the scope of the current suite.&lt;/p&gt;
&lt;p&gt;Variables set with this keyword are available everywhere within the scope of the currently executed test suite. Setting variables with this keyword thus has the same effect as creating them using the Variable table in the test data file or importing them from variable files.&lt;/p&gt;
&lt;p&gt;Possible child test suites do not see variables set with this keyword by default, but that can be controlled by using &lt;code&gt;children=&amp;lt;option&amp;gt;&lt;/code&gt; as the last argument. If the specified &lt;code&gt;&amp;lt;option&amp;gt;&lt;/code&gt; given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the variable is set also to the child suites. Parent and sibling suites will never see variables set with this keyword.&lt;/p&gt;
&lt;p&gt;The name of the variable can be given either as a normal variable name (e.g. &lt;code&gt;${NAME}&lt;/code&gt;) or in escaped format as &lt;code&gt;\${NAME}&lt;/code&gt; or &lt;code&gt;$NAME&lt;/code&gt;. Variable value can be given using the same syntax as when variables are created in the Variable table.&lt;/p&gt;
&lt;p&gt;If a variable already exists within the new scope, its value will be overwritten. Otherwise a new variable is created. If a variable already exists within the current scope, the value can be left empty and the variable within the new scope gets the value within the current scope.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;${SCALAR}&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;${SCALAR}&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;children=true&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;@{LIST}&lt;/td&gt;
&lt;td&gt;First item&lt;/td&gt;
&lt;td&gt;Second item&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;&amp;amp;{DICT}&lt;/td&gt;
&lt;td&gt;key=value&lt;/td&gt;
&lt;td&gt;foo=bar&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ID} =&lt;/td&gt;
&lt;td&gt;Get ID&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;${ID}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;To override an existing value with an empty value, use built-in variables &lt;code&gt;${EMPTY}&lt;/code&gt;, &lt;code&gt;@{EMPTY}&lt;/code&gt; or &lt;code&gt;&amp;amp;{EMPTY}&lt;/code&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;${SCALAR}&lt;/td&gt;
&lt;td&gt;${EMPTY}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;@{LIST}&lt;/td&gt;
&lt;td&gt;@{EMPTY}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;&amp;amp;{DICT}&lt;/td&gt;
&lt;td&gt;&amp;amp;{EMPTY}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;b&gt;NOTE:&lt;/b&gt; If the variable has value which itself is a variable (escaped or not), you must always use the escaped format to set the variable:&lt;/p&gt;
&lt;p&gt;Example:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${NAME} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;\${var}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;${NAME}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;# Sets variable ${var}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Suite Variable&lt;/td&gt;
&lt;td&gt;\${NAME}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;# Sets variable ${NAME}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This limitation applies also to &lt;a href="#Set%20Test%20Variable" class="name"&gt;Set Test Variable&lt;/a&gt;, &lt;a href="#Set%20Global%20Variable" class="name"&gt;Set Global Variable&lt;/a&gt;, &lt;a href="#Variable%20Should%20Exist" class="name"&gt;Variable Should Exist&lt;/a&gt;, &lt;a href="#Variable%20Should%20Not%20Exist" class="name"&gt;Variable Should Not Exist&lt;/a&gt; and &lt;a href="#Get%20Variable%20Value" class="name"&gt;Get Variable Value&lt;/a&gt; keywords.&lt;/p&gt;</doc>
<shortdoc>Makes a variable available everywhere within the scope of the current suite.</shortdoc>
</kw>
<kw name="Set Tags" lineno="3472">
<arguments repr="*tags">
<arg kind="VAR_POSITIONAL" required="false" repr="*tags">
<name>tags</name>
</arg>
</arguments>
<doc>&lt;p&gt;Adds given &lt;code&gt;tags&lt;/code&gt; for the current test or all tests in a suite.&lt;/p&gt;
&lt;p&gt;When this keyword is used inside a test case, that test gets the specified tags and other tests are not affected.&lt;/p&gt;
&lt;p&gt;If this keyword is used in a suite setup, all test cases in that suite, recursively, gets the given tags. It is a failure to use this keyword in a suite teardown.&lt;/p&gt;
&lt;p&gt;The current tags are available as a built-in variable &lt;code&gt;@{TEST TAGS}&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Remove%20Tags" class="name"&gt;Remove Tags&lt;/a&gt; if you want to remove certain tags and &lt;a href="#Fail" class="name"&gt;Fail&lt;/a&gt; if you want to fail the test case after setting and/or removing tags.&lt;/p&gt;</doc>
<shortdoc>Adds given ``tags`` for the current test or all tests in a suite.</shortdoc>
</kw>
<kw name="Set Task Variable" lineno="1704">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Makes a variable available everywhere within the scope of the current task.&lt;/p&gt;
&lt;p&gt;This is an alias for &lt;a href="#Set%20Test%20Variable" class="name"&gt;Set Test Variable&lt;/a&gt; that is more applicable when creating tasks, not tests.&lt;/p&gt;</doc>
<shortdoc>Makes a variable available everywhere within the scope of the current task.</shortdoc>
</kw>
<kw name="Set Test Documentation" lineno="3410">
<arguments repr="doc, append=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="doc">
<name>doc</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="append=False">
<name>append</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets documentation for the current test case.&lt;/p&gt;
&lt;p&gt;By default the possible existing documentation is overwritten, but this can be changed using the optional &lt;code&gt;append&lt;/code&gt; argument similarly as with &lt;a href="#Set%20Test%20Message" class="name"&gt;Set Test Message&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The current test documentation is available as a built-in variable &lt;code&gt;${TEST DOCUMENTATION}&lt;/code&gt;. This keyword can not be used in suite setup or suite teardown.&lt;/p&gt;</doc>
<shortdoc>Sets documentation for the current test case.</shortdoc>
</kw>
<kw name="Set Test Message" lineno="3357">
<arguments repr="message, append=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="message">
<name>message</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="append=False">
<name>append</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets message for the current test case.&lt;/p&gt;
&lt;p&gt;If the optional &lt;code&gt;append&lt;/code&gt; argument is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the given &lt;code&gt;message&lt;/code&gt; is added after the possible earlier message by joining the messages with a space.&lt;/p&gt;
&lt;p&gt;In test teardown this keyword can alter the possible failure message, but otherwise failures override messages set by this keyword. Notice that in teardown the message is available as a built-in variable &lt;code&gt;${TEST MESSAGE}&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;It is possible to use HTML format in the message by starting the message with &lt;code&gt;*HTML*&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Test Message&lt;/td&gt;
&lt;td&gt;My message&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Test Message&lt;/td&gt;
&lt;td&gt;is continued.&lt;/td&gt;
&lt;td&gt;append=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${TEST MESSAGE}&lt;/td&gt;
&lt;td&gt;My message is continued.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Test Message&lt;/td&gt;
&lt;td&gt;&lt;span class="name"&gt;*&lt;/span&gt;HTML&lt;span class="name"&gt;*&lt;/span&gt; &amp;lt;b&amp;gt;Hello!&amp;lt;/b&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword can not be used in suite setup or suite teardown.&lt;/p&gt;</doc>
<shortdoc>Sets message for the current test case.</shortdoc>
</kw>
<kw name="Set Test Variable" lineno="1687">
<arguments repr="name, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Makes a variable available everywhere within the scope of the current test.&lt;/p&gt;
&lt;p&gt;Variables set with this keyword are available everywhere within the scope of the currently executed test case. For example, if you set a variable in a user keyword, it is available both in the test case level and also in all other user keywords used in the current test. Other test cases will not see variables set with this keyword.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt; for more information and examples.&lt;/p&gt;</doc>
<shortdoc>Makes a variable available everywhere within the scope of the current test.</shortdoc>
</kw>
<kw name="Set Variable" lineno="1625">
<arguments repr="*values">
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the given values which can then be assigned to a variables.&lt;/p&gt;
&lt;p&gt;This keyword is mainly used for setting scalar variables. Additionally it can be used for converting a scalar variable containing a list to a list variable or to multiple scalar variables. It is recommended to use &lt;a href="#Create%20List" class="name"&gt;Create List&lt;/a&gt; when creating new lists.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${hi} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;Hello, world!&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${hi2} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;I said: ${hi}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${var1}&lt;/td&gt;
&lt;td&gt;${var2} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;Hello&lt;/td&gt;
&lt;td&gt;world&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{list} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;${list with some items}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${item1}&lt;/td&gt;
&lt;td&gt;${item2} =&lt;/td&gt;
&lt;td&gt;Set Variable&lt;/td&gt;
&lt;td&gt;${list with 2 items}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Variables created with this keyword are available only in the scope where they are created. See &lt;a href="#Set%20Global%20Variable" class="name"&gt;Set Global Variable&lt;/a&gt;, &lt;a href="#Set%20Test%20Variable" class="name"&gt;Set Test Variable&lt;/a&gt; and &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt; for information on how to set variables so that they are available also in a larger scope.&lt;/p&gt;</doc>
<shortdoc>Returns the given values which can then be assigned to a variables.</shortdoc>
</kw>
<kw name="Set Variable If" lineno="2356">
<arguments repr="condition, *values">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="VAR_POSITIONAL" required="false" repr="*values">
<name>values</name>
</arg>
</arguments>
<doc>&lt;p&gt;Sets variable based on the given condition.&lt;/p&gt;
&lt;p&gt;The basic usage is giving a condition and two values. The given condition is first evaluated the same way as with the &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; keyword. If the condition is true, then the first value is returned, and otherwise the second value is returned. The second value can also be omitted, in which case it has a default value None. This usage is illustrated in the examples below, where &lt;code&gt;${rc}&lt;/code&gt; is assumed to be zero.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${var1} =&lt;/td&gt;
&lt;td&gt;Set Variable If&lt;/td&gt;
&lt;td&gt;${rc} == 0&lt;/td&gt;
&lt;td&gt;zero&lt;/td&gt;
&lt;td&gt;nonzero&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${var2} =&lt;/td&gt;
&lt;td&gt;Set Variable If&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 0&lt;/td&gt;
&lt;td&gt;value1&lt;/td&gt;
&lt;td&gt;value2&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${var3} =&lt;/td&gt;
&lt;td&gt;Set Variable If&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 0&lt;/td&gt;
&lt;td&gt;whatever&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${var1} = 'zero'
${var2} = 'value2'
${var3} = None
&lt;/pre&gt;
&lt;p&gt;It is also possible to have 'else if' support by replacing the second value with another condition, and having two new values after it. If the first condition is not true, the second is evaluated and one of the values after it is returned based on its truth value. This can be continued by adding more conditions without a limit.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${var} =&lt;/td&gt;
&lt;td&gt;Set Variable If&lt;/td&gt;
&lt;td&gt;${rc} == 0&lt;/td&gt;
&lt;td&gt;zero&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 0&lt;/td&gt;
&lt;td&gt;greater than zero&lt;/td&gt;
&lt;td&gt;less then zero&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${var} =&lt;/td&gt;
&lt;td&gt;Set Variable If&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;${rc} == 0&lt;/td&gt;
&lt;td&gt;zero&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;${rc} == 1&lt;/td&gt;
&lt;td&gt;one&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;${rc} == 2&lt;/td&gt;
&lt;td&gt;two&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;${rc} &amp;gt; 2&lt;/td&gt;
&lt;td&gt;greater than two&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 0&lt;/td&gt;
&lt;td&gt;less than zero&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Get%20Variable%20Value" class="name"&gt;Get Variable Value&lt;/a&gt; if you need to set variables dynamically based on whether a variable exist or not.&lt;/p&gt;</doc>
<shortdoc>Sets variable based on the given condition.</shortdoc>
</kw>
<kw name="Should Be Empty" lineno="1459">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the given item is empty.&lt;/p&gt;
&lt;p&gt;The length of the item is got using the &lt;a href="#Get%20Length" class="name"&gt;Get Length&lt;/a&gt; keyword. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Verifies that the given item is empty.</shortdoc>
</kw>
<kw name="Should Be Equal" lineno="599">
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
<doc>&lt;p&gt;Fails if the given objects are unequal.&lt;/p&gt;
&lt;p&gt;Optional &lt;code&gt;msg&lt;/code&gt;, &lt;code&gt;values&lt;/code&gt; and &lt;code&gt;formatter&lt;/code&gt; arguments specify how to construct the error message if this keyword fails:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;If &lt;code&gt;msg&lt;/code&gt; is not given, the error message is &lt;code&gt;&amp;lt;first&amp;gt; != &amp;lt;second&amp;gt;&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;If &lt;code&gt;msg&lt;/code&gt; is given and &lt;code&gt;values&lt;/code&gt; gets a true value (default), the error message is &lt;code&gt;&amp;lt;msg&amp;gt;: &amp;lt;first&amp;gt; != &amp;lt;second&amp;gt;&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;If &lt;code&gt;msg&lt;/code&gt; is given and &lt;code&gt;values&lt;/code&gt; gets a false value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the error message is simply &lt;code&gt;&amp;lt;msg&amp;gt;&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;formatter&lt;/code&gt; controls how to format the values. Possible values are &lt;code&gt;str&lt;/code&gt; (default), &lt;code&gt;repr&lt;/code&gt; and &lt;code&gt;ascii&lt;/code&gt;, and they work similarly as Python built-in functions with same names. See &lt;a href="#String%20representations" class="name"&gt;String representations&lt;/a&gt; for more details.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, comparison is done case-insensitively. If both arguments are multiline strings, this keyword uses &lt;a href="#Multiline%20string%20comparison" class="name"&gt;multiline string comparison&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;expected&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;expected&lt;/td&gt;
&lt;td&gt;Custom error message&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;expected&lt;/td&gt;
&lt;td&gt;Custom message&lt;/td&gt;
&lt;td&gt;values=False&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;expected&lt;/td&gt;
&lt;td&gt;ignore_case=True&lt;/td&gt;
&lt;td&gt;formatter=repr&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if the given objects are unequal.</shortdoc>
</kw>
<kw name="Should Be Equal As Integers" lineno="755">
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
<doc>&lt;p&gt;Fails if objects are unequal after converting them to integers.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt; for information how to convert integers from other bases than 10 using &lt;code&gt;base&lt;/code&gt; argument or &lt;code&gt;0b/0o/0x&lt;/code&gt; prefixes.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;42&lt;/td&gt;
&lt;td&gt;${42}&lt;/td&gt;
&lt;td&gt;Error message&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;ABCD&lt;/td&gt;
&lt;td&gt;abcd&lt;/td&gt;
&lt;td&gt;base=16&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;0b1011&lt;/td&gt;
&lt;td&gt;11&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Fails if objects are unequal after converting them to integers.</shortdoc>
</kw>
<kw name="Should Be Equal As Numbers" lineno="792">
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
<doc>&lt;p&gt;Fails if objects are unequal after converting them to real numbers.&lt;/p&gt;
&lt;p&gt;The conversion is done with &lt;a href="#Convert%20To%20Number" class="name"&gt;Convert To Number&lt;/a&gt; keyword using the given &lt;code&gt;precision&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Numbers&lt;/td&gt;
&lt;td&gt;${x}&lt;/td&gt;
&lt;td&gt;1.1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;# Passes if ${x} is 1.1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Numbers&lt;/td&gt;
&lt;td&gt;1.123&lt;/td&gt;
&lt;td&gt;1.1&lt;/td&gt;
&lt;td&gt;precision=1&lt;/td&gt;
&lt;td&gt;# Passes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Numbers&lt;/td&gt;
&lt;td&gt;1.123&lt;/td&gt;
&lt;td&gt;1.4&lt;/td&gt;
&lt;td&gt;precision=0&lt;/td&gt;
&lt;td&gt;# Passes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Numbers&lt;/td&gt;
&lt;td&gt;112.3&lt;/td&gt;
&lt;td&gt;75&lt;/td&gt;
&lt;td&gt;precision=-2&lt;/td&gt;
&lt;td&gt;# Passes&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;As discussed in the documentation of &lt;a href="#Convert%20To%20Number" class="name"&gt;Convert To Number&lt;/a&gt;, machines generally cannot store floating point numbers accurately. Because of this limitation, comparing floats for equality is problematic and a correct approach to use depends on the context. This keyword uses a very naive approach of rounding the numbers before comparing them, which is both prone to rounding errors and does not work very well if numbers are really big or small. For more information about comparing floats, and ideas on how to implement your own context specific comparison algorithm, see &lt;a href="http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/"&gt;http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If you want to avoid possible problems with floating point numbers, you can implement custom keywords using Python's &lt;a href="http://docs.python.org/library/decimal.html"&gt;decimal&lt;/a&gt; or &lt;a href="http://docs.python.org/library/fractions.html"&gt;fractions&lt;/a&gt; modules.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Not%20Be%20Equal%20As%20Numbers" class="name"&gt;Should Not Be Equal As Numbers&lt;/a&gt; for a negative version of this keyword and &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if objects are unequal after converting them to real numbers.</shortdoc>
</kw>
<kw name="Should Be Equal As Strings" lineno="871">
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
<doc>&lt;p&gt;Fails if objects are unequal after converting them to strings.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt;, &lt;code&gt;values&lt;/code&gt; and &lt;code&gt;formatter&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), comparison is done case-insensitively. If both arguments are multiline strings, this keyword uses &lt;a href="#Multiline%20string%20comparison" class="name"&gt;multiline string comparison&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;Strings are always &lt;a href="http://www.macchiato.com/unicode/nfc-faq"&gt;NFC normalized&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if objects are unequal after converting them to strings.</shortdoc>
</kw>
<kw name="Should Be True" lineno="558">
<arguments repr="condition, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given condition is not true.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;condition&lt;/code&gt; is a string (e.g. &lt;code&gt;${rc} &amp;lt; 10&lt;/code&gt;), it is evaluated as a Python expression as explained in &lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt; and the keyword status is decided based on the result. If a non-string item is given, the status is got directly from its &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;truth value&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The default error message (&lt;code&gt;&amp;lt;condition&amp;gt; should be true&lt;/code&gt;) is not very informative, but it can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;${rc} &amp;lt; 10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;'${status}' == 'PASS'&lt;/td&gt;
&lt;td&gt;# Strings must be quoted&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;${number}&lt;/td&gt;
&lt;td&gt;# Passes if ${number} is not zero&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;# Passes if ${list} is not empty&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Variables used like &lt;code&gt;${variable}&lt;/code&gt;, as in the examples above, are replaced in the expression before evaluation. Variables are also available in the evaluation namespace, and can be accessed using special &lt;code&gt;$variable&lt;/code&gt; syntax as explained in the &lt;a href="#Evaluating%20expressions" class="name"&gt;Evaluating expressions&lt;/a&gt; section.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;$rc &amp;lt; 10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;$status == 'PASS'&lt;/td&gt;
&lt;td&gt;# Expected string must be quoted&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; automatically imports Python's &lt;a href="http://docs.python.org/library/os.html"&gt;os&lt;/a&gt; and &lt;a href="http://docs.python.org/library/sys.html"&gt;sys&lt;/a&gt; modules that contain several useful attributes:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;os.linesep == '\n'&lt;/td&gt;
&lt;td&gt;# Unixy&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;os.linesep == '\r\n'&lt;/td&gt;
&lt;td&gt;# Windows&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;sys.platform == 'darwin'&lt;/td&gt;
&lt;td&gt;# OS X&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be True&lt;/td&gt;
&lt;td&gt;sys.platform.startswith('java')&lt;/td&gt;
&lt;td&gt;# Jython&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Fails if the given condition is not true.</shortdoc>
</kw>
<kw name="Should Contain" lineno="1055">
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
<doc>&lt;p&gt;Fails if &lt;code&gt;container&lt;/code&gt; does not contain &lt;code&gt;item&lt;/code&gt; one or more times.&lt;/p&gt;
&lt;p&gt;Works with strings, lists, and anything that supports Python's &lt;code&gt;in&lt;/code&gt; operator.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with arguments &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and compared items are strings, it indicates that comparison should be case-insensitive. If the &lt;code&gt;container&lt;/code&gt; is a list-like object, string items in it are compared case-insensitively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;PASS&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain&lt;/td&gt;
&lt;td&gt;${some list}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;msg=Failure!&lt;/td&gt;
&lt;td&gt;values=False&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain&lt;/td&gt;
&lt;td&gt;${some list}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;ignore_case=True&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if ``container`` does not contain ``item`` one or more times.</shortdoc>
</kw>
<kw name="Should Contain Any" lineno="1111">
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
<doc>&lt;p&gt;Fails if &lt;code&gt;container&lt;/code&gt; does not contain any of the &lt;code&gt;*items&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Works with strings, lists, and anything that supports Python's &lt;code&gt;in&lt;/code&gt; operator.&lt;/p&gt;
&lt;p&gt;Supports additional configuration parameters &lt;code&gt;msg&lt;/code&gt;, &lt;code&gt;values&lt;/code&gt;, &lt;code&gt;ignore_case&lt;/code&gt; and &lt;code&gt;strip_spaces&lt;/code&gt;, and &lt;code&gt;collapse_spaces&lt;/code&gt; which have exactly the same semantics as arguments with same names have with &lt;a href="#Should%20Contain" class="name"&gt;Should Contain&lt;/a&gt;. These arguments must always be given using &lt;code&gt;name=value&lt;/code&gt; syntax after all &lt;code&gt;items&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Note that possible equal signs in &lt;code&gt;items&lt;/code&gt; must be escaped with a backslash (e.g. &lt;code&gt;foo\=bar&lt;/code&gt;) to avoid them to be passed in as &lt;code&gt;**configuration&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Any&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;substring 1&lt;/td&gt;
&lt;td&gt;substring 2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Any&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;item 1&lt;/td&gt;
&lt;td&gt;item 2&lt;/td&gt;
&lt;td&gt;item 3&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Any&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;item 1&lt;/td&gt;
&lt;td&gt;item 2&lt;/td&gt;
&lt;td&gt;item 3&lt;/td&gt;
&lt;td&gt;ignore_case=True&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain Any&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;@{items}&lt;/td&gt;
&lt;td&gt;msg=Custom message&lt;/td&gt;
&lt;td&gt;values=False&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Fails if ``container`` does not contain any of the ``*items``.</shortdoc>
</kw>
<kw name="Should Contain X Times" lineno="1228">
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
<doc>&lt;p&gt;Fails if &lt;code&gt;container&lt;/code&gt; does not contain &lt;code&gt;item&lt;/code&gt; &lt;code&gt;count&lt;/code&gt; times.&lt;/p&gt;
&lt;p&gt;Works with strings, lists and all objects that &lt;a href="#Get%20Count" class="name"&gt;Get Count&lt;/a&gt; works with. The default error message can be overridden with &lt;code&gt;msg&lt;/code&gt; and the actual count is always logged.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and compared items are strings, it indicates that comparison should be case-insensitive. If the &lt;code&gt;container&lt;/code&gt; is a list-like object, string items in it are compared case-insensitively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain X Times&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;hello&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Contain X Times&lt;/td&gt;
&lt;td&gt;${some list}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;3&lt;/td&gt;
&lt;td&gt;ignore_case=True&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if ``container`` does not contain ``item`` ``count`` times.</shortdoc>
</kw>
<kw name="Should End With" lineno="977">
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
<doc>&lt;p&gt;Fails if the string &lt;code&gt;str1&lt;/code&gt; does not end with the string &lt;code&gt;str2&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;, as well as for semantics of the &lt;code&gt;ignore_case&lt;/code&gt;, &lt;code&gt;strip_spaces&lt;/code&gt;, and &lt;code&gt;collapse_spaces&lt;/code&gt; options.&lt;/p&gt;</doc>
<shortdoc>Fails if the string ``str1`` does not end with the string ``str2``.</shortdoc>
</kw>
<kw name="Should Match" lineno="1324">
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
<doc>&lt;p&gt;Fails if the given &lt;code&gt;string&lt;/code&gt; does not match the given &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Pattern matching is similar as matching files in a shell with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; acting as wildcards. See the &lt;a href="#Glob%20patterns" class="name"&gt;Glob patterns&lt;/a&gt; section for more information.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and compared items are strings, it indicates that comparison should be case-insensitive.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``string`` does not match the given ``pattern``.</shortdoc>
</kw>
<kw name="Should Match Regexp" lineno="1343">
<arguments repr="string, pattern, msg=None, values=True">
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
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;string&lt;/code&gt; does not match &lt;code&gt;pattern&lt;/code&gt; as a regular expression.&lt;/p&gt;
&lt;p&gt;See the &lt;a href="#Regular%20expressions" class="name"&gt;Regular expressions&lt;/a&gt; section for more information about regular expressions and how to use then in Robot Framework test data.&lt;/p&gt;
&lt;p&gt;Notice that the given pattern does not need to match the whole string. For example, the pattern &lt;code&gt;ello&lt;/code&gt; matches the string &lt;code&gt;Hello world!&lt;/code&gt;. If a full match is needed, the &lt;code&gt;^&lt;/code&gt; and &lt;code&gt;$&lt;/code&gt; characters can be used to denote the beginning and end of the string, respectively. For example, &lt;code&gt;^ello$&lt;/code&gt; only matches the exact string &lt;code&gt;ello&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Possible flags altering how the expression is parsed (e.g. &lt;code&gt;re.IGNORECASE&lt;/code&gt;, &lt;code&gt;re.MULTILINE&lt;/code&gt;) must be embedded to the pattern like &lt;code&gt;(?im)pattern&lt;/code&gt;. The most useful flags are &lt;code&gt;i&lt;/code&gt; (case-insensitive), &lt;code&gt;m&lt;/code&gt; (multiline mode), &lt;code&gt;s&lt;/code&gt; (dotall mode) and &lt;code&gt;x&lt;/code&gt; (verbose).&lt;/p&gt;
&lt;p&gt;If this keyword passes, it returns the portion of the string that matched the pattern. Additionally, the possible captured groups are returned.&lt;/p&gt;
&lt;p&gt;See the &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; keyword for an explanation on how to override the default error message with the &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt; arguments.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Match Regexp&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;\\d{6}&lt;/td&gt;
&lt;td&gt;# Output contains six numbers&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Match Regexp&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;^\\d{6}$&lt;/td&gt;
&lt;td&gt;# Six numbers and nothing more&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${ret} =&lt;/td&gt;
&lt;td&gt;Should Match Regexp&lt;/td&gt;
&lt;td&gt;Foo: 42&lt;/td&gt;
&lt;td&gt;(?i)foo: \\d+&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${match}&lt;/td&gt;
&lt;td&gt;${group1}&lt;/td&gt;
&lt;td&gt;${group2} =&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;...&lt;/td&gt;
&lt;td&gt;Should Match Regexp&lt;/td&gt;
&lt;td&gt;Bar: 43&lt;/td&gt;
&lt;td&gt;(Foo|Bar): (\\d+)&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;=&amp;gt;&lt;/p&gt;
&lt;pre&gt;
${ret} = 'Foo: 42'
${match} = 'Bar: 43'
${group1} = 'Bar'
${group2} = '43'
&lt;/pre&gt;</doc>
<shortdoc>Fails if ``string`` does not match ``pattern`` as a regular expression.</shortdoc>
</kw>
<kw name="Should Not Be Empty" lineno="1468">
<arguments repr="item, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="item">
<name>item</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the given item is not empty.&lt;/p&gt;
&lt;p&gt;The length of the item is got using the &lt;a href="#Get%20Length" class="name"&gt;Get Length&lt;/a&gt; keyword. The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;</doc>
<shortdoc>Verifies that the given item is not empty.</shortdoc>
</kw>
<kw name="Should Not Be Equal" lineno="698">
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
<doc>&lt;p&gt;Fails if the given objects are equal.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, comparison is done case-insensitively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if the given objects are equal.</shortdoc>
</kw>
<kw name="Should Not Be Equal As Integers" lineno="738">
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
<doc>&lt;p&gt;Fails if objects are equal after converting them to integers.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Convert%20To%20Integer" class="name"&gt;Convert To Integer&lt;/a&gt; for information how to convert integers from other bases than 10 using &lt;code&gt;base&lt;/code&gt; argument or &lt;code&gt;0b/0o/0x&lt;/code&gt; prefixes.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal%20As%20Integers" class="name"&gt;Should Be Equal As Integers&lt;/a&gt; for some usage examples.&lt;/p&gt;</doc>
<shortdoc>Fails if objects are equal after converting them to integers.</shortdoc>
</kw>
<kw name="Should Not Be Equal As Numbers" lineno="775">
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
<doc>&lt;p&gt;Fails if objects are equal after converting them to real numbers.&lt;/p&gt;
&lt;p&gt;The conversion is done with &lt;a href="#Convert%20To%20Number" class="name"&gt;Convert To Number&lt;/a&gt; keyword using the given &lt;code&gt;precision&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal%20As%20Numbers" class="name"&gt;Should Be Equal As Numbers&lt;/a&gt; for examples on how to use &lt;code&gt;precision&lt;/code&gt; and why it does not always work as expected. See also &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if objects are equal after converting them to real numbers.</shortdoc>
</kw>
<kw name="Should Not Be Equal As Strings" lineno="830">
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
<doc>&lt;p&gt;Fails if objects are equal after converting them to strings.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), comparison is done case-insensitively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;Strings are always &lt;a href="http://www.macchiato.com/unicode/nfc-faq"&gt;NFC normalized&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if objects are equal after converting them to strings.</shortdoc>
</kw>
<kw name="Should Not Be True" lineno="549">
<arguments repr="condition, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given condition is true.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20True" class="name"&gt;Should Be True&lt;/a&gt; for details about how &lt;code&gt;condition&lt;/code&gt; is evaluated and how &lt;code&gt;msg&lt;/code&gt; can be used to override the default error message.&lt;/p&gt;</doc>
<shortdoc>Fails if the given condition is true.</shortdoc>
</kw>
<kw name="Should Not Contain" lineno="998">
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
<doc>&lt;p&gt;Fails if &lt;code&gt;container&lt;/code&gt; contains &lt;code&gt;item&lt;/code&gt; one or more times.&lt;/p&gt;
&lt;p&gt;Works with strings, lists, and anything that supports Python's &lt;code&gt;in&lt;/code&gt; operator.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with arguments &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;. &lt;code&gt;ignore_case&lt;/code&gt; has exactly the same semantics as with &lt;a href="#Should%20Contain" class="name"&gt;Should Contain&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;strip_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done without leading and trailing spaces. If &lt;code&gt;strip_spaces&lt;/code&gt; is given a string value &lt;code&gt;LEADING&lt;/code&gt; or &lt;code&gt;TRAILING&lt;/code&gt; (case-insensitive), the comparison is done without leading or trailing spaces, respectively.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;collapse_spaces&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;) and both arguments are strings, the comparison is done with all white spaces replaced by a single space character.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain&lt;/td&gt;
&lt;td&gt;${some list}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain&lt;/td&gt;
&lt;td&gt;${output}&lt;/td&gt;
&lt;td&gt;FAILED&lt;/td&gt;
&lt;td&gt;ignore_case=True&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;code&gt;strip_spaces&lt;/code&gt; is new in Robot Framework 4.0 and &lt;code&gt;collapse_spaces&lt;/code&gt; is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Fails if ``container`` contains ``item`` one or more times.</shortdoc>
</kw>
<kw name="Should Not Contain Any" lineno="1170">
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
<doc>&lt;p&gt;Fails if &lt;code&gt;container&lt;/code&gt; contains one or more of the &lt;code&gt;*items&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Works with strings, lists, and anything that supports Python's &lt;code&gt;in&lt;/code&gt; operator.&lt;/p&gt;
&lt;p&gt;Supports additional configuration parameters &lt;code&gt;msg&lt;/code&gt;, &lt;code&gt;values&lt;/code&gt;, &lt;code&gt;ignore_case&lt;/code&gt; and &lt;code&gt;strip_spaces&lt;/code&gt;, and &lt;code&gt;collapse_spaces&lt;/code&gt; which have exactly the same semantics as arguments with same names have with &lt;a href="#Should%20Contain" class="name"&gt;Should Contain&lt;/a&gt;. These arguments must always be given using &lt;code&gt;name=value&lt;/code&gt; syntax after all &lt;code&gt;items&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Note that possible equal signs in &lt;code&gt;items&lt;/code&gt; must be escaped with a backslash (e.g. &lt;code&gt;foo\=bar&lt;/code&gt;) to avoid them to be passed in as &lt;code&gt;**configuration&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain Any&lt;/td&gt;
&lt;td&gt;${string}&lt;/td&gt;
&lt;td&gt;substring 1&lt;/td&gt;
&lt;td&gt;substring 2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain Any&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;item 1&lt;/td&gt;
&lt;td&gt;item 2&lt;/td&gt;
&lt;td&gt;item 3&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain Any&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;item 1&lt;/td&gt;
&lt;td&gt;item 2&lt;/td&gt;
&lt;td&gt;item 3&lt;/td&gt;
&lt;td&gt;ignore_case=True&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Not Contain Any&lt;/td&gt;
&lt;td&gt;${list}&lt;/td&gt;
&lt;td&gt;@{items}&lt;/td&gt;
&lt;td&gt;msg=Custom message&lt;/td&gt;
&lt;td&gt;values=False&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Fails if ``container`` contains one or more of the ``*items``.</shortdoc>
</kw>
<kw name="Should Not End With" lineno="955">
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
<doc>&lt;p&gt;Fails if the string &lt;code&gt;str1&lt;/code&gt; ends with the string &lt;code&gt;str2&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;, as well as for semantics of the &lt;code&gt;ignore_case&lt;/code&gt;, &lt;code&gt;strip_spaces&lt;/code&gt;, and &lt;code&gt;collapse_spaces&lt;/code&gt; options.&lt;/p&gt;</doc>
<shortdoc>Fails if the string ``str1`` ends with the string ``str2``.</shortdoc>
</kw>
<kw name="Should Not Match" lineno="1306">
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
<doc>&lt;p&gt;Fails if the given &lt;code&gt;string&lt;/code&gt; matches the given &lt;code&gt;pattern&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Pattern matching is similar as matching files in a shell with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; acting as wildcards. See the &lt;a href="#Glob%20patterns" class="name"&gt;Glob patterns&lt;/a&gt; section for more information.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;ignore_case&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the comparison is case-insensitive.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;span class="name"&gt;`values&lt;/span&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if the given ``string`` matches the given ``pattern``.</shortdoc>
</kw>
<kw name="Should Not Match Regexp" lineno="1390">
<arguments repr="string, pattern, msg=None, values=True">
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
</arguments>
<doc>&lt;p&gt;Fails if &lt;code&gt;string&lt;/code&gt; matches &lt;code&gt;pattern&lt;/code&gt; as a regular expression.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Match%20Regexp" class="name"&gt;Should Match Regexp&lt;/a&gt; for more information about arguments.&lt;/p&gt;</doc>
<shortdoc>Fails if ``string`` matches ``pattern`` as a regular expression.</shortdoc>
</kw>
<kw name="Should Not Start With" lineno="912">
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
<doc>&lt;p&gt;Fails if the string &lt;code&gt;str1&lt;/code&gt; starts with the string &lt;code&gt;str2&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;, as well as for semantics of the &lt;code&gt;ignore_case&lt;/code&gt;, &lt;code&gt;strip_spaces&lt;/code&gt;, and &lt;code&gt;collapse_spaces&lt;/code&gt; options.&lt;/p&gt;</doc>
<shortdoc>Fails if the string ``str1`` starts with the string ``str2``.</shortdoc>
</kw>
<kw name="Should Start With" lineno="934">
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
<doc>&lt;p&gt;Fails if the string &lt;code&gt;str1&lt;/code&gt; does not start with the string &lt;code&gt;str2&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;See &lt;a href="#Should%20Be%20Equal" class="name"&gt;Should Be Equal&lt;/a&gt; for an explanation on how to override the default error message with &lt;code&gt;msg&lt;/code&gt; and &lt;code&gt;values&lt;/code&gt;, as well as for semantics of the &lt;code&gt;ignore_case&lt;/code&gt;, &lt;code&gt;strip_spaces&lt;/code&gt;, and &lt;code&gt;collapse_spaces&lt;/code&gt; options.&lt;/p&gt;</doc>
<shortdoc>Fails if the string ``str1`` does not start with the string ``str2``.</shortdoc>
</kw>
<kw name="Skip" lineno="2509">
<arguments repr="msg=Skipped with Skip keyword.">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=Skipped with Skip keyword.">
<name>msg</name>
<default>Skipped with Skip keyword.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Skips the rest of the current test.&lt;/p&gt;
&lt;p&gt;Skips the remaining keywords in the current test and sets the given message to the test. If the test has teardown, it will be executed.&lt;/p&gt;</doc>
<shortdoc>Skips the rest of the current test.</shortdoc>
</kw>
<kw name="Skip If" lineno="2517">
<arguments repr="condition, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="condition">
<name>condition</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Skips the rest of the current test if the &lt;code&gt;condition&lt;/code&gt; is True.&lt;/p&gt;
&lt;p&gt;Skips the remaining keywords in the current test and sets the given message to the test. If &lt;code&gt;msg&lt;/code&gt; is not given, the &lt;code&gt;condition&lt;/code&gt; will be used as the message. If the test has teardown, it will be executed.&lt;/p&gt;
&lt;p&gt;If the &lt;code&gt;condition&lt;/code&gt; evaluates to False, does nothing.&lt;/p&gt;</doc>
<shortdoc>Skips the rest of the current test if the ``condition`` is True.</shortdoc>
</kw>
<kw name="Sleep" lineno="2798">
<arguments repr="time_, reason=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time_">
<name>time_</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="reason=None">
<name>reason</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Pauses the test executed for the given time.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;time&lt;/code&gt; may be either a number or a time string. Time strings are in a format such as &lt;code&gt;1 day 2 hours 3 minutes 4 seconds 5milliseconds&lt;/code&gt; or &lt;code&gt;1d 2h 3m 4s 5ms&lt;/code&gt;, and they are fully explained in an appendix of Robot Framework User Guide. Optional &lt;span class="name"&gt;reason&lt;/span&gt; can be used to explain why sleeping is necessary. Both the time slept and the reason are logged.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Sleep&lt;/td&gt;
&lt;td&gt;42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Sleep&lt;/td&gt;
&lt;td&gt;1.5&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Sleep&lt;/td&gt;
&lt;td&gt;2 minutes 10 seconds&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Sleep&lt;/td&gt;
&lt;td&gt;10s&lt;/td&gt;
&lt;td&gt;Wait for a reply&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Pauses the test executed for the given time.</shortdoc>
</kw>
<kw name="Variable Should Exist" lineno="1567">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails unless the given variable exists within the current scope.&lt;/p&gt;
&lt;p&gt;The name of the variable can be given either as a normal variable name (e.g. &lt;code&gt;${NAME}&lt;/code&gt;) or in escaped format (e.g. &lt;code&gt;\${NAME}&lt;/code&gt;). Notice that the former has some limitations explained in &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Variable%20Should%20Not%20Exist" class="name"&gt;Variable Should Not Exist&lt;/a&gt; and &lt;a href="#Keyword%20Should%20Exist" class="name"&gt;Keyword Should Exist&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails unless the given variable exists within the current scope.</shortdoc>
</kw>
<kw name="Variable Should Not Exist" lineno="1586">
<arguments repr="name, msg=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="msg=None">
<name>msg</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Fails if the given variable exists within the current scope.&lt;/p&gt;
&lt;p&gt;The name of the variable can be given either as a normal variable name (e.g. &lt;code&gt;${NAME}&lt;/code&gt;) or in escaped format (e.g. &lt;code&gt;\${NAME}&lt;/code&gt;). Notice that the former has some limitations explained in &lt;a href="#Set%20Suite%20Variable" class="name"&gt;Set Suite Variable&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The default error message can be overridden with the &lt;code&gt;msg&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Variable%20Should%20Exist" class="name"&gt;Variable Should Exist&lt;/a&gt; and &lt;a href="#Keyword%20Should%20Exist" class="name"&gt;Keyword Should Exist&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Fails if the given variable exists within the current scope.</shortdoc>
</kw>
<kw name="Wait Until Keyword Succeeds" lineno="2274">
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
<doc>&lt;p&gt;Runs the specified keyword and retries if it fails.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;name&lt;/code&gt; and &lt;code&gt;args&lt;/code&gt; define the keyword that is executed similarly as with &lt;a href="#Run%20Keyword" class="name"&gt;Run Keyword&lt;/a&gt;. How long to retry running the keyword is defined using &lt;code&gt;retry&lt;/code&gt; argument either as timeout or count. &lt;code&gt;retry_interval&lt;/code&gt; is the time to wait between execution attempts.&lt;/p&gt;
&lt;p&gt;If &lt;code&gt;retry&lt;/code&gt; is given as timeout, it must be in Robot Framework's time format (e.g. &lt;code&gt;1 minute&lt;/code&gt;, &lt;code&gt;2 min 3 s&lt;/code&gt;, &lt;code&gt;4.5&lt;/code&gt;) that is explained in an appendix of Robot Framework User Guide. If it is given as count, it must have &lt;code&gt;times&lt;/code&gt; or &lt;code&gt;x&lt;/code&gt; postfix (e.g. &lt;code&gt;5 times&lt;/code&gt;, &lt;code&gt;10 x&lt;/code&gt;). &lt;code&gt;retry_interval&lt;/code&gt; must always be given in Robot Framework's time format.&lt;/p&gt;
&lt;p&gt;By default &lt;code&gt;retry_interval&lt;/code&gt; is the time to wait &lt;i&gt;after&lt;/i&gt; a keyword has failed. For example, if the first run takes 2 seconds and the retry interval is 3 seconds, the second run starts 5 seconds after the first run started. If &lt;code&gt;retry_interval&lt;/code&gt; start with prefix &lt;code&gt;strict:&lt;/code&gt;, the execution time of the previous keyword is subtracted from the retry time. With the earlier example the second run would thus start 3 seconds after the first run started. A warning is logged if keyword execution time is longer than a strict interval.&lt;/p&gt;
&lt;p&gt;If the keyword does not succeed regardless of retries, this keyword fails. If the executed keyword passes, its return value is returned.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Wait Until Keyword Succeeds&lt;/td&gt;
&lt;td&gt;2 min&lt;/td&gt;
&lt;td&gt;5 sec&lt;/td&gt;
&lt;td&gt;My keyword&lt;/td&gt;
&lt;td&gt;argument&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Wait Until Keyword Succeeds&lt;/td&gt;
&lt;td&gt;3x&lt;/td&gt;
&lt;td&gt;200ms&lt;/td&gt;
&lt;td&gt;My keyword&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${result} =&lt;/td&gt;
&lt;td&gt;Wait Until Keyword Succeeds&lt;/td&gt;
&lt;td&gt;3x&lt;/td&gt;
&lt;td&gt;strict: 200ms&lt;/td&gt;
&lt;td&gt;My keyword&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;All normal failures are caught by this keyword. Errors caused by invalid syntax, test or keyword timeouts, or fatal exceptions (caused e.g. by &lt;a href="#Fatal%20Error" class="name"&gt;Fatal Error&lt;/a&gt;) are not caught.&lt;/p&gt;
&lt;p&gt;Running the same keyword multiple times inside this keyword can create lots of output and considerably increase the size of the generated output files. It is possible to remove unnecessary keywords from the outputs using &lt;code&gt;--RemoveKeywords WUKS&lt;/code&gt; command line option.&lt;/p&gt;
&lt;p&gt;Support for "strict" retry interval is new in Robot Framework 4.1.&lt;/p&gt;</doc>
<shortdoc>Runs the specified keyword and retries if it fails.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
