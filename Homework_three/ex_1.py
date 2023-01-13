# 1.1 f-string
sentence = 'Dream big'
sentence = sentence.split()
print(f'!{sentence[1]} ! {sentence[0]}!')

# 1.2 method format()
print('!{} ! {}!'.format(sentence[1], sentence[0]))

# 1.3 method %
print('!%s ! %s!' % (sentence[1], sentence[0]))