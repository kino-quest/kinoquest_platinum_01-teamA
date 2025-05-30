document.addEventListener('DOMContentLoaded', function() {
  const helpBtn = document.querySelector('.understanding-help');
  const popupWrapper = document.getElementById('understanding-popup-wrapper');
  const popupClose = document.getElementById('understanding-popup-close');

  helpBtn.addEventListener('click', function() {
    popupWrapper.style.display = 'block';
  });
  popupClose.addEventListener('click', function() {
    popupWrapper.style.display = 'none';
  });
  popupWrapper.addEventListener('click', function(e) {
    if (e.target === popupWrapper) {
      popupWrapper.style.display = 'none';
    }
  });
});