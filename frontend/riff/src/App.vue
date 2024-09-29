<template>
  <nav class="sidebar">
    <h3 class="nav-header">Riff</h3>
    <ul class="nav-links">
      <li><a href="">Home</a></li>
      <li><a href="">Explore</a></li>
      <li><a href="">Account</a></li>
    </ul>
    <!-- div class playlist -->
  </nav>
  <Account />
</template>


<script>
import Account from './components/Account.vue';
export default {
  components: {
    Account,
  }
};
</script>