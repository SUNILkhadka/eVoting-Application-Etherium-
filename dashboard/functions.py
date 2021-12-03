from web3 import Web3
import json
import random
from .models import Candidate

# Initalizing connection with ganache .
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
if web3.isConnected():
	print('Web3 connected to local host...')

# Variable initilize 
try:
	print(ListOfCandidate)
except NameError as e :
	print(e)
	ListOfCandidate = []

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

def add_Candidate(MyContract,accounts):
	tx = {
		'from': accounts[2]
	}
	# List of candidates
	cand = Candidate.objects.all()
	for i in cand:
		ListOfCandidate.append(i.name)
	for x in range(len(ListOfCandidate)):
		MyContract.functions.addCandidate(ListOfCandidate[x]).transact(tx)


# Adding candidates to the Blockchain
if not ListOfCandidate:
		add_Candidate(MyContract,accounts)

def deployContract(Voter_name):
	
	#Function Calls
	res = {}
	res = Transactions(MyContract,accounts,address,Voter_name)
	return res

def Transactions(MyContract,accounts,address,Voter_name):
	tx = {
		'from': accounts[2]
	}
	tx_for_vote = {
		'from': accounts[5],
		'to': accounts[7]
	}
	for x in ListOfCandidate:
		if x == str(Voter_name):
			tx_hash = MyContract.functions.vote(ListOfCandidate.index(x)+1).transact(tx)
			print(tx_hash)
			print("Voted for :",x)

def final_result():
	tx = {
		'from': accounts[5]
	}
	result = {}
	results = []
	for x in range(1,len(ListOfCandidate)+1):
		results.append(MyContract.functions.getResult(x).call(tx))
	result['candidates']= ListOfCandidate
	result['result']= results
	print("Success....")
	return (result)

