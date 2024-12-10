from creators.TestCase import TestCase
from ..BaseTestCreator import BaseTestCreator
from typing import Type
from star.Component import Component


# This class is responsible for creating the test cases for the PATCH heartbeat endpoint
class HeartBeatTestCreator(BaseTestCreator):
    
    TEST_NAME = "PATCH_heartbeat"
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
    
    def _init_test_cases(self):
        sol: Component = self.get_sol()
        star_uuid = self.get_star_uuid()
        com: Component = self.get_components()[0]
        name = self.get_test_name()
        com_1_uuid = com.get_uuid()
        
        test_cases = [
            TestCase(test_name=name, case_desc="Only valid json data", expected_status=200, star_uuid=star_uuid, sol=sol, com_1=com, com_path=com_1_uuid , status=200, base_host=sol.get_ip(), base_port=sol.get_port()),
            TestCase(test_name=name, case_desc="Unknown COM_UUID in path", expected_status=404, star_uuid=star_uuid, sol=sol, com_1=com, com_path=4711 , status=200, base_host=sol.get_ip(), base_port=sol.get_port()),
            TestCase(test_name=name, case_desc="Mismatching COM_UUID in json path", expected_status=409, star_uuid=star_uuid, sol=sol, com_1=com.get_modified_clone(new_uuid=4711), com_path=com_1_uuid, status=200, base_host=sol.get_ip(), base_port=sol.get_port()),
            TestCase(test_name=name, case_desc="Mismatching IP in json path", expected_status=409, star_uuid=star_uuid, sol=sol, com_1=com.get_modified_clone(new_ip="4.7.1.1"), com_path=com_1_uuid, status=200, base_host=sol.get_ip(), base_port=sol.get_port()),
            TestCase(test_name=name, case_desc="Status in json is not 200", expected_status=409, star_uuid=star_uuid, sol=sol, com_1=com, com_path=com_1_uuid, status=505, base_host=sol.get_ip(), base_port=sol.get_port()),
            TestCase(test_name=name, case_desc="Unknown STAR_UUD in json data", expected_status=401, star_uuid="ABCD", sol=sol, com_1=com, com_path=com_1_uuid, status=200, base_host=sol.get_ip(), base_port=sol.get_port()),
            TestCase(test_name=name, case_desc="Mismatching SOL_UUID in json data", expected_status=401, star_uuid=star_uuid, sol=sol.get_modified_clone(new_uuid=4711), com_1=com, com_path=com_1_uuid, status=200, base_host=sol.get_ip(), base_port=sol.get_port())
        ]
        self.add_test_cases(test_cases)