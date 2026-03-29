const webhookURL = "https://discord.com/api/webhooks/1487814743744843976/BvnlOCUyVYNqKO7Z1AYig-TdScNWB7LnKppQLUAE9FpTFuMsTjPW1e1OtueNc_1DQZkf";

function wyslijNaDiscord(ranga, cena) {
    const wiadomosc = {
        "username": "Sklep PLAYMC",
        "avatar_url": "https://crafatar.com/avatars/xIWOJTEKIx",
        "embeds": [{
            "title": "💰 NOWE KLIKNIĘCIE W SKLEPIE!",
            "description": `Ktoś właśnie wybrał rangę **${ranga}** za **${cena}**!`,
            "color": 3066993,
            "fields": [
                { "name": "Status", "value": "Oczekiwanie na wpłatę PayPal", "inline": true },
                { "name": "Serwer", "value": "PLAYMC.PL", "inline": true }
            ],
            "footer": { "text": "Sprawdź saldo na PayPal!" },
            "timestamp": new Date()
        }]
    };

    fetch(webhookURL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(wiadomosc)
    }).then(() => console.log("Powiadomienie wysłane!"));
}

document.addEventListener('DOMContentLoaded', () => {
    const przyciski = document.querySelectorAll('.buy-btn');
    przyciski.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const ranga = e.target.closest('.card').querySelector('h3').innerText;
            const cena = e.target.closest('.card').querySelector('.price').innerText;
            wyslijNaDiscord(ranga, cena);
            if (window.confetti) {
                confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
            }
            alert("Przenoszę do PayPal. PAMIĘTAJ: W tytule przelewu wpisz swój NICK Z GRY!");
        });
    });
});