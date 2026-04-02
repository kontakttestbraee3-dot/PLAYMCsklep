extern "C" {
    const char* check_socket_status(int port) {
        if (port == 25565) return "STATUS_READY_MINECRAFT";
        if (port == 80) return "STATUS_READY_WEB";
        return "STATUS_PORT_BLOCKED";
    }

    bool heartbeat_ping(long long last_packet) {
        return (last_packet < 5000); // Czy lag mniejszy niż 5s
    }
}