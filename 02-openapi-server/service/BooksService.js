"use strict";

/**
 *
 * bookId Integer
 * no response value expected for this operation
 **/
exports.deleteBook = function (bookId) {
  return new Promise(function (resolve, reject) {
    resolve();
  });
};

/**
 *
 * bookId Integer
 * no response value expected for this operation
 **/
exports.deleteBookBorrower = function (bookId) {
  return new Promise(function (resolve, reject) {
    resolve();
  });
};

/**
 *
 * bookId Integer
 * returns Book
 **/
exports.getBook = function (bookId) {
  return new Promise(function (resolve, reject) {
    var examples = {};
    examples["application/json"] = {
      name: "name",
      borrower: "",
      id: 0,
    };
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
};

/**
 *
 * bookId Integer
 * returns User
 **/
exports.getBookBorrower = function (bookId) {
  return new Promise(function (resolve, reject) {
    var examples = {};
    examples["application/json"] = {
      name: "name",
      id: 0,
    };
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
};

/**
 *
 * returns List
 **/
exports.getBooks = function () {
  return new Promise(function (resolve, reject) {
    var examples = {};
    examples["application/json"] = [
      {
        name: "The Hitchhiker's Guide to the Galaxy",
        id: 1,
      },
      {
        name: "The Restaurant at the End of the Universe",
        id: 2,
      },
      {
        name: "Life, the Universe and Everything",
        id: 3,
      },
      {
        name: "So Long, and Thanks for All the Fish",
        id: 4,
      },
      {
        name: "Mostly Harmless",
        id: 5,
      },
    ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
};

/**
 *
 * body Book
 * bookId Integer
 * returns Book
 **/
exports.putBook = function (body, bookId) {
  return new Promise(function (resolve, reject) {
    var examples = {};
    examples["application/json"] = {
      name: "name",
      borrower: "",
      id: 0,
    };
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
};

/**
 *
 * body User
 * bookId Integer
 * returns User
 **/
exports.putBookBorrower = function (body, bookId) {
  return new Promise(function (resolve, reject) {
    var examples = {};
    examples["application/json"] = {
      name: "name",
      id: 0,
    };
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
};
