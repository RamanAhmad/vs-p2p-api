from http import HTTPStatus
from util.ColumnNameEnum import ColumnName
from star.Component import Component


class TestCase:
    VALID_STATUS_CODES = {code.value for code in HTTPStatus}
    def __init__(self, test_name: str, case_desc: str, expected_status, star_uuid: str = None, sol: Component = None, com_self: Component = None, com_other: Component = None, com_path = None, status = None, base_host: str = None, base_port: int = None):
        if not test_name or not case_desc or not expected_status or test_name.strip() == "" or case_desc.strip() == "":
            raise ValueError("expected status, test name and case description cannot be None, empty or only whitespaces")
        self.__test_case: dict[ColumnName, object] = {column_name: None for column_name in ColumnName}
        self.__init_values(test_name, case_desc, expected_status, star_uuid, sol, com_self, com_other, com_path, status, base_host, base_port)
        
        
    def __init_values(self, test_name: str, case_desc: str, expected_status, star_uuid: str = None, sol: Component = None, com_self: Component = None, com_other: Component = None, com_path = None, status = None, base_host: str = None, base_port: int = None):
        self.set_value(ColumnName.TEST_NAME, test_name)
        self.set_value(ColumnName.CASE_DESC, case_desc)
        TestCase._check_response_code(expected_status)
        self.set_value(ColumnName.EXPECTED_STATUS, expected_status)
        if star_uuid:
            self.set_value(ColumnName.STAR_UUID, star_uuid)
        if sol:
            self.__set_component_values(sol)
        if com_self:
            self.__set_component_values(com_self, 1)
        if com_other:
            self.__set_component_values(com_other, 2)
        if com_path:
            self.set_value(ColumnName.COM_PATH, com_path)
        if status:
            TestCase._check_response_code(status)
            self.set_value(ColumnName.STATUS, status)
        if base_host:
            self.set_value(ColumnName.BASE_HOST, base_host)
        elif sol:
            self.set_value(ColumnName.BASE_HOST, sol.get_ip())
        if base_port:
            self.set_value(ColumnName.BASE_PORT, int(base_port))
        elif sol:
            self.set_value(ColumnName.BASE_PORT, int(sol.get_port()))
        
        
    # This method sets the values of the columns related to the component.
    # The column names are determined by the com_number parameter.
    # Default value for com_number is 0, resulting in the values being set for the SOL component.
    def __set_component_values(self, component: Component, com_number: int = 0):
        if com_number not in range(0, 3):
            raise ValueError("COM number must be 0, 1 or 2")
        
        column_map = {
            0: (ColumnName.SOL_UUID, ColumnName.SOL_IP, ColumnName.SOL_PORT),
            1: (ColumnName.COM_SELF_UUID, ColumnName.COM_SELF_IP, ColumnName.COM_SELF_TCP),
            2: (ColumnName.COM_OTHER_UUID, ColumnName.COM_OTHER_IP, ColumnName.COM_OTHER_TCP)
        }
        
        uuid_col, ip_col, port_col = column_map[com_number]
        
        self.set_value(uuid_col, component.get_uuid())
        if component.has_ip():
            self.set_value(ip_col, component.get_ip())
        if component.has_port():
            self.set_value(port_col, component.get_port())
    
    
    def get_test_case(self) -> dict[ColumnName, object]:
        return self.__test_case
    
    def set_value(self, column: ColumnName, value: object):
        self.__check_column(column)
        self.__check_value(value)
        self.__test_case[column] = value
        
    def get_value(self, column_name: ColumnName) -> object:
        self.__check_column(column_name)
        return self.__test_case[column_name]
    
    def __check_column(self, column_name: ColumnName):
        if column_name not in self.__test_case:
            raise ValueError(f"Column {column_name} is not a valid column name")
        
    def __check_value(self, value: object):
        if value is None:
            raise ValueError("Value cannot be None")
        
    def to_value_list(self) -> list:
        return [self.__test_case[column_name] for column_name in ColumnName]
    
    @staticmethod
    def get_column_names() -> list[str]:
        return [column_name.value for column_name in ColumnName]
    
    def is_empty(self) -> bool:
        return all(value is None for value in self)
    
    def __iter__(self):
        for value in self.to_value_list():
            yield value
            
    def __str__(self):
        return ", ".join(str(value) for value in self)
    
    @staticmethod
    def _check_response_code(status):
        if not str(status).isdigit():
            raise ValueError("Status code must be a number.")
        if int(status) not in TestCase.VALID_STATUS_CODES:
            raise ValueError("Status code must be a valid HTTP status code.")
    