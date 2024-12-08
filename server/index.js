const express = require('express');
const db = require('./db');

const app = express();
const PORT = process.env.PORT || 5000;
app.use(express.json()); 

app.get('/', (req, res) => {
    res.send("Hello, world")
})

app.get('/data', async (req, res) => {
    try {
      const result = await db.query('SELECT * FROM data_model');
      res.json(result.rows.reverse());  
    } catch (error) {
      console.error('Error executing query', error.stack);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

app.post('/upload', async (req, res) => {
    const { data, en_data } = req.body;
    console.log(data)

    if (!data) {
        return res.status(400).json({message: "Data are required"})
    }

    try {
        const result = await db.query(
            'INSERT INTO data_model (data, en_data) VALUES ($1, $2) RETURNING id',
            [data, en_data]
          );
      
          res.status(201).json({ id: result.rows[0].id, data, en_data });
    } catch (e) {
        console.error('Error inserting data', e)
        res.status(500).json({ error: 'Internal server error '})
    }

})

app.listen(PORT, () => {
    console.log(`http://localhost:${PORT}`)
})