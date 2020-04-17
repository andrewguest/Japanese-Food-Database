<template>
  <div class="columns">
    <div class="column is-2 is-offset-4">
      <div
        class="button is-medium is-rounded"
        style="background-color: #75dddd;"
        :disabled="foodButtonDisabled"
        @click="onClickButton('food')"
      >Show food</div>
    </div>
    <div class="column is-2">
      <div
        class="button is-medium is-rounded"
        style="background-color: #75dddd;"
        :disabled="drinkButtonDisabled"
        @click="onClickButton('drink')"
      >Show drinks</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CategorySwitchButtons",
  props: {
    foodButtonDisabled: Boolean,
    drinkButtonDisabled: Boolean
  },
  methods: {
    onClickButton(event) {
      this.$emit("buttonClicked", event);
    }
  }
};
</script>
