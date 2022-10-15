class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        if len(nums) < 3:
            return False
        i = 0
        j = 2147483648
        k = 2147483648
        while i < len(nums):
            print('nums[i] = ' + str(nums[i]) + 'j = ' + str(j) + 'k = ' + str(k))
            if nums[i] <= j:
                j = nums[i]
            elif nums[i] <= k:
                k = nums[i]
            else:
                return True
            i += 1
        return False


def main():
    nums = [0,4,2,1,0,-1,-3]
    sol = Solution()
    print(sol.increasingTriplet(nums))


if __name__ == '__main__':
    main()