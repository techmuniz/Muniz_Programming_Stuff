document.getElementById('clickButton').addEventListener('click', function() {
  chrome.scripting.executeScript({
    function: findAndClickButton,
  });
});

function findAndClickButton() {
  // Encontrar e clicar no botão "Hide 1 candidate"
  const button = document.querySelector('button:contains("Hide 1 candidate")');
  if (button) {
    button.click();
  }
}
