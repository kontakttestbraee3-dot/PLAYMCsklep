const webhookURL = "https://discord.com/api/webhooks/1487814743744843976/BvnlOCUyVYNqKO7Z1AYig-TdScNWB7LnKppQLUAE9FpTFuMsTjPW1e1OtueNc_1DQZkf";

function wyslijNaDiscord(ranga, cena) {
    const wiadomosc = {
        "username": "System Płatności PlayMC.pl", // Nazwa bota na DC
        "avatar_url": "https://crafatar.com/avatars/xIWOJTEKIx", // Tu możesz dać link do logo serwera
        "embeds": [{
            "title": "⚡ NOWE ZAMÓWIENIE: " + ranga,
            "description": "Gracz właśnie wybrał pakiet w sklepie internetowym.",
            "color": 15844367, // Złoty kolor (Gold)
            "fields": [
                { "name": "Ranga", "value": ranga, "inline": true },
                { "name": "Kwota", "value": cena, "inline": true },
                { "name": "Instrukcja", "value": "Sprawdź panel PayPal i nadaj rangę komendą /lp user nick parent set " + ranga.toLowerCase(), "inline": false }
            ],
            "footer": { "text": "Serwer: PlayMC.pl | Automatyczny System Powiadomień" },
            "timestamp": new Date()
        }]
    };

    fetch(webhookURL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(wiadomosc)
    });
}