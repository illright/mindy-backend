<script lang="ts">
	import Vue from 'vue';
	import { Bar } from 'vue-chartjs';

	export default Vue.extend({
		extends: Bar,
		props: ['labels', 'students'],
		data() {
			return {
				chartData: {
					labels: this.labels,
					datasets: this.students.map((student: string) => ({
						backgroundColor: '#' + Math.floor(Math.random() * 16777215).toString(16),
						label: student,
						data: [...Array(6)].map(() => this.getRandomInt(0, 10)),
					})),
				},
				options: {

				},
			};
		},
		methods: {
			getRandomInt(low = 0, high = 10) {
				return Math.floor(Math.random() * (high - low)) + low;
			},
		},
		mounted() {
			this.renderChart(this.chartData, this.options);
		},
	});
</script>