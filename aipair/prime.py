def isPrime():
    """Check if a number is prime."""
    n = int(input("Enter a number: "))
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isPerfect(number):
    """Check if a number is perfect."""
    if number < 1:
        return False
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Avoid adding the square root twice
                divisors_sum += number // i
    return divisors_sum == number




    





