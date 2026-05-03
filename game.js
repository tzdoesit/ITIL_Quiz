
let questions = [], current = 0, score = 0;
//console.log

fetch("questions.json")
    .then(r => r.json()) // retrieve data from json and make it into javascript readable data structure (array)
    .then(data => { questions = shuffle(data); showQuestion(); });

// //test
// console.log(questions[0]);


// Create a function that shuffles the Questions and their order so the quiz doesn't feel stale.
// Using Fisher-Yates algorithm for shuffling.
function shuffle(array) {
    //console.log(array)
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1)); // this takes a math.random 0~1 floating point, then multiply by i+1 and then round down using the math.floor function so it's a clean integer.
        [array[i], array[j]] = [array[j], array[i]]; // move indexes (shuffling) by moving top index - 1 with the randomized index among the array.
        console.log(array);
    }
    return array;
}


//testing/practicing shuffle
testArray = ["T","O","M","M","Y"];
shuffle(testArray);
//console.log(testArray);


function showQuestion() {
    //console.log(questions, current)
    //console.log(questions);
    //console.log(data);
    const q = questions[current];
    document.getElementById("question-text").textContent = q.question;
    document.getElementById("topic-label").textContent = q.topic;
    document.getElementById("score-label").textContent =
        `${score}/${current} - ${current ? Math.round(score/current*100) : 0}`;

    // Multiple Choice Options
    const opts = document.getElementById("options");
    opts.innerHTML = "";
    q.options.forEach((opt, i) => {
        const btn = document.createElement("button");
        btn.className = "option";
        btn.textContent = ["A","B","C","D"][i] + ". " + opt;
        btn.onclick = () => selectAnswer(i);
        opts.appendChild(btn);
    });
    document.getElementById("next-btn").style.display = "none"
}

function selectAnswer(chosen) {
    const q = questions[current];
    const btns = document.querySelectorAll(".option");
    btns.forEach((btn,i) => {
        btn.disabled = true;
        if (i === q.answer) btn.classList.add("correct");
        else if (i === chosen) btn.classList.add("wrong");
    });
    if (chosen === q.answer) score++;
    document.getElementById("next-btn").style.display = "block";
}

document.getElementById("next-btn").onclick = () => {
    current++;
    if (current < questions.length) showQuestion();
    else {
        document.getElementById("app").innerHTML = 
        `<h1>Done! You scored ${score}/${questions.length}
        (${Math.round(score/questions.length*100)}%)</h1>`;
        
    }
};

