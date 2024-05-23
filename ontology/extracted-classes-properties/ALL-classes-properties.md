### Namespaces
@prefix description: <http://realonline.imareal.sbg.ac.at/rdf/v1/description/> .
@prefix entity: <http://realonline.imareal.sbg.ac.at/rdf/v1/description/entity/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix realonline: <http://realonline.imareal.sbg.ac.at/rdf/v1/> .
@prefix relation: <http://realonline.imareal.sbg.ac.at/rdf/v1/ontology/relation/> .
@prefix ro_ont: <http://realonline.imareal.sbg.ac.at/rdf/v1/ontology/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix thesaurus: <http://realonline.imareal.sbg.ac.at/rdf/v1/thesaurus/> .
@prefix work: <http://realonline.imareal.sbg.ac.at/rdf/v1/work/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

### Class
- ro_ont:Entity_handlung: Represents an action or activity.
- ro_ont:Entity_historort: Represents a historical location.
- ro_ont:Entity_kleidung: Represents a type of clothing.
- ro_ont:Entity_koerperteil: Represents a part of the body.
- ro_ont:Entity_objekt: Represents an object.
- ro_ont:Entity_originalzitat: Represents an original quote.
- ro_ont:Entity_ort: Represents a place.
- ro_ont:Entity_person: Represents a person.
- ro_ont:Entity_szene: Represents a scene.
- ro_ont:description: Represents a description.
- ro_ont:entity: Represents an entity.
- ro_ont:thesaurus: Represents a thesaurus.
- ro_ont:thesaurus_term: Represents a term in the thesaurus.
- ro_ont:value: Represents a value.
- ro_ont:work: Represents a work.
- skos:Concept: Represents a SKOS concept.
- ro_ont:thesaurus_entry: Represents an entry in the thesaurus.
- ro_ont:Entity_text: Represents a text entity.
- ro_ont:Entity_marginalia: Represents a marginalia entity.
- ro_ont:Entity_object: Represents an object entity.
- ro_ont:Entity_quality: Represents a quality entity.
- ro_ont:Entity_locrelator: Represents a locrelator entity.
- ro_ont:Entity_item: Represents an item entity.
- ro_ont:Entity_time: Represents a time entity.
- ro_ont:Entity_image: Represents an image entity.
- ro_ont:Entity_material: Represents a material entity.
- ro_ont:Entity_processing: Represents a processing entity.
- ro_ont:Entity_ornament: Represents an ornament entity.
- ro_ont:Entity_room: Represents a room entity.
- ro_ont:Entity_objectbio: Represents an object biography entity.
- ro_ont:Entity_action: Represents an action entity.
- ro_ont:Entity_heraldic: Represents a heraldic entity.
- ro_ont:Entity_origin: Represents an origin entity.

