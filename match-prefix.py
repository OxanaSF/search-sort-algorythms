def match_prefix(lst, prefix):
    # write your code
    low = 0
    high = len(lst) - 1

    while low <= high:
      mid = (low + high) // 2
      if lst[mid][0: len(prefix)] == prefix:
        return mid

      elif lst[mid][0: len(prefix)] > prefix:
        high = mid -1
      else:
        low = mid + 1

    return -1

print(match_prefix(['bicycle', 'ex-wife', 'replace'], 're'))

print(match_prefix(['bicycle', 'replace', 'ex-wife'], 're'))

print(match_prefix(['bicycle', 'place', 'ex-wife'], 're'))



