from util.TestTargetEnum import TestTarget
from creators.TestCase import TestCase
from ..BaseTestCreator import BaseTestCreator as BTC
from typing import Type
from star.Component import Component


# This class is responsible for creating the test cases for the PATCH heartbeat endpoint
class HeartBeatTestCreator(BTC):
    
    TEST_NAME = "PATCH_heartbeat"
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
    
    def _init_test_cases(self):
        sol: Component = self.get_sol()
        star_uuid = self.get_star_uuid()
        com_self: Component = self.get_components()[0]
        com_other: Component = self.get_components()[1]

        name = self.get_test_name()
        
        test_cases = [
            TestCase(test_name=name, case_desc="Only valid json data", expected_status=200, star_uuid=star_uuid, sol=sol, com_self=com_self, com_path=com_self.get_uuid(), status=200),
            TestCase(test_name=name, case_desc="Unknown COM_UUID in path", expected_status=404, star_uuid=star_uuid, sol=sol, com_self=com_self, com_path=BTC.FAKE_UUID , status=200),
            TestCase(test_name=name, case_desc="Mismatching COM_UUID in json path", expected_status=409, star_uuid=star_uuid, sol=sol, com_self=com_self.get_modified_clone(new_uuid=BTC.FAKE_UUID), com_path=com_self.get_uuid(), status=200),
            TestCase(test_name=name, case_desc="Mismatching IP in json path", expected_status=409, star_uuid=star_uuid, sol=sol, com_self=com_self.get_modified_clone(new_ip=BTC.FAKE_IP), com_path=com_self.get_uuid(), status=200),
            TestCase(test_name=name, case_desc="Status in json is not 200", expected_status=409, star_uuid=star_uuid, sol=sol, com_self=com_self, com_path=com_self.get_uuid(), status=BTC.FAKE_STATUS),
            TestCase(test_name=name, case_desc="Unknown STAR_UUD in json data", expected_status=401, star_uuid=BTC.FAKE_STAR_UUID, sol=sol, com_self=com_self, com_path=com_self.get_uuid(), status=200),
            TestCase(test_name=name, case_desc="Mismatching SOL_UUID in json data", expected_status=401, star_uuid=star_uuid, sol=sol.get_modified_clone(new_uuid=BTC.FAKE_UUID), com_self=com_self, com_path=com_self.get_uuid(), status=200)
        ]
        self.add_test_cases(test_cases)
        
    def runs_against(self) -> TestTarget:
        return TestTarget.SOL