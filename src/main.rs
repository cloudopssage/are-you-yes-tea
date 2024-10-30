mod models;
mod handlers;

use actix_web::{web, App, HttpServer};
use handlers::{add_book, get_books};
use std::sync::Mutex;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let books = web::Data::new(Mutex::new(vec![]));

    HttpServer::new(move || {
        App::new()
            .app_data(books.clone())
            .route("/books", web::get().to(get_books))
            .route("/books", web::post().to(add_book))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
