import logging
import socket
import sys
from time import sleep
import json

port = 8013
broadcast_ip = "172.17.255.255"
file="resources/test_environment.postman_environment.json"
msg="HELLO?"

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger  

logger = get_module_logger(__name__)
            
def send_and_receive_broadcast():
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    allips = [ip[-1][0] for ip in interfaces]
    for ip in set(allips):
        logger.info(f'sending on {ip}:{port}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.settimeout(5.0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((ip,port))
        sock.sendto(msg.encode(), (broadcast_ip, port))
        sleep(1)
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        logger.info(f"received message from %s: %s" %(addr,data))
        if data and data != "HELLO?":
            write_environment(data)
            sock.close()
            return True
        sock.close()
    return False

def write_environment(response):
    values = json.loads(response)
    result = write_values_to_environment_file(values)
    with open(file, 'w') as fp:
        json.dump(result, fp, indent=2)
    
def write_values_to_environment_file(values):
    with open(file) as json_file:
        environment = json.load(json_file)
        environment_values = environment["values"]
        for key, value in values.items():
            if key.lower() == "star":
                environment_values = insertValue(environment_values,"STAR_1_UUID",value)
            elif key.lower() == "sol":
                environment_values = insertValue(environment_values,"SOL_1_UUID",value)
            elif key.lower() == "component":
                environment_values = insertValue(environment_values,"COM_1_UUID",value)
            elif key.lower() == "sol-ip":
                environment_values = insertValue(environment_values,"SOL_1_IP",value)
            elif key.lower() == "sol-tcp":
                environment_values = insertValue(environment_values,"SOL_1_TCP",str(value))
            environment_values.append({"key":key, "value":value, "type":"default", "enabled":True})
        environment["values"] = environment_values
    return environment

def insertValue(values, key, value):
    for key_val_pair in values:
        if key_val_pair["key"] == key:
            key_val_pair["value"] = value
    return values    

if __name__ == "__main__":
    try:
        broadcast_ip = sys.argv[1]
    except:
        logger.warning(f'no broadcast ip specified, using {broadcast_ip}')        
        
    try:
        port = int(sys.argv[2])
    except:
        logger.warning(f'no broadcast port specified, using {port}')             
    
    isSuccess = send_and_receive_broadcast()    
    logger.info('Finish')  
    if not isSuccess:
        logger.warning('Failed')

