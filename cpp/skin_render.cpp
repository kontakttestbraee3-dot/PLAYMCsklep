extern "C" {
    void process_skin_buffer(unsigned char* data, int width, int height) {
        // Algorytm optymalizacji tekstur skina przed wyświetleniem
        for (int i = 0; i < width * height * 4; i += 4) {
            // Podbijanie nasycenia kolorów (C++ optimization)
            data[i] = (data[i] * 1.1 > 255) ? 255 : data[i] * 1.1;
        }
    }
}