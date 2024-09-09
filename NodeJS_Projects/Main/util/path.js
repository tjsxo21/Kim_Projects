const path = require("path");

// Full path to the main module file
module.exports = path.dirname(process.mainModule.filename);
