def fibonacci(n):
   if n == 1 or n == 2:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    x = fibonacci(5)
    print(x)
