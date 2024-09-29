<template>
    <div class="login-container">
      <h2>To continue, log in to Spotify.</h2>
      <form @submit.prevent="submitLogin">
        <div class="input-group">
          <label for="username">Email address or username</label>
          <input v-model="username" id="username" type="text" placeholder="Email address or username" required>
        </div>
        <div class="input-group">
          <label for="password">Password</label>
          <input v-model="password" id="password" type="password" placeholder="Password" required>
        </div>
        <!-- <div class="forgot-password">
          <a href="#">Forgot your password?</a>
        </div> -->
        <div class="login-options">
          <button type="submit">LOG IN</button>
        </div>
      </form>
      <div class="signup">
        <p>Don't have an account? <a href="/signup">Signup</a></p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginForm',
    data() {
      return {
        username: '',
        password: '',
      }
    },
    methods: {
        submitLogin() {
            // emit the user login data to the parent component when login-attempt event is called
            this.$emit('login-attempt', {
                username: this.username,
                password: this.password
            }); 
        }
    }
  }
  </script>
  
  <style scoped>
  .login-container {
  max-width: 450px;
  margin: 0 auto;
  padding: 20px;
  background-color: #181818;
  border-radius: 8px;
  color: #ffffff;
}

h2 {
  font-size: 18px;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 20px;
  text-align: center;
}

.input-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #b3b3b3;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 4px;
  background-color: #282828;
  color: #ffffff;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border: 1px solid #1DB954;
}

button {
  background-color: #1DB954;
  color: white;
  border: none;
  border-radius: 25px;
  padding: 14px;
  font-weight: bold;
  cursor: pointer;
}

button:hover {
  background-color: #1ED760;
}

.signup {
  text-align: center;
  margin-top: 20px;
}

.signup a {
  color: #1DB954;
  text-decoration: none;
  font-weight: bold;
}

.signup a:hover {
  color: #1ED760;
}

  </style>