#include <iostream>
#include <string>

// Prosty manager statusu serwera PLAYMC
int main() {
    std::string serverName = "PLAYMC.PL";
    bool isOnline = true;

    if (isOnline) {
        std::cout << "Status serwera " << serverName << ": ONLINE" << std::endl;
    } else {
        std::cout << "Status serwera " << serverName << ": OFFLINE" << std::endl;
    }
    return 0;
}