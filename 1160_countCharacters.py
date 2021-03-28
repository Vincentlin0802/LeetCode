import collections

def countCharacters(words, chars):
    ans = 0
    cnt = collections.Counter(chars)
    for w in words:
        c = collections.Counter(w)
        if all([c[i] <= cnt[i] for i in c]):
            ans += len(w)
    return ans


if __name__ == '__main__':
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    print(countCharacters(words, chars))