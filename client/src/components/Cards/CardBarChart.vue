<template>
	<div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-ld rounded-lg">
		<div class="rounded-t mb-0 px-4 py-3 bg-transparent">
			<div class="flex flex-wrap items-center">
				<div class="relative w-full max-w-full flex-grow flex-1">
					<h2 class=" text-base font-bold">
						{{ chartTitle }}
					</h2>
				</div>
			</div>
		</div>
		<div class="px-4 flex-auto">
			<div class="relative h-350-px">
				<div v-if="fetchingData" class="m-auto text-center font-bold text-base">
					<span>
						Loading data...
					</span>
				</div>
				<BarChart v-else :chartData="chartData" />
			</div>
		</div>
	</div>
</template>

<script>
	import { defineComponent } from 'vue';
	import { Chart, registerables } from "chart.js";
	import { BarChart } from 'vue-chart-3';

	import axios from 'axios';

	Chart.register(...registerables);

	export default defineComponent({
		name: 'CardBarChart',
		components: {
			BarChart
		},
		props: {
			chartTitle: { type: String, default: 'Chart Title'}
		},
		methods: {
			async fetchData() {
				this.fetchingData = true

				let response = await axios.get(import.meta.env.VITE_DJANGO_BASE_URL + '/sentiment_overview/')

				if (response.statusText !== "OK") {
						throw new Error(`HTTP error! status: ${response.status}`)
					};

				return await response;
			}
		},
		data() {
			const chartData = {
				labels: ['Pfizer', 'Sinovac', 'AstraZeneca', 'Moderna'],
				datasets: [
					{
						label: "Positive",
						data: [30, 40, 60, 70]
					},
					{
						label: "Negative",
						data: [30, 40, 60, 70]
					},
				],
			};

			let fetchingData = false;

			return {
				chartData,
				fetchingData
			};
		},
		mounted() {
			this.fetchData()
				.then(response => {

					this.chartData = {
						labels: [],
						datasets: [
							{
								label: "Positive",
								data: []
							},
							{
								label: "Negative",
								data: []
							}
						]
					};

					response.data.forEach(item => {
						
						if(item.sentiments !== null) {
							this.chartData.labels.push((item.name.charAt(0).toUpperCase() + item.name.slice(1)))
							this.chartData.datasets[0].data.push(item.sentiments[0]['positive'])
							this.chartData.datasets[1].data.push(item.sentiments[0]['negative'])
						}
						else {
							this.chartData.labels.push((item.name.charAt(0).toUpperCase() + item.name.slice(1)))
							this.chartData.datasets[0].data.push(0)
							this.chartData.datasets[1].data.push(0)
						}

						this.fetchingData = false
						console.log(this.fetchingData)
					});
				})
				.catch()
		}
	});
</script>