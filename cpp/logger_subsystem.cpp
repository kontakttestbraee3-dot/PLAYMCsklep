#include <sstream>

extern "C" {
    const char* format_log_entry(const char* level, const char* message) {
        static std::string buffer;
        buffer = "[";
        buffer += level;
        buffer += "] SYSTEM_MSG: ";
        buffer += message;
        return buffer.c_str();
    }
}