
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.signal_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)

lUnless = []


class rule_031(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Checks the alignment of declaration identifiers in the process declarative region.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'process', '031', lAlign, token.process_statement.process_keyword, token.process_statement.begin_keyword, lUnless)
        self.solution = 'Align the first character of each identifier.'
