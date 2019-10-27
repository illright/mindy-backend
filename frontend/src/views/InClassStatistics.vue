<template>
	<div class="statistics-wrapper">
		<h2>{{ courseName }} In-Class Statistics</h2>

		<div class="statistics">
			<h3>Overall Performance</h3>
			<h3>Students To Help</h3>
			<h3>Students' Performance</h3>
			<div class="list">
				<span>
				Average tasks solved
				</span>
				<span>
				6.7/10
				</span>

				<span>
				Students in class
				</span>
				<span>
				25/30
				</span>

				<span>
					How many students solved
				</span>

				<span>20</span>
				<span>19</span>
				<span>40</span>
				<span>15</span>
				<span>60</span>
				<span>13</span>
				<span>80</span>
				<span>8</span>
				<span>100</span>
				<span>1</span>
			</div>


			<div class="list">
				<span>Kevin Clein</span>
				<span>George Bush</span>
				<span>Kventin Tarantino</span>
				<span>George Washignton</span>

				<!--<span>{{student name}}</span>-->
			</div>

			<div class="list">
				<span>Kevin Clein</span>
				<span>18</span>
				<span>George Bush</span>
				<span>22</span>
				<span>Kventin Tarantino</span>
				<span>20</span>
				<span>George Washignton</span>
				<span>27</span>
				<span>Oliver Sachs</span>
				<span>26</span>
				<span>Jane Street</span>
				<span>30</span>

				<!--<span>{{student name}}</span>-->
				<!--<span>{{tasks6}}</span>-->

			</div>

		</div>

		<div class="center">
			<Button filled>overall course statistics</Button>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';
	import Button from '@/components/Button.vue';

	export default Vue.extend({
		components: {Button},
		computed: {
			courseName() {
				return 'Some Course';
			},
		 },
	});
</script>

<style lang="scss">
	h2, h3 {
		font-weight: 600;
	}

	.statistics {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		column-gap: 2em;
	}

	.list {
		height: 10em;
		border-radius: 15px;
		border: 1px solid #ddd;
	}

	.center {
		margin-top: 1.5em;
		display: flex;
		justify-content: center;
	}
</style>