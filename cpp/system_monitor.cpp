extern "C" {
    float get_memory_load(long long used, long long total) {
        if (total == 0) return 0.0f;
        return ((float)used / (float)total) * 100.0f;
    }

    const char* get_cpu_architecture() {
        return "X64_EXTENDED_PLAYMC_BLADE";
    }
}