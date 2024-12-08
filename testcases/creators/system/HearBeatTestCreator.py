from ..BaseTestCreator import BaseTestCreator
from typing import Type
from ColumnName import ColumnName
from star.Component import Component


# This class is responsible for creating the test cases for the PATCH heartbeat endpoint
class HeartBeatTestCreator(BaseTestCreator):
    
    FILE_NAME = "PATCH_heartbeat"
    
    HEADERS = [
        ColumnName.COM_PATH,
        ColumnName.STAR_1_UUID,
        ColumnName.SOL_1_UUID,
        ColumnName.COM_1_UUID,
        ColumnName.COM_1_IP,
        ColumnName.COM_1_TCP,
        ColumnName.STATUS,
        ColumnName.EXPECTED_STATUS,
        ColumnName.TEST_NAME
    ]
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        super().__init__(generator)
        self.__component_1: Component = self.get_components()[0]
        
    
    def get_test_cases(self) -> list[list]:
        star_uuid = self.get_star_uuid()
        sol_uuid = self.get_sol_uuid()
        status = 200
        com_uuid = self.__component_1.get_uuid()
        com_ip = self.__component_1.get_ip()
        com_port = self.__component_1.get_port()
        
        test_cases = [
            [com_uuid, star_uuid, sol_uuid, com_uuid, com_ip, com_port, status, 200, "Only valid json data"],
            [4711, star_uuid, sol_uuid, com_uuid, com_ip, com_port, status, 404, "Unknown COM_UUID in path"],
            [com_uuid, star_uuid, sol_uuid, 4711, com_ip, com_port, status, 409, "Mismatching COM_UUID in json data"],
            [com_uuid, star_uuid, sol_uuid, com_uuid, "1.1.1.1", com_port, status, 409, "Mismatching IP for given COM_UUID"],
            [com_uuid, star_uuid, sol_uuid, com_uuid, com_ip, com_port, 401, 409, "Status in json is not 200"],
            [com_uuid, "ABCD", sol_uuid, com_uuid, com_ip, com_port, status, 401, "Unknown STAR_UUID in json data"],
            [com_uuid, star_uuid, 4711, com_uuid, com_ip, com_port, status, 401, "Mismatching SOL_UUID in json data"],
        ]
        return test_cases