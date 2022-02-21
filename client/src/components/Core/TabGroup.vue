<template>
	<div>
		<ul class="flex flex-auto">
			<li
				v-for="(tab, index) in tabs"	
			>
				{{ tab.title }}
			</li>
		</ul>
	</div>
</template>

<script>
	import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'TabGroup',
		props: {

		},
		data() {
			return {
				selectedIndex: 0,
				tabs: []
			}
		}
	});
</script>