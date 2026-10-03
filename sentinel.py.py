import time
import hashlib

class PhantomLogicSentinel:
    def __init__(self):
        self.secure_vault = {
            "user_admin": "secret_pass_123",
            "system_config": "active",
            "honey_trap_token": "TRAP_XYZ_999"
        }
        self.vault_signature = self._calculate_signature(str(self.secure_vault))

    def _calculate_signature(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def scan_and_protect(self, query_key, access_type):
        print(f"\n[SCAN] Access attempt for key: '{query_key}' with pattern ({access_type})...")
        time.sleep(0.5)

        if query_key == "honey_trap_token":
            self.trigger_live_mutation(query_key)
            return "❌ ALERT: Unauthorized manipulation attempt detected! Deception shield activated and attacker isolated."

        current_signature = self._calculate_signature(str(self.secure_vault))
        if current_signature != self.vault_signature:
            return "🚨 SECURITY WARNING: Silent structural modification detected, system locked!"

        return f"✅ Access granted successfully to secure data: {self.secure_vault.get(query_key, 'Not found')}"

    def trigger_live_mutation(self, trapped_key):
        print("⚠️ [SHIELD]: Activating reverse response mechanism and encrypting path...")
        self.secure_vault[trapped_key] = "FAKE_DATA_STREAM_ACTIVATED"

if __name__ == "__main__":
    sentinel = PhantomLogicSentinel()
    print(sentinel.scan_and_protect("system_config", "READ"))
    print(sentinel.scan_and_protect("honey_trap_token", "MODIFY"))
    print(sentinel.scan_and_protect("honey_trap_token", "READ"))