import nmap

inicio = 75

fim = 80

alvo = '172.19.160.1'

scanner = nmap.PortScanner()

for ip in range(inicio, fim+1):
    res= scanner.scan(alvo,str(ip))

res=res['scan'][alvo]['tcp'][ip]['state']

print(f'porta{ip} is {res}.')