### Property
- ro_ont:archivnr (Domain: ro_ont:work, Range: xsd:string) - Archive number associated with a work.
- ro_ont:bildthema (Domain: ro_ont:work, Range: xsd:string) - Image theme associated with a work.
- ro_ont:comments (Domain: ro_ont:value, Range: rdf:List) - Comments associated with a value.
- ro_ont:contains_entity (Domain: ro_ont:description, Range: ro_ont:entity) - Contains entity within a description.
- ro_ont:dianr (Domain: ro_ont:work, Range: xsd:string) - DIA number associated with a work.
- ro_ont:ensemblenr (Domain: ro_ont:work, Range: xsd:string) - Ensemble number associated with a work.
- ro_ont:has_description (Domain: ro_ont:work, Range: ro_ont:description) - Has a description for a work.
- ro_ont:has_thesaurus_entry (Domain: ro_ont:value, Range: ro_ont:thesaurus_entry) - Has an entry in the thesaurus for a value.
- ro_ont:index (Domain: ro_ont:work, Range: xsd:positiveInteger) - Index associated with a work.
- ro_ont:raumordnung_id (Domain: ro_ont:work, Range: xsd:string) - Raumordnung ID associated with a work.
- ro_ont:relation/abschnitt_objekt_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: section object reference for an entity.
- ro_ont:relation/abschnitt_person_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: section person reference for an entity.
- ro_ont:relation/abschnitt_raum_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: section space reference for an entity.
- ro_ont:relation/inventar_abschnitt_child (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: inventory section child for an entity.
- ro_ont:relation/inventar_person_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: inventory person reference for an entity.
- ro_ont:relation/inventar_raum_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: inventory space reference for an entity.
- ro_ont:relation/objekt_mass_child (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object mass child for an entity.
- ro_ont:relation/objekt_objekt_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object to object reference for an entity.
- ro_ont:relation/objekt_objektbewertung_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object evaluation contains an entity.
- ro_ont:relation/objekt_objekteigenschaft_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object property contains an entity.
- ro_ont:relation/objekt_objektfarbe_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object color contains an entity.
- ro_ont:relation/objekt_objektformelement_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object form element contains an entity.
- ro_ont:relation/objekt_objektherstellungstechnik_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object manufacturing technique contains an entity.
- ro_ont:relation/objekt_objektmaterial_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object material contains an entity.
- ro_ont:relation/objekt_objektmenge_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object quantity contains an entity.
- ro_ont:relation/objekt_objektsonstiges_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: object miscellaneous contains an entity.
- ro_ont:relation/ort_raum_child (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: place to space child for an entity.
- ro_ont:relation/raum_objekt_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space to object reference for an entity.
- ro_ont:relation/raum_raum_bezug (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space to space reference for an entity.
- ro_ont:relation/raum_raumbewertung_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space evaluation contains an entity.
- ro_ont:relation/raum_raumeigenschaft_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space property contains an entity.
- ro_ont:relation/raum_raumfarbe_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space color contains an entity.
- ro_ont:relation/raum_raumformelement_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space form element contains an entity.
- ro_ont:relation/raum_raumherstellungstechnik_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space manufacturing technique contains an entity.
- ro_ont:relation/raum_raummaterial_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space material contains an entity.
- ro_ont:relation/raum_raummenge_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space quantity contains an entity.
- ro_ont:relation/raum_raumsonstiges_contains (Domain: ro_ont:entity, Range: ro_ont:entity) - Relationship: space miscellaneous contains an entity.
- ro_ont:workreference (Domain: ro_ont:work, Range: xsd:string) - Work reference for a work.
- ro_ont:text_marginalia_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_marginalia) - Child marginalia entity related to text.
- ro_ont:text_object_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_object) - Child object entity related to text.
- ro_ont:text_quality_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_quality) - Child quality entity related to text.
- ro_ont:code (Domain: ro_ont:entity, Range: xsd:string) - Code associated with an entity.
- ro_ont:has_description (Domain: ro_ont:work, Range: ro_ont:description) - Has a description for a work.
- ro_ont:authority_file (Domain: ro_ont:entity, Range: xsd:string) - Authority file for an entity.
- ro_ont:text_locrelator_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_locrelator) - Child locrelator entity related to text.
- ro_ont:bildthema (Domain: ro_ont:work, Range: xsd:string) - Image theme associated with a work.
- ro_ont:text_item_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_item) - Child item entity related to text.
- ro_ont:dianr (Domain: ro_ont:work, Range: xsd:string) - DIA number associated with a work.
- ro_ont:text_person_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_person) - Child person entity related to text.
- ro_ont:has_thesaurus_entry (Domain: ro_ont:value, Range: ro_ont:thesaurus_entry) - Has an entry in the thesaurus for a value.
- ro_ont:text_time_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_time) - Child time entity related to text.
- ro_ont:index (Domain: ro_ont:work, Range: xsd:positiveInteger) - Index associated with a work.
- ro_ont:text_image_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_image) - Child image entity related to text.
- ro_ont:text_material_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_material) - Child material entity related to text.
- ro_ont:text_processing_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_processing) - Child processing entity related to text.
- ro_ont:text_ornament_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_ornament) - Child ornament entity related to text.
- ro_ont:archivnr (Domain: ro_ont:work, Range: xsd:string) - Archive number associated with a work.
- ro_ont:text_room_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_room) - Child room entity related to text.
- ro_ont:text_objectbio_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_objectbio) - Child object bio entity related to text.
- ro_ont:thesaurus_entry (Domain: ro_ont:thesaurus, Range: ro_ont:thesaurus_term) - Entry in the thesaurus.
- ro_ont:prov (Domain: ro_ont:entity, Range: xsd:string) - Provenance associated with an entity.
- ro_ont:has_id (Domain: ro_ont:entity, Range: xsd:string) - ID associated with an entity.
- ro_ont:text_action_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_action) - Child action entity related to text.
- ro_ont:text (Domain: ro_ont:entity, Range: xsd:string) - Text associated with an entity.
- ro_ont:text_heraldic_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_heraldic) - Child heraldic entity related to text.
- ro_ont:forename (Domain: ro_ont:Entity_person, Range: xsd:string) - Forename of a person.
- ro_ont:contains_entity (Domain: ro_ont:description, Range: ro_ont:entity) - Contains entity within a description.
- ro_ont:surname (Domain: ro_ont:Entity_person, Range: xsd:string) - Surname of a person.
- ro_ont:text_origin_child (Domain: ro_ont:Entity_text, Range: ro_ont:Entity_origin) - Child origin entity related to text.
- ro_ont:standard_nhg (Domain: ro_ont:entity, Range: xsd:string) - Standard NHG associated with an entity.
- ro_ont:normalisation (Domain: ro_ont:entity, Range: xsd:string) - Normalization associated with an entity.
- ro_ont:bundesland
- ro_ont:datierung
- ro_ont:ensemble
- ro_ont:fol
- ro_ont:enstehungsort
- ro_ont:form
- ro_ont:institution
- ro_ont:invnr
- ro_ont:literatur
- ro_ont:objektart
- ro_ont:post
- ro_ont:provenienz
- ro_ont:quelle
- ro_ont:staat
- ro_ont:technik
- ro_ont:farbe
- ro_ont:sex
- relation:handlung_person_bezug
- relation:kleidung_kleidung_child
- relation:kleidung_kleidung_hat_bezug
- relation:kleidung_objekt_bezug
- relation:kleidung_objekt_hat_bezug
- relation:kleidung_originalzitat_child
- relation:koerperteil_koerperteil_child
- relation:koerperteil_objekt_child
- relation:koerperteil_originalzitat_child
- relation:objekt_objekt_bezug
- relation:objekt_objekt_child
- relation:objekt_objekt_hat_bezug
- relation:objekt_originalzitat_child
- relation:person_kleidung_child
- relation:person_koerperteil_child
- relation:person_objekt_attribut
- relation:person_objekt_bezug
- relation:person_objekt_child
- relation:person_objekt_hat_bezug
- relation:person_person_bezug
- relation:szene_handlung_child
- relation:szene_historort_child
- relation:szene_objekt_child
- relation:szene_ort_child
- relation:szene_person_child

