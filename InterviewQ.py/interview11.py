def check(bananas, mid_val, H):
    time = 0
    for i in range(len(bananas)):
        # to get the ceil value
        if (bananas[i] % mid_val != 0):
            # in case of odd number, use ceiling division
            time += bananas[i] // mid_val + 1
        else:
            # in case of even number
            time += bananas[i] // mid_val
    
    # check if the time required is less than or equal to H
    if time <= H:
        return True
    else:
        return False


def minEatingSpeed(piles, H):
    # The minimum speed of eating must be at least 1
    start = 1

    # The maximum speed of eating is the maximum number of bananas in any pile
    end = max(piles)

    while start < end:
        mid = start + (end - start) // 2

        # Check if the mid speed is valid
        if check(piles, mid, H):
            # If valid, continue to search lower speed
            end = mid
        else:
            # If can't finish bananas in given hours, increase the speed
            start = mid + 1
    
    return start  # or 'end', since start == end at the end of the loop


# Driver code
piles = [30, 11, 23, 4, 20]
H = 6
print(minEatingSpeed(piles, H))

piles = [3, 6, 7, 11]
H = 8
print(minEatingSpeed(piles, H))