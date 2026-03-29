// Dane Twoich usług
const serviceID = "service_q1kynjt";
const templateID = "template_r619zzc";
const webhookURL = "https://discord.com/api/webhooks/1487814743744843976/BvnlOCUyVYNqKO7Z1AYig-TdScNWB7LnKppQLUAE9FpTFuMsTjPW1e1OtueNc_1DQZkf";

function wyslijPowiadomienia(ranga, cena) {
    // 1. WYSYŁKA NA MAIL (Na Twój telefon)
    const params = {
        ranga: ranga,
        cena: cena,
        data: new Date().toLocaleString()
    };

    emailjs.send(serviceID, templateID, params)
        .then(() => console.log("📧 Mail wysłany pomyślnie!"))
        .catch((err) => console.log("❌ Błąd maila: ", err));

    // 2. WYSYŁKA NA DISCORDA
    const dcMsg = {
        "username": "Sklep PlayMC.pl",
        "embeds": [{
            "title": "💰 NOWY KLIK W SKLEPIE!",
            "description": `Gracz wybrał: **${ranga}** za **${cena}**`,
            "color": 15844367,
            "footer": { "text": "Sprawdź PayPal i Gmail!" }
        }]
    };

    fetch(webhookURL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dcMsg)
    });

    // 3. KONFETTI
    if (window.confetti) {
        confetti({
            particleCount: 150,
            spread: 70,
            origin: { y: 0.6 }
        });
    }
}

// Podpięcie pod przyciski
document.addEventListener('DOMContentLoaded', () => {
    const przyciski = document.querySelectorAll('.buy-btn');
    
    przyciski.forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Pobieramy dane z karty
            const card = e.target.closest('.card');
            const ranga = card.querySelector('h3').innerText;
            const cena = card.querySelector('.price').innerText;

            wyslijPowiadomienia(ranga, cena);
            
            alert("Przenoszę do PayPal... Pamiętaj o wpisaniu NICKU w tytule!");
        });
    });
});