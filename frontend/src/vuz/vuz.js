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
import ReportFormPage from './pages/ReportForm.vue'
import ReportPage from './pages/Report.vue'
import RatingsPage from './pages/Ratings.vue'
import HistoryPage from './pages/History.vue'

axios.defaults.baseURL = '/api';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(VueCookie);

const routes = [
    { name: 'index', path: '/', component: IndexPage },
    { name: 'report-form', path: '/report-form/', component: ReportFormPage },
    { name: 'report', path: '/report/:form-id', component: ReportPage, props: true },
    { name: 'ratings', path: '/ratings/', component: RatingsPage },
    { name: 'history', path: '/history/', component: HistoryPage },
]

const router = new VueRouter({
    routes: routes,
    mode: 'history',
    base: '/vuz/'
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