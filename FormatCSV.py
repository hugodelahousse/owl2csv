#!/bin/bash/python
import sys
prefixDict = {
    "rdfs": "<http://www.w3.org/2000/01/rdf-schema#>",
    "owl": "<http://www.w3.org/2002/07/owl#>",
    "event": "<http://purl.org/NET/c4dm/event.owl#>",
    "xmlsn": "<http://xmlns.com/foaf/0.1/familyName>",
    "xsd": "<http://www.w3.org/2001/XMLSchema#>",
    "afn": "<http://jena.apache.org/ARQ/function#>",
    "cdm": "<http://publications.europa.eu/ontology/cdm>",
    "frbr": "<http://erlangen-crm.org/current/>",
    "skos": "<http://www.w3.org/2004/02/skos/core#>",
    "frbroo":"<http://erlangen-crm.org/efrbroo/>",
    "doremus":"<http://data.doremus.org/ontology#>",
   

}

if len(sys.argv) < 2:
    print("Input file not found")
    exit()

filename = sys.argv[1]
with open(filename, "r") as f:
    data = f.read()
    for prefix, uri in prefixDict.iteritems():
        data = data.replace(uri[1:-1], prefix+":")
with open(filename, "w") as f:
    f.write(data)
