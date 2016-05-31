#Stage 1

def create_table(secret):

	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #alphabet without J
			 
	secret = ''.join(secret.split())
	secret = secret.upper()

	if 'J' in secret:
		secret = secret.replace('J', 'I')
	else:
		pass
		
	# ndsecret secret stands for secret with no duplicates

	ndsecret = ''

	for ch in secret:
		if ch not in ndsecret:
			ndsecret = ndsecret + ch
		else:
			pass

			
	for ch in alphabet:
		if ch not in ndsecret:
			ndsecret += ch
		else:
			pass

	ndlsecret = list(ndsecret)	

	
	position = 0
	global table
	table = list()
	#convert a list to a 5 x 5 array

	for x in range(5):
		row = []
		for c in range(5):
			row.append(ndlsecret[position])
			position = position + 1
		table.append(row)

	return table
		

def format_message(message):
	
	message = message.upper()
	message = ''.join(message.split())
	if 'J' in message:
		message = message.replace('J', 'I')
	else:
		pass

	message_list =  list(message)
	
	i = 0
	
	for i in range(len(message_list)/2):
		if message_list[i] == message_list[i + 1] == 'X':
			message_list.insert(i + 1, 'Q')	
		elif message_list[i] == message_list[i + 1]:
			message_list.insert(i + 1, 'X')
		else:
			pass
		i = i+2

	if len(message_list)%2 != 0:
		if message_list[-1] != 'Z':
			message_list.append("Z")
		else:
			message_list.append("Q")
	#group into pairs
	msg_list_new = []
	i = 0
		
	for i in range((len(message_list))/2 ):
		msg_list_new.append(message_list[2*i:2*i+2])
		
	
	return msg_list_new

secret = raw_input('Please enter the key: ')
message = raw_input('Please enter the message: ')
create_table(secret)
format_message(message)

#Stage 2

def find_letter(letter):
	x = 0
	y = 0
	
	for i in range(5):
		for k in range(5):
			if table[i][k] == letter:
				x = i
				y = k
				
	return x, y		

def encode_pair(a, b):
	if a == b:
		print 'ERROR letters to encode_pair must be distinct'
	r1, c1 = find_letter(a)
	r2,c2 = find_letter(b)
	
	if r1 == r2:
		x = (c1 +1)%5
		y = (c2 + 1)%5
		return table[r1][x], table[r1][y]
	elif c1 == c2:
		x = (r1+1)%5
		y = (r2+1)%5
		return table[x][c1], table[y][c1]
	else:
		return table[r1][c2], table[r1][c1]
		
#print encode_pair('A', 'L') 

#At this point I ran out of ideas :( needed some help

def encode(message):
	message=format_message(message)
	final_table=create_table(secret)
	global cipher
	cipher = []
	
	for l in message:
		v1,w1=find_letter(l[0])
		v2,w2=find_letter(l[1])
		
		if v1==v2:
				if w1==4:
						w1=-1
				if w2==4:
						w2=-1
				cipher.append(final_table[v1][w1+1])
				cipher.append(final_table[v1][w2+1])                
		elif w1==w2:
				if v1==4:
						v1=-1;
				if v2==4:
						v2=-1;
				cipher.append(final_table[v1+1][w1])
				cipher.append(final_table[v2+1][w2])
		else:
				cipher.append(final_table[v1][w2])
				cipher.append(final_table[v2][w1])
	return cipher


s = encode(message)
cipher_text = ''.join(cipher)
print 'Your ciphertext of', message, 'is equivalent to',cipher_text, 'in Playfair cipher.'



