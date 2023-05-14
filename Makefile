all: examples.pdf

%.pdf: %.tex %.bib
	xelatex $(basename $@)
	bibtex $(basename $@)
	xelatex $(basename $@)
	xelatex $(basename $@)
