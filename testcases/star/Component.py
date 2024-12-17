import re


class Component:
    def __init__(self, uuid, ip: str = None, port = None):
        if not uuid:
            raise ValueError("UUID cannot be None, empty or only whitespaces.")
        Component.__check_com_uuid(uuid)
        self.__uuid = uuid
        
        Component.__check_ip(ip)
        Component.__check_port(port)
        self.__ip: str = ip
        self.__port = port
        
    def get_uuid(self):
        return self.__uuid
    
    def get_ip(self) -> str:
        return self.__ip
    
    def set_ip(self, ip: str):
        Component.__check_ip(ip)
        self.__ip = ip
        
    def set_port(self, port):
        Component.__check_port(port)
        self.__port = port
    
    def get_port(self):
        return self.__port
    
    def has_ip(self) -> bool:
        return self.__ip is not None
    
    def has_port(self) -> bool:
        return self.__port is not None
    
    
    def get_modified_clone(self, new_uuid = None, new_ip: str = None, new_tcp = None) -> 'Component':
        if new_uuid is None:
            new_uuid = self.__uuid
        if new_ip is None:
            new_ip = self.__ip
        if new_tcp is None:
            new_tcp = self.__port
        return Component(new_uuid, new_ip, new_tcp)
    
    
         
    @staticmethod
    def __check_com_uuid(uuid):
        if not isinstance(uuid, (str, int)):
            raise ValueError("UUID must be a string or an integer.")
        if not str(uuid).isdigit() or not (1000 <= int(uuid) <= 9999):
            raise ValueError("UUID must be a string formatted number from 1000 to 9999.")
    
    @staticmethod
    def __check_ip(ip: str):
        if ip is None:
            return
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
            raise ValueError("IP must be a valid IPv4 address.")
        
    @staticmethod
    def __check_port(port):
        if port is None:
            return
        if not isinstance(port, (str, int)):
            raise ValueError("Port must be a string or an integer.")
        if not str(port).isdigit() or not (1024 <= int(port) <= 65535):
            raise ValueError("Port must be a number from 1024 to 65535.")