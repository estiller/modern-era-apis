'use strict';

var utils = require('../utils/writer.js');
var Books = require('../service/BooksService');

module.exports.deleteBook = function deleteBook (req, res, next, bookId) {
  Books.deleteBook(bookId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteBookBorrower = function deleteBookBorrower (req, res, next, bookId) {
  Books.deleteBookBorrower(bookId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getBook = function getBook (req, res, next, bookId) {
  Books.getBook(bookId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getBookBorrower = function getBookBorrower (req, res, next, bookId) {
  Books.getBookBorrower(bookId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getBooks = function getBooks (req, res, next) {
  Books.getBooks()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putBook = function putBook (req, res, next, body, bookId) {
  Books.putBook(body, bookId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.putBookBorrower = function putBookBorrower (req, res, next, body, bookId) {
  Books.putBookBorrower(body, bookId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
