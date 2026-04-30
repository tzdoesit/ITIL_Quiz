
let questions = [], current = 0, score = 0;

// test
console.log("hi")

fetch("questions.json")
    .then(r => r.json())
    .then(data => { questions = data; showQuestion(); });


function showQuestion() {
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

