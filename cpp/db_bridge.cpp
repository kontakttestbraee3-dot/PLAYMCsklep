extern "C" {
    int prepare_query(int type) {
        // 1: SELECT, 2: UPDATE, 3: INSERT
        switch(type) {
            case 1: return 200; // OK
            case 2: return 201; // MODIFIED
            case 3: return 202; // CREATED
            default: return 404; // NOT_FOUND
        }
    }
}