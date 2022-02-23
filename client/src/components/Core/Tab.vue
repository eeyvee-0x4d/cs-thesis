<template>
	<div class="mr-2" v-show="isActive">
		<slot></slot>
	</div>
</template>

<script>
	import { defineComponent } from 'vue';


	export default defineComponent({
		name: 'Tab',
		props: {
			title: { type: String, dafault: 'Tab'}
		},
		data() {
			return {
				isActive: true
			}
		},
		created() {
			this.$parent.tabs.push(this)
		}
	});
	
</script>