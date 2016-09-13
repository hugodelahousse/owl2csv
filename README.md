# ts-observe

A small tool to observe classes, properties and inheritance in ontologies

## Requirements:

* Jena >= 3.X installed and arq added to the path (check by running `arq --version`)
* Python >= 2.7 installed
* Being able to launch bash script

## Usage:

* `./ts-observe <ontology> <Observe query> <output file>`
* If you want the output file to use prefixes instead of the full uris, you have to document them in the FormatCSV.py file.
