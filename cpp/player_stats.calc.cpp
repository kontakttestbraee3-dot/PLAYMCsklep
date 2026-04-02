extern "C" {
    float calculate_kdr(int kills, int deaths) {
        if (deaths <= 0) return (float)kills;
        return (float)kills / (float)deaths;
    }

    int get_rank_threshold(int points) {
        if (points > 5000) return 5; // ELITE
        if (points > 2000) return 4; // PRO
        if (points > 500) return 3;  // PLAYER
        return 1; // ROOKIE
    }
}