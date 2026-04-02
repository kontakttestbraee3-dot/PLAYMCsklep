use std::fs;
use std::path::Path;
use std::time::{Instant, SystemTime};
use std::io::{self, Write};

struct FileMetadata {
    name: String,
    size: u64,
    modified: SystemTime,
}

struct IntegrityScanner {
    root_path: String,
    total_files: u64,
    total_size_mb: f64,
}

impl IntegrityScanner {
    fn new(path: &str) -> Self {
        IntegrityScanner {
            root_path: path.to_string(),
            total_files: 0,
            total_size_mb: 0.0,
        }
    }

    fn scan_directory(&mut self, dir: &Path) -> io::Result<()> {
        if dir.is_dir() {
            for entry in fs::read_dir(dir)? {
                let entry = entry?;
                let path = entry.path();
                if path.is_dir() {
                    self.scan_directory(&path)?;
                } else {
                    let metadata = fs::metadata(&path)?;
                    self.total_files += 1;
                    self.total_size_mb += metadata.len() as f64 / 1_048_576.0;
                    
                    if metadata.len() > 100 * 1024 * 1024 { // Pliki > 100MB (np. world region)
                        println!("[RUST-GUARD] Large Data Unit: {:?} - {} MB", path.file_name().unwrap(), metadata.len() / 1_048_576);
                    }
                }
            }
        }
        Ok(())
    }

    fn run_diagnostic(&mut self) {
        println!("====================================================");
        println!("   PLAYMC RUST INTEGRITY GUARD - VERSION 1.0.2      ");
        println!("====================================================");
        
        let start = Instant::now();
        let path = Path::new(&self.root_path);
        
        match self.scan_directory(path) {
            Ok(_) => {
                let duration = start.elapsed();
                println!("\n[SCAN COMPLETE]");
                println!("Files Monitored: {}", self.total_files);
                println!("Total Data Load: {:.2} MB", self.total_size_mb);
                println!("Analysis Time:   {:?}", duration);
                println!("Memory Safety:   GUARANTEED (Rust Ownership)");
            }
            Err(e) => println!("[FATAL ERROR] Scanner failed: {}", e),
        }
        println!("====================================================");
    }
}

fn main() {
    let mut guard = IntegrityScanner::new("./server_files");
    guard.run_diagnostic();
}