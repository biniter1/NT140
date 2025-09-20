**Chức năng chi tiết**: Chứa scripts tự động hóa (deploy, build, cron jobs cho periodic scans). Ví dụ: script backup results, run scans nightly. Mục đích: DevOps, không phải core code.

# Hướng dẫn code:

Sử dụng subprocess cho shell, schedule cho cron. Giữ idempotent.

# Code mẫu scripts/backup.py
```python
import shutil
import datetime
from pathlib import Path

def backup_results(source_dir: str, backup_dir: str) -> None:
    """Backup output files to dated folder."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    backup_path = Path(backup_dir) / timestamp
    backup_path.mkdir(exist_ok=True)
    shutil.copytree(Path(source_dir), backup_path)

if __name__ == "__main__":
    backup_results("output/", "backups/")
```