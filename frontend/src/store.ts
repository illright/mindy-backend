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
			const response = await fetch(`${BASE_URL}/courses`);
			const json = await response.json();
			for (const course of json) {
				commit('setCourses', course);
			}
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
	},
});
