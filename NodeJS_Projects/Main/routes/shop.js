const path = require("path");

const express = require("express");

const shopController = require("../controllers/shop");

const router = express.Router();

console.log("In shop.js");

router.get("/", shopController.getIndex);

router.get("/products", shopController.getProducts);

//Colon tells express that after /products/any value can be there
router.get("/products/:productId", shopController.getProduct);

router.get("/cart", shopController.getCart);

router.post("/cart", shopController.postCart);

router.post("/cart-delete-item", shopController.postCartDeleteProduct);

router.get("/orders", shopController.getOrders);

router.get("/checkout", shopController.getCheckout);

module.exports = router;
