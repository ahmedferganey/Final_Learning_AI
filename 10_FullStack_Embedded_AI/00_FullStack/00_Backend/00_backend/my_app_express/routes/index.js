var express = require('express');
var router = express.Router();


console.log("server is running on port " + process.env.PORT);

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
