<template>
  <div class="app-container">
    <!-- Sidebar -->
    <nav class="sidebar">
      <h3 class="nav-header">Riff</h3>
      <ul class="nav-links">
        <li><a href="/home">Home</a></li>
        <li><a href="/explore">Explore</a></li>
        <li><a href="/account">Account</a></li>
      </ul>
    </nav>
    
  <!-- Main content -->
  <div class="main-content">
      <router-view />  <!-- This is where the routed components will render -->
    </div>
  </div>

</template>

<script>
import Account from './components/Account.vue';
export default {
  name: 'App',
};
</script>
