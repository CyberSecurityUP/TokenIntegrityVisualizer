import json

PRIVILEGE_MAP = {
    "SeDebugPrivilege": "Allows attaching to any process → Potential credential theft",
    "SeImpersonatePrivilege": "Allows impersonating tokens → Lateral movement risk",
    "SeBackupPrivilege": "Read any file regardless of ACL → Sensitive data exposure",
    "SeTcbPrivilege": "Act as part of OS → Full system compromise",
    "SeLoadDriverPrivilege": "Load unsigned drivers → Kernel code execution",
}

with open("data/mitre_mapping.json") as f:
    MITRE_MAP = json.load(f)

class PrivilegeMapper:
    @staticmethod
    def map_privileges(privileges):
        mapped = []
        for priv, flag in privileges:
            mitre_info = MITRE_MAP.get(priv, None)
            mapped.append({
                "privilege": priv,
                "enabled": bool(flag),
                "business_impact": PRIVILEGE_MAP.get(priv, "Unknown impact"),
                "mitre": mitre_info if mitre_info else {}
            })
        return mapped
