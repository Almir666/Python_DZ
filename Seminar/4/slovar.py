# lang = {'а': 'a',
#          'б': 'b',
#          'в': 'v',
#          'г': 'g',
#          'д': 'd',
#          'е': 'e',
#          'ё': 'e',
#          'ж': 'zh',
#          'з': 'z',
#          'и': 'i',
#          'й': 'y',
#          'к': 'k',
#          'л': 'l',
#          'м': 'm',
#          'н': 'n',
#          'о': 'o',
#          'п': 'p',
#          'р': 'r',
#          'с': 's',
#          'т': 't',
#          'у': 'u',
#          'ф': 'f',
#          'х': 'kh',
#          'ц': 'ts',
#          'ч': 'ch',
#          'ш': 'sh',
#          'щ': 'shch',
#          'ъ': '',
#          'ы': 'y',
#          'ь': '',
#          'э': 'e',
#          'ю': 'yu',
#          'я': 'ya',
#          ' ': ' '
# }

# value = 'Мама мыла раму'
# result = ''

# for i in value:
#     result += lang[i.lower()]

# print(result)

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():

	if "а" <= s <= "я":
		slug += t[ord(s) - ord('а')]
	# elif s == "ё":
	# 	slug = 'yo'
	# elif s in " !?;:.,":
	# 	slug = "-"
	else:
		slug += s

# while slug.count('--'):
# 	slug = slug.replace('--', '-')

print(slug)