import Vue from 'vue';
import store from './store';
import Router, { NavigationGuard } from 'vue-router';
import Dashboard from './views/Dashboard.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Course from './views/Course.vue';
import Lesson from './views/Lesson.vue';
import Statistics from './views/Statistics.vue';
import ClassStatistics from './views/InClassStatistics.vue';
import PracticeControl from './views/PracticeControl.vue';

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
		{
			path: '/register',
			name: 'register',
			component: Register,
		},
		{
			path: '/courses/:id',
			name: 'course',
			component: Course,
		},
		{
			path: '/lessons/:id',
			name: 'lesson',
			component: Lesson,
		},
		{
			path: '/statistics',
			name: 'statistics',
			component: Statistics,
		},
		{
			path: '/practice-control',
			name: 'practice-control',
			component: PracticeControl,
		},
		{
			path: '/class-stats',
			name: 'class-stats',
			component: ClassStatistics,
		},
	],
});
