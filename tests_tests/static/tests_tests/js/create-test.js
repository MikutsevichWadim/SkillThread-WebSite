document.addEventListener('DOMContentLoaded', function () {
    const questionsContainer = document.getElementById('questionsContainer');
    const addQuestionBtn = document.getElementById('addQuestion');
    const templates = document.getElementById('templates');
    let questionCounter = 0;
    let answerCounter = 0;

    addQuestionBtn.addEventListener('click', function () {
        questionCounter++;
        const questionTemplate = templates.querySelector('.question-template').cloneNode(true);
        questionTemplate.setAttribute('data-question-id', `question-${questionCounter}`);
        questionTemplate.querySelector('.question-text').setAttribute('name', `questions[question-${questionCounter}][text]`);

        // Обработчики для нового вопроса
        attachQuestionHandlers(questionTemplate);

        questionsContainer.appendChild(questionTemplate);
    });

    function attachQuestionHandlers(questionElement) {
        const addOptionBtn = questionElement.querySelector('.addOption');
        const removeQuestionBtn = questionElement.querySelector('.removeQuestion');
        const answerOptionsContainer = questionElement.querySelector('.answer-options');

        // Добавление вариантов ответа
        addOptionBtn.addEventListener('click', function () {
            answerCounter++;
            const answerTemplate = templates.querySelector('.answer-template').cloneNode(true);
            const questionId = questionElement.getAttribute('data-question-id');
            answerTemplate.querySelector('.answer-text').setAttribute('name', `questions[${questionId}][answers][answer-${answerCounter}][text]`);

            const correctOption = answerTemplate.querySelector('.correct-option');
            correctOption.setAttribute('name', `questions[${questionId}][correctAnswer]`);
            correctOption.setAttribute('value', `answer-${answerCounter}`);

            attachOptionHandlers(answerTemplate);
            answerOptionsContainer.appendChild(answerTemplate);
        });

        // Удаление вопроса
        removeQuestionBtn.addEventListener('click', function () {
            questionElement.remove();
        });
    }

    function attachOptionHandlers(optionElement) {
        const removeOptionBtn = optionElement.querySelector('.removeOption');
        removeOptionBtn.addEventListener('click', function () {
            optionElement.remove();
        });
    }
});
