from os import makedirs
from os.path import join, isdir, exists
import http
from abc import ABC, abstractmethod
from typing import Type
from star.Component import Component

class BaseTestCreator(ABC):
    VALID_STATUS_CODES = {code.value for code in http.HTTPStatus}
    BASE_DIR: str = "out/test_cases"
    
    def __init__(self, generator: Type['TestGenerator']): # type: ignore
        self.__generator: Type['TestGenerator'] = generator # type: ignore
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
        print(self.get_headers())
        for test_case in self.get_test_cases():
            print(test_case)
            
    def get_status(self) -> int:
        if not hasattr(self, '_status'):
            raise NotImplementedError("Subclasses must define _status.")
        return self._status
            
    def export_to_csv(self):
        if not exists(BaseTestCreator.BASE_DIR) or not isdir(BaseTestCreator.BASE_DIR):
            makedirs(BaseTestCreator.BASE_DIR)
        file_name = self.get_file_name() if self.get_file_name().endswith(".csv") else self.get_file_name() + ".csv"
        file_path = join(BaseTestCreator.BASE_DIR, file_name)
        with open(file_path, "w") as file:
            file.write(",".join(self.get_headers()) + "\n")
            for test_case in self.get_test_cases():
                file.write(",".join(f'"{item}"' if isinstance(item, str) else str(item) for item in test_case) + "\n")
            
    
    def get_file_name(self) -> str:
        if not hasattr(self, 'FILE_NAME'):
            raise NotImplementedError("Subclasses must define FILE_NAME.")
        return self.FILE_NAME
    
    def get_headers(self) -> list[str]:
        if not hasattr(self, 'HEADERS'):
            raise NotImplementedError("Subclasses must define HEADERS.")
        return [header.value for header in self.HEADERS]
            
    @abstractmethod
    def get_test_cases(self) -> list[list]:
        pass
    
    
    
        
    @staticmethod
    def _check_response_code(status: str):
        if not status.isdigit():
            raise ValueError("Status code must be a number.")
        if int(status) not in BaseTestCreator.VALID_STATUS_CODES:
            raise ValueError("Status code must be a valid HTTP status code.")
    