# Install Homebrew

* Run `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` in the terminal
* Then run `brew install jena`
* Then `git clone http://github.com/Guhogu/owl2csv`
* Go to the owl2csv folder: `cd owl2csv`
* From this folder you can run `./owl2csv -d/--dataset <Ontologies> -q/--query <Observe query> -o/--output <output file> -p <prefix reference>`
* For example: `./owl2csv --dataset cdm.rdf euvoc.rdf org.rdf skos.rdf skos-xl.rdf vcard.rdf --query ObserveInheritance.rq --output output.csv -p prefixes.json`   
