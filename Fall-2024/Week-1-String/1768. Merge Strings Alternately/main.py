def mergeAlternately(word1: str, word2: str) -> str:
        result = ""
        i,j = 0,0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1    
        return result

# Time Complexity: O(n+m)
# Space Complexity: O(1)

def main():
    print(f"this is the result: {mergeAlternately(word1 = "abc", word2 = "pqr")}")
                                   
if __name__ == "__main__":
    main()