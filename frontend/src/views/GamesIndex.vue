<template>
  <div id="games-index">
    <ol>
      <li v-for="game in games" :key="game.game_code">
        <a :href="`/games/${game.game_code}/`">{{ game.game_code }}</a>
      </li>
    </ol>
    <button v-on:click="handleNewClick">New</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GamesIndex",
  data() {
    return {
      games: [],
    };
  },
  mounted() {
    axios
      .get("/api/games/")
      .then((response) => (this.games = response.data));
  },
  methods: {
    handleNewClick: function() {
      axios.post("/api/games/").then((response) => {
        console.log(response.data);
        this.$router.push({
          name: "GamesShow",
          params: { id: response.data.game_code },
        });
      });
    },
  },
};
</script>
