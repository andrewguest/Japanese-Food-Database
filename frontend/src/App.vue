<template>
  <div class="app">
    <section class="section">
      <div class="container">
        <Navbar />
      </div>
    </section>
  </div>
</template>

<script>
//import axios from "axios";
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar
  },
  data() {
    return {};
  },
  methods: {}
};
</script>