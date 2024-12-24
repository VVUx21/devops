//express app that serves the html file

const express = require('express');
const path = require('path');

const app = express();

app.set('view engine', 'ejs'); // Set EJS as the template engine
app.set('views', path.join(__dirname, 'views')); // Set the directory for EJS files
app.use(express.static(path.join(__dirname, 'public'))); // Serve static files

const URL = process.env.BACKEND_URL || 'http://localhost:8080/api'; // Replace with your actual API URL

app.get('/', async (req, res) => {
  const options = {
    method: 'GET',
  };

  try {
    const response = await fetch(URL, options);
    const data = await response.json();
    res.render('index', { data }); // Pass data to the 'index.ejs' template
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({
      error: 'Server error',
      message: error.message || 'An error occurred while processing the request',
    });
  }
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
