<template>
	<!-- Visualize start -->
	<div class="flex flex-col space-y-4">
		<div class="border border-4 rounded-lg text-center">
			<CardModelStats />
		</div>
		<div class="border border-4 rounded-lg text-center">
			<CardHeader />
		</div>
		<div class="border border-4 rounded-lg">
			<CardBarChart chartTitle="Sentiments Overview" />
		</div>
		<div class="border border-4 rounded-lg">
			<TabsWrapper />
		</div>
		<div class="border border-4 rounded-lg">
			<CardTable title="Predicted Sentiments"/>
		</div>
	</div>
	<!-- Visualize end -->
</template>

<script>
	import { defineComponent } from 'vue';

	import CardHeader from '../components/Cards/CardHeader.vue';
	import CardBarChart from '../components/Cards/CardBarChart.vue';
	import TabsWrapper from '../components/Core/TabsWrapper.vue';
	import CardTable from '../components/Cards/CardTable.vue';
	import CardModelStats from '../components/Cards/CardModelStats.vue';

	export default defineComponent({
		name: 'Visualization',
		components: {
			CardHeader,
			CardBarChart,
			CardTable,
			TabsWrapper,
			CardModelStats,
		}
	})
</script>