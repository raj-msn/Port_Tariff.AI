import requests
import json

# API endpoint
# BASE_URL = "https://port-tariff-ai.onrender.com"
BASE_URL = "http://localhost:8000"

# Test vessel data for SUDESTADA at Port of Durban
vessel_info = """Port: Durban
Vessel Details:

General

Vessel Name: SUDESTADA

Built: 2010

Flag: MLT - Malta

Classification Society: Registro Italiano Navale

Call Sign: [Not provided]

 
Main Details

Lloyds / IMO No.: [Not provided]

Type: Bulk Carrier

DWT: 93,274

GT / NT: 51,300 / 31,192

LOA (m): 229.2

Beam (m): 38

Moulded Depth (m): 20.7

LBP: 222

Drafts SW S / W / T (m): 14.9 / 0 / 0

Suez GT / NT: - / 49,069

 
Communication

E-mail: [Not provided]

Commercial E-mail: [Not provided]


DRY

Number of Holds: 7

 
Cargo Details

Cargo Quantity: 40,000 MT

Days Alongside: 3.39 days

Arrival Time: 15 Nov 2024 10:12

Departure Time: 22 Nov 2024 13:00


Activity/Operations

Activity: Exporting Iron Ore

Number of Operations: 2"""

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        print("✅ Health check passed!\n")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure it's running with: uvicorn api:app --reload")
        return False
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_calculate_all_tariffs():
    """Test calculating all tariffs"""
    print("🔍 Testing calculate all tariffs...")
    
    payload = {
        "vessel_info": vessel_info,
        "requested_dues": None  # None means calculate all
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/calculate-tariffs",
            headers={"Content-Type": "application/json"},
            json=payload
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ All tariffs calculated successfully!")
            print("\n📊 Results:")
            for tariff_name, amount in result["results"].items():
                print(f"   • {tariff_name}: {amount}")
            print()
            return result
        else:
            print(f"❌ API Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

def test_calculate_specific_tariffs():
    """Test calculating specific tariffs only"""
    print("🔍 Testing calculate specific tariffs (Port, Light, Pilotage)...")
    
    payload = {
        "vessel_info": vessel_info,
        "requested_dues": ["Port Dues", "Light Dues", "Pilotage Dues"]
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/calculate-tariffs",
            headers={"Content-Type": "application/json"},
            json=payload
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Specific tariffs calculated successfully!")
            print("\n📊 Results:")
            for tariff_name, amount in result["results"].items():
                print(f"   • {tariff_name}: {amount}")
            print()
            return result
        else:
            print(f"❌ API Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

if __name__ == "__main__":
    print("🚢 Port Tariff Calculator API Test Script")
    print("=" * 50)
    
    # Test sequence
    if test_health_check():
        test_calculate_all_tariffs()
        test_calculate_specific_tariffs()
    
    print("\n🏁 Test script completed!")
    # print("\nTo run the API server: uvicorn api:app --reload")
    # print("To view API docs: http://127.0.0.1:8000/docs")