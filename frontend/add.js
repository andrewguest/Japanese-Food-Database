var app = new Vue({
    el: '#vueForm',
    data: {
        form: {
            name: '',
            region: '',
            taste: '',
            url: '',
            image_path: '',
        }
    },
    methods: {
        addNewCandy(){
            axios.post('https://bokksu-favorites.herokuapp.com/api/japan/food', {
                name: this.form.name,
                region: this.form.region,
                taste: this.form.taste,
                url: this.form.url,
                image_path: this.form.image_path
            }).then(function (response) {
                console.log(response);
            })
            .catch((e) => {
                console.log(this.form.name),
                console.log(this.form.region),
                console.log(this.form.taste),
                console.log(this.form.url),
                console.log(e.response.data),
                console.log(e.response)
            })
        }
    }
})