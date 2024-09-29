import { createRouter, createWebHistory } from "vue-router";
import Account from "@/components/Account.vue";
import Signup from "@/components/auth/Signup.vue";
import Explore from "@/components/Explore.vue";

const routes = [
    { path: '/account', component: Account },
    { path: '/signup', component: Signup },
    { path: '/explore', component: Explore },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;
  