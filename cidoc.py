"""The implemented class hierarchy MUST not be confused with the CIDOC-CRM class hierarchy! There might be some classes
in between that have not been implemented.

"""
import logging
from rdflib import Namespace, URIRef, Literal, XSD
from entity import Entity

# this should be CIDOCNAMESPACE
CIDOCNAMESPACE = "http://www.cidoc-crm.org/cidoc-crm/"
CRM = Namespace(CIDOCNAMESPACE)


class E1CRMEntity(Entity):
    """ E1 CRM Entity

    P1 is identified by (identifies): E41 Appellation P2 has type (is type of): E55 Type
    P3 has note: E62 String
    (P3.1 has type: E55 Type) [Not implemented]
    P48 has preferred identifier (is preferred identifier of): E42 Identifier
    P137 exemplifies (is exemplified by): E55 Type
    (P137.1 in the taxonomic role: E55 Type) [Not implemented]

    Inverse: P140i was attributed by (assigned attribute to): E13 Attribute Assignment
    P141i was assigned by (assigned): E13 Attribute Assignment
    """

    class_uri = CIDOCNAMESPACE + "E1_CRM_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p1_is_identified_by(self, *entities, uris: list = None) -> bool:
        """P1 is identified by (identifies): E41 Appellation

        Add triples "P1 is identified by" and inverse to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = CRM.P1_is_identified_by
        prop_inverse = CRM.P1i_identifies

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p2_has_type(self, *entities, uris: list = None) -> bool:
        """P2 has type (is type of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P2_has_type
        prop_inverse = CRM.P2i_is_type_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p3_has_note(self, content: str, lang: str = None) -> bool:
        """P3 has note: E62 String

        Args:
            content (str): Textual content of the note
            lang (str, optional): Language of the note. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = CRM.P3_has_note

        if lang:
            self.graph.add((URIRef(self.uri), prop, Literal(content, lang=lang)))
        else:
            self.graph.add((URIRef(self.uri), prop, Literal(content)))

        return True

    def p48_has_preferred_identifier(self, *entities, uris: list = None) -> bool:
        """P48 has preferred identifier (is preferred identifier of): E42 Identifier

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P48_has_preferred_identifier
        prop_inverse = CRM.P48i_is_preferred_identifier_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p137_exemplifies(self, *entities, uris: list = None) -> bool:
        """P137 exemplifies( is exemplified by): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P137_exemplifies
        prop_inverse = CRM.P137i_is_exemplified_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p140i_was_attributed_by(self, *entities, uris: list = None) -> bool:
        """P140i was attributed by (assigned attribute to): E13 Attribute Assignment

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P140i_was_attributed_by
        prop_inverse = CRM.P140_assigned_attribute_to

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p141i_was_assigned_by(self, *entities, uris: list = None) -> bool:
        """P141i was assigned by (assigned): E13 Attribute Assignment

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P141i_was_assigned_by
        prop_inverse = CRM.P141_assigned

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E77PersistentItem(E1CRMEntity):
    """E77 Persistent Item

    SubClassOf E1 CRM Entity

    The class E77 Persistent Item does not have any specialized properties.
    """
    class_uri = CIDOCNAMESPACE + "E77_Persistent_Item"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class E70Thing(E77PersistentItem):
    """E70 Thing

    SubClassOf E77_Persistent_Item

    P43 has dimension (is dimension of): E54 Dimension
    P101 had as general use (was use of): E55 Type
    P130 shows features of (features are also found on): E70 Thing
    (P130.1 kind of similarity: E55 Type) [Not implemented]

    Inverse: P16i was used for (used specific object): E7 Activity
    """
    class_uri = CIDOCNAMESPACE + "E70_Thing"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p43_has_dimension(self, *entities, uris: list = None) -> bool:
        """P43 has dimension (is dimension of): E54 Dimension

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P43_has_dimension
        prop_inverse = CRM.P43i_is_dimension_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p101_had_as_general_use(self, *entities, uris: list = None) -> bool:
        """P101 had as general use (was use of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P101_had_as_general_use
        prop_inverse = CRM.P101i_was_use_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p130_shows_features_of(self, *entities, uris: list = None) -> bool:
        """P130 shows features of (features are also found on): E70 Thing

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P130_shows_features_of
        prop_inverse = CRM.P130i_features_are_also_found_on

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p16i_was_used_for(self, *entities, uris: list = None) -> bool:
        """P16i was used for (used specific object): E7 Activity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P16i_was_used_for
        prop_inverse = CRM.P16_used_specific_object

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E71HumanMadeThing(E70Thing):
    """E71 Human-Made Thing

    subClassOf E70 Thing

    P102 has title (is title of): E35 Title
    (P102.1 has type: E55 Type) [Not implemented]
    P103 was intended for (was intention of): E55 Type
    """

    class_uri = CIDOCNAMESPACE + "E71_Human-Made_Thing"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p102_has_title(self, *entities, uris: list = None) -> bool:
        """P102 has title (is title of): E35 Title

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P102_has_title
        prop_inverse = CRM.P102i_is_title_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p103_was_intended_for(self, *entities, uris: list = None) -> bool:
        """P103 was intended for (was intention of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P103_was_intended_for
        prop_inverse = CRM.P103i_was_intention_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E28ConceptualObject(E71HumanMadeThing):
    """E28 Conceptual Object

    SubClassOf E71 Human-Made Thing
    E28 does not have specialized properties.

    Inverse: P94i was created by (has created): E65 Creation
    """

    class_uri = CIDOCNAMESPACE + "E28_Conceptual_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p94i_was_created_by(self, *entities, uris: list = None) -> bool:
        """P94i was created by (has created): E65 Creation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P94i_was_created_by
        prop_inverse = CRM.P94_has_created

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E89PropositionalObject(E28ConceptualObject):
    """E89 Propositional Object

    SubClassOf E28 Conceptual Object

    P148 has component (is component of): E89 Propositional Object
    P67 refers to (is referred to by): E1 CRM Entity
    (P67.1 has type: E55 Type) [Not implemented]
    P129 is about (is subject of): E1 CRM Entity
    """

    class_uri = CIDOCNAMESPACE + "E89_Propositional_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p148_has_component(self, *entities, uris: list = None) -> bool:
        """P148 has component (is component of): E89 Propositional Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P148_has_component
        prop_inverse = CRM.P148i_is_component_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p67_refers_to(self, *entities, uris: list = None) -> bool:
        """P67 refers to (is referred to by): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P67_refers_to
        prop_inverse = CRM.P67i_is_referred_to_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p129_is_about(self, *entities, uris: list = None) -> bool:
        """P129 is about (is subject of): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P129_is_about
        prop_inverse = CRM.P129i_is_subject_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E72LegalObject(E70Thing):
    """E72 Legal Object

    SubClassOf E70 Thing

    P104 is subject to (applies to): E30 Right [inherited from E72 Legal Object]
    P105 right held by (has right on): E39 Actor [inherited from E72 Legal Object]
    """

    class_uri = CIDOCNAMESPACE + "E72_Legal_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p104_is_subject_to(self, *entities, uris: list = None) -> bool:
        """P104 is subject to (applies to): E30 Right [inherited from E72 Legal Object]

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P104_is_subject_to
        prop_inverse = CRM.P104i_applies_to

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p105_ight_held_by(self, *entities, uris: list = None) -> bool:
        """P105 right held by (has right on): E39 Actor [inherited from E72 Legal Object]

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P105_right_held_by
        prop_inverse = CRM.P105i_has_right_on

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E90SymbolicObject(E28ConceptualObject, E72LegalObject):
    """E90 Symbolic Object

    SubClassOf E28 Conceptual Object AND E72 Legal Object.

    P106 is composed of (forms part of): E90 Symbolic Object
    P190 has symbolic content: E62 String
    """

    class_uri = CIDOCNAMESPACE + "E90_Symbolic_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p106_is_composed_of(self, *entities, uris: list = None) -> bool:
        """P106 is composed of (forms part of): E90 Symbolic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P106_is_composed_of
        prop_inverse = CRM.P106i_forms_part_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p190_has_symbolic_content(self, content: str, lang: str = None) -> bool:
        """P190 has symbolic content: E62 String

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = CRM.P190_has_symbolic_content

        if lang:
            self.graph.add((URIRef(self.uri), prop, Literal(content, lang=lang)))
        else:
            self.graph.add((URIRef(self.uri), prop, Literal(content)))

        return True


class E73InformationObject(E90SymbolicObject, E89PropositionalObject):
    """E73 Information Object

    SubClassOf E90 Symbolic Object AND E89 Propositional Object

    P165 incorporates (is incorporated in): E90 Symbolic Object

    """

    class_uri = CIDOCNAMESPACE + "E73_Information_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p165_incorporates(self, *entities, uris: list = None) -> bool:
        """P165 incorporates (is incorporated in): E90 Symbolic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P165_incorporates
        prop_inverse = CRM.P165i_is_incorporated_in

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E29DesignOrProcedure(E73InformationObject):
    """E29 Design or Procedure

    subClassOf E73 Information Object

    P68 foresees use of (use foreseen by): E57 Material [Not implemented]
    P69 has association with (is associated with): E29 Design or Procedure
    (P69.1 has type: E55 Type) [Not implemented]

    Inverse: P33 used specific technique (was used by): E29 Design or Procedure
    """
    class_uri = CIDOCNAMESPACE + "E29_Design_or_Procedure"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p69_has_association_with(self, *entities, uris: list = None) -> bool:
        """P69 has association with (is associated with): E29 Design or Procedure

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P69_has_association_with
        prop_inverse = CRM.P69i_is_associated_with

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p33i_was_used_by(self, *entities, uris: list = None) -> bool:
        """P33i was used by (used specific technique): E7 Activity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P33i_was_used_by
        prop_inverse = CRM.P33_used_specific_technique

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E33LinguisticObject(E73InformationObject):
    """E33 Linguistic Object

    subClassOf E73 Information Object

    P72 has language (is language of): E56 Language
    P73 has translation (is translation of): E33 Linguistic Object
    """

    class_uri = CIDOCNAMESPACE + "E33_Linguistic_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p72_has_language(self, *entities, uris: list = None) -> bool:
        """P72 has language (is language of): E56 Language

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P72_has_language
        prop_inverse = CRM.P72i_is_language_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p73_has_translation(self, *entities, uris: list = None) -> bool:
        """P73 has translation (is translation of): E33 Linguistic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P73_has_translation
        prop_inverse = CRM.P73i_is_translation_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E41Appellation(E90SymbolicObject):
    """E41 Appellation

    subClassOf E90 Symbolic Object

    P139 has alternative form: E41 Appellation
    Implemented inverse: P1i_identifies: E1 CRM Entity
    """

    class_uri = CIDOCNAMESPACE + "E41_Appellation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p139_has_alternative_form(self, *entities, uris: list = None) -> bool:
        """P139 has alternative form: E41 Appellation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P139_has_alternative_form
        prop_inverse = CRM.P139i_is_alternative_form_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p1i_identifies(self, *entities, uris: list = None) -> bool:
        """P1i identifies (is identified by): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P1i_identifies
        prop_inverse = CRM.P1_is_identified_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E42Identifier(E41Appellation):
    """E42 Identifier

    SubClassOf E41 Appellation

    No specialized properties.
    """

    class_uri = CIDOCNAMESPACE + "E42_Identifier"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class E35Title(E41Appellation, E33LinguisticObject):
    """E35 Title

    SubClassOf E41 Appellation AND E33 Linguistic Object

    No specialized properties.
    Inverse: P102i is title of (has title): E71 Human-Made Thing
    """
    class_uri = CIDOCNAMESPACE + "E35_Title"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p102i_is_title_of(self, *entities, uris: list = None) -> bool:
        """P102i is title of (has title): E71 Human-Made Thing

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P102i_is_title_of
        prop_inverse = CRM.P102_has_title

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E55Type(E28ConceptualObject):
    """E55 Type

    SubClassOf E28 Conceptual Object

    P127 has broader term (has narrower term): E55 Type
    P150 defines typical parts of (define typical wholes for): E55 Type

    Implemented inverse: P2i is type of: E1 CRM Entity
    P125i was type of object used in (used object of type) E7 Activity
    """

    class_uri = CIDOCNAMESPACE + "E55_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p127_has_broader_term(self, *entities, uris: list = None) -> bool:
        """P127 has broader term (has narrower term): E55 Type

        Implemented in both directions, see self.has_broader_term

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P127_has_broader_term
        prop_inverse = CRM.P127i_has_narrower_term

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p127i_has_narrower_term(self, *entities, uris: list = None) -> bool:
        """P127i has narrower term (has broader term): E55 Type

        Implemented in both directions, see self.has_broader_term

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P127i_has_narrower_term
        prop_inverse = CRM.P127_has_broader_term

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p150_defines_typical_parts_of(self, *entities, uris: list = None) -> bool:
        """P150 defines typical parts of (defines typical wholes for): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P150_defines_typical_parts_of
        prop_inverse = CRM.P150i_defines_typical_wholes_for

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p150i_defines_typical_wholes_for(self, *entities, uris: list = None) -> bool:
        """P150i defines typical wholes for (defines typical parts of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P150i_defines_typical_wholes_for
        prop_inverse = CRM.P150_defines_typical_parts_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p2i_is_type_of(self, *entities, uris: list = None) -> bool:
        """P2i is type of (has type): E1 CRM Entity

        Implemented in both directions, see self.has_type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P2i_is_type_of
        prop_inverse = CRM.P2_has_type

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p125i_was_type_of_object_used_in(self, *entities, uris: list = None) -> bool:
        """P125i was type of object used in (used object of type) E7 Activity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P125i_was_type_of_object_used_in
        prop_inverse = CRM.P125_used_object_of_type

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E56Language(E55Type):
    """E56 Language

    subClassOf E55 Type

    No specialized properties.

    Inverse: P72i_is_language_of (has language): E33 Linguistic Object
    """

    class_uri = CIDOCNAMESPACE + "E56_Language"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p72i_is_language_of(self, *entities, uris: list = None) -> bool:
        """P72i is language of (has language): E33 Linguistic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P72i_is_language_of
        prop_inverse = CRM.P72_has_language

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E58MeasurementUnit(E55Type):
    """E58 Measurement Unit

    subClassOf E55 Type

    No specialized properties.
    """

    class_uri = CIDOCNAMESPACE + "E58_Measurement_Unit"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class E2TemporalEntity(E1CRMEntity):
    """E2 Temporal Entity

    subClassOf E1 CRM Entity

    P4 has time-span (is time-span of): E52 Time-Span
    P173 starts before or with the end of (ends after or with the start of): E2 Temporal Entity [Not implemented]
    P174 starts before the end of (ends after the start of): E2 Temporal Entity [Not implemented]
    P175 starts before or with the start of (starts after or with the start of): E2 Temporal Entity [Not implemented]
    P176 starts before the start of (starts after the start of): E2 Temporal Entity [Not implemented]
    P182 ends before or with the start of (starts after or with the end of): E2 Temporal Entity [Not implemented]
    P183 ends before the start of (starts after the end of): E2 Temporal Entity [Not implemented]
    P184 ends before or with the end of (ends with or after the end of): E2 Temporal Entity [Not implemented]
    P185 ends before the end of (ends after the end of): E2 Temporal Entity [Not implemented]

    """
    class_uri = CIDOCNAMESPACE + "E2_Temporal_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p4_has_timespan(self, *entities, uris: list = None) -> bool:
        """P4 has time-span (is time-span of): E52 Time-Span

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM["P4_has_time-span"]
        prop_inverse = CRM["P4i_is_time-span_of"]

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E4Period(E2TemporalEntity):
    """E4 Period

    P7 took place at (witnessed): E53 Place
    P8 took place on or within (witnessed): E18 Physical Thing [Not implemented]
    P9 consists of (forms part of): E4 Period

    This is there because of the examples: Italian Renaissance (Macdonald, 1992), Sturm und Drang (Berkoff, 2013),
    Cubism (Cox, 2000), ...
    """

    class_uri = CIDOCNAMESPACE + "E4_Period"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p7_took_place_at(self, *entities, uris: list = None) -> bool:
        """P7 took place at (witnessed): E53 Place

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P7_took_place_at
        prop_inverse = CRM.P7i_witnessed

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p9_consists_of(self, *entities, uris: list = None) -> bool:
        """P9 consists of (forms part of): E4 Period

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P9_consists_of
        prop_inverse = CRM.P9i_forms_part_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E5Event(E4Period):
    """E5 Event
    SubClassOf E4 Period

    P11 had participant (participated in): E39 Actor
    P12 occurred in the presence of (was present at): E77 Persistent Item
    """

    class_uri = CIDOCNAMESPACE + "E5_Event"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p11_had_participant(self, *entities, uris: list = None) -> bool:
        """P11 had participant (participated in): E39 Actor

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P11_had_participant
        prop_inverse = CRM.P11i_participated_in

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p12_occurred_in_the_presence_of(self, *entities, uris: list = None) -> bool:
        """P12 occurred in the presence of (was present at): E77 Persistent Item

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P12_occurred_in_the_presence_of
        prop_inverse = CRM.P12i_was_present_at

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E7Activity(E5Event):
    """E7 Activity

    SubClassOf E5 Event

    P14 carried out by (performed): E39 Actor
    (P14.1 in the role of: E55 Type) [Not implemented]
    P15 was influenced by (influenced): E1 CRM Entity
    P16 used specific object (was used for): E70 Thing
    (P16.1 mode of use: E55 Type) [Not implemented]
    P17 was motivated by (motivated): E1 CRM Entity
    P19 was intended use of (was made for): E71 Human-Made Thing
    (P19.1 mode of use: E55 Type) [Not implemented]
    P20 had specific purpose (was purpose of): E5 Event
    P21 had general purpose (was purpose of): E55 Type
    P32 used general technique (was technique of): E55 Type
    P33 used specific technique (was used by): E29 Design or Procedure
    P125 used object of type (was type of object used in): E55 Type
    """

    class_uri = CIDOCNAMESPACE + "E7_Activity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p14_carried_out_by(self, *entities, uris: list = None) -> bool:
        """P14 carried out by (performed): E39 Actor

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P14_carried_out_by
        prop_inverse = CRM.P14i_performed

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p15_was_influenced_by(self, *entities, uris: list = None) -> bool:
        """P15 was influenced by (influenced): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P15_was_influenced_by
        prop_inverse = CRM.P15i_influenced

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p16_used_specific_object(self, *entities, uris: list = None) -> bool:
        """P16 used specific object (was used for): E70 Thing

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P16_used_specific_object
        prop_inverse = CRM.P16i_was_used_for

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p17_was_motivated_by(self, *entities, uris: list = None) -> bool:
        """P17 was motivated by (motivated): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P17_was_motivated_by
        prop_inverse = CRM.P17i_motivated

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p19_was_intended_use_of(self, *entities, uris: list = None) -> bool:
        """P19 was intended use of (was made for): E71 Human-Made Thing

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P19_was_intended_use_of
        prop_inverse = CRM.P19i_was_made_for

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p20_had_specific_purpose(self, *entities, uris: list = None) -> bool:
        """P20 had specific purpose (was purpose of): E5 Event

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P20_had_specific_purpose
        prop_inverse = CRM.P20i_was_purpose_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p21_had_general_purpose(self, *entities, uris: list = None) -> bool:
        """P21 had general purpose (was purpose of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P21_had_general_purpose
        prop_inverse = CRM.P21i_was_purpose_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p32_used_general_technique(self, *entities, uris: list = None) -> bool:
        """P32 used general technique (was technique of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P32_used_general_technique
        prop_inverse = CRM.P32i_was_technique_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p33_used_specific_technique(self, *entities, uris: list = None) -> bool:
        """P33 used specific technique (was used by): E29 Design or Procedure

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P33_used_specific_technique
        prop_inverse = CRM.P33i_was_used_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p125_used_object_of_type(self, *entities, uris: list = None) -> bool:
        """P125 used object of type (was type of object used in): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P125_used_object_of_type
        prop_inverse = CRM.P125i_was_type_of_object_used_in

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E13AttributeAssignment(E7Activity):
    """E13 Attribute Assignment

    SubClassOf E7 Activity

    P140 assigned attribute to (was attributed by): E1 CRM Entity
    P141 assigned (was assigned by): E1 CRM Entity
    P177 assigned property type E55 Type
    """

    class_uri = CIDOCNAMESPACE + "E13_Attribute_Assignment"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p140_assigned_attribute_to(self, *entities, uris: list = None) -> bool:
        """P140 assigned attribute to (was attributed by): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P140_assigned_attribute_to
        prop_inverse = CRM.P140i_was_attributed_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p141_assigned(self, *entities, uris: list = None) -> bool:
        """P141 assigned (was assigned by): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P141_assigned
        prop_inverse = CRM.P141i_was_assigned_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p177_assigned_property_of_type(self, *entities, uris: list = None) -> bool:
        """P177 assigned property of type: E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P177_assigned_property_of_type
        prop_inverse = CRM.P177i_is_type_of_property_assigned

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E54Dimension(E1CRMEntity):
    """E54 Dimension

    SubClassOf E1 CRM Entity

    P90 has value: E60 Number
    P91 has unit (is unit of): E58 Measurement Unit
    """

    class_uri = CIDOCNAMESPACE + "E54_Dimension"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p90_has_value(self, content: str, datatype: str = None) -> bool:
        """P90 has value: E60 Number

        Args:
            content (str): Textual content of the note
            datatype (str, optional): Datatype that will be added to Literal. Use XSD datatypes.

        Returns:
             bool: True if added
        """
        prop = CRM.P90_has_value

        if datatype:
            datatype_uri = XSD[datatype]
            self.graph.add((URIRef(self.uri), prop, Literal(content, datatype=datatype_uri)))
        else:
            self.graph.add((URIRef(self.uri), prop, Literal(content)))

        return True

    def p91_has_unit(self, *entities, uris: list = None) -> bool:
        """P91 has unit (is unit of): E58 Measurement Unit

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P91_has_unit
        prop_inverse = CRM.P91i_is_unit_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E39Actor(E77PersistentItem):
    """E39 Actor

    SubClassOf E77 Persistent Item

    P74 has current or former residence (is current or former residence of): E53 Place
    P75 possesses (is possessed by): E30 Right
    P76 has contact point (provides access to): E41 Appellation
    """
    class_uri = CIDOCNAMESPACE + "E39_Actor"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p74_has_current_or_former_residence(self, *entities, uris: list = None) -> bool:
        """P74 has current or former residence (is current or former residence of): E53 Place

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P74_has_current_or_former_residence
        prop_inverse = CRM.P74i_is_current_or_former_residence_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p75_possesses(self, *entities, uris: list = None) -> bool:
        """P75 possesses (is possessed by): E30 Right

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P75_possesses
        prop_inverse = CRM.P75i_is_possessed_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def p76_has_contact_point(self, *entities, uris: list = None) -> bool:
        """P76 has contact point (provides access to): E41 Appellation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P76_has_contact_point
        prop_inverse = CRM.P76i_provides_access_to

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E74Group(E39Actor):
    """E74 Group

    SubClassOf E39 Actor

    P107 has current or former member (is current or former member of): E39 Actor
    (P107.1 kind of member: E55 Type) [Not implemented]
    """

    class_uri = CIDOCNAMESPACE + "E74_Group"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p107_has_current_or_former_member(self, *entities, uris: list = None) -> bool:
        """P107 has current or former member (is current or former member of): E39 Actor

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P107_has_current_or_former_member
        prop_inverse = CRM.P107i_is_current_or_former_member_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E18PhysicalThing(E72LegalObject):
    """
    E18 Physical Thing

    SubClassOf E72 Legal Object

    P44 has condition (is condition of): Ε3 Condition State [Not implemented]
    P45 consists of (is incorporated in): E57 Material [Not implemented]
    P46 is composed of (forms part of): E18 Physical Thing [Not implemented]
    P49 has former or current keeper (is former or current keeper of): E39 Actor [Not implemented]
    P50 has current keeper (is current keeper of): E39 Actor [Not implemented]
    P51 has former or current owner (is former or current owner of): E39 Actor [Not implemented]
    P52 has current owner (is current owner of): E39 Actor [Not implemented]
    P53 has former or current location (is former or current location of): E53 Place [Not implemented]
    P59 has section (is located on or within): E53 Place [Not implemented]
    P128 carries (is carried by): E90 Symbolic Object [Not implemented]
    P156 occupies (is occupied by): E53 Place [Not implemented]
    P196 defines (is defined by): E92 Spacetime Volume [Not implemented]

    These properties are probably not needed for the current implementation, thus are skipped.
    """
    class_uri = CIDOCNAMESPACE + "E18_Physical_Thing"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class E19PhysicalObject(E18PhysicalThing):
    """E19 Physical Object

    subClassOf E18 Physical Thing

    P54 has current permanent location (is current permanent location of): E53 Place [Not implemented]
    P55 has current location (currently holds): E53 Place [Not implemented]
    P56 bears feature (is found on): E26 Physical Feature [Not implemented]
    P57 has number of parts: E60 Number [Not implemented]

    These properties are probably not needed for the current implementation, thus are skipped.
    """

    class_uri = CIDOCNAMESPACE + "E19_Physical_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class E20BiologicalObject(E19PhysicalObject):
    """E20 Biological Object

    subClassOf E19 Physical Object

    The class does not have specialized properties.
    """

    class_uri = CIDOCNAMESPACE + "E20_Biological_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class E21Person(E20BiologicalObject):
    """E21 Person

    subClassOf E20 Biological Object

    P152 has parent (is parent of): E21 Person
    """

    class_uri = CIDOCNAMESPACE + "E21_Person"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p152_has_parent(self, *entities, uris: list = None) -> bool:
        """P152 has parent (is parent of): E21 Person

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P152_has_parent
        prop_inverse = CRM.P152i_is_parent_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E30Right(E89PropositionalObject):
    """E30 Right

    subClassOf E89 Propositional Object

    No specialized properties.

    Inverse: P75i is possessed by (possesses): E39 Actor

    """
    class_uri = CIDOCNAMESPACE + "E30_Right"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p75i_is_possessed_by(self, *entities, uris: list = None) -> bool:
        """P75i is possessed by (possesses): E39 Actor

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P75i_is_possessed_by
        prop_inverse = CRM.P75_possesses

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E63BeginningOfExistence(E5Event):
    """E63 Beginning of Existence

    SubClassOf E5 Event

    P92 brought into existence (was brought into existence by): E77 Persistent Item
    """
    class_uri = CIDOCNAMESPACE + "E63_Beginning_of_Existence"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p92_brought_into_existence(self, *entities, uris: list = None) -> bool:
        """P92 brought into existence (was brought into existence by): E77 Persistent Item

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P92_brought_into_existence
        prop_inverse = CRM.P92i_was_brought_into_existence_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class E65Creation(E7Activity, E63BeginningOfExistence):
    """E65 Beginning of Existence

    SubClassOf E7 Activity AND E63 Beginning of Existence

    P94 has created (was created by): E28 Conceptual Object
    """
    class_uri = CIDOCNAMESPACE + "E65_Creation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def p94_has_created(self, *entities, uris: list = None) -> bool:
        """P94 has created (was created by): E28 Conceptual Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P94_has_created
        prop_inverse = CRM.P94i_was_created_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

# Modification
