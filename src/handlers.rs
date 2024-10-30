use actix_web::{web, HttpResponse, Responder};
use std::sync::Mutex;

use crate::models::Book;

type BookStore = Mutex<Vec<Book>>;

pub async fn get_books(data: web::Data<BookStore>) -> impl Responder {
    let books = data.lock().unwrap();
    HttpResponse::Ok().json(&*books)
}

pub async fn add_book(
    data: web::Data<BookStore>,
    new_book: web::Json<Book>,
) -> impl Responder {
    let mut books = data.lock().unwrap();
    books.push(new_book.into_inner());
    HttpResponse::Ok().json(books.clone())
}
