from enum import Enum

class ColumnName(Enum):
    STATUS = "STATUS"
    EXPECTED_STATUS = "EXPECTED_STATUS"
    TEST_NAME = "TEST_CASE"
    COM_PATH = "COM_PATH"
    STAR_1_UUID = "STAR_1_UUID"
    SOL_1_UUID = "SOL_1_UUID"
    COM_1_UUID = "COM_1_UUID"
    COM_2_UUID = "COM_2_UUID"
    COM_1_IP = "COM_1_IP"
    COM_1_TCP = "COM_1_TCP"
    COM_2_IP = "COM_2_IP"
    COM_2_TCP = "COM_2_TCP"