const { Pool } = require('pg');

const pool = new Pool({
  user: process.env.user || 'zhyrgal',        
  host: process.env.host || 'localhost',        
  database: process.env.database || 'keyloggerdb',
  password: process.env.password || 'zhyrgal006',
  port: process.env.port || 5432,             
});

const query = (text, params) => pool.query(text, params);

module.exports = {
  query,
};
