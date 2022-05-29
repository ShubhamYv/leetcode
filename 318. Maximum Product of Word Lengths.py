def maxProducts(words):
    words.sort(key=len, reverse=True)
    best, bitsets = 0, {}
    for i in range(len(words)):
        wlen, bitset = len(words[i]), 0
        if wlen * len(words[0]) < best:
            return best
        for c in words[i]:
            bitset |= 1 << ord(c) - 97
        if bitset not in bitsets:
            for k, v in bitsets.items():
                if not bitset & k:
                    best = max(best, wlen * v)
            bitsets[bitset] = wlen
    return best

def main():
    words= ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(maxProducts(words))

if __name__ == '__main__':
    main()