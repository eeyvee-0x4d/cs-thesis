<template>
	<div class="relative px-4">
		<p class="text-base font-bold"> {{ kpiHeader }} </p>
		<p class="text-4xl font-bold text-center"> {{ kpiBigNumber }} </p>
		<p class="text-base font-bold text-center"> {{ kpiSubHeader }} </p>
	</div>
</template>

<script setup>
	import { defineProps } from 'vue'

	const name = 'card-stats';
	const props = defineProps({
		kpiHeader: String,
		kpiBigNumber: String,
		kpiSubHeader: String
	});

</script>