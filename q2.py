def main():
    print("Hello World!")


def countPairsWithDiffK(arr, n, k):
    arr.sort()
    l = 0
    r = 0
    count = 0
    while r < n:
        if arr[r] - arr[l] == k:
            count += 1
            l = l + 1
            r = r + 1
        elif arr[r] - arr[l] < k:
            r = r + 1
        else:
            l = l + 1
    return count

if __name__ == "__main__":
    # Driver program
    #arr = [-1, 1, 5, 3]
    arr = [-1, 1, 5, 3]
    n = len(arr)
    k = 2
    print("Count of pairs with given diff is ",
          countPairsWithDiffK(arr, n, k))
