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
        <li v-for="(letter, index) in letters_drawn" :key="`letter-${index}`">
          {{ letter }}
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
    axios
      .get(`http://localhost:8000/games/${this.$route.params.id}/`)
      .then((response) => {
        this.game = response.data;
        this.letter_count = Math.min(this.game.letters_remaining.length, 7);
      });
  },
  methods: {
    draw_letters: function() {
      axios
        .post(`http://localhost:8000/games/${this.$route.params.id}/draw/`, {
          count: this.letter_count,
        })
        .then((response) => {
          this.game = response.data.game;
          this.letters_drawn = response.data.letters_drawn;
          this.letter_count = Math.min(this.game.letters_remaining.length, 7);
        });
    },
  },
};
</script>
