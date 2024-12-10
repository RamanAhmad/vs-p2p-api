from creators.TestCase import TestCase
from ..BaseTestCreator import BaseTestCreator
from typing import Type
from star.Component import Component


# This class is responsible for creating the test cases for the GET status of component endpoint
class CompStatusTestCreator(BaseTestCreator):
    
    TEST_NAME = "GET_status"
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
    
    def _init_test_cases(self):
        star_uuid = self.get_star_uuid()
        com_1: Component = self.get_components()[0]
        com_1_uuid = com_1.get_uuid()
        self.get_components()[0]
        
        test_cases = [
            TestCase(test_name=self.get_test_name(), case_desc="Valid and active component", expected_status=200, com_path=com_1_uuid, star_uuid=star_uuid, base_host=com_1.get_ip(), base_port=com_1.get_port()),
            TestCase(test_name=self.get_test_name(), case_desc="Component not part of the star", expected_status=401, com_path=4711, star_uuid=star_uuid, base_host=com_1.get_ip(), base_port=com_1.get_port())
        ]
        
        self.add_test_cases(test_cases)