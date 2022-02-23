<template>
	<div>
		<Tabs>
			<Tab v-for="tab, index in tabs" :key="index" :title="tab">
				<CardLineChart :chartTitle="tab + ' Vaccine Sentiment Trend'"/>
			</Tab>
		</Tabs>
	</div>
</template>

<script>
	import Tabs from './Tabs.vue';
	import Tab from './Tab.vue';
	import CardLineChart from '../Cards/CardLineChart.vue'

	import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'TabsWrapper',
		components: {
			Tabs,
			Tab,
			CardLineChart
		},
		data() {
			let tabs = ["Pfizer", "Sinovac", "Astrazeneca", "Moderna"];

			return {
				tabs
			}
		}
	});
</script>