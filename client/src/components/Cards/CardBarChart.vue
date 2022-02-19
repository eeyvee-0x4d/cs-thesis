<template>
	<div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-ld rounded-lg">
		<div class="rounded-t mb-0 px-4 py-3 bg-transparent">
			<div class="flex flex-wrap items-center">
				<div class="relative w-full max-w-full flex-grow flex-1">
					<h2 class=" text-base font-bold">
						Chart Title
					</h2>
				</div>
			</div>
		</div>
		<div class="px-4 flex-auto">
			<div class="relative h-350-px">
				<BarChart :chartData="testData" />
			</div>
		</div>
	</div>
</template>

<script>
	import { defineComponent } from 'vue';
	import { Chart, registerables } from "chart.js";
	import { BarChart } from 'vue-chart-3';

	Chart.register(...registerables);

	export default defineComponent({
		name: 'CardBarChart',
		components: {
			BarChart
		},
		setup() {
			const testData = {
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

			return {testData};
		},
	});
</script>