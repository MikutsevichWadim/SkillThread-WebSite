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
