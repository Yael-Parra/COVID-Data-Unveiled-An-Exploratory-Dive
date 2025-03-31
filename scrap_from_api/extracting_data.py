import os
import csv
import requests
from datetime import datetime
import json

BASE_URL = "https://api.covidtracking.com/v1"

# Define all endpoints
endpoints = {
    "us_daily": "/us/daily.json",
    "us_current": "/us/current.json",
    "states_daily": "/states/daily.json",
    "states_current": "/states/current.json",
    "states_info": "/states/info.json"
}

def create_data_directory():
    """Create data directory if it doesn't exist"""
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/backup", exist_ok=True)

def save_as_csv(data, filename):
    """Save data as CSV file"""
    filepath = os.path.join("data", f"{filename}.csv")
    try:
        with open(filepath, "w", newline="", encoding='utf-8') as file:
            if data and isinstance(data, list) and len(data) > 0:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            else:
                print(f"⚠️ No valid data to write for {filename}")
    except Exception as e:
        print(f"⚠️ Error writing CSV for {filename}: {str(e)}")

def save_as_json(data, filename):
    """Save data as JSON file for backup"""
    filepath = os.path.join("data/backup", f"{filename}.json")
    try:
        with open(filepath, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f"⚠️ Error writing JSON for {filename}: {str(e)}")

def fetch_data():
    """Fetch data from all endpoints"""
    create_data_directory()
    
    # Create a metadata file with timestamp
    metadata = {
        "fetch_time": datetime.now().isoformat(),
        "endpoints": list(endpoints.keys()),
        "source": "The COVID Tracking Project",
        "url": BASE_URL
    }
    
    with open(os.path.join("data", "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)
    
    for name, endpoint in endpoints.items():
        url = BASE_URL + endpoint
        print(f"\nFetching {name} data from {url}")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises exception for 4XX/5XX errors
            
            data = response.json()
            
            if not data:
                print(f"⚠️ No data returned for {name}")
                continue
                
            # Save data in both CSV and JSON formats
            save_as_csv(data, name)
            save_as_json(data, name)
            
            print(f"✅ Successfully saved {name} data ({len(data) if isinstance(data, list) else 1} records)")
            
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Failed to fetch {name}: {str(e)}")
        except ValueError as e:
            print(f"⚠️ Invalid JSON response for {name}: {str(e)}")
        except Exception as e:
            print(f"⚠️ Unexpected error processing {name}: {str(e)}")

if __name__ == "__main__":
    fetch_data()
    print("\nData extraction complete!")