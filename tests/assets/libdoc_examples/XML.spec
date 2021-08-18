<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="XML" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2021-08-18T02:53:35Z" specversion="3" source="../../../../.cache/pypoetry/virtualenvs/rfdocsindexer--g8aZv4K-py3.9/lib/python3.9/site-packages/robot/libraries/XML.py" lineno="37">
<version>4.1</version>
<doc>&lt;p&gt;Robot Framework test library for verifying and modifying XML documents.&lt;/p&gt;
&lt;p&gt;As the name implies, &lt;i&gt;XML&lt;/i&gt; is a test library for verifying contents of XML files. In practice it is a pretty thin wrapper on top of Python's &lt;a href="http://docs.python.org/library/xml.etree.elementtree.html"&gt;ElementTree XML API&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;The library has the following main usages:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Parsing an XML file, or a string containing XML, into an XML element structure and finding certain elements from it for for further analysis (e.g. &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; and &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keywords).&lt;/li&gt;
&lt;li&gt;Getting text or attributes of elements (e.g. &lt;a href="#Get%20Element%20Text" class="name"&gt;Get Element Text&lt;/a&gt; and &lt;a href="#Get%20Element%20Attribute" class="name"&gt;Get Element Attribute&lt;/a&gt;).&lt;/li&gt;
&lt;li&gt;Directly verifying text, attributes, or whole elements (e.g &lt;a href="#Element%20Text%20Should%20Be" class="name"&gt;Element Text Should Be&lt;/a&gt; and &lt;a href="#Elements%20Should%20Be%20Equal" class="name"&gt;Elements Should Be Equal&lt;/a&gt;).&lt;/li&gt;
&lt;li&gt;Modifying XML and saving it (e.g. &lt;a href="#Set%20Element%20Text" class="name"&gt;Set Element Text&lt;/a&gt;, &lt;a href="#Add%20Element" class="name"&gt;Add Element&lt;/a&gt; and &lt;a href="#Save%20Xml" class="name"&gt;Save XML&lt;/a&gt;).&lt;/li&gt;
&lt;/ul&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#Parsing%20XML" class="name"&gt;Parsing XML&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Using%20lxml" class="name"&gt;Using lxml&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Finding%20elements%20with%20xpath" class="name"&gt;Finding elements with xpath&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Element%20attributes" class="name"&gt;Element attributes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Handling%20XML%20namespaces" class="name"&gt;Handling XML namespaces&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Importing" class="name"&gt;Importing&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Parsing XML"&gt;Parsing XML&lt;/h2&gt;
&lt;p&gt;XML can be parsed into an element structure using &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; keyword. The XML to be parsed can be specified using a path to an XML file or as a string or bytes that contain XML directly. The keyword returns the root element of the structure, which then contains other elements as its children and their children. Possible comments and processing instructions in the source XML are removed.&lt;/p&gt;
&lt;p&gt;XML is not validated during parsing even if has a schema defined. How possible doctype elements are handled otherwise depends on the used XML module and on the platform. The standard ElementTree strips doctypes altogether but when &lt;a href="#Using%20lxml" class="name"&gt;using lxml&lt;/a&gt; they are preserved when XML is saved.&lt;/p&gt;
&lt;p&gt;The element structure returned by &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;, as well as elements returned by keywords such as &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;, can be used as the &lt;code&gt;source&lt;/code&gt; argument with other keywords. In addition to an already parsed XML structure, other keywords also accept paths to XML files and strings containing XML similarly as &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;. Notice that keywords that modify XML do not write those changes back to disk even if the source would be given as a path to a file. Changes must always saved explicitly using &lt;a href="#Save%20Xml" class="name"&gt;Save XML&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;When the source is given as a path to a file, the forward slash character (&lt;code&gt;/&lt;/code&gt;) can be used as the path separator regardless the operating system. On Windows also the backslash works, but it the test data it needs to be escaped by doubling it (&lt;code&gt;\\&lt;/code&gt;). Using the built-in variable &lt;code&gt;${/}&lt;/code&gt; naturally works too.&lt;/p&gt;
&lt;p&gt;Note: Support for XML as bytes is new in Robot Framework 3.2.&lt;/p&gt;
&lt;h2 id="Using lxml"&gt;Using lxml&lt;/h2&gt;
&lt;p&gt;By default this library uses Python's standard &lt;a href="http://docs.python.org/library/xml.etree.elementtree.html"&gt;ElementTree&lt;/a&gt; module for parsing XML, but it can be configured to use &lt;a href="http://lxml.de"&gt;lxml&lt;/a&gt; module instead when &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; the library. The resulting element structure has same API regardless which module is used for parsing.&lt;/p&gt;
&lt;p&gt;The main benefits of using lxml is that it supports richer xpath syntax than the standard ElementTree and enables using &lt;a href="#Evaluate%20Xpath" class="name"&gt;Evaluate Xpath&lt;/a&gt; keyword. It also preserves the doctype and possible namespace prefixes saving XML.&lt;/p&gt;
&lt;h2 id="Example"&gt;Example&lt;/h2&gt;
&lt;p&gt;The following simple example demonstrates parsing XML and verifying its contents both using keywords in this library and in &lt;i&gt;BuiltIn&lt;/i&gt; and &lt;i&gt;Collections&lt;/i&gt; libraries. How to use xpath expressions to find elements and what attributes the returned elements contain are discussed, with more examples, in &lt;a href="#Finding%20elements%20with%20xpath" class="name"&gt;Finding elements with xpath&lt;/a&gt; and &lt;a href="#Element%20attributes" class="name"&gt;Element attributes&lt;/a&gt; sections.&lt;/p&gt;
&lt;p&gt;In this example, as well as in many other examples in this documentation, &lt;code&gt;${XML}&lt;/code&gt; refers to the following example XML document. In practice &lt;code&gt;${XML}&lt;/code&gt; could either be a path to an XML file or it could contain the XML itself.&lt;/p&gt;
&lt;pre&gt;
&amp;lt;example&amp;gt;
  &amp;lt;first id="1"&amp;gt;text&amp;lt;/first&amp;gt;
  &amp;lt;second id="2"&amp;gt;
    &amp;lt;child/&amp;gt;
  &amp;lt;/second&amp;gt;
  &amp;lt;third&amp;gt;
    &amp;lt;child&amp;gt;more text&amp;lt;/child&amp;gt;
    &amp;lt;second id="child"/&amp;gt;
    &amp;lt;child&amp;gt;&amp;lt;grandchild/&amp;gt;&amp;lt;/child&amp;gt;
  &amp;lt;/third&amp;gt;
  &amp;lt;html&amp;gt;
    &amp;lt;p&amp;gt;
      Text with &amp;lt;b&amp;gt;bold&amp;lt;/b&amp;gt; and &amp;lt;i&amp;gt;italics&amp;lt;/i&amp;gt;.
    &amp;lt;/p&amp;gt;
  &amp;lt;/html&amp;gt;
