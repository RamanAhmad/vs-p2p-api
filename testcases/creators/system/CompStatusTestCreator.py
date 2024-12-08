from ..BaseTestCreator import BaseTestCreator
from typing import Type
from ColumnName import ColumnName
from star.Component import Component


# This class is responsible for creating the test cases for the GET status of component endpoint
class CompStatusTestCreator(BaseTestCreator):
    
    FILE_NAME = "GET_status"
    
    HEADERS = [
        ColumnName.STAR_1_UUID,
        ColumnName.COM_1_UUID,
        ColumnName.EXPECTED_STATUS,
        ColumnName.TEST_NAME
    ]
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
        self.__component_1: Component = self.get_components()[0]
        
    
    def get_test_cases(self) -> list[list]:
        star_uuid = self.get_star_uuid()
        com_uuid = self.__component_1.get_uuid()
        
        test_cases = [
            [star_uuid, com_uuid, 200, "Valid and active component"],
            [star_uuid, 4711, 401, "Component not part of the star"],
            [star_uuid, "", 401, "Empty com_uuid in path"]
        ]
        return test_cases