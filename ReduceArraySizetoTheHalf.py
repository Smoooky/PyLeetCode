class Solution:
    def minSetSize(self, arr: list) -> int:
        counter = {}
        for i in arr:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}
        sum = 0
        res = 0
        for i in counter.keys():
            res += 1
            sum += counter[i]
            if sum >= (len(arr) / 2):
                return res


def main():
    arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
    sol = Solution()
    print(sol.minSetSize(arr))


if __name__ == '__main__':
    main()