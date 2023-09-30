---
toc: false
comments: true
layout: post
title: Basics Test
description: JS Test Application
courses: {compsci: {week: 3} }
type: hacks
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---

{% include nav_basics.html %}


```python
%%html
<!-- Create HTML elements to display quiz content -->
<div class="question" id="question">Loading question...</div>
<div class="options" id="options"></div>
<div id="result"></div>
<div class="buttons" id="buttons"></div>

<script>
    // Define the quiz questions and answers with multiple-choice options
    const quizData = [
        {
            question: "What is a class Anusha is taking this year?",
            options: ["English", "US History", "CSP"],
            correctAnswer: "CSP"
        },
        {
            question: "What grade is Anusha in right now?",
            options: ["10", "9", "11"],
            correctAnswer: "10"
        },
        {
            question: "What is Anusha's favorite place to visit?",
            options: ["lake", "beach", "mountains"],
            correctAnswer: "beach"
        },
        {
            question: "What is Anusha's favorite food?",
            options: ["ice cream", "cookies", "pasta"],
            correctAnswer: "ice cream"
        },
        {
            question: "Is Anusha good at drawing on Freeform?",
            options: ["No", "Yes", "Maybe"],
            correctAnswer: "No"
        }
    ];

    let currentQuestionIndex = 0;

    // Get references to HTML elements
    const questionElement = document.getElementById("question");
    const optionsElement = document.getElementById("options");
    const resultElement = document.getElementById("result");
    const buttonsElement = document.getElementById("buttons");

    // Function to display the current question
    function displayQuestion() {
        if (currentQuestionIndex < quizData.length) {
            const currentQuestion = quizData[currentQuestionIndex];
            
            // Display the question text
            questionElement.textContent = currentQuestion.question;

            // Create buttons for multiple-choice options
            optionsElement.innerHTML = "";
            currentQuestion.options.forEach(option => {
                const button = document.createElement("button");
                button.textContent = option;
                
                // Add an event listener to check the answer when the button is clicked
                button.addEventListener("click", () => checkAnswer(option));
                
                optionsElement.appendChild(button);
            });

            // Create "Next" or "Finish" button based on quiz progress
            buttonsElement.innerHTML = "";
            if (currentQuestionIndex < quizData.length - 1) {
                const nextButton = document.createElement("button");
                nextButton.textContent = "Next";
                
                // Add an event listener to move to the next question when the button is clicked
                nextButton.addEventListener("click", () => nextQuestion());
                
                buttonsElement.appendChild(nextButton);
            } else {
                const finishButton = document.createElement("button");
                finishButton.textContent = "Finish";
                
                // Add an event listener to finish the quiz when the button is clicked
                finishButton.addEventListener("click", () => finishQuiz());
                
                buttonsElement.appendChild(finishButton);
            }
        } else {
            // Quiz is finished
            questionElement.textContent = "Quiz finished!";
            optionsElement.innerHTML = "";
            buttonsElement.innerHTML = "";
        }
    }

    // Function to check the user's answer
    function checkAnswer(userAnswer) {
        const currentQuestion = quizData[currentQuestionIndex];
        if (userAnswer == currentQuestion.correctAnswer) {
            resultElement.textContent = "Correct!";
        } else {
            resultElement.textContent = "Incorrect!";
        }
    }

    // Function to move to the next question
    function nextQuestion() {
        currentQuestionIndex++;
        resultElement.textContent = "";
        displayQuestion();
    }

    // Function to finish the quiz
    function finishQuiz() {
        currentQuestionIndex = quizData.length;
        resultElement.textContent = "Quiz finished!";
        displayQuestion();
    }

    // Start the quiz by displaying the first question
    displayQuestion();
</script>

```


<!-- Create HTML elements to display quiz content -->
<div class="question" id="question">Loading question...</div>
<div class="options" id="options"></div>
<div id="result"></div>
<div class="buttons" id="buttons"></div>

<script>
    // Define the quiz questions and answers with multiple-choice options
    const quizData = [
        {
            question: "What is a class Anusha is taking this year?",
            options: ["English", "US History", "CSP"],
            correctAnswer: "CSP"
        },
        {
            question: "What grade is Anusha in right now?",
            options: ["10", "9", "11"],
            correctAnswer: "10"
        },
        {
            question: "What is Anusha's favorite place to visit?",
            options: ["lake", "beach", "mountains"],
            correctAnswer: "beach"
        },
        {
            question: "What is Anusha's favorite food?",
            options: ["ice cream", "cookies", "pasta"],
            correctAnswer: "ice cream"
        },
        {
            question: "Is Anusha good at drawing on Freeform?",
            options: ["No", "Yes", "Maybe"],
            correctAnswer: "No"
        }
    ];

    let currentQuestionIndex = 0;

    // Get references to HTML elements
    const questionElement = document.getElementById("question");
    const optionsElement = document.getElementById("options");
    const resultElement = document.getElementById("result");
    const buttonsElement = document.getElementById("buttons");

    // Function to display the current question
    function displayQuestion() {
        if (currentQuestionIndex < quizData.length) {
            const currentQuestion = quizData[currentQuestionIndex];

            // Display the question text
            questionElement.textContent = currentQuestion.question;

            // Create buttons for multiple-choice options
            optionsElement.innerHTML = "";
            currentQuestion.options.forEach(option => {
                const button = document.createElement("button");
                button.textContent = option;

                // Add an event listener to check the answer when the button is clicked
                button.addEventListener("click", () => checkAnswer(option));

                optionsElement.appendChild(button);
            });

            // Create "Next" or "Finish" button based on quiz progress
            buttonsElement.innerHTML = "";
            if (currentQuestionIndex < quizData.length - 1) {
                const nextButton = document.createElement("button");
                nextButton.textContent = "Next";

                // Add an event listener to move to the next question when the button is clicked
                nextButton.addEventListener("click", () => nextQuestion());

                buttonsElement.appendChild(nextButton);
            } else {
                const finishButton = document.createElement("button");
                finishButton.textContent = "Finish";

                // Add an event listener to finish the quiz when the button is clicked
                finishButton.addEventListener("click", () => finishQuiz());

                buttonsElement.appendChild(finishButton);
            }
        } else {
            // Quiz is finished
            questionElement.textContent = "Quiz finished!";
            optionsElement.innerHTML = "";
            buttonsElement.innerHTML = "";
        }
    }

    // Function to check the user's answer
    function checkAnswer(userAnswer) {
        const currentQuestion = quizData[currentQuestionIndex];
        if (userAnswer == currentQuestion.correctAnswer) {
            resultElement.textContent = "Correct!";
        } else {
            resultElement.textContent = "Incorrect!";
        }
    }

    // Function to move to the next question
    function nextQuestion() {
        currentQuestionIndex++;
        resultElement.textContent = "";
        displayQuestion();
    }

    // Function to finish the quiz
    function finishQuiz() {
        currentQuestionIndex = quizData.length;
        resultElement.textContent = "Quiz finished!";
        displayQuestion();
    }

    // Start the quiz by displaying the first question
    displayQuestion();
</script>


