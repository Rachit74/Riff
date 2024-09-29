<template>
  <div class="app-container">
    <!-- Sidebar -->
    <nav class="sidebar">
      <h3 class="nav-header">Riff</h3>
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">Explore</a></li>
        <li><a href="#">Account</a></li>
      </ul>
    </nav>
    
    <!-- Main content -->
    <div class="main-content">
      <Account />
    </div>
  </div>
</template>

<script>
import Account from './components/Account.vue';
export default {
  components: {
    Account,
  }
};
</script>