### example

´´´
work:003971B a ro_ont:work;
  ro_ont:ante realonline:value_417466;
  ro_ont:archivnr "003971B";
  ro_ont:bildthema realonline:value_417451;
  ro_ont:bundesland realonline:value_417459;
  ro_ont:datierung realonline:value_417469;
  ro_ont:dianr realonline:value_417465;
  ro_ont:ensemble realonline:value_417453;
  ro_ont:enstehungsort realonline:value_417464;
  ro_ont:fol realonline:value_417452;
  ro_ont:form realonline:value_417467;
  ro_ont:has_description description:003971B_4906;
  ro_ont:institution realonline:value_417457;
  ro_ont:invnr realonline:value_417454;
  ro_ont:literatur realonline:value_417455;
  ro_ont:objektart realonline:value_417463;
  ro_ont:post realonline:value_417458;
  ro_ont:provenienz realonline:value_417456;
  ro_ont:quelle realonline:value_417468;
  ro_ont:staat realonline:value_417460;
  ro_ont:standort realonline:value_417461;
  ro_ont:technik realonline:value_417462;
  rdfs:label "003971B - Elija und die Witwe von Sarepta" .

realonline:value_417466 a ro_ont:value;
  ro_ont:index "1"^^xsd:int;
  rdf:value "1351";
  rdfs:label "1351 (Ante)" .

realonline:value_417451 a ro_ont:value;
  ro_ont:has_thesaurus_entry thesaurus:bildthema_elija_und_die_witwe_von_sarepta;
  ro_ont:index "1"^^xsd:int;
  rdf:value "Elija und die Witwe von Sarepta";
  rdfs:label "Elija und die Witwe von Sarepta (Bildthema)" .

