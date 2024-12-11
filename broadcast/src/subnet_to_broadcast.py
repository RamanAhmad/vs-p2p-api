import sys

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
    sys.stdout.write(get_bridge_broadcast_ip(subnet))