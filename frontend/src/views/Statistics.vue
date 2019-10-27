<template>
	<div class="statistics-wrapper">
		<h2>{{ courseName }} Overall Statistics</h2>
		<div class="activities">
			<Button
				v-for="act in items"
				filled
				:key="act"
				@click="selected = act"
			>
				{{ act }}
			</Button>
		</div>

		<div class="statistics">
			<h3>Overall Performance</h3>
			<h3>Students</h3>
			<BarChart :label="selected" :students="students" />
			<div class="graph" style="padding: 1.5em;">
				<div class="group">0-20%</div>
				<ul>
					<li>Tom</li>
				</ul>
                <div class="group">20-40%</div>
				<ul>
					<li>Polly</li>
                    <li>Sergey</li>
				</ul>
                <div class="group">40-60%</div>
				<ul>
					<li>George</li>
                    <li>Olya</li>
                    <li>Jane</li>
                    <li>Jonson</li>
				</ul>
                <div class="group">60-80%</div>
				<ul>
					<li>Kate</li>
                    <li>Sonya</li>
				</ul>
                <div class="group">80-100%</div>
				<ul>
					<li>Oliver</li>
                    <li>Ivan</li>
				</ul>

			</div>
		</div>

		<div class="center">
			<Button filled><router-link to="/class-stats" tag="span">practice sessions</router-link></Button>
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
				selected: 'classwork',
				items: ['classwork', 'homework', 'home quizzes', 'in-class quizzes', 'class attendance', 'online attendance'],
				students: ['Lev', 'Anna', 'Polly', 'Cee', 'Lesha', 'Kate', 'olya', 'olesea', 'peter', 'ivan', 'insaf', 'george', 'ilia', 'evgenyi', 'dmitriy', 'sasha', 'egor', 'sergey', 'nastay', 'nadya'],
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