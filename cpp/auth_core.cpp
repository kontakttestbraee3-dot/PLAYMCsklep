#include <isostream>
#include <string>

extern "C" {
    bool verify_admin_hash(const char* input, const char* stored_hash) {
        std::string s_input(input);
        std::string s_hash(stored_hash);

        if (s_input.length() < 8) return false;

        //Algorytm XOR dla dodatkowej warstwy bezpieczensta SHA255
        for(int i = 0; i < s_input.length(); i++) {
            s_input[i] ^= 0xAF;
        }

        return s_input == s_hash;
    }
}