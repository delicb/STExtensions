SmartTest sublime extensions
============================

This package provides few snippets that are useful when working with SmartTest
in SublimeText editor.
List of features that this package supports:
* Sytax coloring for Tesla
* Set of snippets for easier repository writting
* Set of snippets for Tesla when using it with SmartTest
* Set of snippets for Python whe using it with SmartTest
* Builders for running tests and plans from SublimeText
* Some experimental stuff that may be removed or, at some point, finished.

Repository
----------

Snippets available for repository is (these are only available if syntax for
file is set to `XML`):

Snippet | Explanation
--------|---------------------------------------------------------
`acc`   | Adds rule for accelerator key
`aid`   | Adds rule for automation id
`ch`    | Creates `children` element and adds first child to it.
`class` | Adds rule for class name
`fwid`  | Adds rule for framework id
`htxt`  | Adds rule for help text
`index` | Adds attribute used for indexing
`item`  | Creates new item with prefefined element for first rule
`name`  | Adds rule for name
`repo`  | Starts new document with proper heading and root element
`type`  | Adds rule for type


Tesla
-----

Snippets available in Tesla code are these (these are only available if syntax
is set to `Tesla`):

Snippet      | Explanation
-------------|-------------------------------------------------------------
`head`       | Inserts test header
`if`         | Inserts condition with `ifTrue:ifFalse:` message and blocks
`info`       | Inserts info logging message
`kproc`      | Inserts snippet for finding process with some name and killing it
`repo`       | Inserts snippet for loading repository
`screenshot` | Inserts snippet for screenshot log message
`waitor`     | Inserts `waitUntil:or:then:` message with blocks.
`warning`    | Inserts warning log message
`write`      | Inserts `writeline:` message

Python
------

Snippets available in Python code are these (these are only available if syntax
is set to `Python`):

Snippet      | Explanation
-------------|-----------------------------------
`head`       | Inserts test header
`info`       | Inserts info log message
`repo`       | Inserts snippet for loading repository
`screenshot` | Inserts screenshot logging message
`ut`         | Inserts unittest class with predefined `setUp` and `tearDown`.
`wait`       | Inserts pattern for waiting until condition is satisfied
`warn`       | Inserts warning log message
