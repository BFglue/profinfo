// import 'font-awesome/css/font-awesome.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap'
import 'bootstrap/scss/bootstrap.scss';

import axios from 'axios'
import moment from 'moment'

import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import VueCookie from 'vue-cookie'
import store from './store'

import IndexPage from './pages/Index.vue'
import ProfessionPage from './pages/Profession.vue'

axios.defaults.baseURL = '/api';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(VueCookie);

const routes = [
    { name: 'index', path: '/', component: IndexPage },
    { name: 'profession', path: '/profession/:profession_id', component: ProfessionPage, props: true },
]

const router = new VueRouter({
    routes: routes,
    mode: 'history',
    base: '/abiturient/'
})

Vue.directive('focus', {
  inserted: function (el) {
    el.focus()
  }
})

Vue.filter('formatDate', function(value, format) {
    if (!format) {
        format = 'DD-MM-YYYY hh:mm'
    }
    if (value) {
        return moment(String(value)).format(format)
    }
})

Vue.filter('substring', function(value, len, end='...') {
    if (value.length <= len) {
        return value
    }
    else {
        return value.substr(0, len) + end
    }

})

new Vue({
    router: router,
    store,
    render: h => h(App)
}).$mount('#app');