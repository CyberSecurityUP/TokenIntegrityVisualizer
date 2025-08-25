import win32security

class ObjectACL:
    @staticmethod
    def get_acl(path):
        try:
            sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
            dacl = sd.GetSecurityDescriptorDacl()
            permissions = []
            for i in range(dacl.GetAceCount()):
                ace = dacl.GetAce(i)
                permissions.append(str(ace))
            return permissions
        except Exception as e:
            return [f"Error: {str(e)}"]
