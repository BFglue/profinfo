<template>
<div>
    <nav-bar></nav-bar>
    <main role="main">
        <div class="container mt-3">
            <transition duration="50" name="component-fade" mode="out-in">
                <router-view></router-view>
            </transition>
        </div>
    </main>
</div>
</template>

<script>

import { mapActions } from 'vuex'
import NavBar from './components/TheNavBar.vue'

export default {
    data () {
        return {}
    },
    components: {
        NavBar,
    },
    mounted() {
        this.fetchProfile()
    },
    methods: {
        ...mapActions([
            'fetchProfile',
        ]),
    }
}
</script>

<style>
    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    h1, h2 {
        font-weight: normal;
    }
    .fade-enter-active, .fade-leave-active {
      transition: opacity .3s;
    }
    .fade-enter, .fade-leave-to {
      opacity: 0;
    }
    .component-fade-enter-active, .component-fade-leave-active {
      transition: opacity .05s;
    }
    .component-fade-enter, .component-fade-leave-to {
      opacity: 0;
    }
</style>
