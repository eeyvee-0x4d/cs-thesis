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
						<Tabs />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import CardHeader from './Cards/CardHeader.vue'
	import CardBarChart from './Cards/CardBarChart.vue'
	import Tabs from './Core/Tabs.vue'
	import Tab from './Core/Tab.vue'
	
</script>