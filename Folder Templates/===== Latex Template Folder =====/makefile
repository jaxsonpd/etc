# @Breif: MakeFile for processing latex files
# @Author; Jack Duignan (JackpDuignan@gmail.com)

# Ensure that make is run in powershell to improve compatibility with linux and windows (rm vs del)
ifeq ($(OS),Windows_NT)
SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -Command
endif

$cleanup_includes_cusdep_generated = 1; # Stops latexmk from removing .pdf files (So that we can actually have a document after "make clean")

all: main.pdf

main.pdf: main.tex
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make main.tex

clean:
	latexmk -c
	rm main.bbl 
	rm main.run.xml
	