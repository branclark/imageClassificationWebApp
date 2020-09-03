let express = require("express");
let app = express();

app.use(function(req, res, next) {
    console.log(`${new Date()} - ${req.method} request for ${req.url}`);
    next();
});

app.use(express.static("static/"));

var port = process.env.PORT || 8080;

app.listen(port, function() {
    console.log("Serving static on" + port);
});