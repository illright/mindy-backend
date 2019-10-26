import Vue from 'vue';
import Vuex from 'vuex';

import { Course } from './types';

Vue.use(Vuex);

const BASE_URL = '';

export default new Vuex.Store({
	state: {
		user: null,
		courses: [] as Course[],
	},
	mutations: {
		setUser(state, payload) {
			state.user = payload;
		},
		setCourse(state, payload: Course) {
			const index = state.courses.findIndex((c) => c.id === payload.id);
			if (index === -1) {
				state.courses.push(payload);
			} else {
				Vue.set(state.courses, index, payload);
			}
		},
	},
	actions: {
		async login({commit}, {email, password}) {
			const response = await fetch(`${BASE_URL}/login`, {
				method: 'POST',
				body: JSON.stringify({ email, password }),
			});
			const json = await response.json();
			commit('setUser', json);
		},
		async getCourses({commit}) {
			/* [
				{id: 1, lessonsCompleted: 2, lessonsTotal: 3, title: 'Mathematics'},
				{id: 2, lessonsCompleted: 1, lessonsTotal: 4, title: 'English'},
				{id: 3, lessonsCompleted: 0, lessonsTotal: 6, title: 'Physics'},
				{id: 4, lessonsCompleted: 10, lessonsTotal: 10, title: 'Russian'},
				{id: 5, lessonsCompleted: 9, lessonsTotal: 10, title: 'Programming'},
			].forEach(c => commit('setCourse', c));
			return; */

			const response = await fetch(`${BASE_URL}/courses`);
			const json = await response.json();
			for (const course of json) {
				commit('setCourse', course);
			}
		},
		async getCourse({commit}, payload) {
			const response = await fetch(`${BASE_URL}/courses/${payload}`);
			const json = await response.json();
			commit('setCourse', json);
		},
		async getLessons({commit}, courseId: string) {
			const response = await fetch(`${BASE_URL}/course/${courseId}/lessons`);
			const json = await response.json();
			commit('setCourse', {
				id: courseId,
				lessons: json,
			});
		},
	},
	getters: {
		logged_in: (state) => state.user != null,
		course: (state) => (id: string) => state.courses.find((c) => c.id === id),
	},
});
