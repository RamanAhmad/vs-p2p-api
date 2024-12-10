from creators.TestCase import TestCase
from creators.system.DeleteCompTestCreator import DeleteCompTestCreator
from creators.system.HeartBeatTestCreator import HeartBeatTestCreator
from creators.system.CompStatusTestCreator import CompStatusTestCreator
from star.Component import Component

from typing import Type
from os import makedirs
from os.path import join, isdir, exists

class TestGenerator:
    BASE_DIR: str = "out/test_cases"
    FILE_NAME: str = "test_cases.csv"
    
    def __init__(self, star_uuid: str, sol: Component, components: list[Component]):
        self.__creators: list['creators.BaseTestCreator'] = [] # type: ignore
        self.__star_uuid = star_uuid
        self.__sol = sol
        self.__components = components

    def add(self, creator: Type['creators.BaseTestCreator']): # type: ignore
        self.__creators.append(creator)
        
    def print_all(self):
        for creator in self.__creators:
            creator.print_test_cases()
            
    def get_star_uuid(self) -> str:
        return self.__star_uuid
    
    def get_sol(self) -> Component:
        return self.__sol
    
    def get_components(self) -> list[Component]:
        return self.__components
    
    def export_to_csv(self):
        creators = self.__creators
        if not exists(TestGenerator.BASE_DIR) or not isdir(TestGenerator.BASE_DIR):
            makedirs(TestGenerator.BASE_DIR)
        file_path = join(TestGenerator.BASE_DIR, TestGenerator.FILE_NAME)
        with open(file_path, "w") as file:
            file.write(",".join(TestCase.get_column_names()) + "\n")
            for creator in creators:
                for test_case in creator.get_test_cases():
                    file.write(",".join(f'"{item}"' if isinstance(item, str) else (str(item) if item is not None else '') for item in test_case) + "\n")
    
def main ():
    sol = Component("1014", "102.0.0.4", "8012")
    comp_1 = Component("1015", "102.0.0.5", "8013")
    comp_2 = Component("1016", "102.0.0.6", "8014")
    star_uuid = "11111111122222222222223333333332"
    generator = TestGenerator(star_uuid, sol, [comp_1, comp_2])
        
    # Add your creators here like below
    HeartBeatTestCreator(generator)
    CompStatusTestCreator(generator)
    DeleteCompTestCreator(generator)
    
    
    generator.export_to_csv()
        

if __name__ == "__main__":
    main()