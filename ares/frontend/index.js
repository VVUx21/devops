//express app that serves the html file

const express = require('express');
const app = express();
const path = require('path');

app.use(express.static(path.join(__dirname,'public')));

const URL = process.env.BACKEND_URL || 'http://localhost:8080/api';  // replace with your actual API URL

const fetch = (...args) => 
  import ('node:fetch').then(({ default:fetch }) => fetch(...args));

app.get('/', async function (req,res) {
  const options ={
    method: 'GET'
  };

  fetch(URL, options).then(res => res.json()).then(json => console.log(json)).catch(error => console.error(error))

  try {
    const response = await fetch(URL, options);
    const data = await response.json();
    res.render('index', data)
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