a = [3, 2, 3, 5, 7, 9, 20, 9, 7, 31]

def dedupe(items):
    seen = set()
    ret = []
    for item in items:
        if item not in seen:
            ret.append(item)
            seen.add(item)
    return ret

def dedupe2(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item

print(dedupe(a))

gen = dedupe2(a)
print(next(gen))
print(next(gen))
print(next(gen))