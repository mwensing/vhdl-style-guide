
from vsg.vhdlFile.classify import package_body_declarative_item

def tokenize(oObject, iObject, lObjects, dVars):
    '''
    { package_declarative_item }
    '''
    if package_body_declarative_item.tokenize(oObject, iObject, lObjects, dVars):
        return True
    return False
