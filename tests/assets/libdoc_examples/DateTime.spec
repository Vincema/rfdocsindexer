<?xml version="1.0" encoding="UTF-8"?>
<keywordspec name="DateTime" type="LIBRARY" format="HTML" scope="GLOBAL" generated="2022-10-06T17:00:29Z" specversion="4" source="/home/kali/Code/rfdocsindexer/.tox/py39/lib/python3.9/site-packages/robot/libraries/DateTime.py" lineno="1">
<version>5.0.1</version>
<doc>&lt;p&gt;A library for handling date and time values.&lt;/p&gt;
&lt;p&gt;&lt;code&gt;DateTime&lt;/code&gt; is a Robot Framework standard library that supports creating and converting date and time values (e.g. &lt;a href="#Get%20Current%20Date" class="name"&gt;Get Current Date&lt;/a&gt;, &lt;a href="#Convert%20Time" class="name"&gt;Convert Time&lt;/a&gt;), as well as doing simple calculations with them (e.g. &lt;a href="#Subtract%20Time%20From%20Date" class="name"&gt;Subtract Time From Date&lt;/a&gt;, &lt;a href="#Add%20Time%20To%20Time" class="name"&gt;Add Time To Time&lt;/a&gt;). It supports dates and times in various formats, and can also be used by other libraries programmatically.&lt;/p&gt;
&lt;h3 id="Table of contents"&gt;Table of contents&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href="#Terminology" class="name"&gt;Terminology&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Date%20formats" class="name"&gt;Date formats&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Time%20formats" class="name"&gt;Time formats&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Millisecond%20handling" class="name"&gt;Millisecond handling&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Programmatic%20usage" class="name"&gt;Programmatic usage&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a href="#Keywords" class="name"&gt;Keywords&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Terminology"&gt;Terminology&lt;/h2&gt;
&lt;p&gt;In the context of this library, &lt;code&gt;date&lt;/code&gt; and &lt;code&gt;time&lt;/code&gt; generally have the following meanings:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;date&lt;/code&gt;: An entity with both date and time components but without any time zone information. For example, &lt;code&gt;2014-06-11 10:07:42&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;time&lt;/code&gt;: A time interval. For example, &lt;code&gt;1 hour 20 minutes&lt;/code&gt; or &lt;code&gt;01:20:00&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;This terminology differs from what Python's standard &lt;a href="http://docs.python.org/library/datetime.html"&gt;datetime&lt;/a&gt; module uses. Basically its &lt;a href="http://docs.python.org/library/datetime.html#datetime-objects"&gt;datetime&lt;/a&gt; and &lt;a href="http://docs.python.org/library/datetime.html#timedelta-objects"&gt;timedelta&lt;/a&gt; objects match &lt;code&gt;date&lt;/code&gt; and &lt;code&gt;time&lt;/code&gt; as defined by this library.&lt;/p&gt;
&lt;h2 id="Date formats"&gt;Date formats&lt;/h2&gt;
&lt;p&gt;Dates can be given to and received from keywords in &lt;a href="#Timestamp" class="name"&gt;timestamp&lt;/a&gt;, &lt;a href="#Custom%20timestamp" class="name"&gt;custom timestamp&lt;/a&gt;, &lt;a href="#Python%20datetime" class="name"&gt;Python datetime&lt;/a&gt; and &lt;a href="#Epoch%20time" class="name"&gt;epoch time&lt;/a&gt; formats. These formats are discussed thoroughly in subsequent sections.&lt;/p&gt;
&lt;p&gt;Input format is determined automatically based on the given date except when using custom timestamps, in which case it needs to be given using &lt;code&gt;date_format&lt;/code&gt; argument. Default result format is timestamp, but it can be overridden using &lt;code&gt;result_format&lt;/code&gt; argument.&lt;/p&gt;
&lt;h3 id="Timestamp"&gt;Timestamp&lt;/h3&gt;
&lt;p&gt;If a date is given as a string, it is always considered to be a timestamp. If no custom formatting is given using &lt;code&gt;date_format&lt;/code&gt; argument, the timestamp is expected to be in &lt;a href="http://en.wikipedia.org/wiki/ISO_8601"&gt;ISO 8601&lt;/a&gt; like format &lt;code&gt;YYYY-MM-DD hh:mm:ss.mil&lt;/code&gt;, where any non-digit character can be used as a separator or separators can be omitted altogether. Additionally, only the date part is mandatory, all possibly missing time components are considered to be zeros.&lt;/p&gt;
&lt;p&gt;Dates can also be returned in the same &lt;code&gt;YYYY-MM-DD hh:mm:ss.mil&lt;/code&gt; format by using &lt;code&gt;timestamp&lt;/code&gt; value with &lt;code&gt;result_format&lt;/code&gt; argument. This is also the default format that keywords returning dates use. Milliseconds can be excluded using &lt;code&gt;exclude_millis&lt;/code&gt; as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;Millisecond handling&lt;/a&gt; section.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date1} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:42.000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date2} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;20140611 100742&lt;/td&gt;
&lt;td&gt;result_format=timestamp&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date1}&lt;/td&gt;
&lt;td&gt;${date2}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;20140612 12:57&lt;/td&gt;
&lt;td&gt;exclude_millis=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-12 12:57:00&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Custom timestamp"&gt;Custom timestamp&lt;/h3&gt;
&lt;p&gt;It is possible to use custom timestamps in both input and output. The custom format is same as accepted by Python's &lt;a href="http://docs.python.org/library/datetime.html#strftime-strptime-behavior"&gt;datetime.strptime&lt;/a&gt; function. For example, the default timestamp discussed in the previous section would match &lt;code&gt;%Y-%m-%d %H:%M:%S.%f&lt;/code&gt;.&lt;/p&gt;
&lt;p&gt;When using a custom timestamp in input, it must be specified using &lt;code&gt;date_format&lt;/code&gt; argument. The actual input value must be a string that matches the specified format exactly. When using a custom timestamp in output, it must be given using &lt;code&gt;result_format&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;28.05.2014 12:05&lt;/td&gt;
&lt;td&gt;date_format=%d.%m.%Y %H:%M&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:00.000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;result_format=%d.%m.%Y&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;28.05.2014&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Python datetime"&gt;Python datetime&lt;/h3&gt;
&lt;p&gt;Python's standard &lt;a href="http://docs.python.org/library/datetime.html#datetime-objects"&gt;datetime&lt;/a&gt; objects can be used both in input and output. In input they are recognized automatically, and in output it is possible to get them by giving &lt;code&gt;datetime&lt;/code&gt; value to &lt;code&gt;result_format&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;One nice benefit with datetime objects is that they have different time components available as attributes that can be easily accessed using the extended variable syntax.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${datetime} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:42.123&lt;/td&gt;
&lt;td&gt;datetime&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.year}&lt;/td&gt;
&lt;td&gt;2014&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.month}&lt;/td&gt;
&lt;td&gt;6&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.day}&lt;/td&gt;
&lt;td&gt;11&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.hour}&lt;/td&gt;
&lt;td&gt;10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.minute}&lt;/td&gt;
&lt;td&gt;7&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.second}&lt;/td&gt;
&lt;td&gt;42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal As Integers&lt;/td&gt;
&lt;td&gt;${datetime.microsecond}&lt;/td&gt;
&lt;td&gt;123000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Epoch time"&gt;Epoch time&lt;/h3&gt;
&lt;p&gt;Epoch time is the time in seconds since the &lt;a href="http://en.wikipedia.org/wiki/Unix_time"&gt;UNIX epoch&lt;/a&gt; i.e. 00:00:00.000 (UTC) January 1, 1970. To give a date as an epoch time, it must be given as a number (integer or float), not as a string. To return a date as an epoch time, it is possible to use &lt;code&gt;epoch&lt;/code&gt; value with &lt;code&gt;result_format&lt;/code&gt; argument. Epoch times are returned as floating point numbers.&lt;/p&gt;
&lt;p&gt;Notice that epoch times are independent on time zones and thus same around the world at a certain time. For example, epoch times returned by &lt;a href="#Get%20Current%20Date" class="name"&gt;Get Current Date&lt;/a&gt; are not affected by the &lt;code&gt;time_zone&lt;/code&gt; argument. What local time a certain epoch time matches then depends on the time zone.&lt;/p&gt;
&lt;p&gt;Following examples demonstrate using epoch times. They are tested in Finland, and due to the reasons explained above they would fail on other time zones.&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;${1000000000}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2001-09-09 04:46:40.000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;2014-06-12 13:27:59.279&lt;/td&gt;
&lt;td&gt;epoch&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;${1402568879.279}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Earliest supported date"&gt;Earliest supported date&lt;/h3&gt;
&lt;p&gt;The earliest date that is supported depends on the date format and to some extent on the platform:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Timestamps support year 1900 and above.&lt;/li&gt;
&lt;li&gt;Python datetime objects support year 1 and above.&lt;/li&gt;
&lt;li&gt;Epoch time supports 1970 and above on Windows.&lt;/li&gt;
&lt;li&gt;On other platforms epoch time supports 1900 and above or even earlier.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2 id="Time formats"&gt;Time formats&lt;/h2&gt;
&lt;p&gt;Similarly as dates, times can be given to and received from keywords in various different formats. Supported formats are &lt;a href="#Number" class="name"&gt;number&lt;/a&gt;, &lt;a href="#Time%20string" class="name"&gt;time string&lt;/a&gt; (verbose and compact), &lt;a href="#Timer%20string" class="name"&gt;timer string&lt;/a&gt; and &lt;a href="#Python%20timedelta" class="name"&gt;Python timedelta&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Input format for time is always determined automatically based on the input. Result format is number by default, but it can be customised using &lt;code&gt;result_format&lt;/code&gt; argument.&lt;/p&gt;
&lt;h3 id="Number"&gt;Number&lt;/h3&gt;
&lt;p&gt;Time given as a number is interpreted to be seconds. It can be given either as an integer or a float, or it can be a string that can be converted to a number.&lt;/p&gt;
&lt;p&gt;To return a time as a number, &lt;code&gt;result_format&lt;/code&gt; argument must have value &lt;code&gt;number&lt;/code&gt;, which is also the default. Returned number is always a float.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;3.14&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${3.14}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;result_format=number&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${3.14}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Time string"&gt;Time string&lt;/h3&gt;
&lt;p&gt;Time strings are strings in format like &lt;code&gt;1 minute 42 seconds&lt;/code&gt; or &lt;code&gt;1min 42s&lt;/code&gt;. The basic idea of this format is having first a number and then a text specifying what time that number represents. Numbers can be either integers or floating point numbers, the whole format is case and space insensitive, and it is possible to add a minus prefix to specify negative times. The available time specifiers are:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;days&lt;/code&gt;, &lt;code&gt;day&lt;/code&gt;, &lt;code&gt;d&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;hours&lt;/code&gt;, &lt;code&gt;hour&lt;/code&gt;, &lt;code&gt;h&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;minutes&lt;/code&gt;, &lt;code&gt;minute&lt;/code&gt;, &lt;code&gt;mins&lt;/code&gt;, &lt;code&gt;min&lt;/code&gt;, &lt;code&gt;m&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;seconds&lt;/code&gt;, &lt;code&gt;second&lt;/code&gt;, &lt;code&gt;secs&lt;/code&gt;, &lt;code&gt;sec&lt;/code&gt;, &lt;code&gt;s&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;milliseconds&lt;/code&gt;, &lt;code&gt;millisecond&lt;/code&gt;, &lt;code&gt;millis&lt;/code&gt;, &lt;code&gt;ms&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;When returning a time string, it is possible to select between &lt;code&gt;verbose&lt;/code&gt; and &lt;code&gt;compact&lt;/code&gt; representations using &lt;code&gt;result_format&lt;/code&gt; argument. The verbose format uses long specifiers &lt;code&gt;day&lt;/code&gt;, &lt;code&gt;hour&lt;/code&gt;, &lt;code&gt;minute&lt;/code&gt;, &lt;code&gt;second&lt;/code&gt; and &lt;code&gt;millisecond&lt;/code&gt;, and adds &lt;code&gt;s&lt;/code&gt; at the end when needed. The compact format uses shorter specifiers &lt;code&gt;d&lt;/code&gt;, &lt;code&gt;h&lt;/code&gt;, &lt;code&gt;min&lt;/code&gt;, &lt;code&gt;s&lt;/code&gt; and &lt;code&gt;ms&lt;/code&gt;, and even drops the space between the number and the specifier.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;1 minute 42 seconds&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${102}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;4200&lt;/td&gt;
&lt;td&gt;verbose&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;1 hour 10 minutes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;- 1.5 hours&lt;/td&gt;
&lt;td&gt;compact&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;- 1h 30min&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Timer string"&gt;Timer string&lt;/h3&gt;
&lt;p&gt;Timer string is a string given in timer like format &lt;code&gt;hh:mm:ss.mil&lt;/code&gt;. In this format both hour and millisecond parts are optional, leading and trailing zeros can be left out when they are not meaningful, and negative times can be represented by adding a minus prefix.&lt;/p&gt;
&lt;p&gt;To return a time as timer string, &lt;code&gt;result_format&lt;/code&gt; argument must be given value &lt;code&gt;timer&lt;/code&gt;. Timer strings are by default returned in full &lt;code&gt;hh:mm:ss.mil&lt;/code&gt; format, but milliseconds can be excluded using &lt;code&gt;exclude_millis&lt;/code&gt; as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;Millisecond handling&lt;/a&gt; section.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;01:42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${102}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;01:10:00.123&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${4200.123}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;102&lt;/td&gt;
&lt;td&gt;timer&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;00:01:42.000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;-101.567&lt;/td&gt;
&lt;td&gt;timer&lt;/td&gt;
&lt;td&gt;exclude_millis=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;-00:01:42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h3 id="Python timedelta"&gt;Python timedelta&lt;/h3&gt;
&lt;p&gt;Python's standard &lt;a href="http://docs.python.org/library/datetime.html#datetime.timedelta"&gt;timedelta&lt;/a&gt; objects are also supported both in input and in output. In input they are recognized automatically, and in output it is possible to receive them by giving &lt;code&gt;timedelta&lt;/code&gt; value to &lt;code&gt;result_format&lt;/code&gt; argument.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${timedelta} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;01:10:02.123&lt;/td&gt;
&lt;td&gt;timedelta&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${timedelta.total_seconds()}&lt;/td&gt;
&lt;td&gt;${4202.123}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Millisecond handling"&gt;Millisecond handling&lt;/h2&gt;
&lt;p&gt;This library handles dates and times internally using the precision of the given input. With &lt;a href="#Timestamp" class="name"&gt;timestamp&lt;/a&gt;, &lt;a href="#Time%20string" class="name"&gt;time string&lt;/a&gt;, and &lt;a href="#Timer%20string" class="name"&gt;timer string&lt;/a&gt; result formats seconds are, however, rounded to millisecond accuracy. Milliseconds may also be included even if there would be none.&lt;/p&gt;
&lt;p&gt;All keywords returning dates or times have an option to leave milliseconds out by giving a true value to &lt;code&gt;exclude_millis&lt;/code&gt; argument. If the argument is given as a string, it is considered true unless it is empty or case-insensitively equal to &lt;code&gt;false&lt;/code&gt;, &lt;code&gt;none&lt;/code&gt; or &lt;code&gt;no&lt;/code&gt;. Other argument types are tested using same &lt;a href="http://docs.python.org/library/stdtypes.html#truth"&gt;rules as in Python&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;When milliseconds are excluded, seconds in returned dates and times are rounded to the nearest full second. With &lt;a href="#Timestamp" class="name"&gt;timestamp&lt;/a&gt; and &lt;a href="#Timer%20string" class="name"&gt;timer string&lt;/a&gt; result formats, milliseconds will also be removed from the returned string altogether.&lt;/p&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:42.000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:42.500&lt;/td&gt;
&lt;td&gt;exclude_millis=yes&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:43&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${dt} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;2014-06-11 10:07:42.500&lt;/td&gt;
&lt;td&gt;datetime&lt;/td&gt;
&lt;td&gt;exclude_millis=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${dt.second}&lt;/td&gt;
&lt;td&gt;${43}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${dt.microsecond}&lt;/td&gt;
&lt;td&gt;${0}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;102&lt;/td&gt;
&lt;td&gt;timer&lt;/td&gt;
&lt;td&gt;exclude_millis=false&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;00:01:42.000&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;102.567&lt;/td&gt;
&lt;td&gt;timer&lt;/td&gt;
&lt;td&gt;exclude_millis=true&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;00:01:43&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;h2 id="Programmatic usage"&gt;Programmatic usage&lt;/h2&gt;
&lt;p&gt;In addition to be used as normal library, this library is intended to provide a stable API for other libraries to use if they want to support same date and time formats as this library. All the provided keywords are available as functions that can be easily imported:&lt;/p&gt;
&lt;pre&gt;
from robot.libraries.DateTime import convert_time

