import requests
import json


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
        response.raise_for_status()  # エラーが発生した場合、例外を発生させる
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
            print(f"Failed to retrieve information for IP address: {ip_data['query']}")
            print(f"Message: {ip_data['message']}")
    else:
        print("No data to display.")


if __name__ == "__main__":
    ip_address = input("Enter an IP address to track: ")
    ip_data = get_ip_info(ip_address)
    print_ip_info(ip_data)
