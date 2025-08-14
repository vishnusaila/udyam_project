import requests
from bs4 import BeautifulSoup
import json
import os

# URL of the form to scrape (Step 1 & Step 2)
URL = "https://udyamregistration.gov.in/UdyamRegistration.aspx"

def scrape_form():
    print(f"Fetching {URL} ...")
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    fields = []
    for tag in soup.find_all(['input', 'select', 'textarea', 'button']):
        label = ""
        if tag.get("id"):
            lbl = soup.find("label", {"for": tag.get("id")})
            if lbl:
                label = lbl.get_text(strip=True)

        fields.append({
            "tag": tag.name,
            "id": tag.get("id"),
            "name": tag.get("name"),
            "type": tag.get("type"),
            "label": label,
            "placeholder": tag.get("placeholder"),
            "required": tag.has_attr("required"),
            "pattern": tag.get("pattern"),
            "maxlength": tag.get("maxlength"),
            "options": [opt.get_text(strip=True) for opt in tag.find_all("option")] if tag.name == "select" else None
        })

    # Save schema.json inside udyam_app folder
    app_folder = os.path.join(os.path.dirname(__file__), "udyam_app")
    output_path = os.path.join(app_folder, "schema.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(fields, f, indent=2, ensure_ascii=False)

    print(f"✅ Schema saved to {output_path}")

if __name__ == "__main__":
    scrape_form()
