class Debugger:
    @staticmethod
    def warning(msg: str):
        print(f"[WARNING] {msg}")

    @staticmethod
    def error(msg: str):
        print(f"[ERROR] {msg}")
    
    @staticmethod
    def debug(msg: str):
        print(f"[DEBUG] {msg}")