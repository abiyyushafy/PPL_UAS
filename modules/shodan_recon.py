import shodan
import socket

# Masukkan Shodan Developer API Key Anda di sini
SHODAN_API_KEY = "MASUKKAN_KEY_ANDA" 

def get_shodan_info(domain):
    print("[*] Menjalankan Shodan Intelligence...")
    try:
        ip = socket.gethostbyname(domain)
        api = shodan.Shodan(SHODAN_API_KEY)
        host = api.host(ip)
        return {
            "IP": host['ip_str'],
            "Ports": host['ports'],
            "Vulnerabilities": host.get('vulns', 'None'),
            "OS": host.get('os', 'n/a')
        }
    except Exception as e:
        return {"Error": "Shodan Lookup Gagal"}
