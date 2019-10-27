<template>
	<div class="statistics-wrapper">
		<h2>{{ courseName }} In-Class Statistics</h2>
		<Button @click="$router.back()">Go back</Button>
		<div class="statistics">
			<h3>Overall Performance</h3>
			<h3>Students To Help</h3>
			<h3>Students' Performance</h3>
			<div class="list">
				<p>
				Average tasks solved
				</p>
				<p>
				6.7/10
				</p>

				<p>
				Students in class
				</p>
				<p>
				25/30
				</p>

				<p>
					How many students solved
				</p>

				<span>20</span> /
				<span>19</span><br/>
				<span>40</span> /
				<span>15</span><br/>
				<span>60</span> /
				<span>13</span><br/>
				<span>80</span> /
				<span>8</span><br/>
				<span>100</span> /
				<span>1</span>
			</div>


			<div class="list">
				<p>Kevin Clein</p>
				<p>George Bush</p>
				<p>Kventin Tarantino</p>
				<p>George Washignton</p>

				<!--<span>{{student name}}</span>-->
			</div>

			<div class="list">
				<p>Kevin Clein</p>
				<p>18</p>
				<p>George Bush</p>
				<p>22</p>
				<p>Kventin Tarantino</p>
				<p>20</p>
				<p>George Washignton</p>
				<p>27</p>
				<p>Oliver Sachs</p>
				<p>26</p>
				<p>Jane Street</p>
				<p>30</p>

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

<style lang="scss" scoped>
	h2, h3 {
		font-weight: 600;
	}

	.statistics {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		column-gap: 2em;
	}

	.list {
		min-height: 10em;
		border-radius: 15px;
		border: 1px solid #ddd;
	}

	.center {
		margin-top: 1.5em;
		display: flex;
		justify-content: center;
	}
</style>