// import path module
const path = require("path");

const express = require("express");

const adminController = require("../controllers/admin");

const router = express.Router();

console.log("In admin.js");

// /admin/add-product => GET (Load a new page)
// router.get - Define a route for handling HTTP GET request
router.get("/add-product", adminController.getAddProduct);
// /admin/products => GET (Load a new page)
router.get("/products", adminController.getProducts);
// /admin/add-product => POST
// router.post - Route for handling HTTP POST request used when a client wants to send data to the server
router.post("/add-product", adminController.postAddProduct);

router.get("/edit-product/:productId", adminController.getEditProduct);

router.post("/edit-product", adminController.postEditProduct);

router.post("/delete-product", adminController.postDeleteProduct);

module.exports = router;
