<template>
  <div id="games-index">
    <h1>Game Code: {{ game.game_code }}</h1>
    <h2>Letters remaining: {{ game.letters_remaining.length }}</h2>
    <form v-on:submit.prevent>
      <input v-model.number="letter_count" type="number" min="1" max="7">
      <button v-on:click="draw_letters">Draw letters</button>
    </form>
    <div class="last-drawn">
      <ol>
        <li 
          v-for="letter in letters_drawn"
          :key="letter"
        >{{ letter }}</li>
      </ol>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GamesShow',
  data () {
    return {
      game: {
        letters_remaining: 100,
      },
      letter_count: 7,
      letters_drawn: [],
    }
  },
  mounted () {
    axios
      .get(`http://localhost:8000/games/${this.$route.params.id}/`)
      .then(response => (this.game = response.data))
  },
  methods: {
    draw_letters: function () {
      console.log(this.letter_count);
      axios
        .post(`http://localhost:8000/games/${this.$route.params.id}/draw/`, {
          count: this.letter_count
        })
        .then(response => {
            this.game = response.data.game;
            this.letters_drawn = response.data.letters_drawn;
        })
    }
  }
}
</script>
