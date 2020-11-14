import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg import severity

from vsg.tests import utils

sSourceCodeDir = os.path.join(os.path.dirname(__file__),'..','code_examples')

lTimestamp = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'timestamp.vhdl'))
oTimestamp = vhdlFile.vhdlFile(lTimestamp)

lSpiSlave = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'spi_slave.vhd'))
oSpiSlave = vhdlFile.vhdlFile(lSpiSlave)

lSpiMaster = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'spi_master.vhd'))
oSpiMaster = vhdlFile.vhdlFile(lSpiMaster)

lGrpDebouncer = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'grp_debouncer.vhd'))
oGrpDebouncer = vhdlFile.vhdlFile(lGrpDebouncer)

lPIC = utils.read_vhdlfile(os.path.join(sSourceCodeDir,'PIC.vhd'))
oPIC = vhdlFile.vhdlFile(lPIC)

dConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','styles', 'jcl.yaml'))
dConfig['debug'] = False

oSeverityList = severity.create_list({})

class testCodeExample(unittest.TestCase):

    def test_timestamp_vhdl(self):
        oRuleList = rule_list.rule_list(oTimestamp, oSeverityList)
        oRuleList.configure(dConfig)
        oRuleList.fix()

        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'timestamp.fixed.vhdl'), lExpected)

        self.assertEqual(lExpected, oTimestamp.get_lines()) 

    @unittest.skip('Need to wait until all rules have been refactored.')
    def test_spi_slave(self):
        oRuleList = rule_list.rule_list(oSpiSlave, oSeverityList)
        oRuleList.configure(dConfig)
        oRuleList.fix()
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_slave.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiSlave.lines[iLineNumber].line, sLine)

    @unittest.skip('Need to wait until all rules have been refactored.')
    def test_spi_master(self):
        oRuleList = rule_list.rule_list(oSpiMaster, oSeverityList)
        oRuleList.configure(dConfig)
        oRuleList.fix()
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'spi_master.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSpiMaster.lines[iLineNumber].line, sLine)

    def test_grp_debouncer(self):
        oRuleList = rule_list.rule_list(oGrpDebouncer, oSeverityList)
        oRuleList.configure(dConfig)
        oRuleList.fix()

        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'grp_debouncer.fixed.vhd'), lExpected)

        self.assertEqual(lExpected, oGrpDebouncer.get_lines()) 

    def test_pic(self):
        oRuleList = rule_list.rule_list(oPIC, oSeverityList)
        oRuleList.configure(dConfig)
        oRuleList.fix()

        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'PIC.fixed.vhd'), lExpected)

        self.assertEqual(lExpected, oPIC.get_lines()) 
