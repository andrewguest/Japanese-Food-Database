import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // which is lazy-loaded when the route is visited.
        component: () => import('../views/About.vue')
    },
    {
        path: '/food',
        name: 'Food',
        // route level code-splitting
        // which is lazy-loaded when the route is visited.
        component: () => import('../views/Food.vue')
    },
    {
        path: '/drinks',
        name: 'Drinks',
        // route level code-splitting
        // which is lazy-loaded when the route is visited.
        component: () => import('../views/Drinks.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
