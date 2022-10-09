from rich.console import Console
from rich.table import Table
import shodan
import sys

# Main section of code Input & Calculate
def main():
    # Import Shodan API Key
    SHODAN_API_KEY = ''
    api = shodan.Shodan(SHODAN_API_KEY)
    
    # Import IP LIST
    IP_LIST = ['']
     
    port_data = []
    banner_data = []
    ip_addr = []

    for index, ip_search in enumerate(IP_LIST):
        host = api.host(str(ip_search))
        for items in host['data']:
            open_ports = str(items['port'])
            port_data.append(open_ports)

            ip_addr.append(items['ip_str'])
        
            banner_data.append(str(items['data']))

    format_output(ip_addr, port_data, banner_data)


# Formatting section Output
def format_output(ip, port, banner): 
    table = Table(title="Shodan Results")
    table = Table(show_lines=True)

    table.add_column("IP", justify="right", style="bright_magenta", no_wrap=True)
    table.add_column("Port", style="green")
    table.add_column("Banner", justify="right", style="red")

    for index, (a, b, c) in enumerate(zip(ip, port, banner)):
        table.add_row(str(a), str(b), str(c))
    
    console = Console()
    console.print(table)

main()
