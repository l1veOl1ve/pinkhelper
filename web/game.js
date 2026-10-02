const tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

tg.setHeaderColor('#ffd1dc');
tg.setBackgroundColor('#ffd1dc');

function openTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    
    document.getElementById(`tab-${tabName}`).classList.remove('hidden');
}

// Отправка данных назад в бота через sendData
function saveCharacter() {
    const input = document.getElementById('new-char-input').value;
    if (!input) return;
    
    tg.sendData(JSON.stringify({
        action: 'add_character',
        text: input
    }));
}

function savePlot() {
    const text = document.getElementById('plot-text').value;
    if (!text) return;

    tg.sendData(JSON.stringify({
        action: 'update_plot',
        text: text
    }));
}

function sendToAI() {
    const prompt = document.getElementById('ai-prompt').value;
    if (!prompt) return;

    tg.sendData(JSON.stringify({
        action: 'ask_ai',
        text: prompt
    }));
}