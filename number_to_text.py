import sys

sys.setrecursionlimit(10000)

unidades = {
    0: "",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
    10: "TEN",
    11: "ELEVEN",
    12: "TWELVE",
    13: "THIRTEEN",
    14: "FOURTEEN",
    15: "FIFTEEN",
    16: "SIXTEEN",
    17: "SEVENTEEN",
    18: "EIGHTEEN",
    19: "NINETEEN"
}

dezenas = {
    0: "",
    2: "TWENTY",
    3: "THIRTY",
    4: "FORTY",
    5: "FIFTY",
    6: "SIXTY",
    7: "SEVENTY",
    8: "EIGHTY",
    9: "NINETY"
}

centenas = {
    0: "",
    1: "ONE HUNDRED"
}

def n_to_world(n):
    if n < 20:
        str = unidades[n]
        return len(str)
    
    hundreds = n // 100
    dozens = (n - hundreds * 100) // 10
    units = n - hundreds * 100 - dozens * 10
    str = '{} {} {}'.format(centenas[hundreds], dezenas[dozens], unidades[units]).strip()
    return len(str)

n = int(input())

def recursive_n_to_world(n, it = 1):
    if it == 1000:
        print(n)
        return n
    return recursive_n_to_world(
        n_to_world(n), it + 1
    )
    
print(
    recursive_n_to_world(n)
)