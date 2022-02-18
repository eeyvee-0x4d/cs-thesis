<template>
	<div class="relative flex flex-col border p-4 divide-y divide-solid">
		<div>
			<h1 class="text-4xl font-bold">Dashboard Header</h1>
			<p class="text-base">Dashboard Description</p>
		</div>
		<div class="grid grid-cols-4 p-4 place-content-evenly divide-x">
			<div>
				<CardStats 
					kpiHeader="Lorem"
					kpiBigNumber="69"
					kpiSubHeader="Tweets"
				/>
			</div>
			<div>
				<CardStats 
					kpiHeader="Lorem"
					kpiBigNumber="69"
					kpiSubHeader="Tweets"
				/>
			</div>
			<div>
				<CardStats 
					kpiHeader="Lorem"
					kpiBigNumber="69"
					kpiSubHeader="Tweets"
				/>
			</div>
			<div>
				<CardStats 
					kpiHeader="Lorem"
					kpiBigNumber="69"
					kpiSubHeader="Tweets"
				/>
			</div>
		</div>
	</div>
</template>

<script setup>
	import CardStats from './CardStats.vue'
</script>