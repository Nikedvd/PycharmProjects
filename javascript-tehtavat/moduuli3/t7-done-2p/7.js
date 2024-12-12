document.addEventListener('DOMContentLoaded', () => {
    const targetImage = document.getElementById('target');
    const triggerText = document.getElementById('trigger');

    triggerText.addEventListener('mouseover', () => {
        targetImage.src = 'img/picB.jpg';
    });

    triggerText.addEventListener('mouseout', () => {
        targetImage.src = 'img/picA.jpg';
    });
});