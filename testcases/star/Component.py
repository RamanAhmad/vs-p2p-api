import re


class Component:
    def __init__(self, uuid: str, ip: str = None, port: str = None):
        if not uuid:
            raise ValueError("UUID cannot be None, empty or only whitespaces.")
        Component.__check_com_uuid(uuid)
        self.__uuid: int = int(uuid)
        
        if ip is not None and port is not None:
            Component.__check_ip(ip)
            Component.__check_port(port)
            self.__ip: str = ip
            self.__port: int = int(port)
        else:
            self.__ip = None
            self.__port = None
        
    def get_uuid(self) -> int:
        return self.__uuid
    
    def get_ip(self) -> str:
        return self.__ip
    
    def set_ip(self, ip: str):
        Component.__check_ip(ip)
        self.__ip = ip
        
    def set_port(self, port: int):
        Component.__check_port(port)
        self.__port = port
    
    def get_port(self) -> int:
        return self.__port
    
    def get_star_uuid(self) -> str:
        return self.__star_uuid
    
    def has_ip(self) -> bool:
        return self.__ip is not None
    
    def has_port(self) -> bool:
        return self.__port is not None
    
    
    def get_modified_clone(self, new_uuid: int = None, new_ip: str = None, new_tcp: int = None) -> 'Component':
        if new_uuid is None:
            new_uuid = self.__uuid
        if new_ip is None:
            new_ip = self.__ip
        else:
            Component.__check_ip(new_ip)
        if new_tcp is None:
            new_tcp = self.__port
        else:
            Component.__check_port(new_tcp)
        return Component(str(new_uuid), str(new_ip) if new_ip else None, str(new_tcp) if new_tcp else None)
    
    
         
    @staticmethod
    def __check_com_uuid(uuid: str):
        if not uuid.isdigit() or not (1000 <= int(uuid) <= 9999):
            raise ValueError("UUID must be a string formatted number from 1000 to 9999.")
    
    @staticmethod
    def __check_ip(ip: str):
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
            raise ValueError("IP must be a valid IPv4 address.")
        
    @staticmethod
    def __check_port(port: str):
        if not port.isdigit() or not (1024 <= int(port) <= 65535):
            raise ValueError("Port must be a number from 1024 to 65535.")