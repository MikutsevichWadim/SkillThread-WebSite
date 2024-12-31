function previewImage(input) {
    const preview = document.getElementById('preview');

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        // Когда файл загружен
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        preview.style.display = 'none';
    }
}

// Привязка события изменения к полю файла
document.getElementByClass('channel-image').addEventListener('change', function () {
    previewImage(this);
});
