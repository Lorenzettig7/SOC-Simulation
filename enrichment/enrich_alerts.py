import requests
import configparser
import json

# Load API keys from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
VT_API_KEY = config['API_KEYS']['virustotal']

# VirusTotal headers
headers = {
    "x-apikey": VT_API_KEY
}

def enrich_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    response = requests.get(url, headers=headers)
    return response.json()

def enrich_hash(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    # Example input (replace as needed)
    ip = "8.8.8.8"
    file_hash = "44d88612fea8a8f36de82e1278abb02f"  # EICAR test file

    ip_result = enrich_ip(ip)
    hash_result = enrich_hash(file_hash)

    with open("sample_output.json", "w") as f:
        json.dump({
            "ip_enrichment": ip_result,
            "hash_enrichment": hash_result
        }, f, indent=4)

    print("Enrichment complete. Results saved to sample_output.json")

if __name__ == "__main__":
    main()
