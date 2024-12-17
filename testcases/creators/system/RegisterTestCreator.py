from creators.TestCase import TestCase
from ..BaseTestCreator import BaseTestCreator as BTC
from typing import Type


# This class is responsible for creating the test cases for the POST register component endpoint
class RegisterTestCreator(BTC):
    
    TEST_NAME = "POST_register"
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
        

    def _init_test_cases(self) -> list[list]:
        star_uuid = self.get_star_uuid()
        sol = self.get_sol()
        com_self = self.get_components()[0]

        test_cases = [
            TestCase(test_name=self.get_test_name(), case_desc="Only valid json data", expected_status=200, star_uuid=star_uuid, sol=sol, com_self=com_self, status=200),
            TestCase(test_name=self.get_test_name(), case_desc="Mismatching COM_UUID in json data", expected_status=409, star_uuid=star_uuid, sol=sol, com_self=com_self.get_modified_clone(new_uuid=BTC.FAKE_UUID), status=200),
            TestCase(test_name=self.get_test_name(), case_desc="Mismatching IP for given COM_UUID", expected_status=409, star_uuid=star_uuid, sol=sol, com_self=com_self.get_modified_clone(new_ip=BTC.FAKE_IP), status=200),
            TestCase(test_name=self.get_test_name(), case_desc="Status in json is not 200", expected_status=409, star_uuid=star_uuid, sol=sol, com_self=com_self, status=BTC.FAKE_STATUS),
            TestCase(test_name=self.get_test_name(), case_desc="Unknown STAR_UUID in json", expected_status=401, star_uuid=BTC.FAKE_STAR_UUID, sol=sol, com_self=com_self, status=200),
            TestCase(test_name=self.get_test_name(), case_desc="Mismatching SOL_UUID in json", expected_status=200, star_uuid=star_uuid, sol=sol.get_modified_clone(new_uuid=BTC.FAKE_UUID), com_self=com_self, status=200)
        ]
        self.add_test_cases(test_cases)