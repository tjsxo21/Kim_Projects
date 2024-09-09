const Sequelize = require("sequelize");

const sequelize = require("../util/database");

// Define model/table Cart in DB
const Cart = sequelize.define("cart", {
  id: {
    type: Sequelize.INTEGER,
    autoIncrement: true,
    allowNull: false,
    primaryKey: true,
  },
});

module.exports = Cart;
