text = "aclc butuan"
pattern = input("Enter the pattern to find in the sentence: ")

found = False

for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        found = True
        length = i + len(pattern)
        print(f"Index: {i}, Length: {length}")
        break

if not found:
    print("Pattern not found in the sentence.")

