import socket


def get_ip_address(domain):
    """
    ドメイン名からIPアドレスを取得する関数

    Args:
      domain: ドメイン名 (例: "example.com")

    Returns:
      IPアドレス (文字列)。取得できない場合は None を返す。
    """
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Error: Could not resolve domain '{domain}': {e}")
        return None


if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    ip_address = get_ip_address(domain_name)
    if ip_address:
        print(f"The IP address of {domain_name} is: {ip_address}")
