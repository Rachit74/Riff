<template>
    <div>
        <!-- Loop through each track -->
        <div v-for="(track, index) in tracks" :key="index" class="track-card">
            <div class="track-cover">
                <img :src="track.cover" alt="Cover Image">
            </div>
            <div class="track-data">
                <span class="track-title-span">{{ track.title }}</span><br>
                <span class="track-artist-span">{{ track.artist }}</span>
            </div>
            <div class="controller">
                <audio :src="track.audio" controls>Your browser does not support the audio element.</audio>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const tracks = ref([]); // Define tracks as a reactive reference

        // Get all tracks
        const getTracks = async () => {
            let response = await fetch('http://localhost:8000/tracks/tracks/');
            const data = await response.json();
            tracks.value = data; // Update the reactive reference
            console.log(tracks.value);
        };

        onMounted(() => {
            getTracks(); // Call getTracks when the component is mounted
        });

        return {
            tracks
        };
    }
};
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
