import sys
from pathlib import Path
text = Path(sys.argv[1]).read_text(encoding="utf-8")
required = ["runAsNonRoot: true", "allowPrivilegeEscalation: false", "readOnlyRootFilesystem: true", "capabilities:", "resources:"]
missing = [x for x in required if x not in text]
if missing:
    print("Kubernetes security validation failed. Missing:", missing)
    sys.exit(1)
print("Kubernetes security validation passed.")
