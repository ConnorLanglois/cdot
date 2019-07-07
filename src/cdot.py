import re

def lex(string):
	separator_pattern = r'(\t|\n)'
	operator_pattern = r'(\(|\)|\^|\*|/|\+|-|=|<|>|<=|>=|and|or)'
	number_pattern = r'(\d+\.\d+|\d+)(?!\w)'
	string_pattern = r"('.+')"
	keyword_pattern = r'\s(if|while|func)\s'
	identifier_pattern = r'(\b[a-zA-Z_]\w*)'
	token_pattern = f'{separator_pattern}|{operator_pattern}|{number_pattern}|{string_pattern}|{keyword_pattern}|{identifier_pattern}'
	non_tokens = re.sub(token_pattern, '', string)

	# TODO: FIX
	if len(non_tokens) > 0:
		print('SYNTAX ERROR:', "'" + non_tokens + "'")

	token_tuples = re.findall(token_pattern, string)
	tokens = [list(filter(lambda token: token != '', token_tuple))[0] for token_tuple in token_tuples]

	return tokens

with open('tests/test.cdot') as cdot:
	print(lex(cdot.read()))
