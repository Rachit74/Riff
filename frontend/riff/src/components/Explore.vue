<template>
    <div class="track-card">
        <div class="track-cover">
            <img src="https://i.scdn.co/image/ab67616d00001e023d9688e3c4838fb3c41415da" alt="Failed">
        </div>
        <div class="track-data">
            <span class="track-title-span">Hobbies</span><br>
            <span class="track-artist-span">BigMoney</span>
        </div>
        <div class="controller">
            <audio src="http://localhost:8000/media/tracks/Hobbies_-_BigMoney_Official_Song.mp3" controls>Your browser does not support the audio element.</audio>
        </div>
    </div>
</template>

<script>
</script>

<style>
.track-card {
    background-color: #181818; /* Dark background similar to Spotify */
    border-radius: 8px; /* Rounded corners */
    padding: 16px; /* Padding around the content */
    display: flex; /* Flex layout for the card */
    flex-direction: column; /* Column layout */
    align-items: center; /* Center content */
    max-width: 300px; /* Limit card width */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    transition: transform 0.2s; /* Animation on hover */
}

.track-card:hover {
    transform: scale(1.05); /* Slightly scale on hover */
}

.track-cover img {
    border-radius: 8px; /* Rounded image corners */
    width: 100%; /* Full width */
    height: auto; /* Maintain aspect ratio */
}

.track-data {
    margin: 12px 0; /* Spacing above and below */
    text-align: center; /* Center text */
}

.track-title-span {
    font-size: 18px; /* Title size */
    font-weight: bold; /* Bold title */
    color: #ffffff; /* White color for title */
}

.track-artist-span {
    font-size: 14px; /* Artist name size */
    color: #b3b3b3; /* Lighter gray for artist */
}

.controller {
    width: 100%; /* Full width for the audio player */
    margin-bottom: 12px; /* Space below the audio player */
}
</style>
