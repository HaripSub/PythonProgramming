original_string = "this is a string"

print(type(original_string))

substring = "STRING"

print(len(original_string))

print(original_string.upper())

print(substring.lower())

print(original_string.title())

print(original_string.capitalize())

print(original_string.find('a'))

print(original_string.replace('this', 'the given variable'))

print(original_string.startswith('this'))

print(original_string.endswith('string'))

print(original_string.find('string'))

print(original_string.count('s'))

print(original_string.center(20))

price_tag = 'This article costs {price:.2f} euros'

print(price_tag.format(price=56.89))

digit_string = "12345"
is_digit = digit_string.isdigit()
print(is_digit)

alpha_string = "abc"
is_alpha = alpha_string.isalpha()
print(is_alpha)

is_upper = "HELLO".isupper()
print(is_upper)

word_list = original_string.split()
print(word_list)

joined_string = '-'.join(word_list)
print(joined_string)