"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις

	return c	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q00'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 'q00': { '0':'q01', '1':'q01', '2':'q01', '3':'q02' },
       			'q01': { '0':'q03', '1':'q03', '2':'q03', '3':'q03', '4':'q03', '5':'q03', '6':'q03', '7':'q03', '8':'q03', '9':'q03' },
       			'q02': { '0':'q03', '1':'q03', '2':'q03', '3':'q03', '4':'q03', '5':'q03' },
       			'q03': { '0':'q04' },
				'q04': { '0':'q05', '1':'q05', '2':'q05', '3':'q05', '4':'q05', '5':'q05', '6':'q05', '7':'q05', '8':'q05', '9':'q05' },
				'q05': { '0':'q06', '1':'q06', '2':'q06', '3':'q06', '4':'q06', '5':'q06', '6':'q06', '7':'q06', '8':'q06', '9':'q06' },
				'q06': { 'K':'q10', 'G':'q07', 'M':'q11'},
				'q07': { '0':'q08', '1':'q08', '2':'q08', '3':'q08', '4':'q08', '5':'q08', '6':'q08', '7':'q08', '8':'q08', '9':'q08' },
				'q08': { '0':'q09', '1':'q09', '2':'q09', '3':'q09', '4':'q09', '5':'q09', '6':'q09', '7':'q09', '8':'q09', '9':'q09' },
				'q09': { 'K':'q10', 'M':'q11' },
				'q10': { 'T':'q13' },
				'q11': { 'P':'q12' },
				'q12': { 'S':'q13' }
     		  } 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 'q13':'WIND_TOKEN' }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	
