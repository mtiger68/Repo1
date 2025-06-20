import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import sys

def trace_number(number):
    try:
        phone = phonenumbers.parse(number)
        print(f"\n[✔] Valid Number: {phonenumbers.is_valid_number(phone)}")
        print(f"[🌍] Timezone     : {timezone.time_zones_for_number(phone)}")
        print(f"[📍] Location     : {geocoder.description_for_number(phone, 'en')}")
        print(f"[📶] Carrier      : {carrier.name_for_number(phone, 'en')}")
    except:
        print("[❌] Invalid number format!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py +919999999999")
    else:
        trace_number(sys.argv[1])
