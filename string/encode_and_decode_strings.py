"""
Design an algorithm to encode a list of strings to strings.
The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode.

Input: ["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you"]
Explanation: One possible encode method is: "lint:;code:;love:;you:;"
"""

TEST = ["lint", "yesteryear", "code", "love", "you", "ear"]
ENCODED_STR = "4#lint10#yesteryear4#code4#love3#you3#ear"


# O(n)
def encode(strs: list) -> str:
    encoded_str = ""
    for word in strs:
        encoded_str += f"{len(word)}#{word}"
    return encoded_str


# O(n)
def decode(s: str) -> list:
    decoded = []
    l = 0
    r = 1
    while r < len(s):
        if s[r] == "#":
            substring = s[r + 1:r + int(s[l:r]) + 1]
            decoded.append(substring)
            l += (int(s[l:r]) + len(s[l:r]) + 1)
            r = l + 1
        else:
            r += 1

    return decoded


def test_encode():
    assert encode(TEST) == "4#lint10#yesteryear4#code4#love3#you3#ear"


def test_decode():
    assert decode(ENCODED_STR) == ["lint", "yesteryear", "code", "love", "you", "ear"]