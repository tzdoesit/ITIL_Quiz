const question = document.getElementById('question');
const choices = Array.from(document.getElementsByClassName('choice-text'));
const why = document.getElementById('why-text');
const progressText = document.getElementById('progressText');
const scoreText = document.getElementById('score');
const progressBarFull = document.getElementById('progressBarFull');
const loader = document.getElementById('loader');
const game = document.getElementById('game');
const topic = document.getElementById('topic');
let currentQuestion = {};
let acceptingAnswers = false;
let score = 0;
let questionCounter = 0;
let availableQuestions = [];
// window.debugMode = true;

let questions = [];
fetch("questions.json")
    .then(res => {
        return res.json();
    })
    .then(loadedQuestions => {
        questions = loadedQuestions;
        startGame();
    })
    .catch(err => {
        console.error(err);
    });

//CONSTANTS
const MAX_QUESTIONS = 40;

startGame = () => {
    questionCounter = 0;
    score = 0;
    availableQuestions = [...questions];
    getNewQuestion();
    game.classList.remove('hidden');
    loader.classList.add('hidden');
};

getNewQuestion = () => {
    if (availableQuestions.length === 0 || questionCounter >= MAX_QUESTIONS) {
        localStorage.setItem('mostRecentScore', score);
        //go to the end page
        return window.location.assign('end.html');
    }
    questionCounter++;
    progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;
    //Update the progress bar
    progressBarFull.style.width = `${(questionCounter / MAX_QUESTIONS) * 100}%`;

    const questionIndex = Math.floor(Math.random() * availableQuestions.length);
    currentQuestion = availableQuestions[questionIndex];
    question.innerHTML = currentQuestion.question;
    topic.innerHTML = currentQuestion.topic;

    choices.forEach((choice) => {
        const number = choice.dataset['number'];

        var choiceText = currentQuestion['choice' + number];
        if (currentQuestion.answer == number && window.debugMode) {
            choiceText += " ✅";
        }

        choice.innerHTML = choiceText;
    });

    availableQuestions.splice(questionIndex, 1);
    acceptingAnswers = true;
};
choices.forEach((choice) => {
    choice.addEventListener('click', (e) => {
        if (!acceptingAnswers) return;
        acceptingAnswers = false;
        const selectedChoice = e.target;
        const selectedAnswer = selectedChoice.dataset['number'];
        const classToApply =
            selectedAnswer == currentQuestion.answer ? 'correct' : 'incorrect';
        document.getElementById("why-text").innerHTML = currentQuestion['text' + selectedAnswer] + "<p><b>the correct answer was: </b></p>" + currentQuestion['choice' + currentQuestion.answer];
        if (classToApply === 'correct') {

            incrementScore();

        }
        selectedChoice.parentElement.classList.add(classToApply);

        setTimeout(() => {
            selectedChoice.parentElement.classList.remove(classToApply);
        }, 1000);

        why.onclick = function () {
            getNewQuestion();
            document.getElementById("why-text").innerHTML = "";
        };



    });
});

incrementScore = () => {
    score += 1;
    const percent = score / MAX_QUESTIONS * 100;
    const roundedPercent = parseFloat(percent.toFixed(1));
    scoreText.innerHTML = score + '/' + MAX_QUESTIONS + ' - ' + roundedPercent + '%';
};
