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
        com = self.get_components()[1]
        sol = self.get_sol()
        
        test_cases = [
            TestCase(test_name=self.get_test_name(), case_desc="valid unregister request from component", com_path=com.get_uuid(), star_uuid=star_uuid, base_host=sol.get_ip(), base_port=sol.get_port(), expected_status=200)
        ]
        self.add_test_cases(test_cases)