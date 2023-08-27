document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('clickButton');
    const targetButton = document.querySelector('.save-to-pipeline__button'); // Seleciona o botão com a classe específica
  
    button.addEventListener('click', function() {
      if (targetButton) {
        targetButton.click(); // Simula o clique no botão
      }
    });
  });
  