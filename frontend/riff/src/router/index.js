import { createRouter, createWebHistory } from "vue-router";
import Account from "@/components/Account.vue";
import Signup from "@/components/auth/Signup.vue";

const routes = [
    { path: '/account', component: Account },
    { path: '/signup', component: Signup },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;
  