<template>
	<div class="relative px-4">
		<p class="text-base font-bold"> {{ kpiHeader }} </p>
		<p class="text-4xl font-bold text-center"> {{ kpiBigNumber }} </p>
		<p class="text-base font-bold text-center"> {{ kpiSubHeader }} </p>
	</div>
</template>

<script>
	export default {
		name: "CardStats",
		props: {
			kpiHeader: {
				type: String,
				default: 'Lorem'
			},
			kpiBigNumber: {
				type: String,
				default: '69'
			},
			kpiSubHeader: {
				type: String,
				default: 'Tweets'
			}
		}
	}
</script>