realonline:value_417459 a ro_ont:value;
  ro_ont:has_thesaurus_entry thesaurus:bundesland_niederösterreich;
  ro_ont:index "1"^^xsd:int;
  rdf:value "Niederösterreich";
  rdfs:label "Niederösterreich (Bundesland)" .

realonline:value_417469 a ro_ont:value;
  ro_ont:index "1"^^xsd:int;
  rdf:value "1349-1351";
  rdfs:label "1349-1351 (Datierung)" .

realonline:value_417465 a ro_ont:value;
  ro_ont:index "1"^^xsd:int;
  rdf:value "7004821";
  rdfs:label "7004821 (Dia-Nr.)" .

realonline:value_417453 a ro_ont:value;
  ro_ont:index "1"^^xsd:int;
  rdf:value "Concordantiae caritatis";
  rdfs:label "Concordantiae caritatis (Ensemble)" .

realonline:value_417464 a ro_ont:value;
  ro_ont:has_thesaurus_entry thesaurus:entstehungsort_lilienfeld;
  ro_ont:index "1"^^xsd:int;
  rdf:value "Lilienfeld";
  rdfs:label "Lilienfeld (Entstehungsort/-gebiet)" .

realonline:value_417452 a ro_ont:value;
  ro_ont:index "1"^^xsd:int;
  rdf:value "fol. 89v";
  rdfs:label "fol. 89v (Fol)" .

realonline:value_417467 a ro_ont:value;
  ro_ont:has_thesaurus_entry thesaurus:form_work_miniatur;
  ro_ont:index "1"^^xsd:int;
  rdf:value "Miniatur";
  rdfs:label "Miniatur (Form/Gestaltung Einzelbild)" .

description:003971B_4906 ro_ont:contains_entity entity:003971B_4906_E1, entity:003971B_4906_E10,
    entity:003971B_4906_E11, entity:003971B_4906_E12, entity:003971B_4906_E13, entity:003971B_4906_E14,
    entity:003971B_4906_E15, entity:003971B_4906_E16, entity:003971B_4906_E17, entity:003971B_4906_E18,
    entity:003971B_4906_E19, entity:003971B_4906_E2, entity:003971B_4906_E20, entity:003971B_4906_E21,
    entity:003971B_4906_E22, entity:003971B_4906_E23, entity:003971B_4906_E3, entity:003971B_4906_E4,
    entity:003971B_4906_E5, entity:003971B_4906_E6, entity:003971B_4906_E7, entity:003971B_4906_E8;
  a ro_ont:description;
  ro_ont:contains_entity entity:003971B_4906_E9;
  rdfs:Class ro_ont:description .

entity:003971B_4906_E1 ro_ont:has_id "E1";
  relation:szene_handlung_child entity:003971B_4906_E2;
  relation:szene_objekt_child entity:003971B_4906_E21, entity:003971B_4906_E22;
  relation:szene_person_child entity:003971B_4906_E12;
  a ro_ont:Entity_szene, ro_ont:entity;
  relation:szene_person_child entity:003971B_4906_E3 .

entity:003971B_4906_E21 ro_ont:farbe realonline:value_417506;
  ro_ont:has_id "E21";
  a ro_ont:Entity_objekt, ro_ont:entity;
  ro_ont:name realonline:value_417507 .

entity:003971B_4906_E12 ro_ont:has_id "E12";
  relation:person_kleidung_child entity:003971B_4906_E18, entity:003971B_4906_E20;
  relation:person_koerperteil_child entity:003971B_4906_E13, entity:003971B_4906_E14;
  relation:person_objekt_child entity:003971B_4906_E15;
  ro_ont:sex realonline:value_417489;
  a ro_ont:Entity_person, ro_ont:entity;
  ro_ont:sname realonline:value_417488 .

thesaurus:gegenstand_fliesenboden a ro_ont:thesaurus_term;
  rdf:value "Fliesenboden";
  rdfs:label "Fliesenboden";
  skos:broader thesaurus:gegenstand_gebäudeteil_-_boden .
´´´