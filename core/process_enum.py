import psutil
from core.token_inspector import TokenInspector

class ProcessEnumerator:
    @staticmethod
    def list_processes():
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                inspector = TokenInspector(proc.info['pid'])
                token_info = inspector.get_token_info()
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "token": token_info
                })
            except Exception as e:
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "error": str(e)
                })
        return processes
