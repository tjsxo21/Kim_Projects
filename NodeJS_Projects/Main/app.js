const path = require("path");

// Look for routes.js file and import module
const express = require("express"); //importing express package
const bodyParser = require("body-parser"); //import body parser package

const errorController = require("./controllers/error");
//Connect to SQL DB
const sequelize = require("./util/database");
const Product = require("./models/product");
const User = require("./models/user");
const Cart = require("./models/cart");
const CartItem = require("./models/cart-item");
const app = express(); //run express as a function
//app.set - Method to set various settings in express application, view engine - Key that tells express which template engine to use
app.set("view engine", "ejs");
// views - key that tells express where to look for view template files, views - where my EJS files are located
app.set("views", "views");

// import router object from admin.js
const adminRoutes = require("./routes/admin");
const shopRoutes = require("./routes/shop");

// take 3 arg - request, response, next
// next is a function that will be passed for it to travel to next middleware
// use method allow us to add a middleware function
//"/ - Slash represents a path"

// Registers a middleware
app.use(bodyParser.urlencoded({ extended: false })); //Enable body parser
// Serves static files, grant access to public folder
app.use(express.static(path.join(__dirname, "public")));
// This code will only run for incoming requests
app.use((req, res, next) => {
  User.findByPk(1)
    .then((user) => {
      //req.user is undefined by default. Storing user from the database in there
      req.user = user;
      next();
    })
    .catch((err) => console.log(err));
});

// Add /admin as a filter, access routes object
app.use("/admin", adminRoutes);
app.use(shopRoutes);
app.use(errorController.get404);

const runServer = () => {
  const PORT = 7000;
  const server = app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });

  server.on("error", (err) => {
    if (err.code === "EADDRINUSE") {
      console.error(`Port ${PORT} is already in use.`);
    } else {
      console.error("Server error:", err);
    }
  });
};

// Define Associations (Relations)
// Each product is associated with only one User
// If a user's deleted, product is also deleted ("CASCADE")
Product.belongsTo(User, { constraints: true, onDelete: "CASCADE" });
// One user can have many products
User.hasMany(Product);
User.hasOne(Cart);
Cart.belongsTo(User);
// One cart can hold multiple products
// { through: CartItem } - Tells where the connection should be stored. It creates cartId, productId in CartItem table
Cart.belongsToMany(Product, { through: CartItem });
// One product can be a part of multiple carts
Product.belongsToMany(Cart, { through: CartItem });

sequelize
  // Syncs my models created in sequelize to the database by creating the appropirate tables
  // .sync({ force: true }) - forces Sequelize to drop and recreate the tables each time you run
  .sync({ force: true })
  .then((result) => {
    return User.findByPk(1);
    //console.log(result);
  })
  .then((user) => {
    if (!user) {
      return User.create({ name: "Max", email: "test@test.com" });
    }
    return user;
  })
  .then((user) => {
    //console.log(user);
    runServer();
  })
  .catch((err) => {
    console.log(err);
  });
