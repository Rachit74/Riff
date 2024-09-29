<template>
    <div class="user-profile-controls">
      <div class="user-info">
        <div class="avatar">{{ user.username.charAt(0).toUpperCase() }}</div>
        <div class="user-details">
          <h2>{{ user.username }}</h2>
          <p>{{ user.email }}</p>
        </div>
      </div>
      <div class="user-stats">
        <div class="stat">
          <span class="stat-value">0</span>
          <span class="stat-label">Playlists</span>
        </div>
        <div class="stat">
          <span class="stat-value">0</span>
          <span class="stat-label">Followers</span>
        </div>
        <div class="stat">
          <span class="stat-value">0</span>
          <span class="stat-label">Following</span>
        </div>
      </div>
      <ul class="user-actions">
        <div v-if="user.artist">
        <li><a href="" class="action-link">Upload</a></li>
        </div>
        <li><a href="" @click.prevent="logout" class="action-link logout">Logout</a></li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ProfileControls',
    props: {
      user: {
        type: Object,
        required: true,
      },
      logout: {
        type: Function,
        required: true,
      }
    }
  }
  </script>
  
  <style scoped>
  .user-profile-controls {
    background-color: #121212;
    color: #fff;
    padding: 24px;
    border-radius: 8px;
    font-family: 'Helvetica', 'Arial', sans-serif;
  }
  
  .user-info {
    display: flex;
    align-items: center;
    margin-bottom: 24px;
  }
  
  .avatar {
    width: 64px;
    height: 64px;
    background-color: #1DB954;
    color: #000;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: bold;
    margin-right: 16px;
  }
  
  .user-details h2 {
    font-size: 28px;
    margin: 0 0 4px 0;
  }
  
  .user-details p {
    font-size: 14px;
    color: #b3b3b3;
    margin: 0;
  }
  
  .user-stats {
    display: flex;
    justify-content: space-around;
    margin-bottom: 24px;
  }
  
  .stat {
    text-align: center;
  }
  
  .stat-value {
    display: block;
    font-size: 24px;
    font-weight: bold;
  }
  
  .stat-label {
    font-size: 12px;
    color: #b3b3b3;
  }
  
  .user-actions {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  .action-link {
    display: block;
    padding: 12px 0;
    color: #fff;
    text-decoration: none;
    font-size: 14px;
    font-weight: bold;
    transition: color 0.3s ease;
  }
  
  .action-link:hover {
    color: #1DB954;
  }
  
  .logout {
    color: #b3b3b3;
  }
  
  .logout:hover {
    color: #ff5252;
  }
  </style>