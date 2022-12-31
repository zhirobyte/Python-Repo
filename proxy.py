import os

def enable_manual_proxy(option1, option2):
    # Turn on the manual proxy setup
    os.system("netsh winhttp set proxy proxy-server='manual'")

    # Set the proxy server for option 1
    os.system("netsh winhttp set proxy proxy-server='http://<option1_proxy_server>:<option1_proxy_port>' bypass-list='*.local'")

    # Turn off the proxy server for option 2
    os.system("netsh winhttp set proxy proxy-server='http://<option2_proxy_server>:<option2_proxy_port>' bypass-list='<local>")

enable_manual_proxy("http://option1_proxy_server:option1_proxy_port", "http://option2_proxy_server:option2_proxy_port")
