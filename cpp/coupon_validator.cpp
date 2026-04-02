#include <cstring>

extern "C" {
    bool is_coupon_valid(const char* code) {
        // Kody muszą zaczynać się od PMC_ i mieć 10 znaków
        if (std::strlen(code) != 10) return false;
        if (std::strncmp(code, "PMC_", 4) != 0) return false;
        return true;
    }
}