def isPalindrome(s: str) -> bool:
    n = len(s)
    L = 0
    R = n - 1
    s.lower()

    while L < R:
        if not s[L].isalnum():
            L += 1
            continue

        if not s[R].isalnum():
            R -= 1
            continue

        if s[L] != s[R]:
            return False

        L += 1
        R -= 1
    return True

# Time Complexity: O(n)
# Space Complexity: O(1)

def main():
    print(f"this is the result: {isPalindrome("racecar")}")
                                   
if __name__ == "__main__":
    main()