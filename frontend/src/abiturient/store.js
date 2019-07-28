import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import each from 'lodash/each'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        profile: {},
    },
    getters: {
        profileShortName(state) {
            if (state.profile.last_name) {
                var name = state.profile.first_name[0] + '.'
                if (state.profile.third_name[0]) name += ' ' + state.profile.third_name[0] + '.'
                name += ' ' + state.profile.last_name
                return name
            }
            else {
                return state.profile.email
            }
        },
    },
    mutations: {
        SET_PROFILE (state, profile) {
            state.profile = profile
        },
    },
    actions: {
        fetchProfile({commit}) {
            return axios.get('/profile/')
                .then((response) => commit('SET_PROFILE', response.data))
        },
    }
})