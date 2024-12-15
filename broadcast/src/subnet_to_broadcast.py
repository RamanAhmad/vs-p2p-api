import logging
import sys

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

def get_bridge_broadcast_ip(subnet_ip):
    net_mask = subnet_ip.split("/")[1]
    if net_mask == "8":
        subnet_broadcast_ip = ".".join([subnet_ip.split(".")[0],"255","255","255"])
        return subnet_broadcast_ip
    if net_mask == "16":
        subnet_broadcast_ip = ".".join([subnet_ip.split(".")[0],subnet_ip.split(".")[1],"255","255"])
        return subnet_broadcast_ip
    if net_mask == "24":
        subnet_broadcast_ip = ".".join([subnet_ip.split(".")[0],subnet_ip.split(".")[1],subnet_ip.split(".")[2],"255"])
        return subnet_broadcast_ip


if __name__ == "__main__":
    subnet = sys.argv[1].replace("\n","").replace("\r","").replace(" ","")
    broadcast_address = get_bridge_broadcast_ip(subnet)
    logger.info("Using " + broadcast_address + " for subnet: " + subnet)
    sys.stdout.write(broadcast_address)