document.getElementById('draw-roles-btn').addEventListener('click', drawRoles);
document.querySelectorAll('.guess-btn').forEach(btn => {
    btn.addEventListener('click', makeGuess);
});

let roles = ['Raja', 'Mantri', 'Chor', 'Sipahi'];
let playerRoles = [];

function drawRoles() {
    playerRoles = roles.sort(() => Math.random() - 0.5);
    document.getElementById('role1').textContent = playerRoles[0];
    document.getElementById('role2').textContent = playerRoles[1];
    document.getElementById('role3').textContent = playerRoles[2];
    document.getElementById('role4').textContent = playerRoles[3];
    
    document.getElementById('guess-section').classList.remove('hidden');
}

function makeGuess(event) {
    const guess = event.target.getAttribute('data-guess');
    const guessIndex = parseInt(guess.replace('player', '')) - 1;
    const mantriIndex = playerRoles.indexOf('Mantri');
    const chorIndex = playerRoles.indexOf('Chor');
    const sipahiIndex = playerRoles.indexOf('Sipahi');
    
    let resultText = '';
    
    if (guessIndex === chorIndex) {
        resultText = `Correct! Sipahi gets 500 points.`;
    } else {
        resultText = `Wrong! Chor gets Sipahi's points.`;
    }
    
    const points = {
        Raja: 1000,
        Mantri: 800,
        Sipahi: guessIndex === chorIndex ? 500 : 0,
        Chor: guessIndex === chorIndex ? 0 : 500
    };
    
    resultText += `<br>Points:<br>Raja: ${points.Raja}<br>Mantri: ${points.Mantri}<br>Sipahi: ${points.Sipahi}<br>Chor: ${points.Chor}`;
    
    document.getElementById('result').innerHTML = resultText;
    document.getElementById('result').classList.remove('hidden');
}

