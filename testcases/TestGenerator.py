from creators.system.DeleteCompTestCreator import DeleteCompTestCreator
from creators.system.HearBeatTestCreator import HeartBeatTestCreator
from typing import Type

from creators.system.RegisterTestCreator import RegisterTestCreator
from creators.system.CompStatusTestCreator import CompStatusTestCreator
from star.Component import Component

class TestGenerator:
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
            
    def export_all(self):
        for creator in self.__creators:
            creator.export_to_csv()
            
    def get_star_uuid(self) -> str:
        return self.__star_uuid
    
    def get_sol(self) -> Component:
        return self.__sol
    
    def get_components(self) -> list[Component]:
        return self.__components
    
def main ():
    sol = Component("1014", "102.0.0.4", "8012")
    comp_1 = Component("1015", "102.0.0.5", "8013")
    comp_2 = Component("1016", "102.0.0.6", "8014")
    star_uuid = "11111111122222222222223333333332"
    generator = TestGenerator(star_uuid, sol, [comp_1, comp_2])
        
    # Add your creator here like below
    HeartBeatTestCreator(generator)
    RegisterTestCreator(generator)
    CompStatusTestCreator(generator)
    DeleteCompTestCreator(generator)
    
    
    generator.export_all()
        

if __name__ == "__main__":
    main()