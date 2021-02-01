<template>
  <div id="games-index">
    <h1>Game Code: {{ game.game_code }}</h1>
    <h2>Letters remaining: {{ game.letters_remaining.length }}</h2>
    <form v-on:submit.prevent v-if="game.letters_remaining.length > 0">
      <input
        v-model.number="letter_count"
        type="number"
        min="1"
        :max="Math.min(game.letters_remaining.length, 7)"
      />
      <button v-on:click="draw_letters">Draw letters</button>
    </form>
    <div class="last-drawn">
      <ol>
        <li v-for="(letter, index) in letters_drawn.sort()" :key="`letter-${index}`">
          <div class="letter-box">
            {{ letter.toUpperCase() }}
          </div>
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GamesShow",
  data() {
    return {
      game: {
        letters_remaining: 100,
      },
      letter_count: 7,
      letters_drawn: [],
    };
  },
  mounted() {
    console.log('Mounted');
    axios
      .get(`http://localhost:8000/games/${this.$route.params.id}/`)
      .then((response) => {
        this.game = response.data;
        this.letter_count = Math.min(response.data.letters_remaining.length, 7);
      });
  },
  methods: {
    draw_letters: function() {
      console.log('Draw letters');
      axios
        .post(`http://localhost:8000/games/${this.$route.params.id}/draw/`, {
          count: this.letter_count,
        })
        .then((response) => {
          this.game = response.data.game;
          this.letters_drawn = response.data.letters_drawn;
          this.letter_count = Math.min(response.data.game.letters_remaining.length, 7);
        });
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=News+Cycle:wght@700&display=swap');
ol {
  list-style-type: none;
}
.last-drawn {
  display: flex;
  flex-direction: column
}
.last-drawn ol {
  display: flex;
  justify-content: center;
}

.last-drawn li {
  align-items: center;
  background-color: #e6d1a3;
  border-radius: 16%;  
  display: flex;
  font-family: 'News Cycle', sans-serif;
  font-size: xx-large;
  height: 75px;
  justify-content: center;
  margin: 4px;
  width: 75px;
}
</style>
