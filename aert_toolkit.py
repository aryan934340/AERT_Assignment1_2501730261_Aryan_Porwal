# Algorithmic Efficiency & Recursion Toolkit (AERT)

# ----------------------------
# STACK ADT IMPLEMENTATION
# ----------------------------

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ----------------------------
# FACTORIAL (RECURSION)
# ----------------------------

def factorial(n):
    if n < 0:
        return "Invalid Input"

    if n == 0:
        return 1

    return n * factorial(n-1)


# ----------------------------
# FIBONACCI
# ----------------------------

naive_calls = 0
memo_calls = 0


def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n

    return fib_naive(n-1) + fib_naive(n-2)


memo = {}

def fib_memo(n):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


# ----------------------------
# TOWER OF HANOI
# ----------------------------

def hanoi(n, source, auxiliary, destination, stack):

    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    hanoi(n-1, auxiliary, source, destination, stack)


# ----------------------------
# RECURSIVE BINARY SEARCH
# ----------------------------

def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid-1)

    else:
        return binary_search(arr, key, mid+1, high)


# ----------------------------
# MAIN FUNCTION
# ----------------------------

def main():

    print("FACTORIAL TESTS")
    print("0! =", factorial(0))
    print("1! =", factorial(1))
    print("5! =", factorial(5))
    print("10! =", factorial(10))

    print("\nFIBONACCI TESTS")

    for n in [5, 10, 20, 30]:

        global naive_calls
        global memo_calls
        global memo

        naive_calls = 0
        memo_calls = 0
        memo = {}

        naive_result = fib_naive(n)
        memo_result = fib_memo(n)

        print(f"\nn = {n}")
        print("Naive Fibonacci:", naive_result)
        print("Naive Calls:", naive_calls)

        print("Memo Fibonacci:", memo_result)
        print("Memo Calls:", memo_calls)

    print("\nTOWER OF HANOI (n = 3)")

    stack = StackADT()

    hanoi(3, "A", "B", "C", stack)

    print("\nBINARY SEARCH TESTS")

    arr = [1,3,5,7,9,11,13]

    print("Search 7:", binary_search(arr,7,0,len(arr)-1))
    print("Search 1:", binary_search(arr,1,0,len(arr)-1))
    print("Search 13:", binary_search(arr,13,0,len(arr)-1))
    print("Search 2:", binary_search(arr,2,0,len(arr)-1))

    empty = []
    print("Search in empty array:", binary_search(empty,5,0,len(empty)-1))


if __name__ == "__main__":
    main()