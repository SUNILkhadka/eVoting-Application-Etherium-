from web3 import Web3
import json
import random
import js2py

# Initalizing connection with ganache .
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
if web3.isConnected():
	print('Web3 connected to local host...')

# Random votes
# rand = []
# for i in range(10):
# 	rand.append(random.randint(1,10))

# print("Using js2py")
# py = js2py.eval_js("import detectEthereumProvider from '@metamask/detect-provider'; const provider = await detectEthereumProvider(); if (provider) {startApp(provider); // initialize your app } else {console.log('Please install MetaMask!');}")
# print(py)
	
def deployContract():
	data = json.load(open("build/contracts/Evoting.json","r"))

	# It indents the data format
	# new_data = json.dumps(data, indent=2)    
	
	# Getting the abi key and bytecode from json file
	abi = data['abi']
	bytecode = data["deployedBytecode"]
	address = web3.toChecksumAddress(data['networks']['5777']['address'])
	
	# Instantiating contract
	MyContract = web3.eth.contract(
		abi= abi, 
		bytecode=bytecode,
		address=address
		)

	# getting accounts form ganache
	accounts = web3.eth.accounts

	#Function Calls
	res = {}
	res = Transactions(MyContract,accounts,address)
	return res

def Transactions(contract,accounts,address):

	tx = {
		'from': accounts[0]
	}
	tx_for_vote = {
		'from': accounts[0],
		'to': accounts[1]
	}

	# List of candidates
	ListOfCandidate = [
		'Sunil khadka',
		'Doleshor khadka',
		'Rameshower yadav',
		'KP Sharma Oli',
		'Sher Bahadur Deuba',
		'Gagan Thapa',
		'Prachanda ',
		'Sushil Koirala',
		'Khil Raj Regmi',
		'Baburam Bhattarai'
	]

	for x in range(10):
		contract.functions.addCandidate(ListOfCandidate[x]).transact(tx)
	
	print('Candidate Added and voting has started')
	for x in range(1):
		# if x%10 == 0:
		# 	print(x)
		tx_hash = contract.functions.vote(random.randint(1,10)).transact(tx_for_vote)
	print("Voting is done")
	tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
	print("transaction done")
	print(tx_receipt)
	# print(contract.functions.getName(1).call())
	# print(contract.functions.getName(2).call())
	
	# Results
	print('Results are :')
	result = {}
	results = []
	for x in range(1,11):
		results.append(contract.functions.getResult(x).call())
	
	# for x in range(10):
	# 	result[str(ListOfCandidate[x])] = results[x]
		# print('Candidate name: {} Vote : {}'.format(ListOfCandidate[x],result[x]))
	result['candidates']= ListOfCandidate
	result['result']= results
	account()
	return (result)

def account():
	acc = web3.eth.get_accounts()

	print(acc)
	