<template>
  <div id="app">
  <h1>{{ message }}</h1>
  <games-index></games-index>
  </div>
</template>

<script>
import GamesIndex from './components/GamesIndex.vue'

export default {
  name: 'App',
  data () {
    return {
      message: 'Welcome to Vue.js'
    }
  },
  components: {
    GamesIndex,
  },
}
</script>
