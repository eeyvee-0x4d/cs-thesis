<template>
	<div class="relative m-auto w-80vw py-4 space-y-4">
		<!-- Dashboard Header start -->
		<div class="relative p-4 border border-4 rounded-lg">
			<h1 class="text-4xl font-bold">Sentiment Analysis</h1>
			<p class="text-base font-normal">Visualizing The Public Perception of The COVID-19 Vaccine Brands Using
Positive-to-Negative Sentiment Ratio</p>
		</div>
		<!-- Dashboard Header end -->

		<!-- Breadcrumb start -->
		<Breadcrumbs />
		<!-- Breadcrumb end -->

		<!-- Upload Section start -->
		<router-view />
		<!-- Upload Section end -->
	</div>
</template>

<script>
	import { defineComponent } from 'vue';

	import Breadcrumbs from '../components/Core/Breadcrumbs.vue';
	import CardUpload from '../components/Cards/CardUpload.vue'

	export default defineComponent({
		name: 'Main',
		components: {
			Breadcrumbs,
			CardUpload
		}
	});
</script>

<style>
	.w-80vw {
		width: 80vw;
	}
</style>