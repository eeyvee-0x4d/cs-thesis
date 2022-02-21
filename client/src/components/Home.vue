<template>
	<div>
		<div class="relative">
			<!-- header stats here -->

			<div class="px-4 md:px-60 sm:px-16 mx-auto w-full">
				<CardHeader />
				<div class="flex flex-wrap">
					<div class="w-full px-4 border">
						<CardBarChart />
					</div>
					<div class="w-full px-4 border">
						<CardLineChart />
					</div>
					<div class="w-full px-4 border">
						<CardLineChart />
					</div>
					<div class="w-full px-4 border">
						<CardTable />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { defineComponent } from 'vue';

	import CardHeader from './Cards/CardHeader.vue'
	import CardBarChart from './Cards/CardBarChart.vue'
	import CardLineChart from './Cards/CardLineChart.vue'
	import CardTable from './Cards/CardTable.vue'

	export default defineComponent({
		name: 'Home',
		components: {
			CardHeader,
			CardBarChart,
			CardLineChart,
			CardTable
		}
	});
	
</script>