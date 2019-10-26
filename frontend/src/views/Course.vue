<template>
	<div class="course-page">
		<h2>Arithmetic Fundamentals</h2>
		<div class="info">
			<Labeled label="provided by">
				<em>Innopolis University</em>
			</Labeled>
			<Labeled label="course time">
				<em>19 Sep 2019 – 20 Jun 2020</em>
			</Labeled>
			<Labeled label="teacher">
				<em>Ivan Konyukhov</em>
				some.email@provider.com
			</Labeled>
		</div>
		<div class="courses">
			<Card outline>
				text
			</Card>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Labeled from '@/components/Labeled.vue';
	import Card from '@/components/Card.vue';
	import { Course } from '@/types';

	export default Vue.extend({
		components: {Labeled, Card},
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

<style lang="scss">
	.course-page {
		padding-left: 60px;
	  padding-right: 60px;
	}

	h2 {
		font-size: 35px;
		font-weight: 600;
	}

	em {
		font-style: normal;
		font-weight: 600;
	}

	.info {
		display: flex;

		.labeled:not(:last-child) {
			margin-right: 5em;
		}
	}

	.courses {
		margin-top: 3em;
	}
</style>
