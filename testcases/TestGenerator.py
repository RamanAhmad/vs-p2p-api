import json
import logging
import os
from sys import argv
import sys
from creators.TestCase import TestCase
from creators.system.RegisterTestCreator import RegisterTestCreator
from creators.system.DeleteCompTestCreator import DeleteCompTestCreator
from creators.system.HeartBeatTestCreator import HeartBeatTestCreator
from creators.system.CompStatusTestCreator import CompStatusTestCreator
from star.Component import Component

from typing import Type
from os import makedirs
from os.path import join, isdir, exists

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    logging.basicConfig(filename="output.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
    return logger  

logger = get_module_logger(__name__)

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
    try:        
        file_path = os.path.join(argv[1])

        with open(file_path) as file:
            environment = json.loads(file.read())
            logger.info("Reading environment file: " + file_path)
            values = environment["values"]
            for entry in values:
                print(entry)
                if entry["key"] == "STAR_UUID":
                    star_uuid = entry["value"]
                elif entry["key"] == "SOL_UUID":
                    sol_uuid = entry["value"]
                elif entry["key"] == "SOL_IP":
                    sol_ip = entry["value"]
                elif entry["key"] == "SOL_UUID":
                    sol_uuid = entry["value"]
                elif entry["key"] == "SOL_TCP":
                    sol_tcp = entry["value"]
                elif entry["key"] == "COM_SELF_UUID":
                    com_self_uuid = entry["value"]
                elif entry["key"] == "COM_SELF_IP":
                    com_self_ip = entry["value"]
                elif entry["key"] == "COM_OTHER_UUID":
                    com_other_uuid = entry["value"]
                elif entry["key"] == "COM_OTHER_IP":
                    com_other_ip = entry["value"]
                elif entry["key"] == "COM_SELF_TCP":
                    com_self_tcp = entry["value"]
                elif entry["key"] == "COM_OTHER_TCP":
                    com_other_tcp = entry["value"]
                    
            sol = Component(sol_uuid, sol_ip, sol_tcp)
            comp_self = Component(com_self_uuid,com_self_ip, com_self_tcp)
            comp_other = Component(com_other_uuid, com_other_ip, com_other_tcp)
           
            
    except Exception as e:
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger.warning(e, exc_type, fname, exc_tb.tb_lineno)
        msg = "No valid environment file path given"
        logger.warning(msg)        
        raise Exception(msg)


    generator = TestGenerator(star_uuid, sol, [comp_self, comp_other])
    
    logger.info("Generating testcases for " + argv[2])
        
    # if (argv[2].strip().lower() == "sol"):
    #     #only sol testcases
    # elif (argv[2].strip().lower() == "com"):
    #     #only com testcases
    # else:
    #     msg = "Specify test: \"sol\" or \"com\""
    #     logger.warning(msg)
    #     raise Exception(msg) 
    
    RegisterTestCreator(generator)
    HeartBeatTestCreator(generator)
    CompStatusTestCreator(generator)
    DeleteCompTestCreator(generator)
    
    generator.export_to_csv() 
    logger.info("Successfully generated csv test cases for " + argv[2])       

if __name__ == "__main__":
    main()
