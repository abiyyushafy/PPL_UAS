import whois

def get_whois_data(domain):
    print("[*] Mengambil data Whois...")
    try:
        w = whois.whois(domain)
        return {
            "Registrar": w.registrar,
            "Organization": w.org,
            "Creation_Date": str(w.creation_date[0]) if isinstance(w.creation_date, list) else str(w.creation_date)
        }
    except:
        return {}
