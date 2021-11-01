

// contract Evoting{
// 	//store candidates
// 	struct Candidate{
// 		uint id;
// 		string name;
// 		uint voteCount;
// 	}

// 	mapping(address => bool) public votedList;
// 	mapping(uint => Candidate) public candidate;

// 	uint private candidateCount;
// 	uint public Voters;
    

//     modifier OnlyIfNotVoted{
//         require(
//         	votedList[msg.sender] == false,
//         	"Sorry! You have already voted"
//         	);				// you can use throw instead;
//         	_;
//     }

// 	function addCandidate
// 		(
// 			string memory _name
// 		) 
// 			public 
// 		{
// 			candidateCount ++;
// 			candidate[candidateCount] = Candidate(candidateCount,_name,0);
// 		}	

// 	function vote(uint _candidateID) public OnlyIfNotVoted {
		
// 		// Checking wether the voter has already voted or not .
// 		require(
//         	votedList[msg.sender] == false //or you can also use !votedList[msg.sender] for condition
//         	//"Sorry! You have already voted"
//         ); 

//         // Checking the candidate is a valid
//         require(
//         	_candidateID >0 && _candidateID <=candidateCount
//         	//"Invalid candidate"
//         );

// 		// update candidate vote count
// 		candidate[_candidateID].voteCount ++;
// 		Voters ++;
// 		votedList[msg.sender] = true;
// 	}
// 	function totalVoters() public view returns(uint){
// 		return Voters;
// 	} 
// 	function getResult(uint _candidateID) public view returns(uint){ 
// 		return (candidate[_candidateID].voteCount);
// 	}
// 	function getName(uint _candidateID) public view returns(string memory){
// 		return (candidate[_candidateID].name);
// 	}
// }