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
        for items in host['data']:

            ip_addr = str(items['ip_str'])
            self.ip = ip_addr

            city = host.get('city', 'n/a')
            self.city = city

            open_port = str(items['port'])
            self.port = open_port

        print(self.ip, self.city, self.port)

    def output_format(self):
        table = Table(title="Shodan results")
        table = Table(show_lines = True)

        table.add_column("IP", justify="right", style="green", no_wrap=True)
        table.add_column("City", justify="right", style="red")
        table.add_column("Port", style="green")

        console = Console()
        console.print(table)



IP1 = diagram(input("Enter the IP address you want to scan: "))
IP1.shodan_search()

