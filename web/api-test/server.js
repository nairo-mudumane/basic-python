const express = require('express');
const app = express();

const fruits = ['banana', 'laranja', 'manga'];

app.get('/', (req, res) => {
  console.log('nmew get request');
  return res.status(200).json({ error: false, data: fruits });
});

app.post('/new', (req, res) => {
  console.log('new post request');
  data = req.body;
  console.log(data);
  //   fruits.push(data.name);
  return res.status(201).json({ error: false, data: fruits });
});

app.listen(3030, () => console.log('server running'));
