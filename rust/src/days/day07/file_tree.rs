pub enum Node {
    File(FileNode),
    Dir(DirNode),
}

pub struct FileNode {
    name: String,
    size: u32,
    dir: DirNode,
}

impl FileNode {
    pub fn new(name: String, size: u32, dir: DirNode) -> Self {
        FileNode {
            name,
            size,
            dir,
        }
    }
}

pub struct DirNode {
    name:  String,
    dir: Option<Box<DirNode>>,
    entries: Vec<Node>,
}

impl DirNode {
    pub fn new(name: String, dir: Option<Box<DirNode>>) ->  Self {
        DirNode {
            name,
            dir,
            entries: Vec::new(),
        }
    }

    pub fn add_entry(mut self, node: Node) -> Self {
        self.entries.push(node);
        self
    }

    pub fn get_size(&self) -> u32 {
        self.entries
            .iter()
            .fold(0, |sum, node| {
                match node {
                    Node::File(file_node) => sum + file_node.size,
                    Node::Dir(dir_node) => sum + dir_node.get_size(),
                }
            })
    }
}