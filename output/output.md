**Chức năng chi tiết**: Xử lý định dạng và lưu kết quả (JSON, CSV, TXT, console). Nó nhận data từ core và export. Mục đích: Linh hoạt output cho CLI/GUI, hỗ trợ logging.

# Hướng dẫn code:

Sử dụng json/csv modules. Tách format khỏi write.

# Code mẫu output/writer.py
```python
import json
import csv
from typing import Dict, Any

def save_to_json(data: List[Dict], filename: str) -> None:
    """Save results to JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def save_to_csv(data: List[Dict], filename: str) -> None:
    """Save results to CSV file."""
    if not data:
        return
    keys = data[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    sample = [{"port": 80, "status": "open"}]
    save_to_json(sample, "results.json")
```