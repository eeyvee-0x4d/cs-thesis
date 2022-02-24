<template>
	<div class="relative flex flex-col border divide-y divide-solid">
		<div class="p-4 text-base text-left font-bold">
			<h1>Data Overview</h1>
		</div>
		<div class="grid grid-cols-4 p-4 place-content-evenly divide-x">
			<div>
				<CardStats/>
			</div>
			<div>
				<CardStats/>
			</div>
			<div>
				<CardStats/>
			</div>
			<div>
				<CardStats/>
			</div>
		</div>
	</div>
</template>

<script>
	import CardStats from './CardStats.vue'
	import CardBarChart from './CardBarChart.vue'

	export default {
		components: {
			CardStats
		}
	}
</script>