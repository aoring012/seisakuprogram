import socket
import requests
import json


def get_ip_address(domain):
    """
    ドメイン名から IP アドレスを取得する関数

    Args:
        domain: ドメイン名 (例: "example.com")

    Returns:
        IP アドレス (文字列)。取得できない場合は None を返す。
    """
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Error: Could not resolve domain '{domain}': {e}")
        return None


def get_ip_info(ip_address):
    """
    IP アドレスから地理的位置情報などの情報を取得する関数

    Args:
        ip_address: 追跡したい IP アドレス

    Returns:
        取得した情報の辞書。エラーが発生した場合は None を返す。
    """
    try:
        url = (
            f"http://ip-api.com/json/{ip_address}"  # 無料の IP アドレス情報 API を使用
        )
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None


def print_ip_info(ip_data):
    """
    IP アドレス情報を整形して表示する関数

    Args:
        ip_data: get_ip_info 関数から返された辞書
    """
    if ip_data:
        if ip_data["status"] == "success":
            print(f"IP Address: {ip_data['query']}")
            print(f"Country: {ip_data['country']}")
            print(f"Region: {ip_data['regionName']}")
            print(f"City: {ip_data['city']}")
            print(f"ZIP: {ip_data['zip']}")
            print(f"Latitude: {ip_data['lat']}")
            print(f"Longitude: {ip_data['lon']}")
            print(f"ISP: {ip_data['isp']}")
            print(f"Organization: {ip_data['org']}")
            print(f"AS: {ip_data['as']}")  # Autonomous System Number
        else:
            print(f"Failed to retrieve information for IP address.")
            print(f"Message: {ip_data['message']}")
    else:
        print("No data to display.")


if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    ip_address = get_ip_address(domain_name)
    if ip_address:
        print(f"The IP address of {domain_name} is: {ip_address}")
        ip_data = get_ip_info(ip_address)
        print_ip_info(ip_data)
    else:
        print(f"Could not retrieve IP address for {domain_name}.")