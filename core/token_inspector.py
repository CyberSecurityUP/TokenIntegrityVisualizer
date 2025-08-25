import win32security
import win32api
import win32con

class TokenInspector:
    def __init__(self, pid):
        self.pid = pid

    def get_token_info(self):
        try:
            process_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, self.pid)
            token_handle = win32security.OpenProcessToken(process_handle, win32con.TOKEN_QUERY)
            user_sid = win32security.GetTokenInformation(token_handle, win32security.TokenUser)[0]

            # Resolver privilégios para nomes legíveis
            raw_privs = win32security.GetTokenInformation(token_handle, win32security.TokenPrivileges)
            privileges = [(TokenInspector.resolve_privilege_name(luid[0]), luid[1]) for luid in raw_privs]

            integrity_level = win32security.GetTokenInformation(token_handle, win32security.TokenIntegrityLevel)
            
            return {
                "pid": self.pid,
                "sid": win32security.ConvertSidToStringSid(user_sid),
                "privileges": privileges,
                "integrity_level": integrity_level
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def resolve_privilege_name(luid):
        try:
            return win32security.LookupPrivilegeName(None, luid)
        except:
            return str(luid)
