from rich.console import Console
from rich.table import Table
import shodan
import sys

def main():
    # Import Shodan API Key
    SHODAN_API_KEY = ''
    api = shodan.Shodan(SHODAN_API_KEY)
    
    IP_LIST = []

    port_data = []
    banner_data = []
    ip_addr = []
    city_data = []
    asn_data = []
    org_data = []
    domains_data = []
    hostname_data = []

    for index, ip_search in enumerate(IP_LIST):
        host = api.host(str(ip_search))
        for items in host['data']:
            open_ports = str(items['port'])
            port_data.append(open_ports)
            
            ip_addr.append(items['ip_str'])
            banner_data.append(str(items['data']))

            city = host.get('city', 'n/a')
            city_data.append(city)
            
            org = str(items['org'])
            org_data.append(org)

            asn = str(items['asn'])
            asn_data.append(asn)

            domains = str(items['domains'])
            domains_data.append(domains)

            hostname = str(items['hostnames'])
            hostname_data.append(hostname)

    table = Table(title="Shodan Results")
    table = Table(show_lines=True)

    table.add_column("IP", justify="right", style="bright_magenta", no_wrap=True)
    table.add_column("Banner", justify="right", style="red")
    table.add_column("Port", style="green")
    table.add_column("City", style="bright_cyan")
    table.add_column("ASN", style="Cyan")
    table.add_column("ORG", style="bright_green")
    table.add_column("Domains", style="red")
    
    # Banner section
    for index, (a, b, c, d, e, f, g, h) in enumerate(zip(ip_addr, port_data, banner_data, city_data, asn_data, org_data, domains_data, hostname_data)):
        table.add_row(str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h))
    
    console = Console()
    console.print(table)

main()
