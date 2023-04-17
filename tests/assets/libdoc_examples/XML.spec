<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="XML" type="LIBRARY" format="ROBOT" scope="GLOBAL" generated="2023-04-17T12:52:22+00:00" specversion="4" source="/home/kali/Code/rfdocsindexer/.venv/lib/python3.10/site-packages/robot/libraries/XML.py" lineno="46">
<version>6.0.2</version>
<doc>Robot Framework library for verifying and modifying XML documents.

As the name implies, _XML_ is a library for verifying contents of XML files.
In practice, it is a pretty thin wrapper on top of Python's
[http://docs.python.org/library/xml.etree.elementtree.html|ElementTree XML API].

The library has the following main usages:

- Parsing an XML file, or a string containing XML, into an XML element
  structure and finding certain elements from it for for further analysis
  (e.g. `Parse XML` and `Get Element` keywords).
- Getting text or attributes of elements
  (e.g. `Get Element Text` and `Get Element Attribute`).
- Directly verifying text, attributes, or whole elements
  (e.g `Element Text Should Be` and `Elements Should Be Equal`).
- Modifying XML and saving it (e.g. `Set Element Text`, `Add Element`
  and `Save XML`).

== Table of contents ==

- `Parsing XML`
- `Using lxml`
- `Example`
- `Finding elements with xpath`
- `Element attributes`
- `Handling XML namespaces`
- `Boolean arguments`
- `Importing`
- `Keywords`

= Parsing XML =

XML can be parsed into an element structure using `Parse XML` keyword.
The XML to be parsed can be specified using a path to an XML file or as
a string or bytes that contain XML directly. The keyword returns the root
element of the structure, which then contains other elements as its
children and their children. Possible comments and processing instructions
in the source XML are removed.

XML is not validated during parsing even if has a schema defined. How
possible doctype elements are handled otherwise depends on the used XML
module and on the platform. The standard ElementTree strips doctypes
altogether but when `using lxml` they are preserved when XML is saved.

The element structure returned by `Parse XML`, as well as elements
returned by keywords such as `Get Element`, can be used as the ``source``
argument with other keywords. In addition to an already parsed XML
structure, other keywords also accept paths to XML files and strings
containing XML similarly as `Parse XML`. Notice that keywords that modify
XML do not write those changes back to disk even if the source would be
given as a path to a file. Changes must always be saved explicitly using
`Save XML` keyword.

When the source is given as a path to a file, the forward slash character
(``/``) can be used as the path separator regardless the operating system.
On Windows also the backslash works, but in the data it needs to be
escaped by doubling it (``\\``). Using the built-in variable ``${/}``
naturally works too.

Note: Support for XML as bytes is new in Robot Framework 3.2.

= Using lxml =

By default, this library uses Python's standard
[http://docs.python.org/library/xml.etree.elementtree.html|ElementTree]
module for parsing XML, but it can be configured to use
[http://lxml.de|lxml] module instead when `importing` the library.
The resulting element structure has same API regardless which module
is used for parsing.

The main benefits of using lxml is that it supports richer xpath syntax
than the standard ElementTree and enables using `Evaluate Xpath` keyword.
It also preserves the doctype and possible namespace prefixes saving XML.

= Example =

The following simple example demonstrates parsing XML and verifying its
contents both using keywords in this library and in _BuiltIn_ and
_Collections_ libraries. How to use xpath expressions to find elements
and what attributes the returned elements contain are discussed, with
more examples, in `Finding elements with xpath` and `Element attributes`
sections.

In this example, as well as in many other examples in this documentation,
``${XML}`` refers to the following example XML document. In practice
``${XML}`` could either be a path to an XML file or it could contain the XML
itself.

| &lt;example&gt;
|   &lt;first id="1"&gt;text&lt;/first&gt;
|   &lt;second id="2"&gt;
|     &lt;child/&gt;
|   &lt;/second&gt;
|   &lt;third&gt;
|     &lt;child&gt;more text&lt;/child&gt;
|     &lt;second id="child"/&gt;
|     &lt;child&gt;&lt;grandchild/&gt;&lt;/child&gt;
|   &lt;/third&gt;
|   &lt;html&gt;
|     &lt;p&gt;
|       Text with &lt;b&gt;bold&lt;/b&gt; and &lt;i&gt;italics&lt;/i&gt;.
|     &lt;/p&gt;
|   &lt;/html&gt;
| &lt;/example&gt;

| ${root} =                | `Parse XML`   | ${XML}  |       |             |
| `Should Be Equal`        | ${root.tag}   | example |       |             |
| ${first} =               | `Get Element` | ${root} | first |             |
| `Should Be Equal`        | ${first.text} | text    |       |             |
| `Dictionary Should Contain Key` | ${first.attrib}  | id    |             |
| `Element Text Should Be` | ${first}      | text    |       |             |
| `Element Attribute Should Be` | ${first} | id      | 1     |             |
| `Element Attribute Should Be` | ${root}  | id      | 1     | xpath=first |
| `Element Attribute Should Be` | ${XML}   | id      | 1     | xpath=first |

Notice that in the example three last lines are equivalent. Which one to
use in practice depends on which other elements you need to get or verify.
If you only need to do one verification, using the last line alone would
suffice. If more verifications are needed, parsing the XML with `Parse XML`
only once would be more efficient.

= Finding elements with xpath =

ElementTree, and thus also this library, supports finding elements using
xpath expressions. ElementTree does not, however, support the full xpath
standard. The supported xpath syntax is explained below and
[https://docs.python.org/library/xml.etree.elementtree.html#xpath-support|
ElementTree documentation] provides more details. In the examples
``${XML}`` refers to the same XML structure as in the earlier example.

If lxml support is enabled when `importing` the library, the whole
[http://www.w3.org/TR/xpath/|xpath 1.0 standard] is supported.
That includes everything listed below but also lot of other useful
constructs.

== Tag names ==

When just a single tag name is used, xpath matches all direct child
elements that have that tag name.

| ${elem} =          | `Get Element`  | ${XML}      | third |
| `Should Be Equal`  | ${elem.tag}    | third       |       |
| @{children} =      | `Get Elements` | ${elem}     | child |
| `Length Should Be` | ${children}    | 2           |       |

== Paths ==

Paths are created by combining tag names with a forward slash (``/``). For
example, ``parent/child`` matches all ``child`` elements under ``parent``
element. Notice that if there are multiple ``parent`` elements that all
have ``child`` elements, ``parent/child`` xpath will match all these
``child`` elements.

| ${elem} =         | `Get Element` | ${XML}     | second/child            |
| `Should Be Equal` | ${elem.tag}   | child      |                         |
| ${elem} =         | `Get Element` | ${XML}     | third/child/grandchild  |
| `Should Be Equal` | ${elem.tag}   | grandchild |                         |

== Wildcards ==

An asterisk (``*``) can be used in paths instead of a tag name to denote
any element.

| @{children} =      | `Get Elements` | ${XML} | */child |
| `Length Should Be` | ${children}    | 3      |         |

== Current element ==

The current element is denoted with a dot (``.``). Normally the current
element is implicit and does not need to be included in the xpath.

== Parent element ==

The parent element of another element is denoted with two dots (``..``).
Notice that it is not possible to refer to the parent of the current
element.

| ${elem} =         | `Get Element` | ${XML} | */second/.. |
| `Should Be Equal` | ${elem.tag}   | third  |             |

== Search all sub elements ==

Two forward slashes (``//``) mean that all sub elements, not only the
direct children, are searched. If the search is started from the current
element, an explicit dot is required.

| @{elements} =      | `Get Elements` | ${XML} | .//second |
| `Length Should Be` | ${elements}    | 2      |           |
| ${b} =             | `Get Element`  | ${XML} | html//b   |
| `Should Be Equal`  | ${b.text}      | bold   |           |

== Predicates ==

Predicates allow selecting elements using also other criteria than tag
names, for example, attributes or position. They are specified after the
normal tag name or path using syntax ``path[predicate]``. The path can have
wildcards and other special syntax explained earlier. What predicates
the standard ElementTree supports is explained in the table below.

|  = Predicate =  |             = Matches =           |    = Example =     |
| @attrib         | Elements with attribute ``attrib``. | second[@id]        |
| @attrib="value" | Elements with attribute ``attrib`` having value ``value``. | *[@id="2"] |
| position        | Elements at the specified position. Position can be an integer (starting from 1), expression ``last()``, or relative expression like ``last() - 1``. | third/child[1] |
| tag             | Elements with a child element named ``tag``. | third/child[grandchild] |

Predicates can also be stacked like ``path[predicate1][predicate2]``.
A limitation is that possible position predicate must always be first.

= Element attributes =

All keywords returning elements, such as `Parse XML`, and `Get Element`,
return ElementTree's
[http://docs.python.org/library/xml.etree.elementtree.html#element-objects|Element objects].
These elements can be used as inputs for other keywords, but they also
contain several useful attributes that can be accessed directly using
the extended variable syntax.

The attributes that are both useful and convenient to use in the data
are explained below. Also other attributes, including methods, can
be accessed, but that is typically better to do in custom libraries than
directly in the data.

The examples use the same ``${XML}`` structure as the earlier examples.

== tag ==

The tag of the element.

| ${root} =         | `Parse XML` | ${XML}  |
| `Should Be Equal` | ${root.tag} | example |

== text ==

The text that the element contains or Python ``None`` if the element has no
text. Notice that the text _does not_ contain texts of possible child
elements nor text after or between children. Notice also that in XML
whitespace is significant, so the text contains also possible indentation
and newlines. To get also text of the possible children, optionally
whitespace normalized, use `Get Element Text` keyword.

| ${1st} =          | `Get Element` | ${XML}  | first        |
| `Should Be Equal` | ${1st.text}   | text    |              |
| ${2nd} =          | `Get Element` | ${XML}  | second/child |
| `Should Be Equal` | ${2nd.text}   | ${NONE} |              |
| ${p} =            | `Get Element` | ${XML}  | html/p       |
| `Should Be Equal` | ${p.text}     | \n${SPACE*6}Text with${SPACE} |

== tail ==

The text after the element before the next opening or closing tag. Python
``None`` if the element has no tail. Similarly as with ``text``, also
``tail`` contains possible indentation and newlines.

| ${b} =            | `Get Element` | ${XML}  | html/p/b  |
| `Should Be Equal` | ${b.tail}     | ${SPACE}and${SPACE} |

== attrib ==

A Python dictionary containing attributes of the element.

| ${2nd} =          | `Get Element`       | ${XML} | second |
| `Should Be Equal` | ${2nd.attrib['id']} | 2      |        |
| ${3rd} =          | `Get Element`       | ${XML} | third  |
| `Should Be Empty` | ${3rd.attrib}       |        |        |

= Handling XML namespaces =

ElementTree and lxml handle possible namespaces in XML documents by adding
the namespace URI to tag names in so called Clark Notation. That is
inconvenient especially with xpaths, and by default this library strips
those namespaces away and moves them to ``xmlns`` attribute instead. That
can be avoided by passing ``keep_clark_notation`` argument to `Parse XML`
keyword. Alternatively `Parse XML` supports stripping namespace information
altogether by using ``strip_namespaces`` argument. The pros and cons of
different approaches are discussed in more detail below.

== How ElementTree handles namespaces ==

If an XML document has namespaces, ElementTree adds namespace information
to tag names in [http://www.jclark.com/xml/xmlns.htm|Clark Notation]
(e.g. ``{http://ns.uri}tag``) and removes original ``xmlns`` attributes.
This is done both with default namespaces and with namespaces with a prefix.
How it works in practice is illustrated by the following example, where
``${NS}`` variable contains this XML document:

| &lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
|                 xmlns="http://www.w3.org/1999/xhtml"&gt;
|   &lt;xsl:template match="/"&gt;
|     &lt;html&gt;&lt;/html&gt;
|   &lt;/xsl:template&gt;
| &lt;/xsl:stylesheet&gt;

| ${root} = | `Parse XML` | ${NS} | keep_clark_notation=yes |
| `Should Be Equal` | ${root.tag} | {http://www.w3.org/1999/XSL/Transform}stylesheet |
| `Element Should Exist` | ${root} | {http://www.w3.org/1999/XSL/Transform}template/{http://www.w3.org/1999/xhtml}html |
| `Should Be Empty` | ${root.attrib} |

As you can see, including the namespace URI in tag names makes xpaths
really long and complex.

If you save the XML, ElementTree moves namespace information back to
``xmlns`` attributes. Unfortunately it does not restore the original
prefixes:

| &lt;ns0:stylesheet xmlns:ns0="http://www.w3.org/1999/XSL/Transform"&gt;
|   &lt;ns0:template match="/"&gt;
|     &lt;ns1:html xmlns:ns1="http://www.w3.org/1999/xhtml"&gt;&lt;/ns1:html&gt;
|   &lt;/ns0:template&gt;
| &lt;/ns0:stylesheet&gt;

The resulting output is semantically same as the original, but mangling
prefixes like this may still not be desirable. Notice also that the actual
output depends slightly on ElementTree version.

== Default namespace handling ==

Because the way ElementTree handles namespaces makes xpaths so complicated,
this library, by default, strips namespaces from tag names and moves that
information back to ``xmlns`` attributes. How this works in practice is
shown by the example below, where ``${NS}`` variable contains the same XML
document as in the previous example.

| ${root} = | `Parse XML` | ${NS} |
| `Should Be Equal` | ${root.tag} | stylesheet |
| `Element Should Exist` | ${root} | template/html |
| `Element Attribute Should Be` | ${root} | xmlns | http://www.w3.org/1999/XSL/Transform |
| `Element Attribute Should Be` | ${root} | xmlns | http://www.w3.org/1999/xhtml | xpath=template/html |

Now that tags do not contain namespace information, xpaths are simple again.

A minor limitation of this approach is that namespace prefixes are lost.
As a result the saved output is not exactly same as the original one in
this case either:

| &lt;stylesheet xmlns="http://www.w3.org/1999/XSL/Transform"&gt;
|   &lt;template match="/"&gt;
|     &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;&lt;/html&gt;
|   &lt;/template&gt;
| &lt;/stylesheet&gt;

Also this output is semantically same as the original. If the original XML
had only default namespaces, the output would also look identical.

== Namespaces when using lxml ==

This library handles namespaces same way both when `using lxml` and when
not using it. There are, however, differences how lxml internally handles
namespaces compared to the standard ElementTree. The main difference is
that lxml stores information about namespace prefixes and they are thus
preserved if XML is saved. Another visible difference is that lxml includes
namespace information in child elements got with `Get Element` if the
parent element has namespaces.

== Stripping namespaces altogether ==

Because namespaces often add unnecessary complexity, `Parse XML` supports
stripping them altogether by using ``strip_namespaces=True``. When this
option is enabled, namespaces are not shown anywhere nor are they included
if XML is saved.

== Attribute namespaces ==

Attributes in XML documents are, by default, in the same namespaces as
the element they belong to. It is possible to use different namespaces
by using prefixes, but this is pretty rare.

If an attribute has a namespace prefix, ElementTree will replace it with
Clark Notation the same way it handles elements. Because stripping
namespaces from attributes could cause attribute conflicts, this library
does not handle attribute namespaces at all. Thus the following example
works the same way regardless how namespaces are handled.

| ${root} = | `Parse XML` | &lt;root id="1" ns:id="2" xmlns:ns="http://my.ns"/&gt; |
| `Element Attribute Should Be` | ${root} | id | 1 |
| `Element Attribute Should Be` | ${root} | {http://my.ns}id | 2 |

= Boolean arguments =

Some keywords accept arguments that are handled as Boolean values true or
false. If such an argument is given as a string, it is considered false if
it is an empty string or equal to ``FALSE``, ``NONE``, ``NO``, ``OFF`` or
``0``, case-insensitively. Other strings are considered true regardless
their value, and other argument types are tested using the same
[http://docs.python.org/library/stdtypes.html#truth|rules as in Python].

True examples:
| `Parse XML` | ${XML} | keep_clark_notation=True    | # Strings are generally true.    |
| `Parse XML` | ${XML} | keep_clark_notation=yes     | # Same as the above.             |
| `Parse XML` | ${XML} | keep_clark_notation=${TRUE} | # Python ``True`` is true.       |
| `Parse XML` | ${XML} | keep_clark_notation=${42}   | # Numbers other than 0 are true. |

False examples:
| `Parse XML` | ${XML} | keep_clark_notation=False    | # String ``false`` is false.   |
| `Parse XML` | ${XML} | keep_clark_notation=no       | # Also string ``no`` is false. |
| `Parse XML` | ${XML} | keep_clark_notation=${EMPTY} | # Empty string is false.       |
| `Parse XML` | ${XML} | keep_clark_notation=${FALSE} | # Python ``False`` is false.   |

Considering ``OFF`` and ``0`` false is new in Robot Framework 3.1.

== Pattern matching ==

Some keywords, for example `Elements Should Match`, support so called
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

Support for brackets like ``[abc]`` and ``[!a-z]`` is new in
Robot Framework 3.1</doc>
<tags>
</tags>
<inits>
<init name="__init__" lineno="461">
<arguments repr="use_lxml=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="use_lxml=False">
<name>use_lxml</name>
<default>False</default>
</arg>
</arguments>
<doc>Import library with optionally lxml mode enabled.

By default this library uses Python's standard
[http://docs.python.org/library/xml.etree.elementtree.html|ElementTree]
module for parsing XML. If ``use_lxml`` argument is given a true value
(see `Boolean arguments`), the library will use [http://lxml.de|lxml]
module instead. See `Using lxml` section for benefits provided by lxml.

Using lxml requires that the lxml module is installed on the system.
If lxml mode is enabled but the module is not installed, this library
will emit a warning and revert back to using the standard ElementTree.</doc>
<shortdoc>Import library with optionally lxml mode enabled.</shortdoc>
</init>
</inits>
<keywords>
<kw name="Add Element" lineno="1135">
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
<doc>Adds a child element to the specified element.

The element to whom to add the new element is specified using ``source``
and ``xpath``. They have exactly the same semantics as with `Get Element`
keyword. The resulting XML structure is returned, and if the ``source``
is an already parsed XML structure, it is also modified in place.

The ``element`` to add can be specified as a path to an XML file or
as a string containing XML, or it can be an already parsed XML element.
The element is copied before adding so modifying either the original
or the added element has no effect on the other
.
The element is added as the last child by default, but a custom index
can be used to alter the position. Indices start from zero (0 = first
position, 1 = second position, etc.), and negative numbers refer to
positions at the end (-1 = second last position, -2 = third last, etc.).

Examples using ``${XML}`` structure from `Example`:
| Add Element | ${XML} | &lt;new id="x"&gt;&lt;c1/&gt;&lt;/new&gt; |
| Add Element | ${XML} | &lt;c2/&gt; | xpath=new |
| Add Element | ${XML} | &lt;c3/&gt; | index=1 | xpath=new |
| ${new} = | Get Element | ${XML} | new |
| Elements Should Be Equal | ${new} | &lt;new id="x"&gt;&lt;c1/&gt;&lt;c3/&gt;&lt;c2/&gt;&lt;/new&gt; |

Use `Remove Element` or `Remove Elements` to remove elements.</doc>
<shortdoc>Adds a child element to the specified element.</shortdoc>
</kw>
<kw name="Clear Element" lineno="1244">
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
<doc>Clears the contents of the specified element.

The element to clear is specified using ``source`` and ``xpath``. They
have exactly the same semantics as with `Get Element` keyword.
The resulting XML structure is returned, and if the ``source`` is
an already parsed XML structure, it is also modified in place.

Clearing the element means removing its text, attributes, and children.
Element's tail text is not removed by default, but that can be changed
by giving ``clear_tail`` a true value (see `Boolean arguments`). See
`Element attributes` section for more information about tail in
general.

Examples using ``${XML}`` structure from `Example`:
| Clear Element            | ${XML}   | xpath=first |
| ${first} = | Get Element | ${XML}   | xpath=first |
| Elements Should Be Equal | ${first} | &lt;first/&gt;    |
| Clear Element            | ${XML}   | xpath=html/p/b | clear_tail=yes |
| Element Text Should Be   | ${XML}   | Text with italics. | xpath=html/p | normalize_whitespace=yes |
| Clear Element            | ${XML}   |
| Elements Should Be Equal | ${XML}   | &lt;example/&gt; |

Use `Remove Element` to remove the whole element.</doc>
<shortdoc>Clears the contents of the specified element.</shortdoc>
</kw>
<kw name="Copy Element" lineno="1277">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Returns a copy of the specified element.

The element to copy is specified using ``source`` and ``xpath``. They
have exactly the same semantics as with `Get Element` keyword.

If the copy or the original element is modified afterwards, the changes
have no effect on the other.

Examples using ``${XML}`` structure from `Example`:
| ${elem} =  | Get Element  | ${XML}  | xpath=first |
| ${copy1} = | Copy Element | ${elem} |
| ${copy2} = | Copy Element | ${XML}  | xpath=first |
| Set Element Text         | ${XML}   | new text    | xpath=first      |
| Set Element Attribute    | ${copy1} | id          | new              |
| Elements Should Be Equal | ${elem}  | &lt;first id="1"&gt;new text&lt;/first&gt; |
| Elements Should Be Equal | ${copy1} | &lt;first id="new"&gt;text&lt;/first&gt;   |
| Elements Should Be Equal | ${copy2} | &lt;first id="1"&gt;text&lt;/first&gt;     |</doc>
<shortdoc>Returns a copy of the specified element.</shortdoc>
</kw>
<kw name="Element Attribute Should Be" lineno="815">
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
<doc>Verifies that the specified attribute is ``expected``.

The element whose attribute is verified is specified using ``source``
and ``xpath``. They have exactly the same semantics as with
`Get Element` keyword.

The keyword passes if the attribute ``name`` of the element is equal to
the ``expected`` value, and otherwise it fails. The default error
message can be overridden with the ``message`` argument.

To test that the element does not have a certain attribute, Python
``None`` (i.e. variable ``${NONE}``) can be used as the expected value.
A cleaner alternative is using `Element Should Not Have Attribute`.

Examples using ``${XML}`` structure from `Example`:
| Element Attribute Should Be | ${XML} | id | 1       | xpath=first |
| Element Attribute Should Be | ${XML} | id | ${NONE} |             |

See also `Element Attribute Should Match` and `Get Element Attribute`.</doc>
<shortdoc>Verifies that the specified attribute is ``expected``.</shortdoc>
</kw>
<kw name="Element Attribute Should Match" lineno="840">
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
<doc>Verifies that the specified attribute matches ``expected``.

This keyword works exactly like `Element Attribute Should Be` except
that the expected value can be given as a pattern that the attribute of
the element must match.

Pattern matching is similar as matching files in a shell with
``*``, ``?`` and ``[chars]`` acting as wildcards. See the
`Pattern matching` section for more information.

Examples using ``${XML}`` structure from `Example`:
| Element Attribute Should Match | ${XML} | id | ?   | xpath=first |
| Element Attribute Should Match | ${XML} | id | c*d | xpath=third/second |</doc>
<shortdoc>Verifies that the specified attribute matches ``expected``.</shortdoc>
</kw>
<kw name="Element Should Exist" lineno="626">
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
<doc>Verifies that one or more element match the given ``xpath``.

Arguments ``source`` and ``xpath`` have exactly the same semantics as
with `Get Elements` keyword. Keyword passes if the ``xpath`` matches
one or more elements in the ``source``. The default error message can
be overridden with the ``message`` argument.

See also `Element Should Not Exist` as well as `Get Element Count`
that this keyword uses internally.</doc>
<shortdoc>Verifies that one or more element match the given ``xpath``.</shortdoc>
</kw>
<kw name="Element Should Not Exist" lineno="641">
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
<doc>Verifies that no element match the given ``xpath``.

Arguments ``source`` and ``xpath`` have exactly the same semantics as
with `Get Elements` keyword. Keyword fails if the ``xpath`` matches any
element in the ``source``. The default error message can be overridden
with the ``message`` argument.

See also `Element Should Exist` as well as `Get Element Count`
that this keyword uses internally.</doc>
<shortdoc>Verifies that no element match the given ``xpath``.</shortdoc>
</kw>
<kw name="Element Should Not Have Attribute" lineno="861">
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
<doc>Verifies that the specified element does not have attribute ``name``.

The element whose attribute is verified is specified using ``source``
and ``xpath``. They have exactly the same semantics as with
`Get Element` keyword.

The keyword fails if the specified element has attribute ``name``. The
default error message can be overridden with the ``message`` argument.

Examples using ``${XML}`` structure from `Example`:
| Element Should Not Have Attribute | ${XML} | id  |
| Element Should Not Have Attribute | ${XML} | xxx | xpath=first |

See also `Get Element Attribute`, `Get Element Attributes`,
`Element Text Should Be` and `Element Text Should Match`.</doc>
<shortdoc>Verifies that the specified element does not have attribute ``name``.</shortdoc>
</kw>
<kw name="Element Text Should Be" lineno="725">
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
<doc>Verifies that the text of the specified element is ``expected``.

The element whose text is verified is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword.

The text to verify is got from the specified element using the same
logic as with `Get Element Text`. This includes optional whitespace
normalization using the ``normalize_whitespace`` option.

The keyword passes if the text of the element is equal to the
``expected`` value, and otherwise it fails. The default error message
can be overridden with the ``message`` argument.  Use `Element Text
Should Match` to verify the text against a pattern instead of an exact
value.

Examples using ``${XML}`` structure from `Example`:
| Element Text Should Be | ${XML}       | text     | xpath=first      |
| Element Text Should Be | ${XML}       | ${EMPTY} | xpath=second/child |
| ${paragraph} =         | Get Element  | ${XML}   | xpath=html/p     |
| Element Text Should Be | ${paragraph} | Text with bold and italics. | normalize_whitespace=yes |</doc>
<shortdoc>Verifies that the text of the specified element is ``expected``.</shortdoc>
</kw>
<kw name="Element Text Should Match" lineno="752">
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
<doc>Verifies that the text of the specified element matches ``expected``.

This keyword works exactly like `Element Text Should Be` except that
the expected value can be given as a pattern that the text of the
element must match.

Pattern matching is similar as matching files in a shell with
``*``, ``?`` and ``[chars]`` acting as wildcards. See the
`Pattern matching` section for more information.

Examples using ``${XML}`` structure from `Example`:
| Element Text Should Match | ${XML}       | t???   | xpath=first  |
| ${paragraph} =            | Get Element  | ${XML} | xpath=html/p |
| Element Text Should Match | ${paragraph} | Text with * and *. | normalize_whitespace=yes |</doc>
<shortdoc>Verifies that the text of the specified element matches ``expected``.</shortdoc>
</kw>
<kw name="Element To String" lineno="1298">
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
<doc>Returns the string representation of the specified element.

The element to convert to a string is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword.

By default the string is returned as Unicode. If ``encoding`` argument
is given any value, the string is returned as bytes in the specified
encoding. The resulting string never contains the XML declaration.

See also `Log Element` and `Save XML`.</doc>
<shortdoc>Returns the string representation of the specified element.</shortdoc>
</kw>
<kw name="Elements Should Be Equal" lineno="883">
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
<doc>Verifies that the given ``source`` element is equal to ``expected``.

Both ``source`` and ``expected`` can be given as a path to an XML file,
as a string containing XML, or as an already parsed XML element
structure. See `introduction` for more information about parsing XML in
general.

The keyword passes if the ``source`` element and ``expected`` element
are equal. This includes testing the tag names, texts, and attributes
of the elements. By default also child elements are verified the same
way, but this can be disabled by setting ``exclude_children`` to a
true value (see `Boolean arguments`).

All texts inside the given elements are verified, but possible text
outside them is not. By default texts must match exactly, but setting
``normalize_whitespace`` to a true value makes text verification
independent on newlines, tabs, and the amount of spaces. For more
details about handling text see `Get Element Text` keyword and
discussion about elements' `text` and `tail` attributes in the
`introduction`.

Examples using ``${XML}`` structure from `Example`:
| ${first} =               | Get Element | ${XML} | first             |
| Elements Should Be Equal | ${first}    | &lt;first id="1"&gt;text&lt;/first&gt; |
| ${p} =                   | Get Element | ${XML} | html/p            |
| Elements Should Be Equal | ${p} | &lt;p&gt;Text with &lt;b&gt;bold&lt;/b&gt; and &lt;i&gt;italics&lt;/i&gt;.&lt;/p&gt; | normalize_whitespace=yes |
| Elements Should Be Equal | ${p} | &lt;p&gt;Text with&lt;/p&gt; | exclude | normalize |

The last example may look a bit strange because the ``&lt;p&gt;`` element
only has text ``Text with``. The reason is that rest of the text
inside ``&lt;p&gt;`` actually belongs to the child elements. This includes
the ``.`` at the end that is the `tail` text of the ``&lt;i&gt;`` element.

See also `Elements Should Match`.</doc>
<shortdoc>Verifies that the given ``source`` element is equal to ``expected``.</shortdoc>
</kw>
<kw name="Elements Should Match" lineno="923">
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
<doc>Verifies that the given ``source`` element matches ``expected``.

This keyword works exactly like `Elements Should Be Equal` except that
texts and attribute values in the expected value can be given as
patterns.

Pattern matching is similar as matching files in a shell with
``*``, ``?`` and ``[chars]`` acting as wildcards. See the
`Pattern matching` section for more information.

Examples using ``${XML}`` structure from `Example`:
| ${first} =            | Get Element | ${XML} | first          |
| Elements Should Match | ${first}    | &lt;first id="?"&gt;*&lt;/first&gt; |

See `Elements Should Be Equal` for more examples.</doc>
<shortdoc>Verifies that the given ``source`` element matches ``expected``.</shortdoc>
</kw>
<kw name="Evaluate Xpath" lineno="1372">
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
<doc>Evaluates the given xpath expression and returns results.

The element in which context the expression is executed is specified
using ``source`` and ``context`` arguments. They have exactly the same
semantics as ``source`` and ``xpath`` arguments have with `Get Element`
keyword.

The xpath expression to evaluate is given as ``expression`` argument.
The result of the evaluation is returned as-is.

Examples using ``${XML}`` structure from `Example`:
| ${count} =      | Evaluate Xpath | ${XML}  | count(third/*) |
| Should Be Equal | ${count}       | ${3}    |
| ${text} =       | Evaluate Xpath | ${XML}  | string(descendant::second[last()]/@id) |
| Should Be Equal | ${text}        | child   |
| ${bold} =       | Evaluate Xpath | ${XML}  | boolean(preceding-sibling::*[1] = 'bold') | context=html/p/i |
| Should Be Equal | ${bold}        | ${True} |

This keyword works only if lxml mode is taken into use when `importing`
the library.</doc>
<shortdoc>Evaluates the given xpath expression and returns results.</shortdoc>
</kw>
<kw name="Get Child Elements" lineno="596">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Returns the child elements of the specified element as a list.

The element whose children to return is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword.

All the direct child elements of the specified element are returned.
If the element has no children, an empty list is returned.

Examples using ``${XML}`` structure from `Example`:
| ${children} =    | Get Child Elements | ${XML} |             |
| Length Should Be | ${children}        | 4      |             |
| ${children} =    | Get Child Elements | ${XML} | xpath=first |
| Should Be Empty  | ${children}        |        |             |</doc>
<shortdoc>Returns the child elements of the specified element as a list.</shortdoc>
</kw>
<kw name="Get Element" lineno="531">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Returns an element in the ``source`` matching the ``xpath``.

The ``source`` can be a path to an XML file, a string containing XML, or
an already parsed XML element. The ``xpath`` specifies which element to
find. See the `introduction` for more details about both the possible
sources and the supported xpath syntax.

The keyword fails if more, or less, than one element matches the
``xpath``. Use `Get Elements` if you want all matching elements to be
returned.

Examples using ``${XML}`` structure from `Example`:
| ${element} = | Get Element | ${XML}     | second |
| ${child} =   | Get Element | ${element} | child  |

`Parse XML` is recommended for parsing XML when the whole structure
is needed. It must be used if there is a need to configure how XML
namespaces are handled.

Many other keywords use this keyword internally, and keywords modifying
XML are typically documented to both to modify the given source and
to return it. Modifying the source does not apply if the source is
given as a string. The XML structure parsed based on the string and
then modified is nevertheless returned.</doc>
<shortdoc>Returns an element in the ``source`` matching the ``xpath``.</shortdoc>
</kw>
<kw name="Get Element Attribute" lineno="773">
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
<doc>Returns the named attribute of the specified element.

The element whose attribute to return is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword.

The value of the attribute ``name`` of the specified element is returned.
If the element does not have such element, the ``default`` value is
returned instead.

Examples using ``${XML}`` structure from `Example`:
| ${attribute} =  | Get Element Attribute | ${XML} | id | xpath=first |
| Should Be Equal | ${attribute}          | 1      |    |             |
| ${attribute} =  | Get Element Attribute | ${XML} | xx | xpath=first | default=value |
| Should Be Equal | ${attribute}          | value  |    |             |

See also `Get Element Attributes`, `Element Attribute Should Be`,
`Element Attribute Should Match` and `Element Should Not Have Attribute`.</doc>
<shortdoc>Returns the named attribute of the specified element.</shortdoc>
</kw>
<kw name="Get Element Attributes" lineno="795">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Returns all attributes of the specified element.

The element whose attributes to return is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword.

Attributes are returned as a Python dictionary. It is a copy of the
original attributes so modifying it has no effect on the XML structure.

Examples using ``${XML}`` structure from `Example`:
| ${attributes} = | Get Element Attributes      | ${XML} | first |
| Dictionary Should Contain Key | ${attributes} | id     |       |
| ${attributes} = | Get Element Attributes      | ${XML} | third |
| Should Be Empty | ${attributes}               |        |       |

Use `Get Element Attribute` to get the value of a single attribute.</doc>
<shortdoc>Returns all attributes of the specified element.</shortdoc>
</kw>
<kw name="Get Element Count" lineno="614">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Returns and logs how many elements the given ``xpath`` matches.

Arguments ``source`` and ``xpath`` have exactly the same semantics as
with `Get Elements` keyword that this keyword uses internally.

See also `Element Should Exist` and `Element Should Not Exist`.</doc>
<shortdoc>Returns and logs how many elements the given ``xpath`` matches.</shortdoc>
</kw>
<kw name="Get Element Text" lineno="656">
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
<doc>Returns all text of the element, possibly whitespace normalized.

The element whose text to return is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword.

This keyword returns all the text of the specified element, including
all the text its children and grandchildren contain. If the element
has no text, an empty string is returned. The returned text is thus not
always the same as the `text` attribute of the element.

By default all whitespace, including newlines and indentation, inside
the element is returned as-is. If ``normalize_whitespace`` is given
a true value (see `Boolean arguments`), then leading and trailing
whitespace is stripped, newlines and tabs converted to spaces, and
multiple spaces collapsed into one. This is especially useful when
dealing with HTML data.

Examples using ``${XML}`` structure from `Example`:
| ${text} =       | Get Element Text | ${XML}       | first        |
| Should Be Equal | ${text}          | text         |              |
| ${text} =       | Get Element Text | ${XML}       | second/child |
| Should Be Empty | ${text}          |              |              |
| ${paragraph} =  | Get Element      | ${XML}       | html/p       |
| ${text} =       | Get Element Text | ${paragraph} | normalize_whitespace=yes |
| Should Be Equal | ${text}          | Text with bold and italics. |

See also `Get Elements Texts`, `Element Text Should Be` and
`Element Text Should Match`.</doc>
<shortdoc>Returns all text of the element, possibly whitespace normalized.</shortdoc>
</kw>
<kw name="Get Elements" lineno="574">
<arguments repr="source, xpath">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="xpath">
<name>xpath</name>
</arg>
</arguments>
<doc>Returns a list of elements in the ``source`` matching the ``xpath``.

The ``source`` can be a path to an XML file, a string containing XML, or
an already parsed XML element. The ``xpath`` specifies which element to
find. See the `introduction` for more details.

Elements matching the ``xpath`` are returned as a list. If no elements
match, an empty list is returned. Use `Get Element` if you want to get
exactly one match.

Examples using ``${XML}`` structure from `Example`:
| ${children} =    | Get Elements | ${XML} | third/child |
| Length Should Be | ${children}  | 2      |             |
| ${children} =    | Get Elements | ${XML} | first/child |
| Should Be Empty  |  ${children} |        |             |</doc>
<shortdoc>Returns a list of elements in the ``source`` matching the ``xpath``.</shortdoc>
</kw>
<kw name="Get Elements Texts" lineno="705">
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
<doc>Returns text of all elements matching ``xpath`` as a list.

The elements whose text to return is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Elements`
keyword.

The text of the matched elements is returned using the same logic
as with `Get Element Text`. This includes optional whitespace
normalization using the ``normalize_whitespace`` option.

Examples using ``${XML}`` structure from `Example`:
| @{texts} =       | Get Elements Texts | ${XML}    | third/child |
| Length Should Be | ${texts}           | 2         |             |
| Should Be Equal  | @{texts}[0]        | more text |             |
| Should Be Equal  | @{texts}[1]        | ${EMPTY}  |             |</doc>
<shortdoc>Returns text of all elements matching ``xpath`` as a list.</shortdoc>
</kw>
<kw name="Log Element" lineno="1318">
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
<doc>Logs the string representation of the specified element.

The element specified with ``source`` and ``xpath`` is first converted
into a string using `Element To String` keyword internally. The
resulting string is then logged using the given ``level``.

The logged string is also returned.</doc>
<shortdoc>Logs the string representation of the specified element.</shortdoc>
</kw>
<kw name="Parse Xml" lineno="488">
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
<doc>Parses the given XML file or string into an element structure.

The ``source`` can either be a path to an XML file or a string
containing XML. In both cases the XML is parsed into ElementTree
[http://docs.python.org/library/xml.etree.elementtree.html#element-objects|element structure]
and the root element is returned. Possible comments and processing
instructions in the source XML are removed.

As discussed in `Handling XML namespaces` section, this keyword, by
default, removes namespace information ElementTree has added to tag
names and moves it into ``xmlns`` attributes. This typically eases
handling XML documents with namespaces considerably. If you do not
want that to happen, or want to avoid the small overhead of going
through the element structure when your XML does not have namespaces,
you can disable this feature by giving ``keep_clark_notation`` argument
a true value (see `Boolean arguments`).

If you want to strip namespace information altogether so that it is
not included even if XML is saved, you can give a true value to
``strip_namespaces`` argument.

Examples:
| ${root} = | Parse XML | &lt;root&gt;&lt;child/&gt;&lt;/root&gt; |
| ${xml} = | Parse XML | ${CURDIR}/test.xml | keep_clark_notation=True |
| ${xml} = | Parse XML | ${CURDIR}/test.xml | strip_namespaces=True |

Use `Get Element` keyword if you want to get a certain element and not
the whole structure. See `Parsing XML` section for more details and
examples.</doc>
<shortdoc>Parses the given XML file or string into an element structure.</shortdoc>
</kw>
<kw name="Remove Element" lineno="1171">
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
<doc>Removes the element matching ``xpath`` from the ``source`` structure.

The element to remove from the ``source`` is specified with ``xpath``
using the same semantics as with `Get Element` keyword. The resulting
XML structure is returned, and if the ``source`` is an already parsed
XML structure, it is also modified in place.

The keyword fails if ``xpath`` does not match exactly one element.
Use `Remove Elements` to remove all matched elements.

Element's tail text is not removed by default, but that can be changed
by giving ``remove_tail`` a true value (see `Boolean arguments`). See
`Element attributes` section for more information about `tail` in
general.

Examples using ``${XML}`` structure from `Example`:
| Remove Element           | ${XML} | xpath=second |
| Element Should Not Exist | ${XML} | xpath=second |
| Remove Element           | ${XML} | xpath=html/p/b | remove_tail=yes |
| Element Text Should Be   | ${XML} | Text with italics. | xpath=html/p | normalize_whitespace=yes |</doc>
<shortdoc>Removes the element matching ``xpath`` from the ``source`` structure.</shortdoc>
</kw>
<kw name="Remove Element Attribute" lineno="1066">
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
<doc>Removes attribute ``name`` from the specified element.

The element whose attribute to remove is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword. The resulting XML structure is returned, and if the ``source``
is an already parsed XML structure, it is also modified in place.

It is not a failure to remove a non-existing attribute. Use `Remove
Element Attributes` to remove all attributes and `Set Element Attribute`
to set them.

Examples using ``${XML}`` structure from `Example`:
| Remove Element Attribute          | ${XML} | id | xpath=first |
| Element Should Not Have Attribute | ${XML} | id | xpath=first |

Can only remove an attribute from a single element. Use `Remove Elements
Attribute` to remove an attribute of multiple elements in one call.</doc>
<shortdoc>Removes attribute ``name`` from the specified element.</shortdoc>
</kw>
<kw name="Remove Element Attributes" lineno="1102">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Removes all attributes from the specified element.

The element whose attributes to remove is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword. The resulting XML structure is returned, and if the ``source``
is an already parsed XML structure, it is also modified in place.

Use `Remove Element Attribute` to remove a single attribute and
`Set Element Attribute` to set them.

Examples using ``${XML}`` structure from `Example`:
| Remove Element Attributes         | ${XML} | xpath=first |
| Element Should Not Have Attribute | ${XML} | id | xpath=first |

Can only remove attributes from a single element. Use `Remove Elements
Attributes` to remove all attributes of multiple elements in one call.</doc>
<shortdoc>Removes all attributes from the specified element.</shortdoc>
</kw>
<kw name="Remove Elements" lineno="1197">
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
<doc>Removes all elements matching ``xpath`` from the ``source`` structure.

The elements to remove from the ``source`` are specified with ``xpath``
using the same semantics as with `Get Elements` keyword. The resulting
XML structure is returned, and if the ``source`` is an already parsed
XML structure, it is also modified in place.

It is not a failure if ``xpath`` matches no elements. Use `Remove
Element` to remove exactly one element.

Element's tail text is not removed by default, but that can be changed
by using ``remove_tail`` argument similarly as with `Remove Element`.

Examples using ``${XML}`` structure from `Example`:
| Remove Elements          | ${XML} | xpath=*/child      |
| Element Should Not Exist | ${XML} | xpath=second/child |
| Element Should Not Exist | ${XML} | xpath=third/child  |</doc>
<shortdoc>Removes all elements matching ``xpath`` from the ``source`` structure.</shortdoc>
</kw>
<kw name="Remove Elements Attribute" lineno="1091">
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
<doc>Removes attribute ``name`` from the specified elements.

Like `Remove Element Attribute` but removes the attribute of all
elements matching the given ``xpath``.</doc>
<shortdoc>Removes attribute ``name`` from the specified elements.</shortdoc>
</kw>
<kw name="Remove Elements Attributes" lineno="1124">
<arguments repr="source, xpath=.">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="source">
<name>source</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="xpath=.">
<name>xpath</name>
<default>.</default>
</arg>
</arguments>
<doc>Removes all attributes from the specified elements.

Like `Remove Element Attributes` but removes all attributes of all
elements matching the given ``xpath``.</doc>
<shortdoc>Removes all attributes from the specified elements.</shortdoc>
</kw>
<kw name="Save Xml" lineno="1331">
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
<doc>Saves the given element to the specified file.

The element to save is specified with ``source`` using the same
semantics as with `Get Element` keyword.

The file where the element is saved is denoted with ``path`` and the
encoding to use with ``encoding``. The resulting file always contains
the XML declaration.

The resulting XML file may not be exactly the same as the original:
- Comments and processing instructions are always stripped.
- Possible doctype and namespace prefixes are only preserved when
  `using lxml`.
- Other small differences are possible depending on the ElementTree
  or lxml version.

Use `Element To String` if you just need a string representation of
the element.</doc>
<shortdoc>Saves the given element to the specified file.</shortdoc>
</kw>
<kw name="Set Element Attribute" lineno="1028">
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
<doc>Sets attribute ``name`` of the specified element to ``value``.

The element whose attribute to set is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword. The resulting XML structure is returned, and if the ``source``
is an already parsed XML structure, it is also modified in place.

It is possible to both set new attributes and to overwrite existing.
Use `Remove Element Attribute` or `Remove Element Attributes` for
removing them.

Examples using ``${XML}`` structure from `Example`:
| Set Element Attribute       | ${XML} | attr | value |
| Element Attribute Should Be | ${XML} | attr | value |
| Set Element Attribute       | ${XML} | id   | new   | xpath=first |
| Element Attribute Should Be | ${XML} | id   | new   | xpath=first |

Can only set an attribute of a single element. Use `Set Elements
Attribute` to set an attribute of multiple elements in one call.</doc>
<shortdoc>Sets attribute ``name`` of the specified element to ``value``.</shortdoc>
</kw>
<kw name="Set Element Tag" lineno="951">
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
<doc>Sets the tag of the specified element.

The element whose tag to set is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword. The resulting XML structure is returned, and if the ``source``
is an already parsed XML structure, it is also modified in place.

Examples using ``${XML}`` structure from `Example`:
| Set Element Tag      | ${XML}     | newTag     |
| Should Be Equal      | ${XML.tag} | newTag     |
| Set Element Tag      | ${XML}     | xxx        | xpath=second/child |
| Element Should Exist | ${XML}     | second/xxx |
| Element Should Not Exist | ${XML} | second/child |

Can only set the tag of a single element. Use `Set Elements Tag` to set
the tag of multiple elements in one call.</doc>
<shortdoc>Sets the tag of the specified element.</shortdoc>
</kw>
<kw name="Set Element Text" lineno="985">
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
<doc>Sets text and/or tail text of the specified element.

The element whose text to set is specified using ``source`` and
``xpath``. They have exactly the same semantics as with `Get Element`
keyword. The resulting XML structure is returned, and if the ``source``
is an already parsed XML structure, it is also modified in place.

Element's text and tail text are changed only if new ``text`` and/or
``tail`` values are given. See `Element attributes` section for more
information about `text` and `tail` in general.

Examples using ``${XML}`` structure from `Example`:
| Set Element Text       | ${XML} | new text | xpath=first    |
| Element Text Should Be | ${XML} | new text | xpath=first    |
| Set Element Text       | ${XML} | tail=&amp;   | xpath=html/p/b |
| Element Text Should Be | ${XML} | Text with bold&amp;italics. | xpath=html/p  | normalize_whitespace=yes |
| Set Element Text       | ${XML} | slanted  | !! | xpath=html/p/i |
| Element Text Should Be | ${XML} | Text with bold&amp;slanted!! | xpath=html/p  | normalize_whitespace=yes |

Can only set the text/tail of a single element. Use `Set Elements Text`
to set the text/tail of multiple elements in one call.</doc>
<shortdoc>Sets text and/or tail text of the specified element.</shortdoc>
</kw>
<kw name="Set Elements Attribute" lineno="1055">
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
<doc>Sets attribute ``name`` of the specified elements to ``value``.

Like `Set Element Attribute` but sets the attribute of all elements
matching the given ``xpath``.</doc>
<shortdoc>Sets attribute ``name`` of the specified elements to ``value``.</shortdoc>
</kw>
<kw name="Set Elements Tag" lineno="973">
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
<doc>Sets the tag of the specified elements.

Like `Set Element Tag` but sets the tag of all elements matching
the given ``xpath``.</doc>
<shortdoc>Sets the tag of the specified elements.</shortdoc>
</kw>
<kw name="Set Elements Text" lineno="1017">
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
<doc>Sets text and/or tail text of the specified elements.

Like `Set Element Text` but sets the text or tail of all elements
matching the given ``xpath``.</doc>
<shortdoc>Sets text and/or tail text of the specified elements.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
<typedocs>
</typedocs>
</keywordspec>
