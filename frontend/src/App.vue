<template>
  <div class="container" id="top">
    <CategorySwitchButtons
      :foodButtonDisabled="food"
      :drinkButtonDisabled="drink"
      @buttonClicked="getAPI"
    />
    <div class="columns is-multiline" id="cards">
      <div class="column is-3" v-for="entry in apiData" :key="entry.id">
        <div class="card">
          <div class="card-content">
            <p class="subtitle">{{ entry['name'] }}</p>
          </div>
          <footer class="card-footer">
            <p class="card-footer-item">
              <span>
                <a :href="entry['url']">Purchase here</a>
              </span>
            </p>
          </footer>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CategorySwitchButtons from "./components/CategorySwitchButtons.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    CategorySwitchButtons
  },
  data() {
    return {
      apiData: null,
      food: false,
      drink: false,
      lastButtonClicked: null,
      msg: "Nothing clicked yet"
    };
  },
  methods: {
    getAPI(buttonName) {
      if (buttonName === "food") {
        this.lastButtonClicked = "food";
        axios
          .get("http://api.myjapandb.com/api/japan/food/all")
          .then(response => {
            this.apiData = response.data;
            this.msg = response.data;
          })
          .catch(e => {
            console.log(e);
          });
      } else if (buttonName === "drink") {
        this.lastButtonClicked = "drink";
        axios
          .get("http://api.myjapandb.com/api/japan/drinks/all")
          .then(response => {
            this.apiData = response.data;
            this.msg = response.data;
          })
          .catch(e => {
            console.log(e);
          });
      }
    },
    init() {
      if (localStorage.lastButtonClicked) {
        this.lastButtonClicked = localStorage.lastButtonClicked;
        this.getAPI(this.lastButtonClicked);
      }
    }
  },
  mounted() {
    this.init();
  },
  watch: {
    lastButtonClicked(newValue) {
      localStorage.lastButtonClicked = newValue;
    }
  }
};
</script>

<style scoped>
#top {
  margin-top: 60px;
}
</style>