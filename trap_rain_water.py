def trap_rain_water(height):
    n = len(height)
    left = right = left_max = right_max = water = 0
    right = n - 1
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

n = int(input())
height = list(map(int, input().split()))
print(trap_rain_water(height))