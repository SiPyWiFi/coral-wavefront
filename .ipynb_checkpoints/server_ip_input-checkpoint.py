import os

filename = "./secret/ip_config.txt"
ip_addr = input("Server IP Addr:")

if os.path.exists(filename):
    print("IP config exists ...")
else:
    f = open(filename, "w+")
    f.write(ip_addr)
    f.close()
    print("IP config created ...")


f = open(filename, "r")
content = f.read()
f.close



if not content == ip_addr:
    print("Saved IP Addr:", content)
    print("Change IP Addr to: ", ip_addr)
    if "y" == input("[y] / [~] + Enter:"):
        f = open(filename, "w+")
        f.write(ip_addr)
        f.close()
else:
    print("IP input and saved are the same!")
print("end ...")