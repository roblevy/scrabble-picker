<template>
  <div id="games-index">
    <ol>
      <li
        v-for="game in games"
        :key="game.game_code"
      >{{ game.game_code }}</li>
    </ol>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GamesIndex',
  data () {
    return {
      games: [],
    }
  },
  mounted () {
    axios
      .get('http://localhost:8000/games/')
      .then(response => (this.games = response.data))
  }
}
</script>
