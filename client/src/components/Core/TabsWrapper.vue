<template>
	<div>
		<div class="rounded-t mb-0 px-4 py-3 bg-transparent">
			<div class="flex flex-wrap items-center">
				<div class="relative w-full max-w-full flex-grow flex-1">
					<h2 class=" text-base font-bold">
						Sentiments over time
					</h2>
				</div>
			</div>
		</div>
		<Tabs>
			<Tab v-for="tab, index in tabs" :key="index" :title="tab.charAt(0).toUpperCase() + tab.slice(1)" :ref="tab">
				<CardLineChart ref="lineChart" :chartTitle="tab.charAt(0).toUpperCase() + tab.slice(1) + ' Vaccine Sentiment Trend'"/>
			</Tab>
		</Tabs>
	</div>
</template>

<script>
	import Tabs from './Tabs.vue';
	import Tab from './Tab.vue';
	import CardLineChart from '../Cards/CardLineChart.vue'

	import axios from 'axios';

	import { defineComponent, ref } from 'vue';

	export default defineComponent({
		name: 'TabsWrapper',
		components: {
			Tabs,
			Tab,
			CardLineChart
		},
		data() {
			let tabs = ["pfizer", "sinovac", "astrazeneca", "moderna"];

			let isFetchingData = false;

			return {
				tabs,
				isFetchingData
			}
		},
		methods: {
			async fetchData() {

				this.isFetchingData = true;

				let response = await axios.get(import.meta.env.VITE_DJANGO_BASE_URL + '/sentiment_trend/')

				if (response.statusText !== "OK") {
						throw new Error(`HTTP error! status: ${response.status}`)
					};

				return await response;
			}
		},
		mounted() {
			this.fetchData()
				.then(response => {
					// console.log(response)
					response.data.forEach((item, index) => {
						// console.log(this.$refs.lineChart[index].testData)

						let chartData = {
							labels: [],
							datasets: [
								{
									label: 'Positive',
									data: [69,69]
								},
								{
									label: 'Negative',
									data: [69,69]
								}
							]
						};

						let labels = []
						let data = []

						for(const [key,value] of Object.entries(item.sentiments[0])) {
							labels.push(key)
							data.push(value)
						}

						this.$refs.lineChart[index].chartData.labels = labels
						this.$refs.lineChart[index].chartData.datasets[0].data = data

						labels = []
						data = []

						for(const [key,value] of Object.entries(item.sentiments[1])) {
							labels.push(key)
							data.push(value)
						}

						this.$refs.lineChart[index].chartData.labels = labels
						this.$refs.lineChart[index].chartData.datasets[1].data = data

						// this.$refs.lineChart[index].chartData = chartData

						this.isFetchingData = false;
					});
				})
				.catch()
		}
	});
</script>