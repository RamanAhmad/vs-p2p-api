import logging
import os
import socket
import sys
from time import sleep
import json

port = 8013
broadcast_ip = "172.17.255.255"
file="broadcast/resources/test_environment.postman_environment.json"
msg="HELLO?"

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    logging.basicConfig(filename="output.log",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
    return logger  

logger = get_module_logger(__name__)

            
def send_and_receive_broadcast():
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    allips = [ip[-1][0] for ip in interfaces]
    for ip in set(allips):
        logger.info(f'Sending HELLO? on {ip}:{port}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.settimeout(5.0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((ip,port))
        print(broadcast_ip)
        print(type(broadcast_ip))
        sock.sendto(msg.encode(), (broadcast_ip, port))
        sleep(1)
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        logger.info(f"Received message from %s: %s" %(addr,data))
        if data and data != "HELLO?":
            write_environment(data, ip)
            sock.close()
            return True
        sock.close()
    return False

def write_environment(response, own_ip):
    values = json.loads(response)
    result = write_values_to_environment_file(values, own_ip)
    with open(file, 'w') as fp:
        json.dump(result, fp, indent=2)
    
def write_values_to_environment_file(values, own_ip):
    with open(file) as json_file:
        environment = json.load(json_file)
        environment_values = environment["values"]
        environment_values = insertValue(environment_values, "COM_SELF_IP", own_ip)

        for key, value in values.items():
            if key.lower() == "star":
                environment_values = insertValue(environment_values,"STAR_UUID",value)
            elif key.lower() == "sol":
                environment_values = insertValue(environment_values,"SOL_UUID",value)
            elif key.lower() == "component" or key.lower() == "comuuid":
                environment_values = insertValue(environment_values,"COM_SELF_UUID",value)
            elif key.lower() == "sol-ip" or key.lower() == "com-ip":
                environment_values = insertValue(environment_values,"SOL_IP",value)
            elif key.lower() == "sol-tcp" or key.lower() == "com-tcp":
                environment_values = insertValue(environment_values,"port",value)
                environment_values = insertValue(environment_values,"SOL_TCP",value)
                environment_values = insertValue(environment_values,"COM_SELF_TCP",value)
                environment_values = insertValue(environment_values,"COM_OTHER_TCP",value)

            environment_values.append({"key":key, "value":value, "type":"default", "enabled":True})
        environment["values"] = environment_values
    return environment

def insertValue(values, key, value):
    for key_val_pair in values:
        if key_val_pair["key"] == key:
            key_val_pair["value"] = value
    return values    

if __name__ == "__main__":
    logger = get_module_logger(sys.argv[0])
    try:
        broadcast_ip = sys.argv[1]
        logger.info(f'broadcast ip specified: {broadcast_ip}')        

    except:
        logger.warning(f'No broadcast ip specified, using {broadcast_ip}')        
        
    try:
        port = int(sys.argv[2])
        logger.info(f'broadcast port specified: {broadcast_ip}')        

    except:
        logger.warning(f'No broadcast port specified, using {port}')             
    try:
        isSuccess = send_and_receive_broadcast()   
    except Exception as e:
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        msg = "Broadcast failed"
        logger.warning(msg, e, exc_type, fname, exc_tb.tb_lineno)
        raise Exception(msg)
        
    logger.info('Finished Broadcast')  
    if not isSuccess:
        logger.warning('Failed')

