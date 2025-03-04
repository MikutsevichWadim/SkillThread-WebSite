window.onload = function() {
    var messageBox = document.querySelector('.message-box');
    if (messageBox) {
        setTimeout(function() {
            messageBox.classList.remove('show');
            messageBox.classList.add('fade');
        }, 5000);
    }
}




document.querySelectorAll('textarea').forEach(textarea => {
    textarea.style.overflow = 'hidden'; // Скрываем скролл
    textarea.addEventListener('input', function () {
        this.style.height = 'auto'; // Сбрасываем высоту
        this.style.height = this.scrollHeight + 'px'; // Устанавливаем высоту по содержимому
    });

    // Устанавливаем начальную высоту при загрузке страницы
    textarea.style.height = textarea.scrollHeight + 'px';
});



// Get the button:
let rollBackToTopButton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        rollBackToTopButton.style.display = "block";
    } else {
        rollBackToTopButton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
