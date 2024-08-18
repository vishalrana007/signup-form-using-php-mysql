
const form = document.getElementById('signup-form');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    const confirmPassword = confirmPasswordInput.value.trim();

    if (username === '' || email === '' || password === '' || confirmPassword === '') {
        errorMessage.textContent = 'Please fill out all fields.';
        return;
    }

    if (password !== confirmPassword) {
        errorMessage.textContent = 'Passwords do not match.';
        return;
    }

    window.alert('Form submitted successfully!');

});


const MySql = require('mysql');

const dbHost = 'localhost';
const dbUser = 'VISHxRANA';
const dbPassword = 'mysql@123';
const dbName = 'signup_db';


const db = MySql.createConnection({
  host: dbHost,
  user: dbUser,
  password: dbPassword,
  database: dbName
});


db.connect((err) => {
    if (err) {
      console.error('Error connecting to database:', err);
      return;
    }
    console.log('Connected to database');
  });

function updateUser(id, username, email, password) {
 
  const query = 'UPDATE users SET username = " ", email = " ", password = " "' ;
  db.query(query, [username, email, password, id], (err) => {
    if (err) {
      console.error('Error updating user:', err);
    } else {
      console.log('User updated successfully');
    }
  });

}


  

  
