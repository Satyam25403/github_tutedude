const express = require('express');
const axios = require('axios');
const path = require('path');
const backend_url = process.env.BACKEND_URL || 'http://localhost:5000/api';
const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', async (req, res) => {
  try {
    const response = await axios.get(backend_url); 
    console.log('Fetched data:', response.data);
    res.render('index', { data: response.data });
    
  } catch (error) {
    res.status(500).send('Error fetching data');
  }
});

app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on http://0.0.0.0:3000');
});
