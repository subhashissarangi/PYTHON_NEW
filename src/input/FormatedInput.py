'''
Created on 30-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

'''

Conversion     Meaning
d            Signed integer decimal.
i            Signed integer decimal.
o            Unsigned octal.
u            Obsolete and equivalent to 'd', i.e. signed integer decimal.
x            Unsigned hexadecimal (lower_case).
X            Unsigned hexadecimal (upper_case).
e            Floating point exponential format (lower_case).
E            Floating point exponential format (upper_case).
f            Floating point decimal format.
F            Floating point decimal format.
g            Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G            Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c            Single character (accepts integer or single character string).
r            String (converts any python object using repr()).
s            String (converts any python object using str()).
%            No argument is converted, results in a "%" character in the result.

'''



print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))
print("Only one percentage sign: %% " % ())


'''
Flag     Meaning
#        Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
0        The conversion result will be zero padded for numeric values.
-        The converted value is left adjusted
         If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
+        A sign character ("+" or "-") will precede the conversion (overrides a "space" flag).
'''
print("%#5X"% (47))
print("%5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("%+d"% (42))
print("% d"% (42))
print("%+2d"% (42))
print("% 2d"% (42))
print("%2d"% (42))

print("First argument: {0}, second one: {1}".format(47,11) )
print("Second argument: {1}, first one: {0}".format(47,11))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148) )

print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))


print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))

'''
Option     Meaning
'<'     The field will be left-aligned within the available space. This is usually the default for strings.
'>'     The field will be right-aligned within the available space. This is the default for numbers.
'0'     If the width field is preceded by a zero ('0') character, sign-aware zero-padding for numeric types will be enabled.

        >>> x = 378
        >>> print("The value is {:06d}".format(x))
        The value is 000378
        >>> x = -378
        >>> print("The value is {:06d}".format(x))
        The value is -00378

','     This option signals the use of a comma for a thousands separator.

        >>> print("The value is {:,}".format(x))
        The value is 78,962,324,245
        >>> print("The value is {0:6,d}".format(x))
        The value is 5,897,653,423
        >>> x = 5897653423.89676
        >>> print("The value is {0:12,.3f}".format(x))
        The value is 5,897,653,423.897
'''
'''
Additionally, we can modify the formatting with the sign option, which is only valid for number types:
Option     Meaning
'+'         indicates that a sign should be used for both positive as well as negative numbers.
'-'         indicates that a sign should be used only for negative numbers, which is the default behavior.
space       indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.
'''

data = dict(province="Ontario",capital="Toronto")
print("The capital of {province} is {capital}".format(**data))
print()

capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))

print()
capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}" 
    print(format_string.format(**capital_country))



print(locals())
a = 42
b=47
def f(self):return 12
print("a={a}, b={b} and f={f}".format(**locals()))

'''
some string methods for formating 
center(...):
'''
s = "Python"
print(s.center(10))
print(s.center(10, "*"))

'''
ljust(...):
'''
print(s.ljust(12))
print(s.ljust(12, "_"))

'''
rjust(...)
'''

print(s.rjust(14))
print(s.rjust(14,"*"))

'''
zfill(...):
'''
account_number = "43447879"
print(account_number.zfill(16))
account_number.rjust(12,"0") 
''' 
 the above statement and this both are same
'''
'''
Python 3.6 introduces formatted string literals. They are prefixed with an 'f'. The formatting syntax is similar to the format
 strings accepted by str.format(). Like the format string of format method, they contain replacement fields formed with curly 
 braces. The replacement fields are expressions, which are evaluated at run time, and then formatted using the format() protocol. 
 It's easiest to understand by looking at the following examples:
'''

price = 11.23
print(f"Price in Euro: {price}")
print(f"Price in Swiss Franks: {price * 1.086}")
print(f"Price in Swiss Franks: {price * 1.086:5.2f}")

for article in ["bread", "butter", "tea"]:
        print(f"{article}")