def example_keyword(timeout):
    seconds = convert_time(timeout)
    # ...
&lt;/pre&gt;
&lt;p&gt;Additionally helper classes &lt;code&gt;Date&lt;/code&gt; and &lt;code&gt;Time&lt;/code&gt; can be used directly:&lt;/p&gt;
&lt;pre&gt;
from robot.libraries.DateTime import Date, Time

def example_keyword(date, interval):
    date = Date(date).convert('datetime')
    interval = Time(interval).convert('number')
    # ...
&lt;/pre&gt;</doc>
<tags>
</tags>
<inits>
</inits>
<keywords>
<kw name="Add Time To Date" lineno="419">
<arguments repr="date, time, result_format=timestamp, exclude_millis=False, date_format=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="date">
<name>date</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time">
<name>time</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=timestamp">
<name>result_format</name>
<default>timestamp</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="date_format=None">
<name>date_format</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Adds time to date and returns the resulting date.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;date:&lt;/code&gt;           Date to add time to in one of the supported &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;time:&lt;/code&gt;           Time that is added in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned date.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;date_format:&lt;/code&gt;    Possible &lt;a href="#Custom%20timestamp" class="name"&gt;custom timestamp&lt;/a&gt; format of &lt;code&gt;date&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Add Time To Date&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:03.111&lt;/td&gt;
&lt;td&gt;7 days&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-04 12:05:03.111&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Add Time To Date&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:03.111&lt;/td&gt;
&lt;td&gt;01:02:03:004&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-05-28 13:07:06.115&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Adds time to date and returns the resulting date.</shortdoc>
</kw>
<kw name="Add Time To Time" lineno="467">
<arguments repr="time1, time2, result_format=number, exclude_millis=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time1">
<name>time1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time2">
<name>time2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=number">
<name>result_format</name>
<default>number</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Adds time to another time and returns the resulting time.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;time1:&lt;/code&gt;          First time in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;time2:&lt;/code&gt;          Second time in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned time.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Add Time To Time&lt;/td&gt;
&lt;td&gt;1 minute&lt;/td&gt;
&lt;td&gt;42&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${102}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Add Time To Time&lt;/td&gt;
&lt;td&gt;3 hours 5 minutes&lt;/td&gt;
&lt;td&gt;01:02:03&lt;/td&gt;
&lt;td&gt;timer&lt;/td&gt;
&lt;td&gt;exclude_millis=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;04:07:03&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Adds time to another time and returns the resulting time.</shortdoc>
</kw>
<kw name="Convert Date" lineno="350">
<arguments repr="date, result_format=timestamp, exclude_millis=False, date_format=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="date">
<name>date</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=timestamp">
<name>result_format</name>
<default>timestamp</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="date_format=None">
<name>date_format</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Converts between supported &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;date:&lt;/code&gt;           Date in one of the supported &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned date.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;date_format:&lt;/code&gt;    Specifies possible &lt;a href="#Custom%20timestamp" class="name"&gt;custom timestamp&lt;/a&gt; format.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;20140528 12:05:03.111&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:03.111&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;epoch&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;${1401267903.111}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Convert Date&lt;/td&gt;
&lt;td&gt;5.28.2014 12:05&lt;/td&gt;
&lt;td&gt;exclude_millis=yes&lt;/td&gt;
&lt;td&gt;date_format=%m.%d.%Y %H:%M&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:00&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Converts between supported `date formats`.</shortdoc>
</kw>
<kw name="Convert Time" lineno="373">
<arguments repr="time, result_format=number, exclude_millis=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time">
<name>time</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=number">
<name>result_format</name>
<default>number</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Converts between supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;time:&lt;/code&gt;           Time in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned time.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;10 seconds&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${10}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;1:00:01&lt;/td&gt;
&lt;td&gt;verbose&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;1 hour 1 second&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Convert Time&lt;/td&gt;
&lt;td&gt;${3661.5}&lt;/td&gt;
&lt;td&gt;timer&lt;/td&gt;
&lt;td&gt;exclude_milles=yes&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;01:01:02&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Converts between supported `time formats`.</shortdoc>
</kw>
<kw name="Get Current Date" lineno="307">
<arguments repr="time_zone=local, increment=0, result_format=timestamp, exclude_millis=False">
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="time_zone=local">
<name>time_zone</name>
<default>local</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="increment=0">
<name>increment</name>
<default>0</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=timestamp">
<name>result_format</name>
<default>timestamp</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Returns current local or UTC time with an optional increment.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;time_zone:&lt;/code&gt;      Get the current time on this time zone. Currently only &lt;code&gt;local&lt;/code&gt; (default) and &lt;code&gt;UTC&lt;/code&gt; are supported. Has no effect if date is returned as an &lt;a href="#Epoch%20time" class="name"&gt;epoch time&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;increment:&lt;/code&gt;      Optional time increment to add to the returned date in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;. Can be negative.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned date (see &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;).&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Get Current Date&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-12 20:00:58.946&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Get Current Date&lt;/td&gt;
&lt;td&gt;UTC&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-12 17:00:58.946&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Get Current Date&lt;/td&gt;
&lt;td&gt;increment=02:30:00&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-12 22:30:58.946&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Get Current Date&lt;/td&gt;
&lt;td&gt;UTC&lt;/td&gt;
&lt;td&gt;- 5 hours&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-06-12 12:00:58.946&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Get Current Date&lt;/td&gt;
&lt;td&gt;result_format=datetime&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date.year}&lt;/td&gt;
&lt;td&gt;${2014}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date.month}&lt;/td&gt;
&lt;td&gt;${6}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Returns current local or UTC time with an optional increment.</shortdoc>
</kw>
<kw name="Subtract Date From Date" lineno="393">
<arguments repr="date1, date2, result_format=number, exclude_millis=False, date1_format=None, date2_format=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="date1">
<name>date1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="date2">
<name>date2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=number">
<name>result_format</name>
<default>number</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="date1_format=None">
<name>date1_format</name>
<default>None</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="date2_format=None">
<name>date2_format</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Subtracts date from another date and returns time between.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;date1:&lt;/code&gt;          Date to subtract another date from in one of the supported &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;date2:&lt;/code&gt;          Date that is subtracted in one of the supported &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned time (see &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;).&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;date1_format:&lt;/code&gt;   Possible &lt;a href="#Custom%20timestamp" class="name"&gt;custom timestamp&lt;/a&gt; format of &lt;code&gt;date1&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;date2_format:&lt;/code&gt;   Possible &lt;a href="#Custom%20timestamp" class="name"&gt;custom timestamp&lt;/a&gt; format of &lt;code&gt;date2&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Subtract Date From Date&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:52&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:10&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${42}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Subtract Date From Date&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:52&lt;/td&gt;
&lt;td&gt;2014-05-27 12:05:10&lt;/td&gt;
&lt;td&gt;verbose&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;1 day 42 seconds&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Subtracts date from another date and returns time between.</shortdoc>
</kw>
<kw name="Subtract Time From Date" lineno="443">
<arguments repr="date, time, result_format=timestamp, exclude_millis=False, date_format=None">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="date">
<name>date</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time">
<name>time</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=timestamp">
<name>result_format</name>
<default>timestamp</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="date_format=None">
<name>date_format</name>
<default>None</default>
</arg>
</arguments>
<doc>&lt;p&gt;Subtracts time from date and returns the resulting date.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;date:&lt;/code&gt;           Date to subtract time from in one of the supported &lt;a href="#Date%20formats" class="name"&gt;date formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;time:&lt;/code&gt;           Time that is subtracted in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned date.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;date_format:&lt;/code&gt;    Possible &lt;a href="#Custom%20timestamp" class="name"&gt;custom timestamp&lt;/a&gt; format of &lt;code&gt;date&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Subtract Time From Date&lt;/td&gt;
&lt;td&gt;2014-06-04 12:05:03.111&lt;/td&gt;
&lt;td&gt;7 days&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:03.111&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${date} =&lt;/td&gt;
&lt;td&gt;Subtract Time From Date&lt;/td&gt;
&lt;td&gt;2014-05-28 13:07:06.115&lt;/td&gt;
&lt;td&gt;01:02:03:004&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${date}&lt;/td&gt;
&lt;td&gt;2014-05-28 12:05:03.111&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Subtracts time from date and returns the resulting date.</shortdoc>
</kw>
<kw name="Subtract Time From Time" lineno="488">
<arguments repr="time1, time2, result_format=number, exclude_millis=False">
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time1">
<name>time1</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="true" repr="time2">
<name>time2</name>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="result_format=number">
<name>result_format</name>
<default>number</default>
</arg>
<arg kind="POSITIONAL_OR_NAMED" required="false" repr="exclude_millis=False">
<name>exclude_millis</name>
<default>False</default>
</arg>
</arguments>
<doc>&lt;p&gt;Subtracts time from another time and returns the resulting time.&lt;/p&gt;
&lt;p&gt;Arguments:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;time1:&lt;/code&gt;          Time to subtract another time from in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;time2:&lt;/code&gt;          Time to subtract in one of the supported &lt;a href="#Time%20formats" class="name"&gt;time formats&lt;/a&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;result_format:&lt;/code&gt;  Format of the returned time.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;exclude_millis:&lt;/code&gt; When set to any true value, rounds and drops milliseconds as explained in &lt;a href="#Millisecond%20handling" class="name"&gt;millisecond handling&lt;/a&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Examples:&lt;/p&gt;
&lt;table border="1"&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Subtract Time From Time&lt;/td&gt;
&lt;td&gt;00:02:30&lt;/td&gt;
&lt;td&gt;100&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;${50}&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;${time} =&lt;/td&gt;
&lt;td&gt;Subtract Time From Time&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;1 minute&lt;/td&gt;
&lt;td&gt;compact&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td&gt;Should Be Equal&lt;/td&gt;
&lt;td&gt;${time}&lt;/td&gt;
&lt;td&gt;- 10s&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;td&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</doc>
<shortdoc>Subtracts time from another time and returns the resulting time.</shortdoc>
</kw>
</keywords>
<datatypes>
</datatypes>
<typedocs>
</typedocs>
</keywordspec>
