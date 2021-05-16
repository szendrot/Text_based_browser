Description
Now it is important for us to present the resulting "text" in a form that is convenient for the user.

If you’re not familiar with HTML, here's a short explanation. When working on the previous task, you probably noticed a lot of <div>, <script>, or <p> “words” on the displayed web page. These are called tags. Browsers need tags to know how exactly to show the page. For example, the website could include headers that look different from the rest of the text. Also, it could have links that are highlighted in blue, and the cursor could look like a pointing finger when it hovers over the link. Tags are used to help the browser identify where the links are, where an image should be, and so on.

Tags are necessary for the browser but aren’t useful for users. Most tags are paired. For example: <p>Some text</p>, where <p> is an opening tag and </p> is a closing tag. Your browser should only display “Some text”, without <p> and </p>.

Each tag has its own purpose: <p> for text, <h1> <h2> … <h6> for headers, <a> for links, <ul> <ol> <li> for lists.

Also, in this stage, try to make your program be able to handle incorrect URLs: for example, if an address without a dot and a top-level domain following it (for example, google and not google.com) is entered, your program should output a line Incorrect URL. Note that if you pass an incorrect URL to the method get(), it'll throw an exception called requests.exceptions.ConnectionError.

Objectives
In this stage, you need to extract and output the content between these tags. No more <div>, <script>, <p> and so on, just a clear readable text! Your browser should display only the content of a limited list of tags (<p>, headers, <a> and <ul>, <ol>, <li>) without showing the tags themselves.

Use the library beautifulsoup4 to make these changes. This library is already installed in your project.

To pass the tests, it's enough to simply find the function allowing us to extract the human-readable text from a web page. If you’re curious, feel free to browse through some more information about parsing!

When an invalid URL is entered (URL without a dot and a top-level domain name), the program should output Incorrect URL.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

> python browser.py dir-for-files
> docs.python.org
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
> exit