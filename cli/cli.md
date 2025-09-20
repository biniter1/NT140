**Chức năng chi tiết**: Thư mục này chứa mã cho giao diện dòng lệnh (CLI), xử lý arguments từ người dùng (ví dụ: quét IP, port range). Nó sử dụng thư viện như argparse để parse lệnh, gọi core functions, và hiển thị kết quả. Mục đích: Cho phép chạy nhanh từ terminal, như netprobe scan --ip 192.168.1.0/24. Đây là phần chính cho người dùng chuyên nghiệp, dễ tích hợp vào scripts.

# Hướng dẫn code:

Sử dụng argparse cho CLI. Giữ hàm nhỏ, tách logic parse khỏi execution.
Thêm logging cho debug. Export CLI như executable với setuptools.

# Code mẫu cli/main_cli.py
```python
import argparse
import logging
from netprobe_core.scanner import NetworkScanner

logging.basicConfig(level=logging.INFO)

def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="NetProbe: Network Scanner CLI")
    parser.add_argument("-t", "--target", required=True, help="Target IP or subnet (e.g., 192.168.1.0/24)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range")
    parser.add_argument("-o", "--output", help="Output file")
    return parser.parse_args()

def run_scan(args: argparse.Namespace) -> None:
    """Run the network scan based on args."""
    scanner = NetworkScanner(args.target, args.ports)
    results = scanner.scan()
    if args.output:
        from output.writer import save_to_file
        save_to_file(results, args.output)
    else:
        print(results)

if __name__ == "__main__":
    args = parse_arguments()
    run_scan(args)
```