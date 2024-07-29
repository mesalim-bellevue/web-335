/**
 * Author: Bernice Templeman
 * Date: 7/18/2024
 * File Name: whatabook-queries.js
 * Description: MongoDB Shell Scripts for the books and customers collections
 */

const { query } = require("express")

// Write a query to display a list of books.
db.books.find()

// Write a query to display a list of books by genre.
db.books.find({"genre": "Technology"})

// Write a query to display a list of book by author.
db.books.find({"author": "Arnaud Lauret"})

// Write a query to display a book by bookId.
db.books.findOne({"bookId": "ISBN-9780321826626"})

// Write a query to display wishlist by customerId
db.customers.findOne(
  {"customerId": "c1001"},
  {"wishlistitems": 1}
)

// Write a query to add books to a custimer's wishlist: https://www.mongodb.com/docs/manual/reference/operator/update/push/
db.customers.updateOne(
  {customerId: "c1001"},
  {$push: {
    wishlistitems: {
      bookId: "ISBN-978-0590353403",
      genre: "Fantasy",
      title: "Harry Potter",
      author: "J.K. Rowling"
    }
  }
})

// Write a query to remove a book from a customer's wishlist: https://www.mongodb.com/docs/manual/reference/operator/update/pull/
db.customers.updateOne(
  {customerId: "c1001"},
  {$pull: {
    wishlistitems: {
      bookId: "ISBN-978-0590353403"
    }
  }
})