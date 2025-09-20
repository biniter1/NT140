**Chức năng chi tiết**: Cho phép mở rộng (ví dụ: plugin cho SNMP probe, email alert). Mỗi plugin là module implement interface từ core. Mục đích: Modularity, cộng đồng contribute.

# Hướng dẫn code:

Sử dụng abstract base class. Load plugins dynamically với importlib.

# Code mẫu plugins/base_plugin.py
```python
from abc import ABC, abstractmethod
from typing import Dict

class BasePlugin(ABC):
    @abstractmethod
    def probe(self, target: str) -> Dict[str, Any]:
        """Probe the target."""
        pass

# Ví dụ: plugins/snmp_plugin.py
from .base_plugin import BasePlugin

class SNMPPlugin(BasePlugin):
    def probe(self, target: str) -> Dict[str, Any]:
        # Implement SNMP logic
        return {"snmp_data": f"Probed {target}"}
```