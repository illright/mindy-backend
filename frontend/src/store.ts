import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		user: null,
	},
	mutations: {

	},
	actions: {

	},
	getters: {
		logged_in: (state) => state.user != null,
	},
});
