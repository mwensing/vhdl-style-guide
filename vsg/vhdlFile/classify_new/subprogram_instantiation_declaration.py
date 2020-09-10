
from vsg.token import subprogram_instantiation_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import signature
from vsg.vhdlFile.classify_new import subprogram_kind
from vsg.vhdlFile.classify_new import generic_map_aspect


'''
    subprogram_instantiation_declaration ::=
        subprogram_kind identifier is new uninstantiated_subprogram_name [ signature ]
            [ generic_map_aspect ] ;
'''


def detect(iToken, lObjects):
    if subprogram_kind.detect(iToken, lObjects):
        if utils.find_in_next_n_tokens('is', 3, iToken, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken
    return iToken


def classify(iToken, lObjects):
    iCurrent = subprogram_kind.classify(iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('new', token.new_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.uninstantiated_subprogram_name, iCurrent, lObjects)
    iCurrent = signature.detect(iCurrent, lObjects)
    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
