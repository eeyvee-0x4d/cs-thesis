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
					<svg role="status" class="inline mr-2 w-6 h-6 text-gray-200 animate-spin fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
					    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
					    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
					</svg>
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
				labels: [],
				datasets: [
					{
						label: "Positive",
						backgroundColor: "#66bd63",
						borderColor: "#66bd63",
						barThickness: 40,
						fill: false,
						data: []
					},
					{
						label: "Negative",
						backgroundColor: "#f46d43",
						borderColor: "#f46d43",
						barThickness: 40,
						fill: false,
						data: []
					},
				],
				options: {
					maintainAspectRatio: false,
					responsive: true,
					tooltips: {
						mode: "index",
						intersect: false
					},
					hover: {
						mode: "nearest",
						intersect: true
					},
				}
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
					console.log(response)

					// this.chartData = {
					// 	labels: [],
					// 	datasets: [
					// 		{
					// 			label: "Positive",
					// 			data: []
					// 		},
					// 		{
					// 			label: "Negative",
					// 			data: []
					// 		}
					// 	]
					// };

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
					});
				})
				.catch()
		}
	});
</script>