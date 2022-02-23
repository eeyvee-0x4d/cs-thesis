<template>
	<div>
		<ul class="flex flex-auto justify-items-stretch">
			<li class="p-4 border w-1/4" 
				v-for="tab, index in tabs"
				:key="tab.title"
				@click="selectTab(index)"
			>
				{{ tab.title }}
			</li>
		</ul>
		<slot></slot>
	</div>
</template>

<script>
	import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'Tabs',
		data() {
			return {
				tabs: []
			}
		},
		onBeforeMount() {
			if(slots.default) {
				state.tabs = slots.default().filter((child) =>child.type.name === "Tab")
			}
		},
		mounted() {
			this.selectTab(0)
		},
		methods: {
			selectTab(selectedTab) {
				// this.tabs.forEach(tab => {
				// 	tab.isActive = (tab.title === selectedTab)
				// });
				this.tabs.forEach((tab, index) => {
					tab.isActive = (index === selectedTab)
				});	
			}
		}
	});
</script>