LingTeX
=======

LingTeX is a package of simple macros I use to write linguistics research in TeX. They all have been tested with XeTeX (which is the best environment for linguists!) but should work with any TeX systems. See `examples.tex` and `examples.pdf` for sample usage.

dupe.py
-------

This runs a simple search for immediately repeated words. Sample use:
    
    ./dupe.py *.tex

simplex
-------

While not necessarily ideal for glossing, phonology and morphology data is best rendered using the `tabular` environment. The `example` environment wraps tabular data, placing an example number and a user-supplied label at the top. 

Usage: place `simplex.sty` in your working directory and add `\usepackage{simplex}` to your document preamble. This enables environments `example` and `unlabeledexample`. 

smooshedbib
-----------

Eliminates newlines between bibliography entries, but otherwise uses your choice of bibliography styles. I use this for abstracts for conferences like NELS.

Usage: place `smooshedbib.sty` in your working directory and add `\usepackage{smoooshedbib}` to your document preamble.
