var app = new Vue({
    el: '#vueForm',
    data: {
        form: {
            name: '',
            region: '',
            taste: '',
            url: ''
        }
    },
    options: {
        taste_options: [
            { value: 'sweet', text: 'Sweet' },
            { value: 'savory', text: 'Savory' }
        ]
    }
})