from rich.console import Console
from rich.table import Table
import shodan
import sys

# ENTER SHODAN KEY HERE
SHODAN_API_KEY = ''
api = shodan.Shodan(SHODAN_API_KEY)


class diagram:
    def __init__(self, *argv):
        for arg in argv:
            self.IP = argv

    def shodan_search(self):
        host = api.host(self.IP)
        self.ip, self.city, self.port = [],[],[]
        for items in host['data']:
            self.ip.append(items['ip_str'])
            self.city.append(host.get('city', 'n/a'))
            self.port.append(items['port'])
        #print(len(self.ip), len(self.city), len(self.port)) # Verifying list match 

    def output_format(self):
        table = Table(title="Shodan results")
        table = Table(show_lines = True)

        table.add_column("IP", justify="right", style="green", no_wrap=True)
        table.add_column("City", justify="right", style="red")
        table.add_column("Port", style="green")

        for index, (a, b, c ) in enumerate(zip(self.ip, self.city, self.port)):
            table.add_row(str(a), str(b), str(c))

        console = Console()
        console.print(table)


IP1 = diagram(input("Enter the IP address you want to scan: "))
IP1.shodan_search()
IP1.output_format()
