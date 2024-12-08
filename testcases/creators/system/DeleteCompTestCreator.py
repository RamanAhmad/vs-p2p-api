from ..BaseTestCreator import BaseTestCreator
from typing import Type
from ColumnName import ColumnName
from star.Component import Component

# This class is responsible for creating the test cases for the DELETE unregister component endpoint
class DeleteCompTestCreator(BaseTestCreator):
    
    FILE_NAME = "DEL_unregister_from_sol"
    
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
            [star_uuid, com_uuid, 401, "Invalid ip"]
        ]
        return test_cases