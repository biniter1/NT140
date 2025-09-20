**Chức năng chi tiết**: Chứa các hàm hỗ trợ mạng như ARP resolution, IP parsing, subnet calculation. Nó hỗ trợ core bằng cách cung cấp utilities cho discovery devices, không chứa logic scanning chính. Mục đích: Reuse code cho CLI/GUI/plugins.

# Hướng dẫn code:

Sử dụng scapy hoặc subprocess cho ARP (nếu có). Giữ functions pure.

# Code mẫu network/ip_utils.py

```python
from ipaddress import IPv4Network
from typing import List

def get_subnet_hosts(subnet: str) -> List[str]:
    """Get list of hosts in subnet."""
    network = IPv4Network(subnet, strict=False)
    return [str(ip) for ip in network.hosts()]

def is_valid_ip(ip: str) -> bool:
    """Validate IP address."""
    try:
        IPv4Network(ip + "/32")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print(get_subnet_hosts("192.168.1.0/24"))
```