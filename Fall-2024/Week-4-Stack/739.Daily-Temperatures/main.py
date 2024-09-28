def dailyTemperatures(self, temps: list[int]) -> list[int]:
    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and stack[-1][0] < t:
            st, si = stack.pop()
            result[si]= i - si
        stack.append((t,i))
    return result

def main():
    print(f"this is the result: {dailyTemperatures([73,74,75,71,69,72,76,73])}")
                                   
if __name__ == "__main__":
    main()