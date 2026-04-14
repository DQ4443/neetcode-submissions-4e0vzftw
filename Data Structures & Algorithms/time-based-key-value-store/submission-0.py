class TimeMap:

    def __init__(self):
        self.storage = {} # key: list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        lst = self.storage[key]
        low, high = 0, len(lst) - 1
        res = ""

        while low <= high:
            mid = (low + high) // 2
            if lst[mid][0] <= timestamp:
                res = lst[mid][1]
                low = mid + 1         # look for a later timestamp
            else:
                high = mid - 1

        return res
            

