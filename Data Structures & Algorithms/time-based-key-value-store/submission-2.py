class TimeMap:
    # store as { key : [(1, happy), (3, sad)]}
    # get should look for key, then binary search on store[key][0]

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        vals = self.store[key]

        low, high = 0, len(vals) - 1
        res = ""

        # record when val <= timestamp

        while low <= high:
            mid = (low + high) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return res

