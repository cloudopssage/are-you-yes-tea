use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone)]
pub struct Book {
    pub id: u32,
    pub title: String,
    pub author: String,
}
