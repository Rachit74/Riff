<template>
    <div>
      <div v-if="isAuthenticated">
        <div v-if="user">
            <ProfileControls :logout="logout" :user="user"/>
        </div>
      </div>
      <div v-else>

        <!-- when event login-attemp or happens then call the login function -->
        <LoginForm @login-attempt="login" />
        <!-- Listen for registration-success event -->
        <Signup @registration-success="login" />
      </div>
    </div>
    <div>
      {{ isAuthenticated }}
    </div>
  </template>
  
  <script>
  import ProfileControls from './ProfileControls.vue';
  import LoginForm from './auth/LoginForm.vue';
  import Signup from './auth/Signup.vue';
  import { ref, onMounted } from 'vue';
  
  export default {
    components: {
      ProfileControls,
      LoginForm,
      Signup,
    },
    setup() {
      let isAuthenticated = ref(false);
      let user = ref(null);
  
      const checkAuthStatus = async () => {
        try {
          const response = await fetch('http://localhost:8000/users/profile/', {
            credentials: 'include',
          })
          if (response.ok) {
            isAuthenticated.value = true;
            user.value = await response.json()
            console.log(user.value);
            console.log(isAuthenticated.value);
          } else {
            isAuthenticated.value = false;
            user.value = null;
          }
        } catch (error) {
          console.error('Auth check failed:', error);
          isAuthenticated.value = false;
          user.value = null;
        }
      }
  
    //   parms are the user creds
      const login = async (parms) => {
        try {
          const csrfResponse = await fetch('http://localhost:8000/users/token/');
          const csrfToken = await csrfResponse.text();
  
          const response = await fetch('http://localhost:8000/users/login/', {
            method: "POST",
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
              username: parms.username,
              password: parms.password,
            }),
            credentials: 'include',
          });
  
          if (response.ok) {
            await checkAuthStatus();
          } else {
            console.error('Login failed');
            isAuthenticated.value = false;
          }
        } catch (error) {
          console.error('Login Failed: ', error);
        }
      }
  
      const logout = async () => {
        try {
          let response = await fetch('http://localhost:8000/users/logout/', {
            method: "GET",
            credentials: "include",
          });
          
          if (response.ok) {
            console.log("Logged Out");
            isAuthenticated.value = false
            user.value = null
          } else {
            console.error("Failed logout", response.statusText);
          }
        } catch (error) {
          console.error(error);
        }
      };
  
      onMounted(checkAuthStatus);
      
      return {
        isAuthenticated,
        user,
        login,
        logout,
      };
    }
  };
  </script>

<style>
.account-container {
  padding: 20px;
  background-color: #121212;
  color: #ffffff;
  border-radius: 8px;
}

h2 {
  color: #ffffff;
  font-weight: 500;
  margin-bottom: 20px;
}

button {
  background-color: #1DB954;
  color: white;
  padding: 12px 24px;
  border-radius: 25px;
  font-weight: 700;
  cursor: pointer;
}

button:hover {
  background-color: #1ED760;
}
</style>