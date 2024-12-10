from enum import Enum

class ColumnName(Enum):
    STATUS = "STATUS"
    EXPECTED_STATUS = "EXPECTED_STATUS"
    TEST_CASE = "TEST_CASE"
    TEST_NAME = "TEST_NAME"
    COM_PATH = "COM_PATH"
    STAR_1_UUID = "STAR_1_UUID"
    SOL_1_UUID = "SOL_1_UUID"
    COM_1_UUID = "COM_1_UUID"
    COM_2_UUID = "COM_2_UUID"
    SOL_1_IP = "SOL_1_IP"
    SOL_1_PORT = "SOL_1_PORT"
    COM_1_IP = "COM_1_IP"
    COM_1_TCP = "COM_1_TCP"
    COM_2_IP = "COM_2_IP"
    COM_2_TCP = "COM_2_TCP"