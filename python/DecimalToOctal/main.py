"""Convert a Decimal Number to an Octal Number."""

import math

def DecimalToOctal(num):
    """Convert a Decimal Number to an Octal Number."""
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.pow(10, counter))
        counter += 1
        num = math.floor(num / 8)  # basically /= 8 without remainder if any
        # This formatting removes trailing '.0' from `octal`.
    return'{0:g}'.format(float(octal))


def main():
    """Print octal equivelents of decimal numbers."""  
    print(DecimalToOctal(10))  # = 12
    
if __name__ == '__main__':
    main()