<script lang="ts">
	import Vue from 'vue';
	import { Bar, mixins } from 'vue-chartjs';

	export default Vue.extend({
		extends: Bar,
		mixins: [mixins.reactiveData],
		props: ['label', 'students'],
		data() {
			return {
				options: {
					scales: {
						yAxes: [{
							display: true,
							ticks: {beginAtZero: true},
						}],
					},
				},
			};
		},
		methods: {
			getRandomInt(low = 0, high = 10) {
				return Math.floor(Math.random() * (high - low)) + low;
			},
		},
		watch: {
			label: {
				handler(newLabel) {
					if(this.chartData == null) {
						Vue.set(this, 'chartData', {});
					}

					const nums: number[] = this.students.map((_: string) => this.getRandomInt(0,10));
					this.chartData.labels = ['0-2', '3-4', '5-6', '7-8', '9-10'];
					const data = [
						nums.filter(num => num >= 0 && num <= 2).length,
						nums.filter(num => num >= 3 && num <= 4).length,
						nums.filter(num => num >= 5 && num <= 6).length,
						nums.filter(num => num >= 7 && num <= 8).length,
						nums.filter(num => num >= 9 && num <= 10).length,
					];

					this.chartData.datasets = [{
						backgroundColor: '#' + Math.floor(Math.random() * 16777215).toString(16),
						label: 'student count',
						data,
					}];

					/* this.chartData.labels = [newLabel];
					this.chartData.datasets = this.students.map((student: string) => ({
						backgroundColor: '#' + Math.floor(Math.random() * 16777215).toString(16),
						label: student,
						data: [this.getRandomInt(1, 10)],
					})); */
					this.renderChart(this.chartData, this.options);
				},
				immediate: true,
			},
		},
	});
</script>