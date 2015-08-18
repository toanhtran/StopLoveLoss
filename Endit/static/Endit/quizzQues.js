var pos = 0, test, test_status, question, choice, choices, chA, chB, chC, correct = 0;
var questions = [
    [ "I typically I am the :", "Breaker upper; I leave a trail of broken hearts", "Broken hearted; Always the bridesmaid never the bride", "Player; Don't hate the player, hate the game", "B" ],
	[ "After a breakup I think", " Glad it's over, that was the longest two weeks of my life. ", "I will be spinster cat person and alone forever", "It was the Titanic but I didn't make it out in time.", "C" ],
	[ "What is the average duration of your past relationships?", "Two - four weeks; My love life is a revolving door", "Six month to a year; Unoffically offical ", "Two years +; I'm serial monagamist", "C" ],
	[ "I believe everyone I date could be 'The One'?", "True; I believe in love at first sight", "False; Love is a battlefield", "Maybe, if their FICO score is over 800", "A" ],
	[ "I attract losers?", "Yes, I'm a loser magnet", "No, I can read people like a book", "Sometimes, I'm 50/50", "A" ]
];
function _(x){
	return document.getElementById(x);
}
function renderQuestion(){
	test = _("test");
	if(pos >= questions.length){
		test.innerHTML = "<h2>You got "+correct+" of "+questions.length+" questions correct. <br> You are clueless when it comes to dating. <br>You need all the help you can get!</h2>";
		_("test_status").innerHTML = "Test Completed";
		pos = 0;
		correct = 0;
		return false;
	}
	_("test_status").innerHTML = "Question "+(pos+1)+" of "+questions.length;
	question = questions[pos][0];
	chA = questions[pos][1];
	chB = questions[pos][2];
	chC = questions[pos][3];
	test.innerHTML = "<h3>"+question+"</h3>";
	test.innerHTML += "<input type='radio' name='choices' value='A'> "+chA+"<br>";
	test.innerHTML += "<input type='radio' name='choices' value='B'> "+chB+"<br>";
	test.innerHTML += "<input type='radio' name='choices' value='C'> "+chC+"<br><br>";
	test.innerHTML += "<button onclick='checkAnswer()'>Submit Answer</button>";
}
function checkAnswer(){
	choices = document.getElementsByName("choices");
	for(var i=0; i<choices.length; i++){
		if(choices[i].checked){
			choice = choices[i].value;
		}
	}
	if(choice == questions[pos][4]){
		correct++;
	}
	pos++;
	renderQuestion();
}
window.addEventListener("load", renderQuestion, false);