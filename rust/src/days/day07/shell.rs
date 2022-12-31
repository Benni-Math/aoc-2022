pub struct ShellLine {
  cmd: Option<Cmd>,
  out: Option<Out>,
}

pub enum ShellLineOut {
  ShellCmd(Cmd),
  ShellOut(Out),
}

pub use ShellLineOut::{ ShellCmd, ShellOut};

pub enum Cmd {
  Cd(String),
  Ls,
}

pub enum Out {
  File(String, u32),
  Dir(String),
}

impl ShellLine {
  pub fn new(shell_line: String) -> Self {
      let input = shell_line.split(' ').collect::<Vec<_>>();
      match (input[0], input[1]) {
          ("$", "cd") => ShellLine{ cmd: Some(Cmd::Cd(input[2].to_string())), out: None },
          ("$", "ls") => ShellLine { cmd: Some(Cmd::Ls), out: None },
          ("dir", dir_name) => {
              ShellLine {
                  cmd: None,
                  out: Some(Out::Dir(dir_name.to_string()))
              }
          },
          (size, file_name) if size.parse::<u32>().is_ok() => {
              let file_size = size.parse::<u32>().unwrap();
              ShellLine {
                  cmd: None,
                  out: Some(Out::File(file_name.to_string(), file_size))
              }
          },
          _ => panic!() // TODO: better error handling...
      }
  }

  pub fn get(&self) -> ShellLineOut {
    match (self.cmd, self.out) {
      (Some(cmd), None) => ShellCmd(cmd),
      (None, Some(out)) => ShellOut(out),
      _ => panic!(),
    }
  }
}