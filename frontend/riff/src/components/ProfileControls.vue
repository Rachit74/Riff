<template>
    <div class="user-profile-controls">
        <ul>
            <li><a href="">Upload</a></li>
            <li><a href="" @click.prevent="logout">Logout</a></li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'ProfileControls',
    props: {
        // user: {
        //     type: Object,
        //     required: true,
        // },
        logout: {
            type: Function,
            required: true,
        }
    }
}
</script>