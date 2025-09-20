**Chức năng chi tiết**: Lõi của đồ án, chứa logic chính như scanning algorithms, socket connections, threading cho concurrency. Nó xử lý quét ARP/TCP/UDP, phát hiện devices/ports. Mục đích: Tách biệt business logic khỏi UI/CLI, dễ test và reuse.

# Hướng dẫn code:

Sử dụng threading cho parallel scans. Áp dụng Clean Code: hàm thuần túy, type hint.
Xử lý exceptions cho network errors.

# Code mẫu netprobe_core/scanner.py

```python
import threading
import socket
from typing import List, Dict

class NetworkScanner:
    def __init__(self, target: str, ports: str = "1-1024"):
        self.target = target
        self.ports = self._parse_ports(ports)
        self.results: List[Dict] = []

    def _parse_ports(self, ports_str: str) -> List[int]:
        """Parse port range."""
        low, high = map(int, ports_str.split("-"))
        return list(range(low, high + 1))

    def scan(self) -> List[Dict]:
        """Scan ports using threading."""
        threads = []
        lock = threading.Lock()
        for port in self.ports:
            t = threading.Thread(target=self._probe_port, args=(port, lock))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return self.results

    def _probe_port(self, port: int, lock: threading.Lock) -> None:
        """Probe a single port."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                with lock:
                    self.results.append({"port": port, "status": "open"})
            sock.close()
        except socket.error:
            pass

if __name__ == "__main__":
    scanner = NetworkScanner("127.0.0.1")
    print(scanner.scan())
```