import requests
import time

# Function to display a banner
def show_banner():
    banner = """
    \033[38;5;3m
    =============================================

      Open Redirectional Vulnerability Scanner

    =============================================
    \033[0m
    """
    print(banner)

def load_payloads(file_path):
    """Load OPEN REDIRECTION payloads from a specified file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def is_vulnerable(response_text, payload):
    """Check if the response contains the payload."""
    return payload in response_text

def scan(url, delay, payloads):
    for payload in payloads:
        # Construct the test URL
        test_url = f"{url}?search={payload}"  # Modify as needed
        try:
            response = requests.get(test_url)
            if is_vulnerable(response.text, payload):
                print(f"[+] Found OPEN REDIRECTION vulnerability with payload: {payload}")
            else:
                print(f"[-] No vulnerability found for payload: {payload}")
        except Exception as e:
            print(f"Error accessing {test_url}: {e}")
        
        # Wait for the specified delay
        time.sleep(delay)
        
# Main execution
if __name__ == "__main__":
    # Display the banner
    show_banner()

    target_url = input("Enter the target URL: ")
    payload_file_path = input("Enter the path to the payloads file: ")
    
    # Load payloads from specified file
    payloads = load_payloads(payload_file_path)
    
    if payloads:
        try:
            rate_limit = float(input("Enter delay between requests (in seconds): "))
            scan(target_url, rate_limit, payloads)
        except ValueError:
            print("Error: Please enter a valid number for the rate limit.")
    else:
        print("No valid payloads loaded. Exiting.")
