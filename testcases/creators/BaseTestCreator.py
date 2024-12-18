from abc import ABC, abstractmethod
from enum import Enum
from typing import Type
from util.TestTargetEnum import TestTarget
from star.Component import Component
from .TestCase import TestCase

class BaseTestCreator(ABC):
    FAKE_IP = "4.7.1.1"
    FAKE_PORT = "4711"
    FAKE_UUID = "4711"
    FAKE_STATUS = "500"
    FAKE_STAR_UUID = "ABCD"
    
    # TODO: Add a way to identify wether the test runs against sol or com_other using an enum
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        self.__generator: Type['TestGenerator'] = generator # type: ignore
        self.__test_cases: list[TestCase] = []
        self._init_test_cases()
        generator.add(self)
        
    def get_star_uuid(self) -> str:
        return self.__generator.get_star_uuid()

    def get_sol_uuid(self) -> int:
        return self.__generator.get_sol().get_uuid()
    
    def get_sol(self) -> Component:
        return self.__generator.get_sol()
    
    def get_components(self) -> list[Component]:
        return self.__generator.get_components()
        
    def print_test_cases(self):
        for test_case in self.get_test_cases():
            print(test_case)
    
    def get_test_name(self) -> str:
        if not hasattr(self, 'TEST_NAME'):
            raise NotImplementedError("Subclasses must define TEST_NAME.")
        return self.TEST_NAME
    
    def get_test_cases(self) -> list[TestCase]:
        return self.__test_cases
    
    def add_test_case(self, test_case: TestCase):
        if not test_case.is_empty():
            self.__test_cases.append(test_case)
            
    def add_test_cases(self, test_cases: list[TestCase]):
        for test_case in test_cases:
            self.add_test_case(test_case)
            
    @abstractmethod
    def _init_test_cases(self):
        pass
    
    
    """
    This method, `runs_against`, is intended to be overridden by subclasses
    of `BaseTestCreator`. It should return an instance of `TestTarget`, which represents
    the target that the test will run against. As of now, a target would be either SOL or COM_OTHER.
    """
    @abstractmethod
    def runs_against(self) -> TestTarget:
        pass