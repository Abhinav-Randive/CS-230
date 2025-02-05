String = "Hello, World!"

def reverse(String):
    for i in range(len(String)-1, -1, -1):
        print(String[i], end="")

print("Original String: ", String)
print("Reversed String: ", end="")
reverse(String)