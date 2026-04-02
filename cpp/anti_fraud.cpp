#include <string>

extern "C" {
    int analyze_transaction(double amount, const char* country_code, int failed_attempts) {
        // Zwraca poziom ryzyka 0-100
        int risk = 0;
        if (amount > 500.0) risk += 40;
        if (failed_attempts > 3) risk += 50;
        
        std::string cc(country_code);
        if (cc != "PL") risk += 15;
        
        return (risk > 100) ? 100 : risk;
    }
}