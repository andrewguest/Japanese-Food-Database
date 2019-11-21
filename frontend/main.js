var app = new Vue({
    el: '#apiData',
    data: {
        foodResults: [],
        drinkResults: []
    },
    filters: {
        capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
    },
    mounted() {
        axios.get("http://food.myjapandb.com:5000/api/japan/food/all")
        .then(response => {this.foodResults = response.data}),
        axios.get("http://food.myjapandb.com:5000/api/japan/drinks/all")
        .then(response => {this.drinkResults = response.data})
    }
});
