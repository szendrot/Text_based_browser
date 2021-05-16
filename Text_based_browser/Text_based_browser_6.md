Theory
Did you ever wonder whether it's possible to make your output colorful? The answer is yes, with the Colorama library allowing to colorize the text in the terminal. The colonizing is performed through special escape sequence characters and is visible to the users of MS Windows. For example, to print a red text, all you need is to do this:

from colorama import Fore
print(Fore.RED + 'red text')
Fore stands for the color of the text (as opposed to the color of the background, for example). Fore.RED adds a special escape sequence to the beginning of the string that allows to highlight it with red. Check out the documentation to see more.

Colorama is already installed in the project so you can feel free to use it.

Description
It’s not enough just to drop the tags. You also need to make your output legible. After all, we would like to have a user-friendly browser, right? In this stage, try to make your browser look more like a browser.

Almost every website contains links. Have you ever wondered why blue was chosen to highlight them?

One of the reasons lies in the physiology of the human eye. Red and green are detected by the same cells in the eye, and one of the most common forms of colorblindness is red-green colorblindness. It affects 7% of men and only 0.4% of women but combined that’s still an average of 1 in every 25 people overall. Nearly everyone can see blue, or, more accurately, almost everyone can distinguish blue as a color different from others.

Also, blue is the darkest color that does not reduce the readability of the text.

Objectives
Keep the functionality from the previous stages, but now make all links in your browser blue.

Each link should start with a new line and be highlighted with blue color.

Don't forget that the rest of the page's text should be printed too (but should not be highlighted).

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input


> https://docs.python.org
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


