# Advent of Code 2022

**Warning**: Only done with the first 7 days so far.

I'll be trying to solve some of the AOC 2022 problems.

To run, get you're AoC 2022 inputs and place them in a directory name `inputs/` in the root of this project. The inputs must be named '01.txt', '02.txt', and so on until '25.txt'. Then, just run `poetry run aoc-2022` in the command line and the outputs for each programming language will be created in the `outputs/` directory.

To run a specific languages, use `poetry run aoc-only <language_name>`.

Compilation and cleaning scripts are also implemented! Try `poetry run compile-all` or `poetry run clean-all` to run on all directories, and `poetry run compile-only <language_name>` or `poetry run clean-only <language_name>`

To speed up Elixir, set MIX_ENV via `export MIX_ENV="prod"`.

## Up Next

 - Incorporate C solutions
 - Upgrade `scripts` (split into modules and add individual run scripts)

## Requirements

To run everything, you'll need the following:

 - Poetry & Python 3.11 (or higher)
    - 3.10 needed for `match-case` statements
    - Python can be installed via your package manager or [online](https://www.python.org/downloads/).
    - Install [Poetry](https://python-poetry.org/docs/) with `curl -sSL https://install.python-poetry.org | python3 -`
 - Typescript 4.9.4^ & Node v16 (ES2022)
    - ES2022 support needed for `String.prototype.replaceAll()`
    - Install NodeJS and NPM - recommended method is via [nvm](https://github.com/nvm-sh/nvm).
    - Then, you can go to the `typescript` director and run `npm i` (to install Typescript globally, run `npm i -g typescript`).
 - Cargo & Rust 1.66
    - Install both of these via [rustup](https://www.rust-lang.org/learn/get-started), i.e. run `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
 - Elixir/Mix 1.14.2 & Erlang/OTP 25 
    - [Guide on the Elixir website](https://elixir-lang.org/install.html)
 - C and Make
    - In most cases, your computer should already have a C compiler and Make installed.
    - If not, then install [GCC](https://www.gnu.org/software/gcc/) with your package manager or from the site.
    - On Mac, you can also run `xcode-select --install` to get a [Clang](https://clang.llvm.org) C compiler.


In the future, I might make a Docker setup for all of this...

## Config & Adding Languages

All of the information on how the languages are compiled, run, and cleaned up is set in the `.config` directory. When adding a new language, add it to the list in `languages.json` and put the commands for compiling/running/cleaning it in the corresponding `.json` files. Then, create a directory with the name of the language and implement your solutions. Just make sure the name of the directory lines up with the key used in the `.json` files. For example, if  make a directory for C#, I would call it `csharp` and then put `"csharp"` as the key in all of the `.config/*.json` files.

There are couple other key things to note - make sure compiled files are put in a `target` directory inside of the languages's directory and make sure the clean command deletes the `target` directory entirely. In addition, your code should output it's answers to stdout, i.e. use whatever 'print' functionality your language has.

## Future Languages

 - Gleam
 - C/C++
 - Forth
 - Common Lisp
 - Smalltalk
 - OCaml
 - Julia
 - Haskell
 - Ruby
 - Clojure
 - Kotlin/Java
 - C#
 - F#
 - PHP
 - Go
 - Swift
 - Val
 - Zig
 - Odin
 - Vale
 - Pony
 - Wren
 - Perl/Raku
 - SNOBOL (SPITBOL)
 - Lua
 - V 
 - D 
 - Idris
 - Agda
 - Lean
 - Coq
 - ARM64 assembly
 - J
 - Ada 
 - Dart
 - Nim
 - Erlang
 - Lobster
 - Scheme
 - Io
 - Prolog
 - Factor
 - Elm
 - PureScript
 - MiniKanren
 - Curry
 - Alice
 - Tcl
 - AWK
 - Fjolnir

or almost anything from 
[this list](https://github.com/robertmuth/awesome-low-level-programming-languages)
or 
[this list](https://learnxinyminutes.com).


# Contributors

 - Benedikt Arnarsson

# License

[Benedikt Arnarsson © MIT](./LICENSE)
