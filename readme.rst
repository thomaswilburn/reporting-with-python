Data Reporting with Python
==========================

This repository contains sample data, homework reading, and data generation scripts for the 2016 Data Reporting with Python (COM499) class at UW. For this class, we'll be using `PythonAnywhere <http://pythonanywhere.com>`_. If you're working from home, the best starter kit is probably to install the `Miniconda <http://http://conda.pydata.org/miniconda.html>`_ distribution for your operating system, and use a Bash shell of some kind (Terminal on a Mac--on Windows, installing `Git <http://git-scm.com>`_ is a good way to start).

You can install this repo by running the following code::

    git clone https://github.com/thomaswilburn/reporting-with-python.git

Week one: basic Python skills
----------------------------

For the first day of class, we'll be learning the basics of writing and launching Python scripts. This includes using imports, variables, lists, and loops. We'll use these skills to process a directory of receipts, looking for any that match a given address.

Homework
~~~~~~~~

Read (and execute) the ``rps.py`` script in the ``samples`` directory, and add comments that explain what the script is doing on each line. Additionally, the script is actually broken: it will run, but the results are wrong in a subtle way. Can you find the bug? Add a comment at the end of the script describing the problem and the circumstances that cause it, or fix the bug inline if you feel ambitious.

Week two: processing CSV files
-----------------------------

Comma-separated values (CSV) files are the simplest building blocks of data exchange, and thus handling them is a fundamental skill for data journalists. This week, we'll learn how to use Python's CSV module to read in a large dataset, then scour it for interesting information.

Homework
~~~~~~~~

There's a second CSV file in the ``reporting-with-python/day2`` folder named ``animals.csv``, containing all records of Seattle animal imports for 2014. Using what we've learned in class, write a script that reads this file and answers the following questions:

* How many bears were imported? How many of each kind of bear?
* What country imports the greatest number of trophies (description of TRO)?
* Last year's Initiative 1401 banned the import (for resale purposes) of elephants, rhinoceros, tigers, lions, leopards, cheetahs, pangolins, marine turtles, sharks, and rays. How many of these animals were actually imported in Seattle in 2014 anyway?

Week three: regular expressions
------------------------------

There's no data reporting tool more powerful, more versatile, or more dangerous than regular expressions. Although we'll spend this class leveraging Python's ``re`` module to dissect text, you can use the basics of regex in any language--or even just from simple command-line tools without any programming at all.

Homework
~~~~~~~~

The following are real regular expressions that I've written in the last year for cleaning up data or working on projects. In plain English, explain what they do. Hint: it may be useful to load them into a Python file and test them, just to see if your explanation is correct.

* ``^([\d.]+) km (.*)$`` - used in a story about earthquake locations
* ``City of (.*?) Council (Position|District) No. (\d+)`` - from our 2015 election results scraper
* ``((\w+ ){0,2})@(\w+)(( \w+){0,2})`` - analyzing Twitter results from a search

Further reading
---------------

* `Python 3 Docs <https://docs.python.org/3/>`_
* `Learn Python the Hard Way <http://learnpythonthehardway.org/book/>`_
* `The Bastards Book of Regular Expressions <http://regex.bastardsbook.com/files/bastards-regexes.pdf>`_
* `The Quartz guide to bad data <https://github.com/Quartz/bad-data-guide>`_
* `How to interview a big pile of data <http://training.npr.org/visual/what-to-do-with-a-big-pile-of-data/>`_
