
from vsg.vhdlFile.classify_new import subtype_indication


def classify_until(lUntils, iToken, lObjects):
    '''
    element_subtype_definition ::=
        subtype_indication
    '''

    return subtype_indication.classify_until(lUntils, iToken, lObjects)
