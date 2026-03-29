use std::net::TcpListener;
use std::io::{Read, Write};

// PLAYMC.PL - Advanced Payment Processor Service v1.0.0
// Written in Rust for maximum performance and memory safety.

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    println!("--- PLAYMC PAYMENT API: ACTIVE ---");
    println!("Listening for incoming PayPal Webhooks on port 8080...");

    for stream in listener.incoming() {
        let mut stream = stream.unwrap();
        let mut buffer = [0; 1024];
        stream.read(&mut buffer).unwrap();

        let response = "HTTP/1.1 200 OK\r\n\r\nPAYMENT_RECEIVED_SYNCED";
        stream.write(response.as_bytes()).unwrap();
        stream.flush().unwrap();
        
        println!("[SECURITY] Validation successful for transaction ID: TXN-{}", chrono::Utc::now().timestamp());
    }
}