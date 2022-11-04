from rich.console import Console
from rich.table import Table
import shodan
import sys

# ENTER SHODAN KEY HERE
SHODAN_API_KEY = ''
api = shodan.Shodan(SHODAN_API_KEY)

claclass diagram:
    def __init__(self, *argv):
        for arg in argv:
            self.IP = argv

    def shodan_search(self):
        host = api.host(self.IP)
        self.ip, self.banner, self.port, self.city, self.domains, self.asn = [],[],[],[],[],[]
        for items in host['data']:
            self.ip.append(items['ip_str'])
            self.banner.append(items['data'])
            self.port.append(items['port'])
            self.city.append(host.get('city', 'n/a'))
            self.domains.append(host.get('domain', 'n/a'))
            self.asn.append(items['asn'])

        #print(len(self.ip), len(self.city), len(self.port), len(self.domains), len(self.asn)) # Verifying that they all match

    def output_format(self):
        table = Table(title="Shodan results")
        table = Table(show_lines = True)

        table.add_column("IP", justify="right", style="green", no_wrap=True)
        table.add_column("Banner", justify="right", style="white")
        table.add_column("Port", style="red")
        table.add_column("City", justify="right", style="green")
        table.add_column("Domains", style="red")
        table.add_column("ASN", style="Cyan")
        
        for index, (a, b, c, d, e, f) in enumerate(zip(self.ip, self.banner, self.port, self.city, self.domains, self.asn)):
            table.add_row(str(a), str(b), str(c), str(d), str(e), str(f))

        console = Console()
        console.print(table)

class startProgram:
    console = Console()
    while True:
        try:
            IP1 = diagram(console.input("[bold blue] Enter an IP address: "))
            IP1.shodan_search()
            IP1.output_format()
        except KeyboardInterrupt:
            console.print("\n[bold red] Exting program...")
            break

IP2 = startProgram()
IP1.shodan_search()
IP1.output_format()
