import Vue from 'vue';
import store from './store';
import Router, { NavigationGuard } from 'vue-router';
import Dashboard from './views/Dashboard.vue';
import Login from './views/Login.vue';

Vue.use(Router);

export default new Router({
	mode: 'history',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/',
			name: 'home',
			component: Dashboard,
			beforeEnter(from, to, next) {
				if (!store.getters.logged_in) {
					next('/login');
				} else {
					next();
				}
			},
		},
		{
			path: '/login',
			name: 'login',
			component: Login,
		},
	],
});
