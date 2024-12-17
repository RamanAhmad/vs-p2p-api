from creators.TestCase import TestCase
from ..BaseTestCreator import BaseTestCreator as BTC
from typing import Type

# This class is responsible for creating the test cases for the DELETE unregister component endpoint
class DeleteCompTestCreator(BTC):
    
    TEST_NAME = "DEL_unregister_component"
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
        
    
    def _init_test_cases(self):
        star_uuid = self.get_star_uuid()
        com_self = self.get_components()[0]
        com_other = self.get_components()[1]
        sol = self.get_sol()
        
        test_cases = [
            TestCase(test_name=self.get_test_name(), case_desc="valid unregister request (comp -> sol)", com_path=com_self.get_uuid(), star_uuid=star_uuid, expected_status=200, base_host=sol.get_ip(), base_port=sol.get_port()),
            # TestCase(test_name=self.get_test_name(), case_desc="valid unregister request (sol -> comp)", com_path=com.get_uuid(), star_uuid=star_uuid, base_host=com_other.get_ip(), base_port=com_other.get_port(), expected_status=200)
            TestCase(test_name=self.get_test_name(), case_desc="Unknown COM_UUID in path (comp -> sol)", com_path=BTC.FAKE_UUID, star_uuid=star_uuid, expected_status=404, base_host=sol.get_ip(), base_port=sol.get_port()),
            # TestCase(test_name=self.get_test_name(), case_desc="Unknown COM_UUID in path (sol -> comp)", com_path=BTC.FAKE_UUID, star_uuid=star_uuid, base_host=com_other.get_ip(), base_port=com_other.get_port(), expected_status=404),
            TestCase(test_name=self.get_test_name(), case_desc="Invalid IP (comp -> sol)", com_path=com_other.get_uuid(), star_uuid=star_uuid, expected_status=401, base_host=sol.get_ip(), base_port=sol.get_port())
        ]
        self.add_test_cases(test_cases)