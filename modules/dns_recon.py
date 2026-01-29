import dns.resolver
import requests

def get_dns_data(domain):
    results = {}
    for r_type in ['A', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, r_type)
            results[r_type] = [str(rdata) for rdata in answers]
        except:
            results[r_type] = []
    return results

def get_subdomains(domain):
    print("[*] Mencari subdomain via crt.sh...")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            return list(set(item['name_value'] for item in res.json()))
    except:
        return []

    return []
