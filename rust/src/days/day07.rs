use std::collections::{ HashMap, hash_map::Entry };
use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

struct FileSystem {
    curr_dir: String,
    directories: HashMap<String, u32>,
}

impl FileSystem {
    pub fn new() -> Self {
        let curr_dir = String::from("/");
        let mut directories = HashMap::new();
        directories.insert("/".to_string(), 0);

        FileSystem {
            curr_dir,
            directories,
        }
    }

    fn sum_small_dirs(self) -> u32 {
        self.directories
            .into_values()
            .fold(0, |sum, size| {
                if size <= 100_000 {
                    sum + size
                } else {
                    sum
                }
            })
    }

    fn min_dir_to_remove(self) -> u32 {
        let space_taken = self.directories.get("/").unwrap();
        let to_remove = space_taken - 40_000_000;
        self.directories
            .into_values()
            .fold(70_000_000, |min, size| {
                if size >= to_remove && size < min {
                    size
                } else {
                    min
                }
            })
    }

    pub fn parse_line(self, line: &str) -> Self {
        match line.split(' ').collect::<Vec<_>>()[..] {
           ["$", "cd", dir_name] => self.change_dir(dir_name),
           ["$", "ls"] => self,
           ["dir", dir_name] => self.add_dir(dir_name),
           [file_size, _file_name] => self.add_file(file_size.parse().unwrap()),
           _ => panic!("This should not occur!"),
        }
    }

    fn change_dir(self, dir_name: &str)-> Self {
        match dir_name {
            ".." => {
                if self.curr_dir == "/" { return self; }
                let mut prev_dir = self.curr_dir;
                prev_dir.pop();

                if let Some(index_of_last) = prev_dir.rfind('/') {
                    let (curr_dir, _last_dir) = prev_dir.split_at(index_of_last + 1);
                    FileSystem {
                        curr_dir: curr_dir.to_string(),
                        directories: self.directories,
                    }
                } else {
                    panic!("Oh no! self.curr_dir was too short: {}", prev_dir);
                }
                
            },
            "/" => FileSystem {
                curr_dir: "/".to_string(),
                directories: self.directories,
            },
            new_dir => {
                FileSystem {
                    curr_dir: self.curr_dir + new_dir + "/",
                    directories: self.directories,
                }
            }
        }
    }

    fn add_dir(mut self, dir_name: &str) -> Self {
        let past_dir = self.curr_dir.clone();
        let new_dir = past_dir +  dir_name + "/";

        if let Entry::Vacant(e) = self.directories.entry(new_dir) {
            e.insert(0);
            self
        } else {
            self
        }
    }

    fn add_file(mut self, file_size: u32) -> Self {
        // TODO: done very manually...
        let len = self.curr_dir.len();
        let mut i = 0;
        while i < len {
            while let Some(c) = self.curr_dir.chars().nth(i) {
                if c == '/' {
                    break;
                }
                i += 1;
            }

            let dir = &self.curr_dir[..=i];
            if let Entry::Occupied(mut e) = self.directories.entry(dir.to_string()) {
                let curr_size = e.get();
                e.insert(curr_size + file_size);
            }

            i += 1;
        }
        
        self
    }
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(FileSystem::new(), |fs, line| fs.parse_line(&line))
        .sum_small_dirs();

    Ok(format!("{}", answer))
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(FileSystem::new(), |fs, line| fs.parse_line(&line))
        .min_dir_to_remove();

    Ok(format!("{}", answer))
}