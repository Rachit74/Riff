<template>
    <div>
        <!-- vue if else statement -->
        <div v-if="isAuthenticated">
            <h3>User is Authenticated</h3>
            <div v-if="user">
                <!-- Only show this if user is not null -->
                {{ user.username }}
                {{ user.artist }}
                {{ user.email  }}
            </div>
        </div>
        <div v-else>
            <h2>Login</h2>
            <!-- @submit.prevent="login" prevents the default action and call the login function -->
            <form action="" @submit.prevent="login">
                <input v-model="username" type="text" placeholder="Username" required>
                <input v-model="password" type="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
    <div>
        <!-- <div v-if="isAuthenticated"> -->
            {{ isAuthenticated  }}
        <!-- </div> -->
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    setup() {
        let isAuthenticated = ref(false);
        let user = ref(null);
        const username = ref('');
        const password = ref('');

        // checkAuthStatus functions which hits the user/profile endpoint to check for a response
        const checkAuthStatus = async () => {
            try {
                const response = await fetch('http://localhost:8000/users/profile/', {
                    credentials: 'include',
                })
                // if the respose is ok then authenticate the use
                if (response.ok) {
                    isAuthenticated.value =  true;
                    user.value = await response.json()
                    console.log(user.value);
                    console.log(isAuthenticated);
                    
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

        const login = async () => {
            try {
                // get the csrf token
                const csrfResponse = await fetch('http://localhost:8000/users/token/');
                const csrfToken = await csrfResponse.text();

                // login form handler
                const response = await fetch('http://localhost:8000/users/login/', {
                    // method and headers 
                    method: "POST",
                    headers : {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },

                    // body data
                    body: JSON.stringify({
                        username: username.value,
                        password: password.value,
                    }),

                    // creds
                    credentials: 'include',
                });

                // check if login valid
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
        
        // when the page is loaded call the checkAuthStatus function
        onMounted(checkAuthStatus);
        
        return {
            isAuthenticated,
            user,
            username,
            password,
            login,

        };
    }
};
</script>
