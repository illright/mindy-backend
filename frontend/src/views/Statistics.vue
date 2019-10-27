<template>
	<div class="statistics-wrapper">
		<h2>{{ courseName }} Overall Statistics</h2>
		<div class="activities">
			<Button
				v-for="act in items"
				filled
				:key="act"
			>
				{{ act }}
			</Button>
		</div>

		<div class="statistics">
			<h3>Overall Performance</h3>
			<h3>Students</h3>
			<BarChart :labels="items" :students="students" />
			<div class="graph" style="padding: 1.5em;">
				<div class="group">0-25%</div>
				<ul>
					<li>Lev</li>
				</ul>
				<div class="group">75-100%</div>
				<ul>
					<li>Cee</li>
					<li>Abdelrahman</li>
					<li>Anna</li>
				</ul>
			</div>
		</div>

		<div class="center">
			<Button filled><router-link to="/practice-control" tag="span">practice sessions</router-link></Button>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Button from '@/components/Button.vue';
	import BarChart from '@/components/BarChart.vue';

	export default Vue.extend({
		components: {
			Button,
			BarChart,
		},
		data() {
			return {
				items: ['classwork', 'homework', 'home quizzes', 'in-class quizzes', 'class attendance', 'online attendance'],
				students: ['Lev', 'Anna', 'Polly', 'Cee'],
			};
		},
		computed: {
			courseName() {
				const course = this.$store.getters.course(1);
				return course == null ? 'Mathematics' : course.name;
			},
		 },
	});
</script>

<style lang="scss">
	h2, h3 {
		font-weight: 600;
	}

	.activities {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
	}

	.statistics {
		display: grid;
		grid-template-columns: 2fr 1fr;
		column-gap: 2em;
	}

	.graph {
		height: 10em;
		border-radius: 15px;
		border: 1px solid #ddd;
	}

	.center {
		margin-top: 1.5em;
		display: flex;
		justify-content: center;
	}

	.group {
		font-weight: 600;
	}
</style>