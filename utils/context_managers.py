import json

class JsonContextManager:
    
    def __init__(self, path: str, mode: str = 'r'):
        self.path = path
        self.mode = mode
        self.data = list[dict[str | int]] = []

    def __enter__(self):
        if 'r' == self.mode:
            try:
                with open(self.path, "r", encoding='utf-8') as f:
                    self.data = json.load(f)
            except FileNotFoundError:
                    self.data = []
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if "w" in self.mode or "rw" in self.mode:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4)
        return False

    def add(self, item: dict):
        self.data.append(item)

    def remove(self, predicate):
        self.data = [i for i in self.data if not predicate(i)]

    def filter(self, predicate):
        return [i for i in self.data if predicate(i)]