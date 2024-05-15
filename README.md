## Material
### Realonline: 
Via REST-API: https://realonline.imareal.sbg.ac.at/api/data/work?apiKey=&detail=true&archivnr=000168 – wobei die archivnr. der jeweilige Datensatz ist.

Als RDF: [REALonline v. 1.1.7](https://realonline.imareal.sbg.ac.at/2022/01/12/realonline-im-rdf-format/) (sbg.ac.at)
### ITEM:
Inventare (ITEM/i): Als RDF (siehe ITEM-RDF.ttl). Mittlerweile sollten die Namespaces auch schon getrennt sein und nicht mehr beide „reo“ heißen.

Rechnungsbücher (ITEM/a): Auf Basis der Bookkeeping Ontology. Die sollten bis zum Workshop-Termin droben sein. Falls ihr die auch einbauen möchtet. Ich leite sie weiter, sobald sie da sind.

## ITEM I
### Summary
- The class thesaurus is well-defined with several instances, hierarchical relationships, comments, and metadata.
- It is a subclass of skos:Concept, indicating its role in knowledge representation.
- The thesaurus class has a range relationship indicating it expects thesaurus_term as the type of its objects.
- thesaurus is explicitly defined as a class with a type declaration.