&amp;lt;/example&amp;gt;
&lt;/pre&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${root} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${root.tag}&lt;/td&gt;
&lt;td&gt;example&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${first} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${first.text}&lt;/td&gt;
&lt;td&gt;text&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Dictionary Should Contain Key&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${first.attrib}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Text%20Should%20Be" class="name"&gt;Element Text Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;text&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Notice that in the example three last lines are equivalent. Which one to use in practice depends on which other elements you need to get or verify. If you only need to do one verification, using the last line alone would suffice. If more verifications are needed, parsing the XML with &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; only once would be more efficient.&lt;/p&gt;
&lt;h2 id="Finding elements with xpath"&gt;Finding elements with xpath&lt;/h2&gt;
&lt;p&gt;ElementTree, and thus also this library, supports finding elements using xpath expressions. ElementTree does not, however, support the full xpath standard. The supported xpath syntax is explained below and &lt;a href="https://docs.python.org/library/xml.etree.elementtree.html#xpath-support"&gt;ElementTree documentation&lt;/a&gt; provides more details. In the examples &lt;code&gt;${XML}&lt;/code&gt; refers to the same XML structure as in the earlier example.&lt;/p&gt;
&lt;p&gt;If lxml support is enabled when &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; the library, the whole &lt;a href="http://www.w3.org/TR/xpath/"&gt;xpath 1.0 standard&lt;/a&gt; is supported. That includes everything listed below but also lot of other useful constructs.&lt;/p&gt;
&lt;h3 id="Tag names"&gt;Tag names&lt;/h3&gt;
&lt;p&gt;When just a single tag name is used, xpath matches all direct child elements that have that tag name.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${elem} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;third&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${elem.tag}&lt;/td&gt;
&lt;td&gt;third&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@{children} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${elem}&lt;/td&gt;
&lt;td&gt;child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Length Should Be&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${children}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Paths"&gt;Paths&lt;/h3&gt;
&lt;p&gt;Paths are created by combining tag names with a forward slash (&lt;code&gt;/&lt;/code&gt;). For example, &lt;code&gt;parent/child&lt;/code&gt; matches all &lt;code&gt;child&lt;/code&gt; elements under &lt;code&gt;parent&lt;/code&gt; element. Notice that if there are multiple &lt;code&gt;parent&lt;/code&gt; elements that all have &lt;code&gt;child&lt;/code&gt; elements, &lt;code&gt;parent/child&lt;/code&gt; xpath will match all these &lt;code&gt;child&lt;/code&gt; elements.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${elem} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${elem.tag}&lt;/td&gt;
&lt;td&gt;child&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${elem} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;third/child/grandchild&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${elem.tag}&lt;/td&gt;
&lt;td&gt;grandchild&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Wildcards"&gt;Wildcards&lt;/h3&gt;
&lt;p&gt;An asterisk (&lt;code&gt;*&lt;/code&gt;) can be used in paths instead of a tag name to denote any element.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{children} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;*/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Length Should Be&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${children}&lt;/td&gt;
&lt;td&gt;3&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Current element"&gt;Current element&lt;/h3&gt;
&lt;p&gt;The current element is denoted with a dot (&lt;code&gt;.&lt;/code&gt;). Normally the current element is implicit and does not need to be included in the xpath.&lt;/p&gt;
&lt;h3 id="Parent element"&gt;Parent element&lt;/h3&gt;
&lt;p&gt;The parent element of another element is denoted with two dots (&lt;code&gt;..&lt;/code&gt;). Notice that it is not possible to refer to the parent of the current element.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${elem} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;*/second/..&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${elem.tag}&lt;/td&gt;
&lt;td&gt;third&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Search all sub elements"&gt;Search all sub elements&lt;/h3&gt;
&lt;p&gt;Two forward slashes (&lt;code&gt;//&lt;/code&gt;) mean that all sub elements, not only the direct children, are searched. If the search is started from the current element, an explicit dot is required.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{elements} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;.//second&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Length Should Be&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${elements}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${b} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;html//b&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${b.text}&lt;/td&gt;
&lt;td&gt;bold&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Predicates"&gt;Predicates&lt;/h3&gt;
&lt;p&gt;Predicates allow selecting elements using also other criteria than tag names, for example, attributes or position. They are specified after the normal tag name or path using syntax &lt;code&gt;path[predicate]&lt;/code&gt;. The path can have wildcards and other special syntax explained earlier. What predicates the standard ElementTree supports is explained in the table below.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;th&gt;Predicate&lt;/th&gt;
&lt;th&gt;Matches&lt;/th&gt;
&lt;th&gt;Example&lt;/th&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@attrib&lt;/td&gt;
&lt;td&gt;Elements with attribute &lt;code&gt;attrib&lt;/code&gt;.&lt;/td&gt;
&lt;td&gt;second[@id]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;@attrib="value"&lt;/td&gt;
&lt;td&gt;Elements with attribute &lt;code&gt;attrib&lt;/code&gt; having value &lt;code&gt;value&lt;/code&gt;.&lt;/td&gt;
&lt;td&gt;*[@id="2"]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;position&lt;/td&gt;
&lt;td&gt;Elements at the specified position. Position can be an integer (starting from 1), expression &lt;code&gt;last()&lt;/code&gt;, or relative expression like &lt;code&gt;last() - 1&lt;/code&gt;.&lt;/td&gt;
&lt;td&gt;third/child[1]&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;tag&lt;/td&gt;
&lt;td&gt;Elements with a child element named &lt;code&gt;tag&lt;/code&gt;.&lt;/td&gt;
&lt;td&gt;third/child[grandchild]&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Predicates can also be stacked like &lt;code&gt;path[predicate1][predicate2]&lt;/code&gt;. A limitation is that possible position predicate must always be first.&lt;/p&gt;
&lt;h2 id="Element attributes"&gt;Element attributes&lt;/h2&gt;
&lt;p&gt;All keywords returning elements, such as &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;, and &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;, return ElementTree's &lt;a href="http://docs.python.org/library/xml.etree.elementtree.html#element-objects"&gt;Element objects&lt;/a&gt;. These elements can be used as inputs for other keywords, but they also contain several useful attributes that can be accessed directly using the extended variable syntax.&lt;/p&gt;
&lt;p&gt;The attributes that are both useful and convenient to use in the test data are explained below. Also other attributes, including methods, can be accessed, but that is typically better to do in custom libraries than directly in the test data.&lt;/p&gt;
&lt;p&gt;The examples use the same &lt;code&gt;${XML}&lt;/code&gt; structure as the earlier examples.&lt;/p&gt;
&lt;h3 id="tag"&gt;tag&lt;/h3&gt;
&lt;p&gt;The tag of the element.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${root} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${root.tag}&lt;/td&gt;
&lt;td&gt;example&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="text"&gt;text&lt;/h3&gt;
&lt;p&gt;The text that the element contains or Python &lt;code&gt;None&lt;/code&gt; if the element has no text. Notice that the text &lt;i&gt;does not&lt;/i&gt; contain texts of possible child elements nor text after or between children. Notice also that in XML whitespace is significant, so the text contains also possible indentation and newlines. To get also text of the possible children, optionally whitespace normalized, use &lt;a href="#Get%20Element%20Text" class="name"&gt;Get Element Text&lt;/a&gt; keyword.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${1st} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${1st.text}&lt;/td&gt;
&lt;td&gt;text&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${2nd} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${2nd.text}&lt;/td&gt;
&lt;td&gt;${NONE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;html/p&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${p.text}&lt;/td&gt;
&lt;td&gt;\n${SPACE*6}Text with${SPACE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="tail"&gt;tail&lt;/h3&gt;
&lt;p&gt;The text after the element before the next opening or closing tag. Python &lt;code&gt;None&lt;/code&gt; if the element has no tail. Similarly as with &lt;code&gt;text&lt;/code&gt;, also &lt;code&gt;tail&lt;/code&gt; contains possible indentation and newlines.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${b} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;html/p/b&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${b.tail}&lt;/td&gt;
&lt;td&gt;${SPACE}and${SPACE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="attrib"&gt;attrib&lt;/h3&gt;
&lt;p&gt;A Python dictionary containing attributes of the element.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${2nd} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${2nd.attrib['id']}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${3rd} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;third&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Empty&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${3rd.attrib}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Handling XML namespaces"&gt;Handling XML namespaces&lt;/h2&gt;
&lt;p&gt;ElementTree and lxml handle possible namespaces in XML documents by adding the namespace URI to tag names in so called Clark Notation. That is inconvenient especially with xpaths, and by default this library strips those namespaces away and moves them to &lt;code&gt;xmlns&lt;/code&gt; attribute instead. That can be avoided by passing &lt;code&gt;keep_clark_notation&lt;/code&gt; argument to &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; keyword. Alternatively &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; supports stripping namespace information altogether by using &lt;code&gt;strip_namespaces&lt;/code&gt; argument. The pros and cons of different approaches are discussed in more detail below.&lt;/p&gt;
&lt;h3 id="How ElementTree handles namespaces"&gt;How ElementTree handles namespaces&lt;/h3&gt;
&lt;p&gt;If an XML document has namespaces, ElementTree adds namespace information to tag names in &lt;a href="http://www.jclark.com/xml/xmlns.htm"&gt;Clark Notation&lt;/a&gt; (e.g. &lt;code&gt;{http://ns.uri}tag&lt;/code&gt;) and removes original &lt;code&gt;xmlns&lt;/code&gt; attributes. This is done both with default namespaces and with namespaces with a prefix. How it works in practice is illustrated by the following example, where &lt;code&gt;${NS}&lt;/code&gt; variable contains this XML document:&lt;/p&gt;
&lt;pre&gt;
&amp;lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns="http://www.w3.org/1999/xhtml"&amp;gt;
  &amp;lt;xsl:template match="/"&amp;gt;
    &amp;lt;html&amp;gt;&amp;lt;/html&amp;gt;
  &amp;lt;/xsl:template&amp;gt;
&amp;lt;/xsl:stylesheet&amp;gt;
&lt;/pre&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${root} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${NS}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${root.tag}&lt;/td&gt;
&lt;td&gt;{&lt;a href="http://www.w3.org/1999/XSL/Transform}stylesheet"&gt;http://www.w3.org/1999/XSL/Transform}stylesheet&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Should%20Exist" class="name"&gt;Element Should Exist&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;{&lt;a href="http://www.w3.org/1999/XSL/Transform}template/{http://www.w3.org/1999/xhtml}html"&gt;http://www.w3.org/1999/XSL/Transform}template/{http://www.w3.org/1999/xhtml}html&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Empty&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${root.attrib}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;As you can see, including the namespace URI in tag names makes xpaths really long and complex.&lt;/p&gt;
&lt;p&gt;If you save the XML, ElementTree moves namespace information back to &lt;code&gt;xmlns&lt;/code&gt; attributes. Unfortunately it does not restore the original prefixes:&lt;/p&gt;
&lt;pre&gt;
&amp;lt;ns0:stylesheet xmlns:ns0="http://www.w3.org/1999/XSL/Transform"&amp;gt;
  &amp;lt;ns0:template match="/"&amp;gt;
    &amp;lt;ns1:html xmlns:ns1="http://www.w3.org/1999/xhtml"&amp;gt;&amp;lt;/ns1:html&amp;gt;
  &amp;lt;/ns0:template&amp;gt;
&amp;lt;/ns0:stylesheet&amp;gt;
&lt;/pre&gt;
&lt;p&gt;The resulting output is semantically same as the original, but mangling prefixes like this may still not be desirable. Notice also that the actual output depends slightly on ElementTree version.&lt;/p&gt;
&lt;h3 id="Default namespace handling"&gt;Default namespace handling&lt;/h3&gt;
&lt;p&gt;Because the way ElementTree handles namespaces makes xpaths so complicated, this library, by default, strips namespaces from tag names and moves that information back to &lt;code&gt;xmlns&lt;/code&gt; attributes. How this works in practice is shown by the example below, where &lt;code&gt;${NS}&lt;/code&gt; variable contains the same XML document as in the previous example.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${root} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${NS}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;span class="name"&gt;Should Be Equal&lt;/span&gt;&lt;/td&gt;
&lt;td&gt;${root.tag}&lt;/td&gt;
&lt;td&gt;stylesheet&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Should%20Exist" class="name"&gt;Element Should Exist&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;template/html&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;xmlns&lt;/td&gt;
&lt;td&gt;&lt;a href="http://www.w3.org/1999/XSL/Transform"&gt;http://www.w3.org/1999/XSL/Transform&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;xmlns&lt;/td&gt;
&lt;td&gt;&lt;a href="http://www.w3.org/1999/xhtml"&gt;http://www.w3.org/1999/xhtml&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;xpath=template/html&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Now that tags do not contain namespace information, xpaths are simple again.&lt;/p&gt;
&lt;p&gt;A minor limitation of this approach is that namespace prefixes are lost. As a result the saved output is not exactly same as the original one in this case either:&lt;/p&gt;
&lt;pre&gt;
&amp;lt;stylesheet xmlns="http://www.w3.org/1999/XSL/Transform"&amp;gt;
  &amp;lt;template match="/"&amp;gt;
    &amp;lt;html xmlns="http://www.w3.org/1999/xhtml"&amp;gt;&amp;lt;/html&amp;gt;
  &amp;lt;/template&amp;gt;
&amp;lt;/stylesheet&amp;gt;
&lt;/pre&gt;
&lt;p&gt;Also this output is semantically same as the original. If the original XML had only default namespaces, the output would also look identical.&lt;/p&gt;
&lt;h3 id="Namespaces when using lxml"&gt;Namespaces when using lxml&lt;/h3&gt;
&lt;p&gt;This library handles namespaces same way both when &lt;a href="#Using%20lxml" class="name"&gt;using lxml&lt;/a&gt; and when not using it. There are, however, differences how lxml internally handles namespaces compared to the standard ElementTree. The main difference is that lxml stores information about namespace prefixes and they are thus preserved if XML is saved. Another visible difference is that lxml includes namespace information in child elements got with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; if the parent element has namespaces.&lt;/p&gt;
&lt;h3 id="Stripping namespaces altogether"&gt;Stripping namespaces altogether&lt;/h3&gt;
&lt;p&gt;Because namespaces often add unnecessary complexity, &lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; supports stripping them altogether by using &lt;code&gt;strip_namespaces=True&lt;/code&gt;. When this option is enabled, namespaces are not shown anywhere nor are they included if XML is saved.&lt;/p&gt;
&lt;h3 id="Attribute namespaces"&gt;Attribute namespaces&lt;/h3&gt;
&lt;p&gt;Attributes in XML documents are, by default, in the same namespaces as the element they belong to. It is possible to use different namespaces by using prefixes, but this is pretty rare.&lt;/p&gt;
&lt;p&gt;If an attribute has a namespace prefix, ElementTree will replace it with Clark Notation the same way it handles elements. Because stripping namespaces from attributes could cause attribute conflicts, this library does not handle attribute namespaces at all. Thus the following example works the same way regardless how namespaces are handled.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${root} =&lt;/td&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;&amp;lt;root id="1" ns:id="2" xmlns:ns="http://my.ns"/&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${root}&lt;/td&gt;
&lt;td&gt;{&lt;a href="http://my.ns}id"&gt;http://my.ns}id&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Boolean arguments"&gt;Boolean arguments&lt;/h2&gt;
&lt;p&gt;Some keywords accept arguments that are handled as Boolean values true or false. If such an argument is given as a string, it is considered false if it is an empty string or equal to &lt;code&gt;FALSE&lt;/code&gt;, &lt;code&gt;NONE&lt;/code&gt;, &lt;code&gt;NO&lt;/code&gt;, &lt;code&gt;OFF&lt;/code&gt; or &lt;code&gt;0&lt;/code&gt;, case-insensitively. Other strings are considered true regardless their value, and other argument types are tested using the same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;True examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=True&lt;/td&gt;
&lt;td&gt;# Strings are generally true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=yes&lt;/td&gt;
&lt;td&gt;# Same as the above.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=${TRUE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;True&lt;/code&gt; is true.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=${42}&lt;/td&gt;
&lt;td&gt;# Numbers other than 0 are true.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;False examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=False&lt;/td&gt;
&lt;td&gt;# String &lt;code&gt;false&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=no&lt;/td&gt;
&lt;td&gt;# Also string &lt;code&gt;no&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=${EMPTY}&lt;/td&gt;
&lt;td&gt;# Empty string is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt;&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;keep_clark_notation=${FALSE}&lt;/td&gt;
&lt;td&gt;# Python &lt;code&gt;False&lt;/code&gt; is false.&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Considering &lt;code&gt;OFF&lt;/code&gt; and &lt;code&gt;0&lt;/code&gt; false is new in Robot Framework 3.1.&lt;/p&gt;
&lt;h3 id="Pattern matching"&gt;Pattern matching&lt;/h3&gt;
&lt;p&gt;Some keywords, for example &lt;a href="#Elements%20Should%20Match" class="name"&gt;Elements Should Match&lt;/a&gt;, support so called &lt;a href="http://en.wikipedia.org/wiki/Glob_(programming)"&gt;glob patterns&lt;/a&gt; where:&lt;/p&gt;
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
&lt;p&gt;Support for brackets like &lt;code&gt;[abc]&lt;/code&gt; and &lt;code&gt;[!a-z]&lt;/code&gt; is new in Robot Framework 3.1&lt;/p&gt;</doc>
<tags>
</tags>
<inits>
<init name="Init" lineno="452">
<arguments repr="use_lxml=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="use_lxml=False">
<name>use_lxml</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Import library with optionally lxml mode enabled.&lt;/p&gt;
&lt;p&gt;By default this library uses Python's standard &lt;a href="http://docs.python.org/library/xml.etree.elementtree.html"&gt;ElementTree&lt;/a&gt; module for parsing XML. If &lt;code&gt;use_lxml&lt;/code&gt; argument is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), the library will use &lt;a href="http://lxml.de"&gt;lxml&lt;/a&gt; module instead. See &lt;a href="#Using%20lxml" class="name"&gt;Using lxml&lt;/a&gt; section for benefits provided by lxml.&lt;/p&gt;
&lt;p&gt;Using lxml requires that the lxml module is installed on the system. If lxml mode is enabled but the module is not installed, this library will emit a warning and revert back to using the standard ElementTree.&lt;/p&gt;</doc>
<shortdoc>Import library with optionally lxml mode enabled.</shortdoc>
</init>
</inits>
<keywords>
<kw name="Add Element" lineno="1114">
<arguments repr="source, element, index=None, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="element">
<name>element</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="index=None">
<name>index</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Adds a child element to the specified element.&lt;/p&gt;
&lt;p&gt;The element to whom to add the new element is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;element&lt;/code&gt; to add can be specified as a path to an XML file or as a string containing XML, or it can be an already parsed XML element. The element is copied before adding so modifying either the original or the added element has no effect on the other . The element is added as the last child by default, but a custom index can be used to alter the position. Indices start from zero (0 = first position, 1 = second position, etc.), and negative numbers refer to positions at the end (-1 = second last position, -2 = third last, etc.).&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Add Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&amp;lt;new id="x"&amp;gt;&amp;lt;c1/&amp;gt;&amp;lt;/new&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Add Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&amp;lt;c2/&amp;gt;&lt;/td&gt;
&lt;td&gt;xpath=new&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Add Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&amp;lt;c3/&amp;gt;&lt;/td&gt;
&lt;td&gt;index=1&lt;/td&gt;
&lt;td&gt;xpath=new&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${new} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;new&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${new}&lt;/td&gt;
&lt;td&gt;&amp;lt;new id="x"&amp;gt;&amp;lt;c1/&amp;gt;&amp;lt;c3/&amp;gt;&amp;lt;c2/&amp;gt;&amp;lt;/new&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Remove%20Element" class="name"&gt;Remove Element&lt;/a&gt; or &lt;a href="#Remove%20Elements" class="name"&gt;Remove Elements&lt;/a&gt; to remove elements.&lt;/p&gt;</doc>
<shortdoc>Adds a child element to the specified element.</shortdoc>
</kw>
<kw name="Clear Element" lineno="1224">
<arguments repr="source, xpath=., clear_tail=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="clear_tail=False">
<name>clear_tail</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Clears the contents of the specified element.&lt;/p&gt;
&lt;p&gt;The element to clear is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;Clearing the element means removing its text, attributes, and children. Element's tail text is not removed by default, but that can be changed by giving &lt;code&gt;clear_tail&lt;/code&gt; a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). See &lt;a href="#Element%20attributes" class="name"&gt;Element attributes&lt;/a&gt; section for more information about tail in general.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Clear Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${first} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;&amp;lt;first/&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Clear Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=html/p/b&lt;/td&gt;
&lt;td&gt;clear_tail=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;Text with italics.&lt;/td&gt;
&lt;td&gt;xpath=html/p&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Clear Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&amp;lt;example/&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Remove%20Element" class="name"&gt;Remove Element&lt;/a&gt; to remove the whole element.&lt;/p&gt;</doc>
<shortdoc>Clears the contents of the specified element.</shortdoc>
</kw>
<kw name="Copy Element" lineno="1257">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a copy of the specified element.&lt;/p&gt;
&lt;p&gt;The element to copy is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;If the copy or the original element is modified afterwards, the changes have no effect on the other.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${elem} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${copy1} =&lt;/td&gt;
&lt;td&gt;Copy Element&lt;/td&gt;
&lt;td&gt;${elem}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${copy2} =&lt;/td&gt;
&lt;td&gt;Copy Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Text&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;new text&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Attribute&lt;/td&gt;
&lt;td&gt;${copy1}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;new&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${elem}&lt;/td&gt;
&lt;td&gt;&amp;lt;first id="1"&amp;gt;new text&amp;lt;/first&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${copy1}&lt;/td&gt;
&lt;td&gt;&amp;lt;first id="new"&amp;gt;text&amp;lt;/first&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${copy2}&lt;/td&gt;
&lt;td&gt;&amp;lt;first id="1"&amp;gt;text&amp;lt;/first&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns a copy of the specified element.</shortdoc>
</kw>
<kw name="Element Attribute Should Be" lineno="804">
<arguments repr="source, name, expected, xpath=., message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected">
<name>expected</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the specified attribute is &lt;code&gt;expected&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The element whose attribute is verified is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The keyword passes if the attribute &lt;code&gt;name&lt;/code&gt; of the element is equal to the &lt;code&gt;expected&lt;/code&gt; value, and otherwise it fails. The default error message can be overridden with the &lt;code&gt;message&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;To test that the element does not have a certain attribute, Python &lt;code&gt;None&lt;/code&gt; (i.e. variable &lt;code&gt;${NONE}&lt;/code&gt;) can be used as the expected value. A cleaner alternative is using &lt;a href="#Element%20Should%20Not%20Have%20Attribute" class="name"&gt;Element Should Not Have Attribute&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Element Attribute Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Attribute Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;${NONE}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Element%20Attribute%20Should%20Match" class="name"&gt;Element Attribute Should Match&lt;/a&gt; and &lt;a href="#Get%20Element%20Attribute" class="name"&gt;Get Element Attribute&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Verifies that the specified attribute is ``expected``.</shortdoc>
</kw>
<kw name="Element Attribute Should Match" lineno="829">
<arguments repr="source, name, pattern, xpath=., message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the specified attribute matches &lt;code&gt;expected&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword works exactly like &lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt; except that the expected value can be given as a pattern that the attribute of the element must match.&lt;/p&gt;
&lt;p&gt;Pattern matching is similar as matching files in a shell with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; acting as wildcards. See the &lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt; section for more information.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Element Attribute Should Match&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;?&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Attribute Should Match&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;c*d&lt;/td&gt;
&lt;td&gt;xpath=third/second&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Verifies that the specified attribute matches ``expected``.</shortdoc>
</kw>
<kw name="Element Should Exist" lineno="615">
<arguments repr="source, xpath=., message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that one or more element match the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Arguments &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt; have exactly the same semantics as with &lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt; keyword. Keyword passes if the &lt;code&gt;xpath&lt;/code&gt; matches one or more elements in the &lt;code&gt;source&lt;/code&gt;. The default error message can be overridden with the &lt;code&gt;message&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Element%20Should%20Not%20Exist" class="name"&gt;Element Should Not Exist&lt;/a&gt; as well as &lt;a href="#Get%20Element%20Count" class="name"&gt;Get Element Count&lt;/a&gt; that this keyword uses internally.&lt;/p&gt;</doc>
<shortdoc>Verifies that one or more element match the given ``xpath``.</shortdoc>
</kw>
<kw name="Element Should Not Exist" lineno="630">
<arguments repr="source, xpath=., message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that no element match the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Arguments &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt; have exactly the same semantics as with &lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt; keyword. Keyword fails if the &lt;code&gt;xpath&lt;/code&gt; matches any element in the &lt;code&gt;source&lt;/code&gt;. The default error message can be overridden with the &lt;code&gt;message&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Element%20Should%20Exist" class="name"&gt;Element Should Exist&lt;/a&gt; as well as &lt;a href="#Get%20Element%20Count" class="name"&gt;Get Element Count&lt;/a&gt; that this keyword uses internally.&lt;/p&gt;</doc>
<shortdoc>Verifies that no element match the given ``xpath``.</shortdoc>
</kw>
<kw name="Element Should Not Have Attribute" lineno="850">
<arguments repr="source, name, xpath=., message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the specified element does not have  attribute &lt;code&gt;name&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The element whose attribute is verified is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The keyword fails if the specified element has attribute &lt;code&gt;name&lt;/code&gt;. The default error message can be overridden with the &lt;code&gt;message&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Have Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Have Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Get%20Element%20Attribute" class="name"&gt;Get Element Attribute&lt;/a&gt;, &lt;a href="#Get%20Element%20Attributes" class="name"&gt;Get Element Attributes&lt;/a&gt;, &lt;a href="#Element%20Text%20Should%20Be" class="name"&gt;Element Text Should Be&lt;/a&gt; and &lt;a href="#Element%20Text%20Should%20Match" class="name"&gt;Element Text Should Match&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Verifies that the specified element does not have  attribute ``name``.</shortdoc>
</kw>
<kw name="Element Text Should Be" lineno="714">
<arguments repr="source, expected, xpath=., normalize_whitespace=False, message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected">
<name>expected</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="normalize_whitespace=False">
<name>normalize_whitespace</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the text of the specified element is &lt;code&gt;expected&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The element whose text is verified is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The text to verify is got from the specified element using the same logic as with &lt;a href="#Get%20Element%20Text" class="name"&gt;Get Element Text&lt;/a&gt;. This includes optional whitespace normalization using the &lt;code&gt;normalize_whitespace&lt;/code&gt; option.&lt;/p&gt;
&lt;p&gt;The keyword passes if the text of the element is equal to the &lt;code&gt;expected&lt;/code&gt; value, and otherwise it fails. The default error message can be overridden with the &lt;code&gt;message&lt;/code&gt; argument.  Use &lt;a href="#Element%20Text%20Should%20Match" class="name"&gt;Element Text Should Match&lt;/a&gt; to verify the text against a pattern instead of an exact value.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;text&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;${EMPTY}&lt;/td&gt;
&lt;td&gt;xpath=second/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${paragraph} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=html/p&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${paragraph}&lt;/td&gt;
&lt;td&gt;Text with bold and italics.&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Verifies that the text of the specified element is ``expected``.</shortdoc>
</kw>
<kw name="Element Text Should Match" lineno="741">
<arguments repr="source, pattern, xpath=., normalize_whitespace=False, message=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="pattern">
<name>pattern</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="normalize_whitespace=False">
<name>normalize_whitespace</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="message=None">
<name>message</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the text of the specified element matches &lt;code&gt;expected&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword works exactly like &lt;a href="#Element%20Text%20Should%20Be" class="name"&gt;Element Text Should Be&lt;/a&gt; except that the expected value can be given as a pattern that the text of the element must match.&lt;/p&gt;
&lt;p&gt;Pattern matching is similar as matching files in a shell with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; acting as wildcards. See the &lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt; section for more information.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Match&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;t???&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${paragraph} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=html/p&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Match&lt;/td&gt;
&lt;td&gt;${paragraph}&lt;/td&gt;
&lt;td&gt;Text with * and *.&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Verifies that the text of the specified element matches ``expected``.</shortdoc>
</kw>
<kw name="Element To String" lineno="1278">
<arguments repr="source, xpath=., encoding=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=None">
<name>encoding</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the string representation of the specified element.&lt;/p&gt;
&lt;p&gt;The element to convert to a string is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;By default the string is returned as Unicode. If &lt;code&gt;encoding&lt;/code&gt; argument is given any value, the string is returned as bytes in the specified encoding. The resulting string never contains the XML declaration.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Log%20Element" class="name"&gt;Log Element&lt;/a&gt; and &lt;a href="#Save%20Xml" class="name"&gt;Save XML&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns the string representation of the specified element.</shortdoc>
</kw>
<kw name="Elements Should Be Equal" lineno="872">
<arguments repr="source, expected, exclude_children=False, normalize_whitespace=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected">
<name>expected</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_children=False">
<name>exclude_children</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="normalize_whitespace=False">
<name>normalize_whitespace</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the given &lt;code&gt;source&lt;/code&gt; element is equal to &lt;code&gt;expected&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Both &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;expected&lt;/code&gt; can be given as a path to an XML file, as a string containing XML, or as an already parsed XML element structure. See &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt; for more information about parsing XML in general.&lt;/p&gt;
&lt;p&gt;The keyword passes if the &lt;code&gt;source&lt;/code&gt; element and &lt;code&gt;expected&lt;/code&gt; element are equal. This includes testing the tag names, texts, and attributes of the elements. By default also child elements are verified the same way, but this can be disabled by setting &lt;code&gt;exclude_children&lt;/code&gt; to a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;).&lt;/p&gt;
&lt;p&gt;All texts inside the given elements are verified, but possible text outside them is not. By default texts must match exactly, but setting &lt;code&gt;normalize_whitespace&lt;/code&gt; to a true value makes text verification independent on newlines, tabs, and the amount of spaces. For more details about handling text see &lt;a href="#Get%20Element%20Text" class="name"&gt;Get Element Text&lt;/a&gt; keyword and discussion about elements' &lt;a href="#text" class="name"&gt;text&lt;/a&gt; and &lt;a href="#tail" class="name"&gt;tail&lt;/a&gt; attributes in the &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${first} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;&amp;lt;first id="1"&amp;gt;text&amp;lt;/first&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${p} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;html/p&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${p}&lt;/td&gt;
&lt;td&gt;&amp;lt;p&amp;gt;Text with &amp;lt;b&amp;gt;bold&amp;lt;/b&amp;gt; and &amp;lt;i&amp;gt;italics&amp;lt;/i&amp;gt;.&amp;lt;/p&amp;gt;&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Be Equal&lt;/td&gt;
&lt;td&gt;${p}&lt;/td&gt;
&lt;td&gt;&amp;lt;p&amp;gt;Text with&amp;lt;/p&amp;gt;&lt;/td&gt;
&lt;td&gt;exclude&lt;/td&gt;
&lt;td&gt;normalize&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;The last example may look a bit strange because the &lt;code&gt;&amp;lt;p&amp;gt;&lt;/code&gt; element only has text &lt;code&gt;Text with&lt;/code&gt;. The reason is that rest of the text inside &lt;code&gt;&amp;lt;p&amp;gt;&lt;/code&gt; actually belongs to the child elements. This includes the &lt;code&gt;.&lt;/code&gt; at the end that is the &lt;a href="#tail" class="name"&gt;tail&lt;/a&gt; text of the &lt;code&gt;&amp;lt;i&amp;gt;&lt;/code&gt; element.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Elements%20Should%20Match" class="name"&gt;Elements Should Match&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Verifies that the given ``source`` element is equal to ``expected``.</shortdoc>
</kw>
<kw name="Elements Should Match" lineno="912">
<arguments repr="source, expected, exclude_children=False, normalize_whitespace=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expected">
<name>expected</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_children=False">
<name>exclude_children</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="normalize_whitespace=False">
<name>normalize_whitespace</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Verifies that the given &lt;code&gt;source&lt;/code&gt; element matches &lt;code&gt;expected&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;This keyword works exactly like &lt;a href="#Elements%20Should%20Be%20Equal" class="name"&gt;Elements Should Be Equal&lt;/a&gt; except that texts and attribute values in the expected value can be given as patterns.&lt;/p&gt;
&lt;p&gt;Pattern matching is similar as matching files in a shell with &lt;code&gt;*&lt;/code&gt;, &lt;code&gt;?&lt;/code&gt; and &lt;code&gt;[chars]&lt;/code&gt; acting as wildcards. See the &lt;a href="#Pattern%20matching" class="name"&gt;Pattern matching&lt;/a&gt; section for more information.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${first} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Elements Should Match&lt;/td&gt;
&lt;td&gt;${first}&lt;/td&gt;
&lt;td&gt;&amp;lt;first id="?"&amp;gt;*&amp;lt;/first&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See &lt;a href="#Elements%20Should%20Be%20Equal" class="name"&gt;Elements Should Be Equal&lt;/a&gt; for more examples.&lt;/p&gt;</doc>
<shortdoc>Verifies that the given ``source`` element matches ``expected``.</shortdoc>
</kw>
<kw name="Evaluate Xpath" lineno="1351">
<arguments repr="source, expression, context=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="expression">
<name>expression</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="context=.">
<name>context</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Evaluates the given xpath expression and returns results.&lt;/p&gt;
&lt;p&gt;The element in which context the expression is executed is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;context&lt;/code&gt; arguments. They have exactly the same semantics as &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt; arguments have with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The xpath expression to evaluate is given as &lt;code&gt;expression&lt;/code&gt; argument. The result of the evaluation is returned as-is.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${count} =&lt;/td&gt;
&lt;td&gt;Evaluate Xpath&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;count(third/*)&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${count}&lt;/td&gt;
&lt;td&gt;${3}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${text} =&lt;/td&gt;
&lt;td&gt;Evaluate Xpath&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;string(descendant::second[last()]/@id)&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${text}&lt;/td&gt;
&lt;td&gt;child&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${bold} =&lt;/td&gt;
&lt;td&gt;Evaluate Xpath&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;boolean(preceding-sibling::*[1] = 'bold')&lt;/td&gt;
&lt;td&gt;context=html/p/i&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${bold}&lt;/td&gt;
&lt;td&gt;${True}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;This keyword works only if lxml mode is taken into use when &lt;a href="#Importing" class="name"&gt;importing&lt;/a&gt; the library.&lt;/p&gt;</doc>
<shortdoc>Evaluates the given xpath expression and returns results.</shortdoc>
</kw>
<kw name="Get Child Elements" lineno="585">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the child elements of the specified element as a list.&lt;/p&gt;
&lt;p&gt;The element whose children to return is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;All the direct child elements of the specified element are returned. If the element has no children, an empty list is returned.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${children} =&lt;/td&gt;
&lt;td&gt;Get Child Elements&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Length Should Be&lt;/td&gt;
&lt;td&gt;${children}&lt;/td&gt;
&lt;td&gt;4&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${children} =&lt;/td&gt;
&lt;td&gt;Get Child Elements&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Empty&lt;/td&gt;
&lt;td&gt;${children}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns the child elements of the specified element as a list.</shortdoc>
</kw>
<kw name="Get Element" lineno="520">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns an element in the &lt;code&gt;source&lt;/code&gt; matching the &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;source&lt;/code&gt; can be a path to an XML file, a string containing XML, or an already parsed XML element. The &lt;code&gt;xpath&lt;/code&gt; specifies which element to find. See the &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt; for more details about both the possible sources and the supported xpath syntax.&lt;/p&gt;
&lt;p&gt;The keyword fails if more, or less, than one element matches the &lt;code&gt;xpath&lt;/code&gt;. Use &lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt; if you want all matching elements to be returned.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${element} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${child} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${element}&lt;/td&gt;
&lt;td&gt;child&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;&lt;a href="#Parse%20Xml" class="name"&gt;Parse XML&lt;/a&gt; is recommended for parsing XML when the whole structure is needed. It must be used if there is a need to configure how XML namespaces are handled.&lt;/p&gt;
&lt;p&gt;Many other keywords use this keyword internally, and keywords modifying XML are typically documented to both to modify the given source and to return it. Modifying the source does not apply if the source is given as a string. The XML structure parsed based on the string and then modified is nevertheless returned.&lt;/p&gt;</doc>
<shortdoc>Returns an element in the ``source`` matching the ``xpath``.</shortdoc>
</kw>
<kw name="Get Element Attribute" lineno="762">
<arguments repr="source, name, xpath=., default=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="default=None">
<name>default</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns the named attribute of the specified element.&lt;/p&gt;
&lt;p&gt;The element whose attribute to return is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The value of the attribute &lt;code&gt;name&lt;/code&gt; of the specified element is returned. If the element does not have such element, the &lt;code&gt;default&lt;/code&gt; value is returned instead.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${attribute} =&lt;/td&gt;
&lt;td&gt;Get Element Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${attribute}&lt;/td&gt;
&lt;td&gt;1&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${attribute} =&lt;/td&gt;
&lt;td&gt;Get Element Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xx&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;default=value&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${attribute}&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Get%20Element%20Attributes" class="name"&gt;Get Element Attributes&lt;/a&gt;, &lt;a href="#Element%20Attribute%20Should%20Be" class="name"&gt;Element Attribute Should Be&lt;/a&gt;, &lt;a href="#Element%20Attribute%20Should%20Match" class="name"&gt;Element Attribute Should Match&lt;/a&gt; and &lt;a href="#Element%20Should%20Not%20Have%20Attribute" class="name"&gt;Element Should Not Have Attribute&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns the named attribute of the specified element.</shortdoc>
</kw>
<kw name="Get Element Attributes" lineno="784">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns all attributes of the specified element.&lt;/p&gt;
&lt;p&gt;The element whose attributes to return is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;Attributes are returned as a Python dictionary. It is a copy of the original attributes so modifying it has no effect on the XML structure.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${attributes} =&lt;/td&gt;
&lt;td&gt;Get Element Attributes&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Dictionary Should Contain Key&lt;/td&gt;
&lt;td&gt;${attributes}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${attributes} =&lt;/td&gt;
&lt;td&gt;Get Element Attributes&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;third&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Empty&lt;/td&gt;
&lt;td&gt;${attributes}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Get%20Element%20Attribute" class="name"&gt;Get Element Attribute&lt;/a&gt; to get the value of a single attribute.&lt;/p&gt;</doc>
<shortdoc>Returns all attributes of the specified element.</shortdoc>
</kw>
<kw name="Get Element Count" lineno="603">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns and logs how many elements the given &lt;code&gt;xpath&lt;/code&gt; matches.&lt;/p&gt;
&lt;p&gt;Arguments &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt; have exactly the same semantics as with &lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt; keyword that this keyword uses internally.&lt;/p&gt;
&lt;p&gt;See also &lt;a href="#Element%20Should%20Exist" class="name"&gt;Element Should Exist&lt;/a&gt; and &lt;a href="#Element%20Should%20Not%20Exist" class="name"&gt;Element Should Not Exist&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns and logs how many elements the given ``xpath`` matches.</shortdoc>
</kw>
<kw name="Get Element Text" lineno="645">
<arguments repr="source, xpath=., normalize_whitespace=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="normalize_whitespace=False">
<name>normalize_whitespace</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns all text of the element, possibly whitespace normalized.&lt;/p&gt;
&lt;p&gt;The element whose text to return is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;This keyword returns all the text of the specified element, including all the text its children and grandchildren contain. If the element has no text, an empty string is returned. The returned text is thus not always the same as the &lt;a href="#text" class="name"&gt;text&lt;/a&gt; attribute of the element.&lt;/p&gt;
&lt;p&gt;By default all whitespace, including newlines and indentation, inside the element is returned as-is. If &lt;code&gt;normalize_whitespace&lt;/code&gt; is given a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;), then leading and trailing whitespace is stripped, newlines and tabs converted to spaces, and multiple spaces collapsed into one. This is especially useful when dealing with HTML data.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${text} =&lt;/td&gt;
&lt;td&gt;Get Element Text&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${text}&lt;/td&gt;
&lt;td&gt;text&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${text} =&lt;/td&gt;
&lt;td&gt;Get Element Text&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Empty&lt;/td&gt;
&lt;td&gt;${text}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${paragraph} =&lt;/td&gt;
&lt;td&gt;Get Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;html/p&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${text} =&lt;/td&gt;
&lt;td&gt;Get Element Text&lt;/td&gt;
&lt;td&gt;${paragraph}&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${text}&lt;/td&gt;
&lt;td&gt;Text with bold and italics.&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;See also &lt;a href="#Get%20Elements%20Texts" class="name"&gt;Get Elements Texts&lt;/a&gt;, &lt;a href="#Element%20Text%20Should%20Be" class="name"&gt;Element Text Should Be&lt;/a&gt; and &lt;a href="#Element%20Text%20Should%20Match" class="name"&gt;Element Text Should Match&lt;/a&gt;.&lt;/p&gt;</doc>
<shortdoc>Returns all text of the element, possibly whitespace normalized.</shortdoc>
</kw>
<kw name="Get Elements" lineno="563">
<arguments repr="source, xpath">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="xpath">
<name>xpath</name>
</arg>
</arguments>
<doc>&lt;p&gt;Returns a list of elements in the &lt;code&gt;source&lt;/code&gt; matching the &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;source&lt;/code&gt; can be a path to an XML file, a string containing XML, or an already parsed XML element. The &lt;code&gt;xpath&lt;/code&gt; specifies which element to find. See the &lt;a href="#Introduction" class="name"&gt;introduction&lt;/a&gt; for more details.&lt;/p&gt;
&lt;p&gt;Elements matching the &lt;code&gt;xpath&lt;/code&gt; are returned as a list. If no elements match, an empty list is returned. Use &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; if you want to get exactly one match.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${children} =&lt;/td&gt;
&lt;td&gt;Get Elements&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;third/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Length Should Be&lt;/td&gt;
&lt;td&gt;${children}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${children} =&lt;/td&gt;
&lt;td&gt;Get Elements&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;first/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Empty&lt;/td&gt;
&lt;td&gt;${children}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns a list of elements in the ``source`` matching the ``xpath``.</shortdoc>
</kw>
<kw name="Get Elements Texts" lineno="694">
<arguments repr="source, xpath, normalize_whitespace=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="xpath">
<name>xpath</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="normalize_whitespace=False">
<name>normalize_whitespace</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns text of all elements matching &lt;code&gt;xpath&lt;/code&gt; as a list.&lt;/p&gt;
&lt;p&gt;The elements whose text to return is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The text of the matched elements is returned using the same logic as with &lt;a href="#Get%20Element%20Text" class="name"&gt;Get Element Text&lt;/a&gt;. This includes optional whitespace normalization using the &lt;code&gt;normalize_whitespace&lt;/code&gt; option.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;@{texts} =&lt;/td&gt;
&lt;td&gt;Get Elements Texts&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;third/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Length Should Be&lt;/td&gt;
&lt;td&gt;${texts}&lt;/td&gt;
&lt;td&gt;2&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;@{texts}[0]&lt;/td&gt;
&lt;td&gt;more text&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;@{texts}[1]&lt;/td&gt;
&lt;td&gt;${EMPTY}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns text of all elements matching ``xpath`` as a list.</shortdoc>
</kw>
<kw name="Log Element" lineno="1298">
<arguments repr="source, level=INFO, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="level=INFO">
<name>level</name>
<default>INFO</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Logs the string representation of the specified element.&lt;/p&gt;
&lt;p&gt;The element specified with &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt; is first converted into a string using &lt;a href="#Element%20To%20String" class="name"&gt;Element To String&lt;/a&gt; keyword internally. The resulting string is then logged using the given &lt;code&gt;level&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The logged string is also returned.&lt;/p&gt;</doc>
<shortdoc>Logs the string representation of the specified element.</shortdoc>
</kw>
<kw name="Parse Xml" lineno="479">
<arguments repr="source, keep_clark_notation=False, strip_namespaces=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="keep_clark_notation=False">
<name>keep_clark_notation</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="strip_namespaces=False">
<name>strip_namespaces</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Parses the given XML file or string into an element structure.&lt;/p&gt;
&lt;p&gt;The &lt;code&gt;source&lt;/code&gt; can either be a path to an XML file or a string containing XML. In both cases the XML is parsed into ElementTree &lt;a href="http://docs.python.org/library/xml.etree.elementtree.html#element-objects"&gt;element structure&lt;/a&gt; and the root element is returned. Possible comments and processing instructions in the source XML are removed.&lt;/p&gt;
&lt;p&gt;As discussed in &lt;a href="#Handling%20XML%20namespaces" class="name"&gt;Handling XML namespaces&lt;/a&gt; section, this keyword, by default, removes namespace information ElementTree has added to tag names and moves it into &lt;code&gt;xmlns&lt;/code&gt; attributes. This typically eases handling XML documents with namespaces considerably. If you do not want that to happen, or want to avoid the small overhead of going through the element structure when your XML does not have namespaces, you can disable this feature by giving &lt;code&gt;keep_clark_notation&lt;/code&gt; argument a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;).&lt;/p&gt;
&lt;p&gt;If you want to strip namespace information altogether so that it is not included even if XML is saved, you can give a true value to &lt;code&gt;strip_namespaces&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${root} =&lt;/td&gt;
&lt;td&gt;Parse XML&lt;/td&gt;
&lt;td&gt;&amp;lt;root&amp;gt;&amp;lt;child/&amp;gt;&amp;lt;/root&amp;gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${xml} =&lt;/td&gt;
&lt;td&gt;Parse XML&lt;/td&gt;
&lt;td&gt;${CURDIR}/test.xml&lt;/td&gt;
&lt;td&gt;keep_clark_notation=True&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${xml} =&lt;/td&gt;
&lt;td&gt;Parse XML&lt;/td&gt;
&lt;td&gt;${CURDIR}/test.xml&lt;/td&gt;
&lt;td&gt;strip_namespaces=True&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Use &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword if you want to get a certain element and not the whole structure. See &lt;a href="#Parsing%20XML" class="name"&gt;Parsing XML&lt;/a&gt; section for more details and examples.&lt;/p&gt;</doc>
<shortdoc>Parses the given XML file or string into an element structure.</shortdoc>
</kw>
<kw name="Remove Element" lineno="1150">
<arguments repr="source, xpath=, remove_tail=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=">
<name>xpath</name>
<default/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="remove_tail=False">
<name>remove_tail</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes the element matching &lt;code&gt;xpath&lt;/code&gt; from the &lt;code&gt;source&lt;/code&gt; structure.&lt;/p&gt;
&lt;p&gt;The element to remove from the &lt;code&gt;source&lt;/code&gt; is specified with &lt;code&gt;xpath&lt;/code&gt; using the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;The keyword fails if &lt;code&gt;xpath&lt;/code&gt; does not match exactly one element. Use &lt;a href="#Remove%20Elements" class="name"&gt;Remove Elements&lt;/a&gt; to remove all matched elements.&lt;/p&gt;
&lt;p&gt;Element's tail text is not removed by default, but that can be changed by giving &lt;code&gt;remove_tail&lt;/code&gt; a true value (see &lt;a href="#Boolean%20arguments" class="name"&gt;Boolean arguments&lt;/a&gt;). See &lt;a href="#Element%20attributes" class="name"&gt;Element attributes&lt;/a&gt; section for more information about &lt;a href="#tail" class="name"&gt;tail&lt;/a&gt; in general.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=second&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Exist&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=second&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Remove Element&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=html/p/b&lt;/td&gt;
&lt;td&gt;remove_tail=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;Text with italics.&lt;/td&gt;
&lt;td&gt;xpath=html/p&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Removes the element matching ``xpath`` from the ``source`` structure.</shortdoc>
</kw>
<kw name="Remove Element Attribute" lineno="1049">
<arguments repr="source, name, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes attribute &lt;code&gt;name&lt;/code&gt; from the specified element.&lt;/p&gt;
&lt;p&gt;The element whose attribute to remove is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;It is not a failure to remove a non-existing attribute. Use &lt;a href="#Remove%20Element%20Attributes" class="name"&gt;Remove Element Attributes&lt;/a&gt; to remove all attributes and &lt;a href="#Set%20Element%20Attribute" class="name"&gt;Set Element Attribute&lt;/a&gt; to set them.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Element Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Have Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Can only remove an attribute from a single element. Use &lt;a href="#Remove%20Elements%20Attribute" class="name"&gt;Remove Elements Attribute&lt;/a&gt; to remove an attribute of multiple elements in one call.&lt;/p&gt;</doc>
<shortdoc>Removes attribute ``name`` from the specified element.</shortdoc>
</kw>
<kw name="Remove Element Attributes" lineno="1083">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes all attributes from the specified element.&lt;/p&gt;
&lt;p&gt;The element whose attributes to remove is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;Use &lt;a href="#Remove%20Element%20Attribute" class="name"&gt;Remove Element Attribute&lt;/a&gt; to remove a single attribute and &lt;a href="#Set%20Element%20Attribute" class="name"&gt;Set Element Attribute&lt;/a&gt; to set them.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Element Attributes&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Have Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Can only remove attributes from a single element. Use &lt;a href="#Remove%20Elements%20Attributes" class="name"&gt;Remove Elements Attributes&lt;/a&gt; to remove all attributes of multiple elements in one call.&lt;/p&gt;</doc>
<shortdoc>Removes all attributes from the specified element.</shortdoc>
</kw>
<kw name="Remove Elements" lineno="1176">
<arguments repr="source, xpath=, remove_tail=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=">
<name>xpath</name>
<default/>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="remove_tail=False">
<name>remove_tail</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes all elements matching &lt;code&gt;xpath&lt;/code&gt; from the &lt;code&gt;source&lt;/code&gt; structure.&lt;/p&gt;
&lt;p&gt;The elements to remove from the &lt;code&gt;source&lt;/code&gt; are specified with &lt;code&gt;xpath&lt;/code&gt; using the same semantics as with &lt;a href="#Get%20Elements" class="name"&gt;Get Elements&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;It is not a failure if &lt;code&gt;xpath&lt;/code&gt; matches no elements. Use &lt;a href="#Remove%20Element" class="name"&gt;Remove Element&lt;/a&gt; to remove exactly one element.&lt;/p&gt;
&lt;p&gt;Element's tail text is not removed by default, but that can be changed by using &lt;code&gt;remove_tail&lt;/code&gt; argument similarly as with &lt;a href="#Remove%20Element" class="name"&gt;Remove Element&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Remove Elements&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=*/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Exist&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=second/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Exist&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xpath=third/child&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Removes all elements matching ``xpath`` from the ``source`` structure.</shortdoc>
</kw>
<kw name="Remove Elements Attribute" lineno="1074">
<arguments repr="source, name, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes attribute &lt;code&gt;name&lt;/code&gt; from the specified elements.&lt;/p&gt;
&lt;p&gt;Like &lt;a href="#Remove%20Element%20Attribute" class="name"&gt;Remove Element Attribute&lt;/a&gt; but removes the attribute of all elements matching the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Removes attribute ``name`` from the specified elements.</shortdoc>
</kw>
<kw name="Remove Elements Attributes" lineno="1105">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Removes all attributes from the specified elements.&lt;/p&gt;
&lt;p&gt;Like &lt;a href="#Remove%20Element%20Attributes" class="name"&gt;Remove Element Attributes&lt;/a&gt; but removes all attributes of all elements matching the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Removes all attributes from the specified elements.</shortdoc>
</kw>
<kw name="Save Xml" lineno="1311">
<arguments repr="source, path, encoding=UTF-8">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="path">
<name>path</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="encoding=UTF-8">
<name>encoding</name>
<default>UTF-8</default>
</arg>
</arguments>
<doc>&lt;p&gt;Saves the given element to the specified file.&lt;/p&gt;
&lt;p&gt;The element to save is specified with &lt;code&gt;source&lt;/code&gt; using the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword.&lt;/p&gt;
&lt;p&gt;The file where the element is saved is denoted with &lt;code&gt;path&lt;/code&gt; and the encoding to use with &lt;code&gt;encoding&lt;/code&gt;. The resulting file always contains the XML declaration.&lt;/p&gt;
&lt;p&gt;The resulting XML file may not be exactly the same as the original:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Comments and processing instructions are always stripped.&lt;/li&gt;
&lt;li&gt;Possible doctype and namespace prefixes are only preserved when &lt;a href="#Using%20lxml" class="name"&gt;using lxml&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;Other small differences are possible depending on the ElementTree or lxml version.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Use &lt;a href="#Element%20To%20String" class="name"&gt;Element To String&lt;/a&gt; if you just need a string representation of the element.&lt;/p&gt;</doc>
<shortdoc>Saves the given element to the specified file.</shortdoc>
</kw>
<kw name="Set Element Attribute" lineno="1013">
<arguments repr="source, name, value, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets attribute &lt;code&gt;name&lt;/code&gt; of the specified element to &lt;code&gt;value&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;The element whose attribute to set is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;It is possible to both set new attributes and to overwrite existing. Use &lt;a href="#Remove%20Element%20Attribute" class="name"&gt;Remove Element Attribute&lt;/a&gt; or &lt;a href="#Remove%20Element%20Attributes" class="name"&gt;Remove Element Attributes&lt;/a&gt; for removing them.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;attr&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Attribute Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;attr&lt;/td&gt;
&lt;td&gt;value&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Attribute&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;new&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Attribute Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;id&lt;/td&gt;
&lt;td&gt;new&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Can only set an attribute of a single element. Use &lt;a href="#Set%20Elements%20Attribute" class="name"&gt;Set Elements Attribute&lt;/a&gt; to set an attribute of multiple elements in one call.&lt;/p&gt;</doc>
<shortdoc>Sets attribute ``name`` of the specified element to ``value``.</shortdoc>
</kw>
<kw name="Set Element Tag" lineno="940">
<arguments repr="source, tag, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="tag">
<name>tag</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the tag of the specified element.&lt;/p&gt;
&lt;p&gt;The element whose tag to set is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Tag&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;newTag&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${XML.tag}&lt;/td&gt;
&lt;td&gt;newTag&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Tag&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;xxx&lt;/td&gt;
&lt;td&gt;xpath=second/child&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Exist&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second/xxx&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Should Not Exist&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;second/child&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Can only set the tag of a single element. Use &lt;a href="#Set%20Elements%20Tag" class="name"&gt;Set Elements Tag&lt;/a&gt; to set the tag of multiple elements in one call.&lt;/p&gt;</doc>
<shortdoc>Sets the tag of the specified element.</shortdoc>
</kw>
<kw name="Set Element Text" lineno="972">
<arguments repr="source, text=None, tail=None, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="text=None">
<name>text</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="tail=None">
<name>tail</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets text and/or tail text of the specified element.&lt;/p&gt;
&lt;p&gt;The element whose text to set is specified using &lt;code&gt;source&lt;/code&gt; and &lt;code&gt;xpath&lt;/code&gt;. They have exactly the same semantics as with &lt;a href="#Get%20Element" class="name"&gt;Get Element&lt;/a&gt; keyword. The resulting XML structure is returned, and if the &lt;code&gt;source&lt;/code&gt; is an already parsed XML structure, it is also modified in place.&lt;/p&gt;
&lt;p&gt;Element's text and tail text are changed only if new &lt;code&gt;text&lt;/code&gt; and/or &lt;code&gt;tail&lt;/code&gt; values are given. See &lt;a href="#Element%20attributes" class="name"&gt;Element attributes&lt;/a&gt; section for more information about &lt;a href="#text" class="name"&gt;text&lt;/a&gt; and &lt;a href="#tail" class="name"&gt;tail&lt;/a&gt; in general.&lt;/p&gt;
&lt;p&gt;Examples using &lt;code&gt;${XML}&lt;/code&gt; structure from &lt;a href="#Example" class="name"&gt;Example&lt;/a&gt;:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Text&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;new text&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;new text&lt;/td&gt;
&lt;td&gt;xpath=first&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Text&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;tail=&amp;amp;&lt;/td&gt;
&lt;td&gt;xpath=html/p/b&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;Text with bold&amp;amp;italics.&lt;/td&gt;
&lt;td&gt;xpath=html/p&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Set Element Text&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;slanted&lt;/td&gt;
&lt;td&gt;!!&lt;/td&gt;
&lt;td&gt;xpath=html/p/i&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Element Text Should Be&lt;/td&gt;
&lt;td&gt;${XML}&lt;/td&gt;
&lt;td&gt;Text with bold&amp;amp;slanted!!&lt;/td&gt;
&lt;td&gt;xpath=html/p&lt;/td&gt;
&lt;td&gt;normalize_whitespace=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;p&gt;Can only set the text/tail of a single element. Use &lt;a href="#Set%20Elements%20Text" class="name"&gt;Set Elements Text&lt;/a&gt; to set the text/tail of multiple elements in one call.&lt;/p&gt;</doc>
<shortdoc>Sets text and/or tail text of the specified element.</shortdoc>
</kw>
<kw name="Set Elements Attribute" lineno="1040">
<arguments repr="source, name, value, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="name">
<name>name</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="value">
<name>value</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets attribute &lt;code&gt;name&lt;/code&gt; of the specified elements to &lt;code&gt;value&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;Like &lt;a href="#Set%20Element%20Attribute" class="name"&gt;Set Element Attribute&lt;/a&gt; but sets the attribute of all elements matching the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Sets attribute ``name`` of the specified elements to ``value``.</shortdoc>
</kw>
<kw name="Set Elements Tag" lineno="962">
<arguments repr="source, tag, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="tag">
<name>tag</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets the tag of the specified elements.&lt;/p&gt;
&lt;p&gt;Like &lt;a href="#Set%20Element%20Tag" class="name"&gt;Set Element Tag&lt;/a&gt; but sets the tag of all elements matching the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Sets the tag of the specified elements.</shortdoc>
</kw>
<kw name="Set Elements Text" lineno="1004">
<arguments repr="source, text=None, tail=None, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="text=None">
<name>text</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="tail=None">
<name>tail</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>&lt;p&gt;Sets text and/or tail text of the specified elements.&lt;/p&gt;
&lt;p&gt;Like &lt;a href="#Set%20Element%20Text" class="name"&gt;Set Element Text&lt;/a&gt; but sets the text or tail of all elements matching the given &lt;code&gt;xpath&lt;/code&gt;.&lt;/p&gt;</doc>
<shortdoc>Sets text and/or tail text of the specified elements.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
</keywordspec>
