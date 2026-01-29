import os
import pandas as pd
from datetime import datetime
from modules.dns_recon import get_dns_data, get_subdomains
from modules.whois_recon import get_whois_data
from modules.shodan_recon import get_shodan_info

def banner():
    print("="*60)
    print("   AUTO-RECON OSINT TOOL | UAS PPL AMIKOM 2025/2026")
    print("="*60)

def main():
    banner()
    target = input("Masukkan Domain Target (contoh: amikom.ac.id): ").strip()
    
    if not target:
        print("[!] Target tidak boleh kosong.")
        return

    # 1. Otomatisasi Pencarian Subdomain & DNS
    print(f"\n[*] Memulai pengumpulan data untuk: {target}")
    subdomains = get_subdomains(target)
    dns_records = get_dns_data(target)

    # 2. Otomatisasi Whois Data
    whois_data = get_whois_data(target)

    # 3. Otomatisasi Shodan Intelligence
    shodan_data = get_shodan_info(target)

    # 4. Penggabungan Data & Ekspor Otomatis
    print("\n[*] Menyusun laporan akhir...")
    
    report_dict = {
        "Target": target,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Registrar": whois_data.get("Registrar"),
        "Org": whois_data.get("Organization"),
        "IP_Address": shodan_data.get("IP"),
        "Open_Ports": str(shodan_data.get("Ports")),
        "Vulnerabilities": str(shodan_data.get("Vulnerabilities")),
        "Total_Subdomains": len(subdomains),
        "Subdomain_List": ", ".join(subdomains[:10]) + "..." if subdomains else "None"
    }

    # Pastikan folder reports ada
    if not os.path.exists('reports'):
        os.makedirs('reports')

    df = pd.DataFrame([report_dict])
    report_path = f"reports/osint_{target}.csv"
    df.to_csv(report_path, index=False)

    print("="*60)
    print(f"[+] PROSES SELESAI!")
    print(f"[+] Laporan PDF/CSV dapat dibuat dari: {report_path}")
    print("="*60)

if __name__ == "__main__":
    main()
