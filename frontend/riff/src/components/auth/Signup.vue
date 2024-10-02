<template>
    <div class="signup-container">
      <h1>Sign up on Riff</h1>
      <form @submit.prevent="registerUser">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" v-model="username" name="username" id="username" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" v-model="email" name="email" id="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" v-model="password" name="password" id="password" required>
        </div>
        <div class="form-group checkbox">
          <input type="checkbox" v-model="artist" name="artist" id="artist">
          <label for="artist">Register as artist?</label>
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    name: 'SignupForm',
    setup() {
      const username = ref('');
      const email = ref('');
      const password = ref('');
      const artist = ref(false);
  
      const registerUser = async () => {
        try {
          const csrfResponse = await fetch('http://localhost:8000/users/token');
          const csrfToken = await csrfResponse.text();
          console.log(csrfToken);
  
          const response = await fetch('http://localhost:8000/users/register/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
              username: username.value,
              email: email.value,
              password: password.value,
              artist: artist.value
            })
          });
  
          if (response.ok) {
            console.log('User registered successfully');
            // Handle successful registration (e.g., redirect to login page)
          } else {
            console.error('Registration failed');
            // Handle registration failure (e.g., show error message)
          }
        } catch (error) {
          console.error('An error occurred during registration:', error);
          // Handle error (e.g., show error message to user)
        }
      };
  
      return {
        username,
        email,
        password,
        artist,
        registerUser
      };
    }
  };
  </script>
  
  <style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #181818;
  border-radius: 8px;
  color: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #1DB954;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #b3b3b3;
  font-weight: 500;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 4px;
  background-color: #282828;
  color: #ffffff;
  margin-bottom: 10px;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  border: 1px solid #1DB954;
  outline: none;
}

.checkbox {
  display: flex;
  align-items: center;
  color: #b3b3b3;
}

.checkbox input {
  margin-right: 10px;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #1DB954;
  color: #ffffff;
  border: none;
  border-radius: 25px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #1ED760;
}

  </style>