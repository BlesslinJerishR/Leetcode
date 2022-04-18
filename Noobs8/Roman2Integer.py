# Roman to Integer
# I V X  L  C  	D	M
# 1 5 10 50 100 500 1000

ri = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

roman = str(input("Enter a Roman Value : ")).upper()
value = []
for rome in list(roman):
    num = ri.get(rome)
    value.append(num)

print(sum(value))

# Example 1 & 2 Passed Successfully