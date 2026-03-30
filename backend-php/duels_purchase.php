<?php
// PLAYMC.PL - Duels Spectator System v1.0
// Handling observer access for 20 minutes

header('Content-Type: application/json');

$price = "4.00";
$currency = "PLN";
$item_name = "Obserwator Duels (20 min)";

// Symulacja odbierania danych z frontendu
$player_nick = $_POST['nick'] ?? 'Nieznany';
$transaction_status = "PENDING";

// Logika nadawania uprawnień (Symulacja komendy w konsoli serwera)
function grantSpectator($nick) {
    // W prawdziwym systemie tutaj byłoby połączenie przez RCON
    // np. "lp user $nick parent addtemp observer 20m"
    return true;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $success = grantSpectator($player_nick);
    
    if ($success) {
        echo json_encode([
            "status" => "success",
            "item" => $item_name,
            "player" => $player_nick,
            "duration" => "20m",
            "message" => "Przekierowywanie do płatności PayPal..."
        ]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Błędne zapytanie"]);
}
?>