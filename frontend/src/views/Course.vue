<template>
	
</template>

<script lang="ts">
	import Vue from 'vue';
	import { Course } from '@/types';
	
	export default Vue.extend({
		data() {
			return {
				id: '',
			};
		},
		computed: {
			course(): Course {
				return this.$store.getters.course(this.id);
			},
		},
		mounted() {
			this.id = this.$route.params.id;
			this.$store.dispatch('getCourse', this.id);
		},
	});
</script>