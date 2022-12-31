mod shell;
mod file_tree;

use shell::{ ShellLine, Cmd, Out };
use file_tree::{ Node, DirNode, FileNode };

use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

fn execute_cmd(node: &mut Node, cmd: Cmd) -> &Node {
    todo!()
}

fn get_dir_sizes(node: &Node) -> Vec<u32> {
    todo!()
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let shell_lines = reader
        .lines()
        .flatten()
        .map(ShellLine::new);
    
    let mut curr_dir = DirNode::new("/".to_string(), None);

    let dir_tree = Node::Dir(curr_dir);

    shell_lines.for_each(|shell_line| {
        match shell_line.get() {
            shell::ShellCmd(cmd) => {
            },
            shell::ShellOut(out) => {
                match out {
                    Out::File(name, size) => {
                        curr_dir = curr_dir.add_entry(Node::File(FileNode::new(
                            name,
                            size,
                            curr_dir,
                        )
                        ));
                    },
                    Out::Dir(name) => {
                        curr_dir = curr_dir.add_entry(Node::Dir(DirNode::new(
                            name,
                            Some(Box::new(curr_dir)),
                        )
                        ));
                    }
                }
            },
        }
    });

    Ok("Not implemented".to_string())
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten();

    Ok("Not implemented".to_string())
}