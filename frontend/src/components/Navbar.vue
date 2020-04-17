<template>
  <div class="nav">
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand has-text-right">
        <router-link to="/">
          <img
            src="../assets/logo.png"
            alt="MyJapanDB logo"
            style="max-width: 45%; max-height: 75%;"
          />
        </router-link>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start has-text-centered">
          <a class="navbar-item">
            <router-link
              to="/about"
              style="color: black; border-right: 2px solid black"
              id="link"
            >About</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/food" style="color: black; :hover: color: blue;" id="link">Food</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/drinks" style="color: black;" id="link">Drinks</router-link>
          </a>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  props: {},
  methods: {}
};
</script>

<style scoped>
a.navbar-item {
  font-family: "Roboto", sans-serif;
  font-size: x-large;
  flex-grow: 1;
  flex-direction: column;
  justify-content: center;
}
#link:hover {
  color: blue;
}
#link {
  padding: 0px 50px 0px 50px;
}

img {
  margin-top: 5%;
}
.navbar-start {
  margin-left: 10%;
}
</style>