#include <iostream>
#include <string>
#include <vector>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <memory>
#include <chrono>
#include <iomanip>

#pragma comment(lib, "ws2_32.lib")

#define RCON_PID 0x1337
#define MAX_PACKET_SIZE 4096

enum PacketType {
    AUTH = 3,
    COMMAND = 2,
    RESPONSE = 0
};

struct RconPacket {
    int length;
    int id;
    int type;
    char payload[MAX_PACKET_SIZE];
};

class PlayMCNetworkCore {
private:
    SOCKET master_socket;
    sockaddr_in server_addr;
    std::string admin_password;
    bool is_authenticated;

    void Log(std::string msg, std::string level = "INFO") {
        auto now = std::chrono::system_clock::now();
        auto in_time_t = std::chrono::system_clock::to_time_t(now);
        std::cout << "[" << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d %X") << "] "
                  << "[" << level << "] " << msg << std::endl;
    }

public:
    PlayMCNetworkCore(std::string ip, int port, std::string password) 
        : admin_password(password), is_authenticated(false) {
        
        WSADATA wsaData;
        if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
            throw std::runtime_error("WSAStartup failed");
        }

        master_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        server_addr.sin_family = AF_INET;
        server_addr.sin_port = htons(port);
        inet_pton(AF_INET, ip.c_str(), &server_addr.sin_addr);
    }

    ~PlayMCNetworkCore() {
        closesocket(master_socket);
        WSACleanup();
    }

    bool ConnectAndAuth() {
        Log("Attempting connection to Windows Host...");
        if (connect(master_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
            Log("Connection REFUSED. Is MC Server running?", "FATAL");
            return false;
        }

        // Budowanie pakietu AUTH
        int payload_len = admin_password.length();
        int total_len = payload_len + 10; // ID + Type + Padding

        std::vector<char> buffer(total_len + 4);
        memcpy(&buffer[0], &total_len, 4);
        int id = RCON_PID;
        memcpy(&buffer[4], &id, 4);
        int type = AUTH;
        memcpy(&buffer[8], &type, 4);
        memcpy(&buffer[12], admin_password.c_str(), payload_len);
        buffer[total_len + 2] = 0;
        buffer[total_len + 3] = 0;

        send(master_socket, buffer.data(), buffer.size(), 0);

        char recv_buf[MAX_PACKET_SIZE];
        recv(master_socket, recv_buf, MAX_PACKET_SIZE, 0);
        
        int response_id;
        memcpy(&response_id, &recv_buf[4], 4);

        if (response_id == -1) {
            Log("Authentication FAILED. Check server.properties password!", "ERROR");
            return false;
        }

        is_authenticated = true;
        Log("Secure Tunnel established via C++ Kernel.");
        return true;
    }

    std::string SendCommand(std::string cmd) {
        if (!is_authenticated) return "NOT_AUTH";

        Log("Injecting command: " + cmd);
        
        // Specjalny prefix [SKLEP]
        std::string final_cmd = "say §d§l[SKLEP] §f" + cmd;
        
        int payload_len = final_cmd.length();
        int total_len = payload_len + 10;
        std::vector<char> buffer(total_len + 4);
        
        memcpy(&buffer[0], &total_len, 4);
        int id = RCON_PID;
        memcpy(&buffer[4], &id, 4);
        int type = COMMAND;
        memcpy(&buffer[8], &type, 4);
        memcpy(&buffer[12], final_cmd.c_str(), payload_len);

        send(master_socket, buffer.data(), buffer.size(), 0);

        char recv_buf[MAX_PACKET_SIZE];
        int bytes = recv(master_socket, recv_buf, MAX_PACKET_SIZE, 0);
        
        if (bytes > 12) {
            return std::string(&recv_buf[12], bytes - 14);
        }
        return "SUCCESS (No Output)";
    }
};

int main(int argc, char* argv[]) {
    std::cout << "--- PLAYMC C++ SYSTEM KERNEL v5.0 ---" << std::endl;
    
    try {
        PlayMCNetworkCore core("127.0.0.1", 25575, "TwojeHaslo123");
        
        if (core.ConnectAndAuth()) {
            std::string msg = (argc > 1) ? argv[1] : "Wiadomosc testowa z silnika C++";
            std::string result = core.SendCommand(msg);
            std::cout << "[SYSTEM RESULT] " << result << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "CRITICAL EXCEPTION: " << e.what() << std::endl;
    }

    return 0;
}