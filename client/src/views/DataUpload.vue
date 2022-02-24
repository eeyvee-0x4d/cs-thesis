<template>
	<div class="flex flex-col space-y-4">
		<CardUpload />
	</div>
</template>

<script>
	import { defineComponent } from 'vue';

	import CardUpload from '../components/Cards/CardUpload.vue';

	export default defineComponent({
		name: 'DataUpload',
		components: {
			CardUpload	
		}
	});
</script>